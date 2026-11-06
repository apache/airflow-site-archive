---
title: TaskOptions
kind: interface
longname: module:Authoring.TaskOptions
description: Named options for dag.task() . Keyword-only so neither field has to be positioned around the other, and so future fields can be added without a new parameter. Unknown keys are rejected, so a typo fails at import time rather than being ignored.
---

# TaskOptions

<Signature
  code="interface TaskOptions {
	inputs?: Readonly<Record<string, TaskRef>>;
	spec?: TaskSpec;
}"
/>

<SourceLink href="/source/src/sdk/dag-ts/#L88" label="dag.ts:88" />

Named options for `dag.task()`.

Keyword-only so neither field has to be positioned around the other, and so future fields can be added without a new parameter. Unknown keys are rejected, so a typo fails at import time rather than being ignored.

---

## Properties

<MemberHeading id="inputs" depth="3" name="inputs" sig="inputs: Readonly<Record<string, TaskRef>>" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L99" sourceLabel="dag.ts:99" />

References to the upstream tasks this task consumes.

Not used yet: a handler receives `{ctx, client}` only, and the Python stub Dag defines task order. Read an upstream return value explicitly instead — `client.getXCom({ key: "return_value", taskId: "extract" })`, where omitting `taskId` reads the _running_ task's own XCom, not the upstream.

In the future these will declare dependencies in native TypeScript Dags.

<MemberHeading id="spec" depth="3" name="spec" sig="spec: TaskSpec" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L101" sourceLabel="dag.ts:101" />

Task-level options. Stored, but not used yet — see [TaskSpec](/module/authoring/taskspec).
