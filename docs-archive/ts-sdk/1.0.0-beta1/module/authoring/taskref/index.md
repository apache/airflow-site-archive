---
title: TaskRef
kind: interface
longname: module:Authoring.TaskRef
---

# TaskRef

<Signature
  code="interface TaskRef<TReturn = unknown> extends Node {
	dagId: string;
	taskId: string;
	after(...upstream: readonly Node[]): TaskRef<TReturn>;
	before(...downstream: readonly Node[]): TaskRef<TReturn>;
}"
/>

<SourceLink href="/source/src/sdk/dag-ts/#L171" label="dag.ts:171" />

**Type Parameters**

- `TReturn` = `unknown`

#### Hierarchy

- `Node`
- `TaskRef`

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L173" sourceLabel="dag.ts:173" />

_Overrides&#x20;_`dagId`

Identifier of the Dag this task belongs to.

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L175" sourceLabel="dag.ts:175" />

Airflow task ID, including any TaskGroup prefix.

## Methods

<MemberHeading id="after" depth="3" name="after" sig="after(...upstream: readonly Node[]): TaskRef<TReturn>" />

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L203" sourceLabel="dag.ts:203" />

_Overrides&#x20;_`after`

Run this task after each of `upstream`, carrying no value — Python's `<<`.

```ts
cleaned.after(loaded, transformed); // [load, transform] >> cleanup
```

Fan-_in_ that carries data is the wiring object instead (`summarize({ north: extractNorth(), south: extractSouth() })`), so each direction has an answer: named keys when values flow, `after` when only order does.

**Parameters**

- `upstream` (readonly Node\[])

**Returns**

- [`TaskRef`](/module/authoring/taskref)`<TReturn>`

<MemberHeading id="before" depth="3" name="before" sig="before(...downstream: readonly Node[]): TaskRef<TReturn>" />

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L190" sourceLabel="dag.ts:190" />

_Overrides&#x20;_`before`

Run this task before each of `downstream`, carrying no value — the TypeScript spelling of Python's `>>`.

```ts
loaded.before(cleaned, notified); // loaded >> [cleanup, notify]
```

Variadic, so one call fans out, and it returns its own receiver rather than its arguments: a fan-out has no single "next" reference to hand back. Declaring an edge that already exists changes nothing.

**Parameters**

- `downstream` (readonly Node\[])

**Returns**

- [`TaskRef`](/module/authoring/taskref)`<TReturn>`
