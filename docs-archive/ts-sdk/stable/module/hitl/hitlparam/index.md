---
title: HITLParam
kind: interface
longname: module:HITL.HITLParam
description: One form field on the Required Actions page, as Python's Param serializes.
---

# HITLParam

<Signature
  code="interface HITLParam {
	description?: string;
	schema?: Readonly<Record<string, JsonValue>>;
	value: JsonValue;
}"
/>

<SourceLink href="/source/src/hitl/spec-ts/#L42" label="spec.ts:42" />

One form field on the Required Actions page, as Python's `Param` serializes.

---

## Properties

<MemberHeading id="description" depth="3" name="description" sig="description: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L48" sourceLabel="spec.ts:48" />

<MemberHeading id="schema" depth="3" name="schema" sig="schema: Readonly<Record<string, JsonValue>>" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L53" sourceLabel="spec.ts:53" />

JSON Schema. The form renders `type`, `enum`, `format`, `items`, `minimum`, `maximum`, `minLength`, `maxLength` and `values_display`.

<MemberHeading id="value" depth="3" name="value" sig="value: JsonValue" />

<MemberMeta badges="readonly" sourceHref="/source/src/hitl/spec-ts/#L47" sourceLabel="spec.ts:47" />

Pre-filled value. When `responseTimeout` passes and `defaults` is set, the scheduler records each param's `value` as the response, so it is also the value used on timeout.
