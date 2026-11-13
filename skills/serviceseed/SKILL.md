---
name: serviceseed
description: "Create, maintain, connect, or review atomic services under the ServiceSeed protocol, including FDE-delivered services and personal service spaces. Preserve caller commitments while an authorized Agent changes implementation. Use for service declarations, host maintenance capabilities, authorized relationships and recovery; not ordinary API design without this lifecycle."
---

# Create and maintain ServiceSeed services

English | [中文译文](SKILL.zh-CN.md)

Build services that can change implementation within authorization while preserving caller commitments. This Skill translates the [protocol](references/protocol.md) into work; it is not an alternative protocol, a running host, or a grant of authority. The [Chinese source](references/protocol.zh-CN.md) resolves translation discrepancies. [VERSION](VERSION) identifies the Skill, and [compatibility.json](compatibility.json) identifies its protocol edition and optional Bridge reference.

Apply the same workflow to services delivered through FDE (forward-deployed engineering) and to personal service spaces. For FDE delivery, identify the customer's approved commitments, resource owners and maintenance delegation. For personal services, identify the owner and permitted callers, data uses, model disclosures and maintainers. These are applications of one protocol, not separate profiles or task templates; neither an FDE role nor personal ownership grants permissions to resources controlled by others.

## Start from the actual task

1. Read the bundled protocol's scope, core, and [atomic service requirements](references/protocol.md#atomic-service), then the sections applicable to this task. Use this bundled edition consistently; do not silently substitute a newer draft during a task. Respect whether the user requested discussion, review, creation, or maintenance.
2. Identify the user's goal, approved business rules and acceptance criteria, current service/contract if any, authorized resources and model visibility, actual host entrypoints, and owners of authorization, state, validation, and publication. Reuse existing facilities. Ask only for missing decisions or authority that affect the requested outcome; do not invent business meanings from field names.
3. When network access and Python 3.9+ are available, run `python3 <skill-directory>/scripts/check_updates.py check`. Only `notify: true` calls for an automatic notice; follow [update handling](references/updates.md), including cached notices and recording after display. An absent source or failed check does not establish currency and does not block service work. Without persistent state, do not promise cross-session deduplication or repeat notices on every use. This Skill creates no scheduler.

## Establish the host's real capabilities

Read [host capabilities and Agent integration](references/host-integration.md) when creating a service, adding Agent access, or diagnosing missing maintenance capabilities. Map each required action to an existing real tool, function, CLI, or controlled endpoint and its actual permissions. Context may be injected or queried; no fixed tool count, MCP dependency, registry, or context database is required.

The Agent needs authorized facts about its responsibility, resources/current implementation, permitted operations, and current trigger/state/pending results. These facts come from existing declarations, grants, and persistent owners. Public capability visibility, invocation rights, internal maintenance visibility, model disclosure, and change permission are distinct. Recheck current authority at disclosure, execution, activation, and delivery; context never grants rights.

