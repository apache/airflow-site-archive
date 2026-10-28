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

<SourceLink href="/source/src/sdk/task-ts/#L30" label="task.ts:30" />

Runtime metadata for the current task invocation.

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L32" sourceLabel="task.ts:32" />

Identifier of the Dag containing this task.

<MemberHeading id="mapindex" depth="3" name="mapIndex" sig="mapIndex: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L40" sourceLabel="task.ts:40" />

-1 for non-mapped tasks, 0..N-1 for mapped instances.

<MemberHeading id="runid" depth="3" name="runId" sig="runId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L36" sourceLabel="task.ts:36" />

Dag run identifier for the current task attempt.

<MemberHeading id="signal" depth="3" name="signal" sig="signal: AbortSignal" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L48" sourceLabel="task.ts:48" />

AbortSignal that fires when Airflow terminates the task subprocess with SIGTERM or SIGINT.

Pass this signal to `fetch()`, timers, or any other API that accepts an abort signal for cooperative cancellation and cleanup.

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L34" sourceLabel="task.ts:34" />

Task ID for this handler invocation, including any TaskGroup prefix.

<MemberHeading id="trynumber" depth="3" name="tryNumber" sig="tryNumber: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-ts/#L38" sourceLabel="task.ts:38" />

Airflow try number for the current task attempt.
