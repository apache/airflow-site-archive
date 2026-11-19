---
title: ApprovalSpec
kind: interface
longname: module:HITL.ApprovalSpec
description: The ApprovalOperator options, named as TypeScript spells them.
---

# ApprovalSpec

<Signature
  code="interface ApprovalSpec<TSubjectArgs extends object | void = void, TBodyArgs extends object | void = TSubjectArgs> extends HITLBaseSpec<TSubjectArgs, TBodyArgs> {
	assignedUsers?: readonly HITLUser[];
	body?: HITLText<TBodyArgs, string | null>;
	defaults?: 'Approve' | 'Reject';
	failOnReject?: boolean;
	ignoreDownstreamTriggerRules?: boolean;
	params?: Readonly<Record<string, HITLParam>>;
	responseTimeout?: number;
	subject: HITLText<TSubjectArgs>;
}"
/>

<SourceLink href="/source/src/hitl/spec-ts/#L92" label="spec.ts:92" />

The `ApprovalOperator` options, named as TypeScript spells them.

**Type Parameters**

- `TSubjectArgs` extends `object | void` = `void`
- `TBodyArgs` extends `object | void` = `TSubjectArgs`

#### Hierarchy

- `HITLBaseSpec<TSubjectArgs, TBodyArgs>`
- `ApprovalSpec`

---

## Properties

<MemberHeading id="assignedusers" depth="3" name="assignedUsers" sig="assignedUsers: readonly HITLUser[]" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L68" sourceLabel="spec.ts:68" />

_Inherited from&#x20;_`assignedUsers`

Users allowed to respond. Anyone who can act on the task may respond when unset.

<MemberHeading id="body" depth="3" name="body" sig="body: HITLText<TBodyArgs, string | null>" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L66" sourceLabel="spec.ts:66" />

_Inherited from&#x20;_`body`

Markdown shown below the headline.

<MemberHeading id="defaults" depth="3" name="defaults" sig="defaults: 'Approve' | 'Reject'" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L97" sourceLabel="spec.ts:97" />

The answer given for the responder when `responseTimeout` passes without a response.

<MemberHeading id="failonreject" depth="3" name="failOnReject" sig="failOnReject: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L108" sourceLabel="spec.ts:108" />

On "Reject", fail this task rather than skip what follows it. Defaults to false, so a rejection succeeds. A retry asks the reviewer again, so `retries` with this option repeats the request on each attempt.

<MemberHeading id="ignoredownstreamtriggerrules" depth="3" name="ignoreDownstreamTriggerRules" sig="ignoreDownstreamTriggerRules: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L102" sourceLabel="spec.ts:102" />

On "Reject", skip every task downstream rather than only the tasks directly downstream. Defaults to false.

<MemberHeading id="params" depth="3" name="params" sig="params: Readonly<Record<string, HITLParam>>" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L70" sourceLabel="spec.ts:70" />

_Inherited from&#x20;_`params`

Form fields the responder fills in, by name. Their answers are the result's `paramsInput`.

<MemberHeading id="responsetimeout" depth="3" name="responseTimeout" sig="responseTimeout: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L75" sourceLabel="spec.ts:75" />

_Inherited from&#x20;_`responseTimeout`

Whole seconds to wait for a response, since TypeScript has no timedelta. Waits indefinitely when unset. Use this rather than `executionTimeout`, which a HITL task does not enforce.

<MemberHeading id="subject" depth="3" name="subject" sig="subject: HITLText<TSubjectArgs>" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L64" sourceLabel="spec.ts:64" />

_Inherited from&#x20;_`subject`

Headline of the request.
