---
title: TaskHandler
kind: class
longname: module:Authoring.TaskHandler
description: "A TypeScript function bound to the Python-owned task it implements. A mixed-language Dag declares its structure in Python, with a @task.stub per task routed to the Node coordinator. TypeScript supplies the task bodies and nothing else: no dag_id of its own, no schedule, no task order. const bundle = new Bundle(); bundle.register(new TaskHandler(\"etl\", \"transform\", transform)); await bundle.serve(); dagId must match the Python Dag's dag_id and taskId a @task.stub in it, including any TaskGroup prefix. Both are written out: nothing is derived from the handler's function name, which the build step is free to rename. Identity and a body, and no more. A handler has no factory to call, so wiring one the way a natively declared task is wired is a compile error rather than a runtime throw. For a native Dag, use {@link module:Authoring.Dag|Dag} instead."
---

# TaskHandler

<SourceLink href="/source/src/sdk/task-handler-ts/#L65" label="task-handler.ts:65" />

A TypeScript function bound to the Python-owned task it implements.

A mixed-language Dag declares its structure in Python, with a `@task.stub` per task routed to the Node coordinator. TypeScript supplies the task bodies and nothing else: no dag\_id of its own, no schedule, no task order.

```ts
const bundle = new Bundle();
bundle.register(new TaskHandler("etl", "transform", transform));
await bundle.serve();
```

`dagId` must match the Python Dag's `dag_id` and `taskId` a `@task.stub` in it, including any TaskGroup prefix. Both are written out: nothing is derived from the handler's function name, which the build step is free to rename.

Identity and a body, and no more. A handler has no factory to call, so wiring one the way a natively declared task is wired is a compile error rather than a runtime throw. For a native Dag, use [Dag](/module/authoring/dag) instead.

**Type Parameters**

- `TArgs` = `void`
- `TReturn` = `unknown`

---

## Constructors

<MemberHeading
  id="constructor"
  depth="3"
  name="constructor"
  sig="new TaskHandler<
	TArgs = void,
	TReturn = unknown,
>(
	dagId: string,
	taskId: string,
	handler: TaskFunction<TArgs, TReturn>,
): TaskHandler<TArgs, TReturn>"
/>

**Parameters**

- `dagId` (string)
- `taskId` (string)
- `handler` ([TaskFunction](/module/authoring/taskfunction)\<TArgs, TReturn>)

**Returns**

`TaskHandler<TArgs, TReturn>`

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-handler-ts/#L67" sourceLabel="task-handler.ts:67" />

Identifier of the Python Dag this task belongs to.

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/task-handler-ts/#L69" sourceLabel="task-handler.ts:69" />

Airflow task ID this handler implements, including any TaskGroup prefix.
