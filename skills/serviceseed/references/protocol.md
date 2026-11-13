# ServiceSeed Atomic Service Protocol — Core Draft

English | [中文原文](protocol.zh-CN.md)

Both languages describe the same protocol. This is a corresponding translation of the Chinese source. Resolve and correct differences in clause meaning against that source; translation does not add requirements.

v0.3 · 2026-11-13 · A draft of common semantics and behavior, including the minimum flow for authorized calls, maintenance activation, and recovery after a lost response. Concrete encoding and transport mappings are not yet finalized.

<a id="document-boundaries"></a>
## Scope and obligations

This protocol addresses developers independently implementing atomic services, service hosts, and maintenance Agent integration. It defines the meanings and behaviors that participants must share for safe operation, maintenance, and interoperability. Implementers need no knowledge of a particular project, business scenario, or discussion history.

The core requirements apply to implementations following this protocol. Optional capabilities carry their corresponding obligations when declared or actually provided. A service contract determines specific business meanings, commitments, and applicable conditions; authorization comes from authorized parties. Internal components, technology stacks, and deployment arrangements may differ, but authorization, fulfillment, and truthful results cannot be omitted.

The requirements expressed as must, must not, and equivalent behavioral obligations are protocol requirements. Details marked unresolved are not complete agreements. The [minimum interaction requirements](#minimum-interaction) and [complete flow](#minimum-flow) specify meanings, preconditions, and observable results, not component or interface boundaries. Implementers still need a shared, explicit invocation binding description and verification of actual behavior. Semantic agreement in this draft does not substitute for a completed transport mapping or interoperability acceptance.

<a id="product-core"></a>
## Service model and goal

**AI follows common rules to create atomic services in a user's service space. Each service has explicit capabilities, continuing runtime state, and controlled Agent maintenance, and can interoperate and compose with other services within authorization.**

A service can adjust its implementation within authorization while continuing to honor its commitments to callers.

- **Atomic:** divided by independent business capability; independently identifiable, runnable, authorizable, maintainable, and composable. An entire business workflow can be a long-lived service, with its internal steps defined by that service. Do not mechanically split services by request or internal step. Declared dependencies do not imply atomic cross-service transactions.
- **Intelligent:** an Agent belongs to the service lifecycle and maintains the implementation according to that service's goals, state, and authorization. Each service has an independent maintenance context. Models may be invoked on demand or shared, but instance permissions and state must remain isolated.
- **Interoperable:** common rules govern capability descriptions, identity proofs, authorization checks, calls, results, and changes. Internal languages, models, and implementations may differ.

**Implementations may change; commitments need an acceptance basis; permissions cannot silently expand.** The protocol standardizes observable behavior. Runtime environments and original resource owners enforce constraints; an AI assertion is insufficient. Ordinary requests may execute the active implementation without involving a model each time.

<a id="protocol-boundaries"></a>
## Granularity: core and optional capabilities

**Common mandatory rules, plus declarable optional capabilities: a service assumes the obligations of the capabilities it actually provides.** Core principles do not require identical modules in every instance. Rules must be consistently understandable and checkable by independent implementations, not merely share capability names. Concrete fields, invocation bindings, and unresolved interaction details remain marked as unresolved.

| Responsibility | What it determines | What it does not replace |
| --- | --- | --- |
| Common protocol | Identity, capability descriptions, contract versions, authorization, success/failure/unfinished results, and controlled maintenance behavior that independent services and hosts must share for safe calls, composition, and maintenance | Specific business content, fixed wrapper types, or uniform internal record tables |
| Service contract | Business meanings, state ownership, dependencies and wrapping relationships, external commitments, applicable conditions, and query/recovery guarantees; authorization scope comes from authorized parties | It cannot grant itself permissions, bypass common constraints, or silently weaken accepted commitments |
| Implementation | Code, orchestration, processes, storage, messaging, and deployment within the contract and authorization, enforcing the common rules | Authorization, truthful results, and promised consistency cannot be treated as optional internal details |

- **Required core.** Service boundaries, interoperability and composition under the common protocol, authorization throughout, and the recursive principle that a wrapped/composed service remains a service under the same protocol. An instance need not contain child services or wrapping layers. [Atomic service requirements](#atomic-service), [controlled creation and maintenance](#agent-boundary), [necessary maintenance context](#maintenance-context), and the [common lifecycle](#lifecycle) remain core.
- **Optional service capabilities.** An ordinary service may provide shared context, reusing applicable read, update, authorization, and version rules. Shared content, structure, and business validation belong to its contract. It is not a global knowledge base, a default owner of other services' runtime state, or a replacement for existing business authorities. Shared context is distinct from the service-specific authorized context that a maintenance Agent must receive.
- **Optional common interactions.** Subscription/notification and synchronization/subscription recovery are declared as needed. Once supported, they must follow their common semantics and service commitments. Subscriptions must explain subscription, cancellation, notification, and loss of authorization, including expiry or revocation. Recoverable subscriptions or state synchronization must explain how current state connects to subsequent changes, versions/freshness, duplicate or missing change detection, and recovery by catching up or retrieving state again. Events, scope, retention, and delivery promises belong to the contract; this protocol does not select transport or consistency implementations.
- **Ordinary runtime recovery remains core.** Operations with ongoing processing or durable effects need identifiable and queryable operations/results, result confirmation after interruption, and safe continuation. This does not depend on subscription support or require uniform workflow/collaboration records or a separate database for each service. Concrete state meanings and recovery promises belong to the contract; necessary persistent state reuses its identified owner.

Calls, reads, updates, subscriptions, and result/notification delivery enforce current authorization for the capabilities actually provided. Composition or wrapping does not grant access to inner resources, internal logs, or maintenance rights. Unknown required capabilities and incompatible commitments cannot be silently ignored. Fixed layer counts/types for all services, mandatory global shared state, a second business authority, or allowing Agents to rewrite authorization and acceptance to maintain availability would depart from this protocol's direction.

<a id="atomic-service"></a>
## What an atomic service must have

These are the minimum semantic requirements for an atomic service following this protocol. Concrete fields and interfaces remain to be finalized.

| Required part | What must be expressible |
| --- | --- |
| Identity and responsible parties | Stable service identity, owning space, authorized controller, and maintenance owner; service identity, external contract version, and implementation version are separately identified |
| Capabilities and commitments | Business capabilities, inputs/outputs and meanings, applicable conditions, side effects, and failure semantics; automatically verifiable commitments, who maintains their criteria, and who decides when a result cannot be determined |
| Runnable implementation and dependencies | Current implementation, resources required to start/run, related services and their contracts; explicit data, network, credential, and cost boundaries, with credentials bound through controlled references |
| Independent authorization boundaries | What callers may use, which resources the implementation may access, and what the Agent may observe/change; authorization source, scope, duration, revocation rules, and applicable budgets for each |
| Persistent state and observable results | Identified owners for active versions, runtime state, unfinished operations, and necessary evidence; authorized parties can query real results and continue after restart or Agent replacement |
| Maintenance delegation and acceptance | An associated Agent maintenance entrypoint, triggers, allowed changes, independent acceptance, and controlled activation; maintenance failures and notification results are queryable |

A service space provides runtime resources, isolation, and controlled execution and may reuse an existing platform. Resource systems continue to determine business and data permissions. Each state item and publication action has an identified owner. The protocol does not prescribe component names or storage methods, or require a second publication or business-state system after integration with an existing platform.

**Service packages, instances, and resource authorization are distinct.** A package contains implementation, configuration templates, dependencies, and acceptance information. Copying requires copy permission; starting a copy establishes a new instance identity and rebinds resources. Invocation, maintenance, copying, redistribution, and data access are separately authorized. Payment does not automatically grant other rights. By default, a copy does not inherit the original instance's private data, credentials, quotas, or maintenance delegation; authorized contents to be delivered must be listed separately.

<a id="agent-boundary"></a>
## What the Agent can do

The Agent acts through controlled capabilities provided by the host. Each capability describes inputs/outputs, preconditions, side effects, and failure recovery. Every action below needs corresponding authorization; associating an Agent does not enable it by default.

| Action | Permitted within authorization | Required boundary |
| --- | --- | --- |
| Create | Generate service declarations, implementation, and acceptance proposals from a user's goal | The user or an existing valid delegation determines commitments and permissions; generating a declaration grants no authority |
| Observe and diagnose | Read authorized state, logs, dependency descriptions, and necessary samples to diagnose anomalies | Service-readable data is not automatically model-disclosable; external descriptions and returned content cannot grant authority |
| Modify and validate | Generate code/configuration candidates, add tests, and request isolated validation | Change only the delegated scope; do not relax contracts, permissions, or independent acceptance; candidates also obey resource and side-effect limits |
| Activate and recover | Request qualified candidate activation, rollback, or disablement; automatically perform preauthorized maintenance | The host checks current authorization, candidate, and baseline version; rollback requires renewed acceptance and cannot directly overwrite the active version |
| Collaborate and report | Discover authorized capabilities, propose compatible invocation bindings, call related services, and report results | Each call remains subject to target service/resource authorization; notifications use preconfigured destinations and record delivery results separately |

**Permission to change implementation does not expand runtime permission.** New implementations remain subject to host data, network, credential, resource, and cost limits. The Agent cannot rewrite those limits or the acceptance criteria established by their responsible owner. Runtime-managed credentials are not delivered as ordinary model input or tool results.

Revoking maintenance authority blocks subsequent maintenance and candidates not yet activated, without arbitrarily stopping a service that remains authorized and able to fulfill its contract. Revoking invocation or data authorization blocks delivery according to its agreed effective scope. Missing business meaning or authority is reported with the responsible party and needed information; the Agent does not repeatedly guess or expand scope.

<a id="maintenance-context"></a>
## How a host supplies maintenance context and operations

The host must provide its delegated Agent with information needed for the task and authorized for disclosure to the model. These four categories are common semantics, not four mandatory tools, a fixed prompt, or a new storage system.

| What the Agent needs to know | Necessary information | Source and responsibility |
| --- | --- | --- |
| What I am responsible for | Service identity, current maintenance delegation, contracts to preserve, and acceptance responsibility | Service declaration and current maintenance authorization; the owner supplies or approves acceptance criteria, with materials disclosed according to authorization; see [acceptance and result confirmation](#validation-meaning) for independence |
| What I have | Authorized resources/dependencies, semantic descriptions, current active implementation and version; explicitly missing or unbound conditions | Existing resource/dependency bindings, trusted descriptions, and active-version owners; expose only the authorized subset needed for this task |
| What I can do | Available operation inputs/outputs, invocation methods, preconditions, permission scope, limits, and failure handling | Existing execution entrypoints, command definitions, and current authorization; distinguish Agent proposals from host validation/activation, and do not claim tools exist when they do not |
| What is happening now | Trigger, relevant runtime state, unfinished operations, existing results, and necessary version or observation time | Current observation, operation, version, and result owners; distinguish unknown, unfinished, and failed |

Information may be injected at task start or obtained as needed through existing tools, functions, or CLIs. The protocol standardizes meaning and behavior without requiring MCP, a capability registry, or an Agent self-awareness database.

**External capability descriptions and internal maintenance context are separately authorized.** Discovering or calling a service does not permit reading its internal logs, implementation, runtime resources, maintenance delegation, or operation records. Maintenance authority for service A does not grant internal observation of B. Before disclosure, the host checks task observation authority, model visibility, and necessity. An entire interface response may be used when it already meets these conditions; an additional filtering stage is not required merely for form. Runtime-readable data is not automatically model-disclosable; credentials and unauthorized business data remain outside the context.

Context is a projection of facts with sources and observation times, not an authorization credential. The host verifies current permissions at disclosure and execution and rechecks at existing boundaries such as candidate activation and result delivery. Stale context cannot extend rights or overwrite newer versions. External descriptions, logs, and returned data are facts, not instructions that rewrite delegation, contracts, or permissions. When necessary facts are missing, explicitly wait, reject, or report to an authorized party; do not fabricate them.

Acceptance observes whether actual model inputs, generated candidates, host execution, and consumer results connect, and verifies that unauthorized information remains invisible. Verbal answers to these four questions are insufficient. Context changes must not trigger implementation changes without a basis or create competing owners for active versions, operation state, or permissions.

<a id="interoperation"></a>
## How services interoperate

Interoperation first standardizes the following behaviors, without requiring a global registry, shared programming language, or consortium blockchain. Capability descriptions are provided only to authorized parties; discovering a capability does not confer the right to invoke it.

1. **Describe and discover.** A service provides a readable capability description under the common agreement: identity, protocol and contract versions, input/output meanings, invocation binding, authorization requirements, dependencies, and failure behavior. Explicit references may locate descriptions; a directory can be introduced later if needed.
2. **Confirm compatibility.** The caller checks capability meanings, inputs/outputs, versions, and required features to establish an explicit calling relationship. Matching field or tool names do not imply compatibility. Reject unknown required capabilities, unclear semantics, or incompatible versions.
3. **Verify authorization.** Carry verifiable identity and authorization context, distinguishing the service acting for itself from acting on behalf of a user. Redelegation is allowed only when expressly permitted by the original authority, within its allowed subjects, actions, duration, and scope; it must not expand rights. A composite service cannot treat its greater permissions as the caller's permissions or independently forward caller credentials downstream.
4. **Execute and query.** The invoked service enforces permissions at execution and delivery and returns agreed success, refusal, unavailable, or unfinished results. Operations with durable effects have recoverable correlation and a query method before effects occur; see [operations and recovery](#operation-recovery). Resolve unknown results with the original owner; do not create duplicate effects by retrying through a different backend.
5. **Maintain the relationship.** Internal changes preserve accepted capabilities and meanings. If external commitments must change, an authorized party establishes the new contract and compatibility arrangements. Callers verify before adopting the new agreement; the Agent cannot silently accept changes for both sides.

Services may be created independently and later establish calls from real capability descriptions obtained with permission. Creation need not share an initializer or know the other party's identity in advance. A service missing a required dependency may persist but must truthfully report that it awaits binding or is unavailable. Binding uses existing valid authorization; descriptions, model judgment, and binding itself cannot create permission. Confirming a relationship requires identity, authorization, contract, and binding compatibility checks and verification of affected commitments and consumer results under [acceptance and result confirmation](#validation-meaning). Saving connection configuration is insufficient. Resuming an accepted relationship after restart still requires current permission checks.

Composition obeys downstream data use and delivery limits, including agreements governing caches and derived results; it cannot bypass restrictions. Revocation cannot erase plaintext copies already retained by recipients. Results-only computation requires restrictions on raw-data and result egress.

Common semantics need a testable invocation binding. Parties must use a mutually supported binding and input/output agreement, not claim compatibility from tool names alone. Transport choices do not change business permissions, result truthfulness, or fulfillment responsibility.

<a id="minimum-interaction"></a>
## Minimum interaction requirements

Providers own their descriptions, execution, and results. Callers own the relationships they accept and downstream use. Existing authorization authorities decide who may execute or view what. A maintenance Agent submits authorized candidates and requests; the host or existing publication owner verifies and activates them. The effect owner retains and confirms operation outcomes. These are responsibilities, not mandatory processes, independent components, or human approval on every action; valid existing delegation may cover automation.

This table defines common semantics, not fixed field names, message encodings, or a tool inventory. One entrypoint may handle several actions; an action may span several interactions. Merging or splitting cannot skip preconditions.

| Interaction | Information and behavior that both sides must establish |
| --- | --- |
| Select an invocation binding | Both sides explicitly select the same accessible binding description and version. It maps logical information to fields, encodings, and entrypoints; explains how identity/authorization proofs are carried and verified; and defines results/errors and recovery scope. It may reference existing mechanisms and need not create a protocol or registry |
| Obtain a capability description | Target identity, protocol version, capabilities and specific contract version, input/output meanings, required features, supported bindings, and permission requirements. The correspondence between description source and target identity must be verifiable. Description grants no invocation rights |
| Verify identity and authorization | Actual acting principal, self versus delegated action, target service/resource, action and scope, recognized authorization source, validity conditions, and revocation requirements. Execution checks the existing trusted authority instead of accepting self-asserted identity/rights; raw credentials do not thereby enter model context |
| Confirm a relationship and call | The caller can recover the accepted target, capability, contract version, binding, and applicable authorization scope. Calls cannot silently substitute a contract; inputs/results correspond to this request. A relationship creates no rights and need not introduce a duplicate relationship database on both sides |
| Submit a candidate and request activation | Target service, maintenance delegation, candidate contents or verifiable reference, baseline implementation version, contract to preserve, and dependencies relevant to validation. Validation evidence corresponds to this candidate and conditions. An activation request is neither permission nor proof of activation |
| Query a durable operation result | Identify the original operation through [recoverable correlation](#operation-recovery) and obtain its real result and necessary evidence references within current query/disclosure authority. Activated version, consumer confirmation, and current availability are expressed separately. Querying does not re-execute the operation |

**Compatibility is not guessed from names.** Both parties support the selected protocol and binding versions and all required features of the declared capability. External calls use the accepted specific contract version. A replacement requires the caller's authority to accept it and an explicit compatibility basis; similar version numbers are not that basis. Reject unknown required features, unclear semantics, or no common binding. Ignorable extensions must be explicitly optional in the binding, and ignoring them must preserve commitments.

The binding also defines operation correlation scope, validity, and result-query/deduplication guarantees without changing this protocol's state meanings or authority boundaries. This body does not yet specify one concrete field/entrypoint mapping for all transports. Two parties claiming this section does not mean they have selected a common binding.

<a id="lifecycle"></a>
## Common lifecycle

**Goal and authorization → generate candidate → independent validation → controlled activation → caller use → observe change → Agent revises candidate → validate and activate again.** Creation and maintenance reuse this process.

These are behavioral requirements and preconditions for controlled change, not prescribed internal states, classes, processes, or tables.

- The responsible owner supplies or approves acceptance criteria. The Agent may add checks but cannot lower success criteria. Validation binds the specific candidate, contract, and dependency conditions. Recheck authorization and current version before activation; stale candidates cannot overwrite newer versions.
- Acceptance, validation, activation, and actual availability are distinct. Report recovery only after confirming results through the caller's real entrypoint. Service availability is separate from maintenance progress; maintenance does not mean the old implementation has stopped.
- The runtime handles persistence and continuation. Duplicate submissions, concurrency, restart, and timeout cannot duplicate effects. Rollback also satisfies current permissions, data constraints, and contracts. Candidates changing persistent state must explain compatibility and recovery; code rollback is not data recovery.
- If recovery is impossible, retain an implementation that can still fulfill its contract; otherwise explicitly report unavailability and escalate to an authorized owner. Safe refusal correctly handles failure but is not successful recovery.

<a id="validation-meaning"></a>
### Independent acceptance and consumer result confirmation

**Independent acceptance protects control of the criteria and truthfulness of results.** An authorized owner supplies or approves activation criteria. The generating Agent cannot alter them or substitute its own pass assertion for actual execution. Independence does not require another model, separate process, or manual confirmation each time. Authorized public examples, tests, and expected results may be provided to the Agent. Hidden tests are optional; unauthorized acceptance data still cannot be disclosed.

Creating or changing relationships checks target identity, current authorization, selected contract, and binding compatibility, and verifies affected commitments and dependency conditions. If a maintenance candidate changes conditions on which validation relies, revalidate affected parts. Still-valid evidence may be reused; rerunning every check is not universally required. Structural validation alone cannot replace business correctness.

**Consumer result confirmation (also called readback here)** obtains a real result through the agreed identity, authorization, and invocation path and checks its source, version or relevant conditions, and affected commitments. It may reuse the actual call response, original operation result, or authorized controlled validation result. It does not require an additional query interface or business call; verification must not duplicate business effects. Saved relationship configuration, passed candidate checks, or accepted activation alone cannot prove restored consumer results.

<a id="operation-recovery"></a>
## Durable operations and confirmation after a lost response

This section applies to requests producing durable effects, including saving relationships and activating candidates. Pure reads do not require persistent operation records. Correlation, results, and effects reuse their original owners. A queryer's cache, session, or model inference cannot replace the original owner's confirmation.

1. **Correlation before effects.** Before the first submission that may cause an effect, the requester holds or can recover sufficient correlation information for the receiver and authorized queryers to locate the same logical operation. It cannot depend solely on a first response that may be lost. Reuse existing request/operation references or an explicitly agreed combination of candidate and preconditions; no new identifier or record system is mandated. Correlation must itself be recoverable when recovery across restart is promised.
2. **Distinguish retries from new operations.** Correlation binds target, original acting principal, action, business content, and necessary preconditions. The same correlation with different content is rejected as a conflict, never overwriting the original request. Identical parameters do not automatically mean the same logical intent; new legitimate intent must be distinguishable from retry. Retry checks current authorization; correlation grants neither execution nor viewing rights.
3. **Duplicate submission does not repeat committed effects.** Within the declared validity scope, duplicate/concurrent requests for an operation resolve to its original operation. Retain committed results; safely continue unfinished work under that operation. A changed current version cannot rewrite prior success as failure. Retry under the same correlation is allowed only when the receiver guarantees no duplicate effects. Otherwise query first and retain an unknown outcome if unresolved; do not bypass this by changing identifiers, backends, or executors.
4. **Query confirms; it does not re-execute.** Query checks current viewing and disclosure permissions. Its result identifies the operation, real progress/effect, and necessary version/evidence correlation. Original execution authority is not perpetual query authority. Denied queries do not change original outcomes. Still-authorized parties may investigate under existing rights; recovery cannot automatically renew rights.
5. **Declare recovery scope beforehand.** Binding or contract states correlation scope, validity, query retention, and duplicate-effect prevention commitments; this protocol sets no universal duration. If outside that scope or the original record is unavailable, explicitly report inability to confirm. Do not execute an unresolved original request as a new one or accept an in-flight request of an unfinished operation as a new operation.

The following result meanings must be distinguishable; implementations need not use these internal names or one common state machine.

| Original operation outcome | What can be inferred | Recovery behavior |
| --- | --- | --- |
| Unfinished | Accepted or executing without a final effect conclusion | Query or safely continue under original correlation, without opening another equivalent operation |
| Effect committed | Original owner confirms the agreed effect occurred; activation identifies the actual activated version | Reuse the original result; consumer confirmation is expressed separately |
| Confirmed no effect | Original owner confirms rejection/failure and that the agreed effect did not occur | Further attempts follow declared retry rules and current authorization; changed intent is a new operation |
| Unknown | Acceptance or effect is not yet confirmable | Query the original owner; claim neither success nor non-execution, and do not blindly resubmit |

Timeout, denied query permission, temporarily unreachable query, no matching record, or an expired record cannot alone prove non-execution. Original commitment of the effect, consumer verification of that version, and current availability are different facts. If later versions have been activated, preserve the original operation's true result. Do not use the current active version or later recovery to infer that the original candidate passed consumer verification.

<a id="minimum-flow"></a>
## Minimum flow: authorized calls, activation, and recovery

The roles are generic: S is a provider service, C a calling service, M S's maintenance Agent, and H its host or existing publication owner. Roles may share a runtime while authorization is checked separately. K is the accepted specific service contract, B the shared binding, P a candidate, V0/V1 baseline/activated implementation versions, and O recoverable activation correlation. These symbols are not mandatory field names.

| Step | Interaction and checks | Completion or failure handling |
| --- | --- | --- |
| 1. Obtain and check description | C obtains S's trusted description through an authorized entrypoint, verifies target identity, and selects supported K, B, and required features | Reject unverifiable origin, unclear semantics, or incompatibility; discoverable does not mean callable |
| 2. Prepare authorized relationship | C supplies existing valid authority or S's existing authorization owner grants it under its rules; S checks the acting principal, delegation, action, and scope | C saves/reuses a pending relationship with K/B; this step does not independently add authority. Missing conditions remain pending or are rejected |
| 3. Confirm relationship and use | C actually calls S through B; S checks execution/delivery permissions; affected commitments and consumer results are verified | Only then confirm the relationship usable and identifiable after restart. Otherwise report pending/unavailable. An existing normal call can supply this result; an extra business call is not required |
| 4. Produce maintenance candidate | When S needs an implementation change, H gives M authorized context; M submits P, preserved K, baseline V0, and relevant dependencies; H validates using owner-approved criteria | Candidate and evidence correspond. Failed validation prevents activation; M's pass assertion cannot replace H's verification |
| 5. Request and perform activation | Before the first activation request, requester and H can correlate it using O. H rechecks maintenance authority, P's evidence, V0, and relevant dependencies; the existing publication owner activates in a controlled manner | Expired authority or changed baseline/dependencies cannot be overridden using old validation. On success, preserve O's actual effect corresponding to V1 and subsequent consumer-confirmation status |
| 6. First response is lost | M or an authorized successor queries H/original effect owner using O instead of guessing by creating another activation | Distinguish unfinished, committed, confirmed no effect, and unknown, as well as this query being denied/unreachable; follow the previous section. Timeout does not imply failure |
| 7. Confirm restored use | An authorized party confirms O's effect and obtains consumer results through the agreed path; C continues using original K/B and current authority | Report restored maintenance only when activation took effect and relevant consumer results meet original commitments. Activation-only evidence remains awaiting confirmation; a denied query is not failed activation |

If authorization changes between steps, subsequent execution/delivery is blocked according to current authorization while earlier true effects are preserved. Failed maintenance may leave running only an implementation that remains authorized and fulfills its contract. Existing entrypoints may merge or automate steps and reuse records for correlation; the flow requires no new management service, fixed tool count, or additional business platform.

<a id="onion-layers"></a>
## Recursive onion wrapping and degradation boundaries

**An onion is a recursive, on-demand relationship of service wrapping and composition. The common protocol does not fix layer counts, responsibilities, or composition arrangements.** A core capability may be wrapped by authorization and then other capabilities as needed. A layer may itself be a service following the same protocol. A network of services may expose a composite service under the same protocol and be wrapped/composed again. Not every instance must use wrapping, and layers need not be independent processes.

Wrapping and composition preserve explicit identity, verifiable authority, external commitments, state responsibility, and failure semantics. Service contracts describe the actual layers, order, and dependencies. Checkable agreements must govern how requests, results, and failures cross layers; concrete expression remains to be refined. Required preconditions such as authorization cannot be bypassed without permission. Wrapping does not grant inner maintenance context; each description's visibility remains separately authorized.

**Available capabilities may decrease; authorization and fulfillment requirements cannot automatically weaken.** Authorized parties establish necessary dependencies, offline conditions, revocation and evidence freshness, data freshness, and success criteria in advance.

| Dependency failure | Permitted behavior | Boundaries that cannot weaken |
| --- | --- | --- |
| Model or maintenance Agent unavailable | Continue an implementation that remains authorized and fulfills its contract; record unfinished maintenance | Do not skip necessary validation or call an unrepaired service recovered |
| Another dependency unavailable, but this operation needs no fresh confirmation from it | Continue when original offline authority, revocation checks, data freshness, and necessary dependencies allow | Do not extend permissions or disguise stale/incomplete data as success |
| Operation needs new authorization or confirmation from an external owner | Wait or report unavailable; retain correlation for already-submitted operations | Do not substitute unilateral approval, execute before authorization, or substitute local state for external success |
| Only optional auxiliary recording is delayed, or the outcome is unknown | Persist pending auxiliary records as agreed; for unknown effects query the original authority or recover idempotently | Required confirmation stays required; queued is not completed, and unknown is not failed |

Invocation/data permissions, maintenance scope, copy/redistribution rights, validity and revocation conditions, data meaning/completeness, independent acceptance, necessary confirmation, truthful outcomes, and idempotency cannot degrade. Older data, partial results, or lower operating standards are permitted only by the original contract and with explicit disclosure to callers. Pausing or unavailability acknowledges temporary inability to fulfill commitments without changing them.

Every fact has an explicit authority. For facts owned externally, local state contains only requests and result projections. Authority replacement must handle in-flight operations, old evidence, and permissions; it cannot be an automatic fault fallback. External acceptance or auxiliary receipts cannot replace effective commitment and business readback.

<a id="open-questions"></a>
## Unresolved protocol details

- The minimum flow's common information and behavior are defined above. Concrete fields, encodings, entrypoints, and authentication mappings still need a binding description that both parties can adopt. It cannot redefine authorization, outcomes, or recovery. Actual binding interoperability requires independent implementation verification.
- How shared context is shared across levels, inherited or overridden, and how dependent services behave remains unresolved. Permission inheritance is not assumed, nor does a shared-context service take ownership of other state.
- Common expression of wrapper composition/order, cross-layer requests/results/failures, and concrete checking of required preconditions need refinement. Recursive principles do not freeze the internal execution structure.
- Concrete subscription/cancellation/notification and synchronization/recovery exchanges, and declarations of delivery, freshness, and recovery guarantees need further discussion. Authorization rules and service contracts determine revocation behavior; this protocol does not impose universal seconds or select a database, messaging system, or transport.

These unresolved details do not freeze components or technology choices. Draft principles do not establish that any implementation already provides these capabilities.
