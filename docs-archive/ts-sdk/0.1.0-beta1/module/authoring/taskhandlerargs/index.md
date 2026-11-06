---
title: TaskHandlerArgs
kind: interface
longname: module:Authoring.TaskHandlerArgs
description: Arguments passed to every task handler.
---

# TaskHandlerArgs

<Signature
  code="interface TaskHandlerArgs {
	client: TaskClient;
	ctx: TaskContext;
}"
/>

<SourceLink href="/source/src/sdk/task-ts/#L47" label="task.ts:47" />

Arguments passed to every task handler.

---

## Properties

<MemberHeading id="client" depth="3" name="client" sig="client: TaskClient" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L51" sourceLabel="task.ts:51" />

Client for reading and writing Airflow task-time data.

<MemberHeading id="ctx" depth="3" name="ctx" sig="ctx: TaskContext" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L49" sourceLabel="task.ts:49" />

Runtime metadata for the current task invocation.
