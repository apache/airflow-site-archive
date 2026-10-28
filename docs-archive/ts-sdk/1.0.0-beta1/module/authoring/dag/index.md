---
title: Dag
kind: class
longname: module:Authoring.Dag
description: "A Dag declared in TypeScript. Declare the tasks with dag.task(taskId, handler) , then call what each returns to lay the Dag out: const extract = dag.task(\"extract\", async (): Promise&#x3C;number> => 42); const load = dag.task(\"load\", async ({ rows }: { rows: number }) => {}); load({ rows: extract() }); Every task has to be called exactly once, so none can be left out of the Dag by accident. A TypeScript handler for a task that a Python Dag declares is a TaskHandler instead, not a task on a Dag . Constructing a Dag has no effect beyond the instance itself. Collect the ones a bundle should serve on a Bundle and await bundle.serve() ."
---

# Dag

<SourceLink href="/source/src/sdk/dag-ts/#L678" label="dag.ts:678" />

A Dag declared in TypeScript.

Declare the tasks with `dag.task(taskId, handler)`, then call what each returns to lay the Dag out:

```ts
const extract = dag.task("extract", async (): Promise<number> => 42);
const load = dag.task("load", async ({ rows }: { rows: number }) => {});
load({ rows: extract() });
```

Every task has to be called exactly once, so none can be left out of the Dag by accident. A TypeScript handler for a task that a _Python_ Dag declares is a `TaskHandler` instead, not a task on a `Dag`.

Constructing a Dag has no effect beyond the instance itself. Collect the ones a bundle should serve on a `Bundle` and await `bundle.serve()`.

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

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L680" sourceLabel="dag.ts:680" />

Identifier of this Dag.

<MemberHeading id="spec" depth="3" name="spec" sig="spec: DagSpec" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L682" sourceLabel="dag.ts:682" />

Dag-level options this instance was constructed with, copied and frozen.

## Accessors

<MemberHeading id="taskids" depth="3" name="taskIds" sig="get taskIds(): readonly string[]" />

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L726" sourceLabel="dag.ts:726" />

Task IDs attached to this Dag, in attachment order.

## Methods

<MemberHeading
  id="if"
  depth="3"
  name="if"
  sig="if<
	TArgs extends void | object = void,
>(
	handler: (args: TArgs) => boolean | Promise<boolean>,
	...args: DeciderArgs<NoInfer<TArgs>>,
): Condition"
/>

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L791" sourceLabel="dag.ts:791" />

Declare a task whose boolean picks a branch; the side not taken is skipped.

```ts
dag.if(hasRows, { rows: validated }).then(loadIfReady).else(loadFallback);
dag.if(hasRows, { rows: validated }, { taskId: "has_rows", retries: 2 }).then(loadIfReady);
```

**Type Parameters**

- `TArgs` extends `void | object` = `void`

**Parameters**

- `handler` ((args: TArgs) => boolean | Promise\<boolean>)
- `args` (DeciderArgs\<NoInfer\<TArgs>>)

**Returns**

- `Condition`

<MemberHeading
  id="switch"
  depth="3"
  name="switch"
  sig="switch<
	TArgs extends void | object = void,
>(
	handler: (args: TArgs) => TaskRef<unknown> | Promise<TaskRef<unknown>>,
	...args: DeciderArgs<NoInfer<TArgs>>,
): Branch"
/>

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L901" sourceLabel="dag.ts:901" />

Declare a task that returns one of its cases; every other case is skipped.

```ts
dag.switch(pickPath, { rows: extracted }).case(handleLong).case(handleShort);
```

**Type Parameters**

- `TArgs` extends `void | object` = `void`

**Parameters**

- `handler` ((args: TArgs) => [TaskRef](/module/authoring/taskref)\<unknown> | Promise\<[TaskRef](/module/authoring/taskref)\<unknown>>)
- `args` (DeciderArgs\<NoInfer\<TArgs>>)

**Returns**

- `Branch`

<MemberHeading id="task" depth="3" name="task" sig="task" />

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L744" sourceLabel="dag.ts:744" />

Declare a task of this Dag, and return the factory that places it.

