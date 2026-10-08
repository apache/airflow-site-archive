---
title: Dag
kind: class
longname: module:Authoring.Dag
description: A Dag declared in TypeScript. Today the Dag structure itself is still declared by a Python stub file; a Dag instance binds TypeScript handlers to that stub's Dag/task IDs. The instance retains its spec and every task's (taskId, handler, spec) so a future serialize() can produce the serialized Dag JSON for native TypeScript Dag declaration. Constructing a Dag has no effect beyond the instance itself. Collect the ones a bundle should serve in a DagRegistry and pass it to serveDags(...) .
---

# Dag

<SourceLink href="/source/src/sdk/dag-ts/#L135" label="dag.ts:135" />

A Dag declared in TypeScript.

Today the Dag structure itself is still declared by a Python stub file; a `Dag` instance binds TypeScript handlers to that stub's Dag/task IDs. The instance retains its `spec` and every task's `(taskId, handler, spec)` so a future `serialize()` can produce the serialized Dag JSON for native TypeScript Dag declaration.

Constructing a Dag has no effect beyond the instance itself. Collect the ones a bundle should serve in a `DagRegistry` and pass it to `serveDags(...)`.

---

## Constructors

<MemberHeading id="constructor" depth="3" name="constructor" sig="new Dag(dagId: string, spec: DagSpec): Dag" />

**Parameters**

- `dagId` (string)
- `spec` ([DagSpec](/module/authoring/dagspec), default: "{}")

**Returns**

`Dag`

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L137" sourceLabel="dag.ts:137" />

Identifier of this Dag. Must match the Python Dag's `dag_id`.

<MemberHeading id="spec" depth="3" name="spec" sig="spec: DagSpec" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L139" sourceLabel="dag.ts:139" />

Dag-level options this instance was constructed with, copied and frozen.

## Accessors

<MemberHeading id="taskids" depth="3" name="taskIds" sig="get taskIds(): readonly string[]" />

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L158" sourceLabel="dag.ts:158" />

Task IDs attached to this Dag, in attachment order.

## Methods

<MemberHeading
  id="task"
  depth="3"
  name="task"
  sig="task<
	TReturn = unknown,
>(
	taskId: string,
	handler: TaskHandler<TReturn>,
	options: TaskOptions,
): TaskRef"
/>

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L168" sourceLabel="dag.ts:168" />

Register a TypeScript handler for a task of this Dag.

`taskId` must match the Dag-side operator's `task_id` exactly, including any TaskGroup prefix. Returns this task's handle.

**Type Parameters**

- `TReturn` = `unknown`

**Parameters**

- `taskId` (string)
- `handler` ([TaskHandler](/module/authoring/taskhandler)\<TReturn>)
- `options` ([TaskOptions](/module/authoring/taskoptions), default: "{}")

**Returns**

- [`TaskRef`](/module/authoring/taskref)
