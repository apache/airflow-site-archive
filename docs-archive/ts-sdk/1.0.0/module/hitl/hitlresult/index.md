---
title: HITLResult
kind: typedef
longname: module:HITL.HITLResult
description: The response a HITL task pushes to XCom and passes downstream. The keys are those of Python's HITLTriggerEventSuccessPayload in camelCase, and respondedAt is an ISO-8601 string where Python's is a datetime. Airflow's own records of the request and the response keep their snake_case keys.
---

# HITLResult

<Signature
  code="HITLResult = {
	chosenOptions: string[];
	paramsInput: Record<string, JsonValue>;
	respondedAt: string;
	respondedByUser: HITLUser | null;
	timedout: boolean;
}"
/>

<SourceLink href="/source/src/hitl/spec-ts/#L118" label="spec.ts:118" />

The response a HITL task pushes to XCom and passes downstream.

The keys are those of Python's `HITLTriggerEventSuccessPayload` in camelCase, and `respondedAt` is an ISO-8601 string where Python's is a datetime. Airflow's own records of the request and the response keep their snake\_case keys.

**Properties**

- `chosenOptions` (string\[])
- `paramsInput` (Record\<string, [JsonValue](/module/types/jsonvalue)>)
- `respondedAt` (string) — ISO-8601 UTC instant of the response, to the millisecond.
- `respondedByUser` ([HITLUser](/module/hitl/hitluser) | null) — `null` when the defaults were applied on timeout.
- `timedout` (boolean) — Whether the defaults were applied because the response timeout passed.
