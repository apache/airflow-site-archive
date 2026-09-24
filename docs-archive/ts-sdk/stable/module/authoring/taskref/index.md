---
title: TaskRef
kind: interface
longname: module:Authoring.TaskRef
description: "A reference to a task registered on a {@link module:Authoring.Dag|Dag}, returned by dag.task(...) . Identity only: the handler is deliberately not exposed. References are what inputs accepts, and what native Dag declaration will use to wire dependencies."
---

# TaskRef

<Signature
  code="interface TaskRef {
	dagId: string;
	taskId: string;
}"
/>

<SourceLink href="/source/src/sdk/dag-ts/#L65" label="dag.ts:65" />

A reference to a task registered on a [Dag](/module/authoring/dag), returned by `dag.task(...)`.

Identity only: the handler is deliberately not exposed.

References are what `inputs` accepts, and what native Dag declaration will use to wire dependencies.

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L67" sourceLabel="dag.ts:67" />

Identifier of the Dag this task belongs to.

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L69" sourceLabel="dag.ts:69" />

Airflow task ID, including any TaskGroup prefix.
