#!/usr/bin/env python3
"""Validate the prepared public package; not a service conformance test."""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


def validate(root):
    root = root.resolve()
    skill = root / "skills/serviceseed"
    errors = []
    version = (skill / "VERSION").read_text().strip()
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version):
        errors.append("Invalid VERSION")
    metadata = json.loads((skill / "compatibility.json").read_text())
    source = json.loads((skill / "update-source.json").read_text())
    if source["tag_prefix"] != "serviceseed-v":
        errors.append("Unexpected update tag prefix")
    # Private forks may deliberately disable checks by omitting a source.
    if source["repository"] is not None and not re.fullmatch(
            r"[A-Za-z0-9][A-Za-z0-9-]{0,38}/[A-Za-z0-9_.-]{1,100}", source["repository"]):
        errors.append("Invalid official repository")
    editions = [skill / metadata["serviceseed_protocol"][lang] for lang in ("english", "chinese")]
    texts = [p.read_text() for p in editions]
    anchors = [re.findall(r'<a id="([^"]+)"', text) for text in texts]
    if anchors[0] != anchors[1] or len(anchors[0]) != len(set(anchors[0])):
        errors.append("Protocol language anchors differ or are duplicated")
    for text in texts:
        if f"v{metadata['serviceseed_protocol']['version']} ·" not in text:
            errors.append("Protocol version does not match compatibility metadata")
    for entry in ("SKILL.md", "SKILL.zh-CN.md"):
        text = (skill / entry).read_text()
        if not text.startswith("---\nname: serviceseed\ndescription: ") or "\n---\n" not in text[4:]:
            errors.append(f"Missing Skill frontmatter: {entry}")
    link_count = 0
    files = [p for p in root.rglob("*") if p.is_file()
             and not any(part in (".git", "__pycache__") for part in p.relative_to(root).parts)]
    for path in files:
        if path.is_symlink():
            errors.append(f"Unexpected symlink: {path.relative_to(root)}")
        if path.suffix == ".py":
            ast.parse(path.read_text(), filename=str(path))
        if path.suffix != ".md":
            continue
        text = path.read_text()
        if re.search(r"/Users/|/home/[^ /]+/|\.runs/", text):
            errors.append(f"Private workspace reference: {path.relative_to(root)}")
        # Local Markdown links, including explicit HTML anchors in the protocol.
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = urlsplit(raw.strip("<>"))
            if target.scheme or target.netloc:
                continue
            candidate = (path.parent / unquote(target.path)).resolve() if target.path else path
            if not candidate.is_relative_to(root):
                errors.append(f"Escaping link in {path.relative_to(root)}: {raw}")
            elif not candidate.exists():
                errors.append(f"Missing link in {path.relative_to(root)}: {raw}")
            elif target.fragment and candidate.suffix == ".md":
                destination = candidate.read_text()
                if f'id="{target.fragment}"' not in destination:
                    errors.append(f"Missing anchor in {path.relative_to(root)}: {raw}")
            link_count += 1
    if errors:
        raise ValueError("\n".join(errors))
    print(f"Validated {len(files)} files, {link_count} local links, bilingual anchors and Skill metadata.")
    print(f"Skill {version}; update source: {'unconfigured' if source['repository'] is None else source['repository']}")
    print("Static package checks only; no runtime or interoperability conformance claim.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate(args.root)
    except (OSError, ValueError, KeyError, SyntaxError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
