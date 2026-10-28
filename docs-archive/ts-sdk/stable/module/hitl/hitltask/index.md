---
title: HITLTask
kind: interface
longname: module:HITL.HITLTask
description: "What hitl(...) and approval(...) return, to pass to dag.task(...) : the options, checked and with their defaults applied."
---

# HITLTask

<Signature
  code="interface HITLTask<TArgs extends object | void = void> extends Operator<TArgs, HITLResult> {
	assignedUsers: readonly HITLUser[];
	body: HITLText<TArgs, string | null> | undefined;
	defaults: readonly string[] | undefined;
	failOnReject: boolean;
	ignoreDownstreamTriggerRules: boolean;
	kind: 'choice' | 'approval';
	multiple: boolean;
	options: readonly string[];
	params: Readonly<Record<string, HITLParam>>;
	responseTimeout: number | undefined;
	subject: HITLText<TArgs>;
}"
/>

<SourceLink href="/source/src/hitl/spec-ts/#L133" label="spec.ts:133" />

What `hitl(...)` and `approval(...)` return, to pass to `dag.task(...)`: the options, checked and with their defaults applied.

**Type Parameters**

- `TArgs` extends `object | void` = `void`

#### Hierarchy

- `Operator<TArgs, HITLResult>`
- `HITLTask`

---

## Properties

<MemberHeading id="assignedusers" depth="3" name="assignedUsers" sig="assignedUsers: readonly HITLUser[]" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L142" sourceLabel="spec.ts:142" />

<MemberHeading id="body" depth="3" name="body" sig="body: HITLText<TArgs, string | null> | undefined" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L136" sourceLabel="spec.ts:136" />

<MemberHeading id="defaults" depth="3" name="defaults" sig="defaults: readonly string[] | undefined" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L140" sourceLabel="spec.ts:140" />

<MemberHeading id="failonreject" depth="3" name="failOnReject" sig="failOnReject: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L148" sourceLabel="spec.ts:148" />

Only an approval acts on this.

<MemberHeading id="ignoredownstreamtriggerrules" depth="3" name="ignoreDownstreamTriggerRules" sig="ignoreDownstreamTriggerRules: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L146" sourceLabel="spec.ts:146" />

Only an approval acts on this.

<MemberHeading id="kind" depth="3" name="kind" sig="kind: 'choice' | 'approval'" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L134" sourceLabel="spec.ts:134" />

<MemberHeading id="multiple" depth="3" name="multiple" sig="multiple: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L141" sourceLabel="spec.ts:141" />

<MemberHeading id="options" depth="3" name="options" sig="options: readonly string[]" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L139" sourceLabel="spec.ts:139" />

<MemberHeading id="params" depth="3" name="params" sig="params: Readonly<Record<string, HITLParam>>" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L143" sourceLabel="spec.ts:143" />

<MemberHeading id="responsetimeout" depth="3" name="responseTimeout" sig="responseTimeout: number | undefined" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L144" sourceLabel="spec.ts:144" />

<MemberHeading id="subject" depth="3" name="subject" sig="subject: HITLText<TArgs>" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L135" sourceLabel="spec.ts:135" />
