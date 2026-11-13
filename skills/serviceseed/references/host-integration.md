# Host capabilities and optional Agent Bridge integration

English | [中文译文](host-integration.zh-CN.md)

Read this when implementing or checking the host-to-maintainer path. These are operational mappings of the [ServiceSeed protocol](protocol.md), not a second set of normative interfaces. Choose concrete request/response shapes, entrypoints and persistence using the existing host. The table does not require one tool per row, a fixed method name, or all methods for every task.

## Supply real operations, not just a connected Agent

| Needed for the task | What the host must make available within authorization | What the actual owner enforces and returns |
| --- | --- | --- |
| Inspect and diagnose | Service identity/delegation/contract and acceptance responsibility; resources/dependencies and their meanings; active implementation/version; trigger, observed state and unfinished operations. Supply current operation descriptions with callable entrypoints, inputs, outputs, limits and recovery semantics | Check observation and model-disclosure authority before disclosure. Facts identify source/version/time; unavailable facts stay missing. Public descriptors do not reveal internal context |
| Create/propose change | An actual submission route for a declaration and executable candidate, preserved contract, baseline version and dependency conditions. Initial creation identifies the responsible owner and approved goal/rules | Preserve the candidate's identity/content and real submission outcome. Submission grants neither new resource rights nor activation permission. Ordinary authorized filesystem submission may suffice if that is the host's real mechanism |
| Validate | An existing controlled executor/checker using owner-approved criteria, candidate and dependency conditions; a way to obtain the actual result/evidence | Enforce candidate execution limits, including data/network/credential access and side effects; preserve which candidate/criteria/conditions were tested. Agent-generated tests may supplement, never replace or weaken approved criteria |
| Activate, roll back, or disable | A request to the existing publication owner carrying candidate/evidence, baseline/contract/conditions and a recoverable operation association known before submission | Recheck current maintenance authority, evidence, current baseline and dependencies. Preserve original effects under duplicate/concurrent submissions. Return actual activated version and operation outcome; consumer verification and current availability remain separate |
| Describe, bind and call a dependency | Authorized trustworthy capability description, shared contract/binding, existing grant proof/reference, real invocation and consumer result; relationship ownership and recoverable accepted selection | Each side checks identity, self/delegated actor, action/scope, execution and delivery rights. Binding does not mint grants. Reject unsupported required features and incompatible contracts. Verify affected commitments before declaring usable |
| Query/continue/report | Original-operation lookup under current query authority, actual status/results, and authorized continuation; configured notification destination/delivery result if notifications are in scope | Query never re-executes. Unknown remains unknown; revoked query rights do not rewrite past effects. Continuation uses declared recovery and current authority. A local log is not notification delivery |

These capabilities may already be provided through application tools, functions, a CLI, injected context plus controlled host execution, or a platform's publication API. An Agent that can only return a candidate can still participate: the host validates and activates under its own authorized control. The task must accurately identify which participant performs each action. Do not grant the Agent direct production code writes merely to bridge a missing controlled entrypoint.

If the user has authorized implementation and the chosen host lacks a required capability, add the smallest suitable entrypoint to that existing owner. If it lies outside the task scope, identify the exact gap and deliver the supported portion. Do not invent another authorization, publication, operation-state or business-result owner. This document does not make arbitrary code execution or new tools mandatory.

## What Bridge covers and what ServiceSeed still supplies

[Agent Bridge Spec](https://github.com/alcheme-labs/agent-bridge-spec) defines general application–Agent integration. Its `agent-bridge-integration` Skill can guide the applicable connection:

- **Role A:** the service host initiates an application-scoped Agent task/session, including authorized background work.
- **Role B:** an existing Agent invokes the service host's authorized methods; this does not require the application to control that Agent's whole conversation.

Use the matching specification's actual capabilities and binding for task/context delivery, output, tools, interactions, identity/disclosure, stopping/limits and recovery. An Agent task ID or a successful tool transport is not automatically the service operation's durable correlation or business success. The binding must connect them to the original effect owner where required; no parallel result database is implied. Canceling model execution does not undo a published candidate or an already-performed business effect.

ServiceSeed supplies the service-specific information and behavior in the table: accepted service commitments, current implementation and dependency semantics, delegated change scope, candidate/baseline correlation, approved validation, activation preconditions, service relationship checks, restart continuation, and truthful consumer confirmation. Bridge's generic method schema cannot decide those business facts. Complete these definitions here even where Bridge offers no specific method; map them to an actual host capability instead of pretending they are built in. Do not move those responsibilities into Bridge merely to make it appear complete.

The reviewed baseline is recorded in [compatibility.json](../compatibility.json): published specification draft 0.3 and [Skill 0.1.0](https://github.com/alcheme-labs/agent-bridge-spec/releases/tag/agent-bridge-integration-v0.1.0), checked at the recorded commit on 2026-11-13. This is document review, not evidence of an executable SDK or runtime compatibility. If a matching Bridge Skill is installed, resolve its real directory and follow its full-repository installation requirements. Otherwise obtain the matching published edition when authorized; never invent an installation package. Bridge absence does not prevent a native connection that satisfies ServiceSeed's requirements.

## Independent versions

The ServiceSeed protocol, this Skill, Bridge's specification, Bridge's Skill and any implementation package have different release lifecycles. Do not lock their version numbers together. [VERSION](../VERSION) is this Skill's sole version value. Its bundled protocol fixes the edition used by this release. The Bridge reference is a reviewed document baseline, not a tested semver range or runtime dependency.

When selecting/updating Bridge, check the intended A/B role, actual runtime, binding, task/context/output handling, identity and disclosure, required interactions/limits, and effect recovery. Record the selected versions and actual evidence in the service project's existing integration record. If these change materially, revalidate the affected path before adopting them. A higher Bridge version does not establish compatibility; an unchanged one does not guarantee every adapter works. When publishing an independently verified range later, distinguish it from this document-only reference.

Run Bridge's own checker only when its Skill is actually used; let that checker own its notices and state. This Skill's checker tracks only ServiceSeed releases. Do not build another Bridge updater or reset its acknowledged/ignored decisions.
