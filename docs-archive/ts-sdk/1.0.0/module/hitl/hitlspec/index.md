---
title: HITLSpec
kind: interface
longname: module:HITL.HITLSpec
description: The HITLOperator options, named as TypeScript spells them.
---

# HITLSpec

<Signature
  code="interface HITLSpec<TSubjectArgs extends object | void = void, TBodyArgs extends object | void = TSubjectArgs> extends HITLBaseSpec<TSubjectArgs, TBodyArgs> {
	assignedUsers?: readonly HITLUser[];
	body?: HITLText<TBodyArgs, string | null>;
	defaults?: readonly string[];
	multiple?: boolean;
	options: readonly string[];
	params?: Readonly<Record<string, HITLParam>>;
	responseTimeout?: number;
	subject: HITLText<TSubjectArgs>;
}"
/>

<SourceLink href="/source/src/hitl/spec-ts/#L79" label="spec.ts:79" />

The `HITLOperator` options, named as TypeScript spells them.

**Type Parameters**

- `TSubjectArgs` extends `object | void` = `void`
- `TBodyArgs` extends `object | void` = `TSubjectArgs`

#### Hierarchy

- `HITLBaseSpec<TSubjectArgs, TBodyArgs>`
- `HITLSpec`

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

<MemberHeading id="defaults" depth="3" name="defaults" sig="defaults: readonly string[]" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L86" sourceLabel="spec.ts:86" />

Options chosen for the responder when `responseTimeout` passes without a response.

<MemberHeading id="multiple" depth="3" name="multiple" sig="multiple: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L88" sourceLabel="spec.ts:88" />

Whether more than one option may be chosen.

<MemberHeading id="options" depth="3" name="options" sig="options: readonly string[]" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L84" sourceLabel="spec.ts:84" />

What the responder chooses from.

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
