---
title: serveDags
kind: function
longname: module:Authoring.serveDags
description: "Serve a bundle's Dags to Airflow. The entry point of a TypeScript Dag bundle. Build the Dags, attach a handler per task with dag.task(...) , collect them in a {@link module:Authoring.DagRegistry|DagRegistry}, then await this at module top level: const dag = new Dag(\"my_dag\"); dag.task(\"extract\", extractFn); await serveDags(new DagRegistry(dag)); The registry is the bundle's complete set of Dags: this process serves one supervisor request, so a second call — which would connect a second pair of sockets — is rejected. A call that fails is not a serve, and may be retried. Resolves when Airflow's supervisor has been sent the terminal frame for the work this process was started for; the same call also answers the build-time --airflow-metadata query airflow-ts-pack makes."
---

# serveDags

<Signature code="serveDags(registry: DagRegistry): Promise<void>" />

<SourceLink href="/source/src/coordinator/runtime-ts/#L91" label="runtime.ts:91" />

**Modifiers:** `async`

Serve a bundle's Dags to Airflow. The entry point of a TypeScript Dag bundle.

Build the Dags, attach a handler per task with `dag.task(...)`, collect them in a [DagRegistry](/module/authoring/dagregistry), then await this at module top level:

```ts
const dag = new Dag("my_dag");
dag.task("extract", extractFn);
await serveDags(new DagRegistry(dag));
```

The registry is the bundle's complete set of Dags: this process serves one supervisor request, so a second call — which would connect a second pair of sockets — is rejected. A call that fails is not a serve, and may be retried. Resolves when Airflow's supervisor has been sent the terminal frame for the work this process was started for; the same call also answers the build-time `--airflow-metadata` query `airflow-ts-pack` makes.

**Parameters**

- `registry` ([DagRegistry](/module/authoring/dagregistry))

**Returns**

- `Promise<void>`