For Agent connection/session integration, optionally use the available `agent-bridge-integration` Skill from [Agent Bridge Spec](https://github.com/alcheme-labs/agent-bridge-spec). Read the matching specification and select the applicable role/binding. If unavailable, use an available authorized native adapter or report the missing integration; do not invent an SDK, invoke a nonexistent Skill, or require Bridge for all services. Bridge does not supply ServiceSeed's service contract, maintenance delegation, candidate validation/activation, service relationships, or business effect owner. Complete those mappings here even if generic Agent tools work. See the reference for version and responsibility boundaries.

## Create or change a service

- Turn the goal and approved rules into a declaration the chosen host can actually consume: stable instance identity and owners; capability meanings, contract version and acceptance basis; implementation/resources/dependencies; separate caller/runtime/maintenance permissions; state/result ownership; maintenance triggers, limits and activation/recovery path. Preserve missing or unbound dependencies explicitly. Creation is not restricted to a catalog of task templates.
- Use the host's supported execution form to generate a candidate. A host limitation is a limitation of this delivery, not a protocol requirement. No universal declaration encoding or service-to-service wire binding has been finalized: document the concrete mapping both parties use and test it, rather than inventing one and calling it the standard.
- The user or authorized owner establishes initial commitments and authority. After acceptance, maintenance keeps the accepted contract. Propose incompatible business changes separately for the authorized parties; do not reinterpret the contract to make tests pass.
- Bind the candidate and evidence to its actual contents/reference, baseline implementation, accepted contract and relevant dependency conditions. The owner supplies or approves criteria; the generating Agent cannot change those criteria or certify itself successful. Authorized examples and expected results may be visible; hidden tests are optional. Request real host validation within resource and side-effect limits.
- Request activation through the existing publication owner. It checks current delegation, candidate/evidence, baseline and relevant dependencies again. Stale candidates cannot overwrite newer versions. Before the first effect-causing submission, preserve recoverable correlation through the host's existing mechanism. Authorization to propose is not authorization to activate.
- Confirm actual effects and consumer results through the agreed call path. Distinguish declaration generated, candidate validated, activated, consumer verified, and currently available. Reuse valid real responses/evidence; do not repeat business effects merely to verify them. If no suitable host or validation entrypoint exists, report a declaration/candidate and the concrete missing edge, not a running compliant service. Implement that edge only within the user's authorized scope.

## Connect independently created services

Use the protocol's [interaction requirements](references/protocol.md#minimum-interaction) and [minimum flow](references/protocol.md#minimum-flow). Obtain a trusted, authorized description; identify both parties and self/delegated actors; select a mutually supported contract, binding, and required features; use or obtain authority from its existing owner. Binding creates no rights and does not expose provider internals.

Save/reuse the accepted relationship through its owner, verify the affected commitments with a real authorized call and consumer result, and confirm usable only then. Restart restores accepted identity/contract/binding and pending work while rechecking current authority. Unknown required features, incompatible meanings, or no common binding are failures to establish compatibility, not reasons to guess or silently route elsewhere. Composition preserves data-use, disclosure, caching, and delegation limits.

## Maintain and recover

Use real triggers, trusted dependency semantics, current implementation/state, and existing operation results to diagnose changes. Keep ordinary calls on an authorized implementation that still fulfills commitments; a model need not run per call. Generate a new candidate and reuse the controlled validation/activation path. Missing essential meaning requires information from its responsible owner, not a guessed repair.

For lost responses, interrupted activation, retry, or restart, follow [operation recovery](references/protocol.md#operation-recovery). Locate the original effect owner with correlation available before the first submission. Distinguish unfinished, committed, confirmed no effect, and unknown. Reuse committed results; retry only under the declared duplicate-effect protection and current authority. Query denial, timeout, missing/expired records, or a later active version cannot prove the original operation failed. Do not change identifiers, backend, or executor to bypass uncertainty. Querying needs current disclosure permission and cannot renew rights or re-execute effects.

Rollback needs current authority and compatibility/acceptance; code rollback is not data recovery. If maintenance fails, retain a still-authorized, contract-fulfilling implementation or report unavailable and the responsible owner's next decision. Record notification delivery separately from local logging. Do not claim recovery before the relevant consumer result is confirmed.

## Verify and hand over

Use actual entrypoints and proportionate existing checks. For creation/maintenance, verify approved business behavior, denied access/model disclosure, controlled activation and consumer results. For relationships, persistent operations or recovery in scope, also cover restart, revocation between steps, stale/concurrent candidates, duplicate submissions and lost-response confirmation. Reuse still-valid evidence and explain genuinely inapplicable cases; a happy-path sample or schema check alone is insufficient.

Return the declaration/implementation and actual run/use/maintenance entrypoints for implementation tasks, plus concise evidence and remaining boundaries. Distinguish documents, source checks, executed behavior, and independently tested interoperability. Loading this Skill, connecting Bridge, or generating code proves none of those by itself. A safe refusal is correct handling but not successful restoration.

Keep optional capabilities optional: recursive wrapping/composition has no fixed layer types; shared context, subscriptions, synchronization, billing, copying, networks, and ledgers are not additions to make unless requested. Actual capabilities still carry their applicable protocol obligations. This Skill grants no permission for paid model calls, production writes, deployment, publication, or automatic updates beyond the user's task authorization.

Respond in the user's language unless they explicitly request another language.
