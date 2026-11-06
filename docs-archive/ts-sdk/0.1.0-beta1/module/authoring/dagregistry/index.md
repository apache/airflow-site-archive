---
title: DagRegistry
kind: class
longname: module:Authoring.DagRegistry
description: "The Dags a bundle process can execute, keyed by Dag ID. This is what a bundle entry point builds and hands to serveDags(registry) : const dag = new Dag(\"my_dag\"); dag.task(\"extract\", extractFn); await serveDags(new DagRegistry(dag)); It holds no sockets and starts nothing, so a test can build one and invoke a handler through {@link module:Authoring.DagRegistry#getTaskHandler|getTaskHandler} without any runtime in scope. Lookups delegate live to each Dag's task map, so tasks added to a Dag after registration are visible — the registry records Dag identity, not a snapshot of its tasks."
---

# DagRegistry

<SourceLink href="/source/src/sdk/registry-ts/#L59" label="registry.ts:59" />

The Dags a bundle process can execute, keyed by Dag ID.

This is what a bundle entry point builds and hands to `serveDags(registry)`:

```ts
const dag = new Dag("my_dag");
dag.task("extract", extractFn);
await serveDags(new DagRegistry(dag));
```

It holds no sockets and starts nothing, so a test can build one and invoke a handler through [getTaskHandler](/module/authoring/dagregistry#gettaskhandler) without any runtime in scope.

Lookups delegate live to each Dag's task map, so tasks added to a Dag after registration are visible — the registry records Dag identity, not a snapshot of its tasks.

---

## Constructors

<MemberHeading id="constructor" depth="3" name="constructor" sig="new DagRegistry(...dags: Dag[]): DagRegistry" />

**Parameters**

- `dags` ([Dag](/module/authoring/dag)\[])

**Returns**

`DagRegistry`

---

## Methods

<MemberHeading
  id="gettaskhandler"
  depth="3"
  name="getTaskHandler"
  sig="getTaskHandler(
	dagId: string,
	taskId: string,
): TaskHandler | undefined"
/>

<MemberMeta sourceHref="/source/src/sdk/registry-ts/#L104" sourceLabel="registry.ts:104" />

Look up a registered handler, the way the runtime dispatches a task. Returns `undefined` when no handler exists.

**Parameters**

- `dagId` (string)
- `taskId` (string)

**Returns**

- [`TaskHandler`](/module/authoring/taskhandler)` | undefined`

<MemberHeading id="register" depth="3" name="register" sig="register(...dags: Dag[]): void" />

<MemberMeta sourceHref="/source/src/sdk/registry-ts/#L77" sourceLabel="registry.ts:77" />

Register Dags. Registering an already-registered `dagId` throws, and a call that throws registers none of its Dags.

The constructor covers the common case; this is for a bundle that collects its Dags across several modules.

**Parameters**

- `dags` ([Dag](/module/authoring/dag)\[])

**Returns**

- `void`
