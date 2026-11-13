# ServiceSeed

English | [中文](README.zh-CN.md)

Official repository: [alcheme-labs/ServiceSeed](https://github.com/alcheme-labs/ServiceSeed) · [Releases](https://github.com/alcheme-labs/ServiceSeed/releases).

**An open specification for services that can maintain their implementations within authorization while preserving their commitments to callers.** AI creates a service in a service space; the host constrains its maintenance Agent; other services use its declared capabilities under explicit contracts and permissions.

For **FDE service delivery and personal service spaces**: let AI create, connect and maintain services while preserving permission boundaries and service contracts.

This package contains the protocol and a companion Skill that helps AI create, maintain, connect and review such services. It does not contain a running service host or a reference runtime. An Agent connection alone does not provide the service-specific maintenance capabilities.

## Start here

- [Protocol in English](skills/serviceseed/references/protocol.md) · [中文协议](skills/serviceseed/references/protocol.zh-CN.md)
- [Skill instructions](skills/serviceseed/SKILL.md) · [Skill 中文译文](skills/serviceseed/SKILL.zh-CN.md)
- [Host capabilities and optional Bridge integration](skills/serviceseed/references/host-integration.md) · [中文](skills/serviceseed/references/host-integration.zh-CN.md)
- [Version/update behavior](skills/serviceseed/references/updates.md) · [中文](skills/serviceseed/references/updates.zh-CN.md)

The protocol defines shared meanings and behavioral obligations. Each service contract supplies business meanings and commitments. Hosts choose their implementation and enforce authorization, candidate validation, controlled activation and result recovery. The Skill supplies a practical workflow and mappings to real host entrypoints, not another normative protocol.

The core flow is: **goal and authority → candidate → independent validation → controlled activation → consumer confirmation → observation and maintenance**. Services can be created independently and later establish authorized calls using compatible descriptions, contracts and bindings. Normal calls may execute an active implementation without invoking a model each time.

## Applications: FDE service protocol and personal service protocol

Here, “FDE service protocol” and “personal service protocol” describe two applications of the same general technical protocol. They share identity, contract, authorization, controlled maintenance and recovery requirements. They do not establish separate specifications or restrict other service uses.

| Application | Problem to address | What this protocol helps establish |
| --- | --- | --- |
| **FDE service delivery and continuing maintenance** | Turn forward-deployed engineering for a customer's business into services that keep running and can be maintained after handover; preserve accepted caller commitments when data sources, dependencies or internal implementations change | Customer-approved business contracts and acceptance, actual resource authorization, maintenance delegation, controlled activation and result confirmation. Being an engineer, vendor or Agent grants no automatic customer data access or change authority |
| **Personal service spaces** | Let individuals use AI to create their own services, provide capabilities to selected people or other services under permission, and delegate continuing maintenance | Service ownership, resource/data-use scope, invocation and maintenance rights, model disclosure, revocation and recovery. Exposing a capability does not automatically expose raw data or internal maintenance context |

Both applications use the same Skill workflow. The corresponding service contract and authorization determine business commitments, sharing recipients, maintenance duration and applicable conditions. These are intended applications; actual fulfillment still requires verification of the chosen host and service. Scenario descriptions are not evidence of completed runtime support.

## Install and use the Skill

Obtain the official repository or a matching release:

```sh
git clone https://github.com/alcheme-labs/ServiceSeed.git
```

Copy the complete `ServiceSeed/skills/serviceseed` directory into your Agent host's skill directory, or link it if the host supports links. It includes both protocol editions and references; no files elsewhere in this repository are needed for Skill use. Do not overwrite an existing local installation without inspecting and preserving changes. Downloading the package does not install it into an Agent host. The first public Skill is named `serviceseed`; earlier unpublished working copies used `serveragent-service`.

Use the host's normal skill-selection mechanism, or for hosts supporting named invocation:

> Use `$serviceseed` to create a service from this goal and these approved business rules, using the attached resource descriptions, authorizations and existing host. Preserve the accepted caller contract during maintenance. Show the actual run, call and maintenance entrypoints and verification results.

Provide the real goal, meanings, permissions and available resources; no task-specific service template is required. A Skill cannot supply missing authority or runtime capabilities. It identifies those gaps and implements them only within the user's authorized scope. For a review-only request, it reviews without developing or deploying a service. Responses follow the user's language.

## Agent Bridge and versions

[Agent Bridge Spec](https://github.com/alcheme-labs/agent-bridge-spec) and its `agent-bridge-integration` Skill are optional references for application–Agent connection/session/tool integration. ServiceSeed still defines its service contract, maintenance delegation/context, candidate validation/activation, dependency relationships and consumer confirmation. Native adapters may implement the same requirements.

Versions are independent. [VERSION](skills/serviceseed/VERSION) is the Skill version; [compatibility.json](skills/serviceseed/compatibility.json) records the bundled protocol and reviewed Bridge baseline. There is no forced same-version upgrade and no claimed tested Bridge version range. Selecting a changed integration requires checking affected roles, bindings and capabilities.

Update checks run on Skill use, with a configurable 24-hour network interval and persistent per-version deduplication. A new release notice explains fetched changes and asks whether to update, remind later or ignore. It does not install automatically. There is no idle background scheduler. [The update source](skills/serviceseed/update-source.json) is `alcheme-labs/ServiceSeed`, selecting GitHub Releases tagged `serviceseed-v<version>`. A network or API failure is reported as an unsuccessful check, not proof that the installed version is current.

## Current status and verification

First edition, 2026-11-13: protocol draft **0.3**, Skill **0.1.0**. The public project is named ServiceSeed; ServerAgent was its working name. The protocol defines common semantics; a universal concrete wire format/binding has not been finalized or independently interoperability-tested. Do not claim that installing the Skill makes generated services interoperable without actual shared-binding and runtime verification.

Bridge's [Skill 0.1.0 release](https://github.com/alcheme-labs/agent-bridge-spec/releases/tag/agent-bridge-integration-v0.1.0) and published specification draft 0.3 are available. The checked commit is recorded in the compatibility metadata; this is document comparison, not runtime compatibility proof. This package does not ship a Bridge runtime or claim a public SDK is available.

The package can be checked with Python 3.9+:

```sh
python3 scripts/validate_package.py
python3 -B -m unittest discover -s tests -p 'test_skill_updates.py' -v
python3 skills/serviceseed/scripts/check_updates.py check
```

The tests exercise update decisions, persistence, concurrency and network failure handling with temporary state and controlled responses. They do not prove real release discovery or service conformance. Runtime acceptance must follow the protocol and the actual service's commitments.

## Contribute and release

Keep protocol requirements in the protocol; keep host choices and task-specific constraints out of universal requirements. Maintain both protocol languages and both Skill languages together. The protocol's Chinese source resolves translation discrepancies; the Skill's Chinese edition corresponds to its English entrypoint. Do not resolve normative ambiguities only inside a Skill instruction.

For a Skill release, update `VERSION`, relevant compatibility metadata and [CHANGELOG](CHANGELOG.md). Use a patch for corrections that preserve required behavior, a minor release for compatible workflow additions, and clearly identify breaking changes; during `0.x`, a minor version may introduce a disclosed breaking change. This is Skill packaging policy, not an interoperability guarantee.

Publish each Skill version as a GitHub Release under `serviceseed-v<version>` with actual changes and compatibility notes. Review the export, license/provenance and validation results, and preserve previously published versions and assets. Creating an ordinary tag alone does not trigger update notices. Never publish private service state, credentials or internal evidence with this package.

Licensed under [Apache-2.0](LICENSE). See [NOTICE](NOTICE) and [update-helper provenance](update-helper-origin.json). The license covers these documents, Skill and helpers; it does not grant runtime data access, service invocation or maintenance permissions.
