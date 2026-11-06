---
title: Bundle
kind: class
longname: module:Authoring.Bundle
description: "What a bundle process provides to Airflow, and the thing that serves it. A bundle entry point builds one, registers what it provides, and awaits serve() at module top level: const dag = new Dag(\"my_dag\"); dag.task(\"extract\", extractFn); const bundle = new Bundle(); bundle.register(dag); await bundle.serve(); Registering holds no sockets and starts nothing, so a test can build a bundle and invoke a handler through {@link module:Authoring.Bundle#getTaskHandler|getTaskHandler} without any runtime in scope. Only serve() connects to Airflow. Lookups delegate live to each Dag's task map, so tasks added to a Dag after registration are visible: the bundle records Dag identity, not a snapshot of its tasks."
---

# Bundle

<SourceLink href="/source/src/sdk/bundle-ts/#L70" label="bundle.ts:70" />

What a bundle process provides to Airflow, and the thing that serves it.

A bundle entry point builds one, registers what it provides, and awaits `serve()` at module top level:

```ts
const dag = new Dag("my_dag");
dag.task("extract", extractFn);

const bundle = new Bundle();
bundle.register(dag);
await bundle.serve();
```

Registering holds no sockets and starts nothing, so a test can build a bundle and invoke a handler through [getTaskHandler](/module/authoring/bundle#gettaskhandler) without any runtime in scope. Only `serve()` connects to Airflow.

Lookups delegate live to each Dag's task map, so tasks added to a Dag after registration are visible: the bundle records Dag identity, not a snapshot of its tasks.

---

## Constructors

<MemberHeading id="constructor" depth="3" name="constructor" sig="new Bundle(...items: Registerable[]): Bundle" />

**Parameters**

- `items` ([Registerable](/module/authoring/registerable)\[])

**Returns**

`Bundle`

---

## Methods

<MemberHeading
  id="gettaskhandler"
  depth="3"
  name="getTaskHandler"
  sig="getTaskHandler(
	dagId: string,
	taskId: string,
): TaskFunction | undefined"
/>

<MemberMeta sourceHref="/source/src/sdk/bundle-ts/#L153" sourceLabel="bundle.ts:153" />

Look up a registered handler, the way the runtime dispatches a task. Returns `undefined` when no handler exists.

**Parameters**

- `dagId` (string)
- `taskId` (string)

**Returns**

- [`TaskFunction`](/module/authoring/taskfunction)` | undefined`

<MemberHeading id="register" depth="3" name="register" sig="register(...items: Registerable[]): void" />

<MemberMeta sourceHref="/source/src/sdk/bundle-ts/#L93" sourceLabel="bundle.ts:93" />

Register what this bundle provides. Registering an already-registered `dagId` throws, and a call that throws registers none of its items.

The constructor covers the common case; this is for a bundle that collects what it provides across several modules.

**Parameters**

- `items` ([Registerable](/module/authoring/registerable)\[])

**Returns**

- `void`

<MemberHeading id="serve" depth="3" name="serve" sig="serve(): Promise<void>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/bundle-ts/#L140" sourceLabel="bundle.ts:140" />

Serve this bundle to Airflow. The entry point of a TypeScript Dag bundle.

A bundle process serves one supervisor request, so a second call, which would connect a second pair of sockets, is rejected. A call that fails is not a serve, and may be retried. Resolves once the supervisor has been sent the terminal frame for the work this process was started for, and the same call answers the build-time `--airflow-metadata` query `airflow-ts-pack` makes.

Everything this bundle provides must be registered before `serve()` is awaited: what is left out is not part of the bundle, and its tasks are marked removed at runtime.

**Returns**

- `Promise<void>`