A handler takes one object of named arguments, and every argument in it becomes an input of the returned TaskFactory; `getContext()` and `getClient()` reach the runtime from inside the call, so neither is an argument. The trailing options object carries this task's own [TaskSpec](/module/authoring/taskspec).

```ts
const extract = dag.task("extract", async () => 42);
const transform = dag.task(async function transform() {}); // id "transform"
```

<Signature
  code="task<
	TArgs extends void | object = void,
	TReturn = unknown,
>(
	taskId: string,
	handler: (args: TArgs) => TReturn | Promise<TReturn>,
	options?: TaskSpec,
): TaskFactory<TArgs, TReturn>"
/>

**Type Parameters**

- `TArgs` extends `void | object` = `void`
- `TReturn` = `unknown`

**Parameters**

- `taskId` (string)
- `handler` ((args: TArgs) => TReturn | Promise\<TReturn>)
- `options` ([TaskSpec](/module/authoring/taskspec), optional)

**Returns**

- `TaskFactory<TArgs, TReturn>`

<Signature
  code="task<
	TArgs extends void | object = void,
	TReturn = unknown,
>(
	handler: (args: TArgs) => TReturn | Promise<TReturn>,
	options?: TaskSpec,
): TaskFactory<TArgs, TReturn>"
/>

Declare a task whose id is the handler's function name.

`airflow-ts-pack` keeps handler names intact, so minification cannot change a task id. An anonymous handler has no name to take one from, and needs [TaskSpec.taskId](/module/authoring/taskspec#taskid) to give it one.

**Type Parameters**

- `TArgs` extends `void | object` = `void`
- `TReturn` = `unknown`

**Parameters**

- `handler` ((args: TArgs) => TReturn | Promise\<TReturn>)
- `options` ([TaskSpec](/module/authoring/taskspec), optional)

**Returns**

- `TaskFactory<TArgs, TReturn>`

<Signature
  code="task<
	TArgs extends void | object = void,
	TResult = unknown,
>(
	taskId: string,
	operator: Operator<TArgs, TResult>,
	options?: TaskSpec,
): TaskFactory<TArgs, TResult>"
/>

Declare a task an operator runs, such as `triggerDagRun(spec)`. Its inputs and result are the operator's own. It has no handler to take an id from, so the id is required.

**Type Parameters**

- `TArgs` extends `void | object` = `void`
- `TResult` = `unknown`

**Parameters**

- `taskId` (string)
- `operator` (Operator\<TArgs, TResult>)
- `options` ([TaskSpec](/module/authoring/taskspec), optional)

**Returns**

- `TaskFactory<TArgs, TResult>`

<Signature
  code="task<
	TArgs extends void | object = void,
	TResult = unknown,
>(
	operator: Operator<TArgs, TResult>,
	options: TaskSpec,
): TaskFactory<TArgs, TResult>"
/>

Declare a task of this Dag, and return the factory that places it.

A handler takes one object of named arguments, and every argument in it becomes an input of the returned TaskFactory; `getContext()` and `getClient()` reach the runtime from inside the call, so neither is an argument. The trailing options object carries this task's own [TaskSpec](/module/authoring/taskspec).

```ts
const extract = dag.task("extract", async () => 42);
const transform = dag.task(async function transform() {}); // id "transform"
```

**Type Parameters**

- `TArgs` extends `void | object` = `void`
- `TResult` = `unknown`

**Parameters**

- `operator` (Operator\<TArgs, TResult>)
- `options` ([TaskSpec](/module/authoring/taskspec))

**Returns**

- `TaskFactory<TArgs, TResult>`

<MemberHeading
  id="taskgroup"
  depth="3"
  name="taskGroup"
  sig="taskGroup(
	groupId: string,
	options?: TaskGroupOptions,
): TaskGroupRef"
/>

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L977" sourceLabel="dag.ts:977" />

Declare a task group of this Dag.

The group prefixes the id of everything declared in it, unless TaskGroupOptions.prefixGroupId turns that off, and stands at either end of an order-only edge in its own right.

```ts
const staging = dag.taskGroup("staging"); // tasks "staging.<id>"
const checks = dag.taskGroup("checks", { prefixGroupId: false }); // ids as written
```

**Parameters**

- `groupId` (string)
- `options` (TaskGroupOptions, optional)

**Returns**

- `TaskGroupRef`
