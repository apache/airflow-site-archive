---
title: TaskContext
kind: interface
longname: module:Authoring.TaskContext
description: Runtime metadata for the current task invocation.
---

# TaskContext

<Signature
  code="interface TaskContext {
	dagId: string;
	mapIndex: number;
	runId: string;
	signal: AbortSignal;
	taskId: string;
	tryNumber: number;
}"
/>

<SourceLink href="/source/src/sdk/task-ts/#L25" label="task.ts:25" />

Runtime metadata for the current task invocation.

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L27" sourceLabel="task.ts:27" />

Identifier of the Dag containing this task.

<MemberHeading id="mapindex" depth="3" name="mapIndex" sig="mapIndex: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L35" sourceLabel="task.ts:35" />

-1 for non-mapped tasks, 0..N-1 for mapped instances.

<MemberHeading id="runid" depth="3" name="runId" sig="runId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L31" sourceLabel="task.ts:31" />

Dag run identifier for the current task attempt.

<MemberHeading id="signal" depth="3" name="signal" sig="signal: AbortSignal" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L43" sourceLabel="task.ts:43" />

AbortSignal that fires when Airflow terminates the task subprocess with SIGTERM or SIGINT.

Pass this signal to `fetch()`, timers, or any other API that accepts an abort signal for cooperative cancellation and cleanup.

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L29" sourceLabel="task.ts:29" />

Task ID for this handler invocation, including any TaskGroup prefix.

<MemberHeading id="trynumber" depth="3" name="tryNumber" sig="tryNumber: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L33" sourceLabel="task.ts:33" />

Airflow try number for the current task attempt.
