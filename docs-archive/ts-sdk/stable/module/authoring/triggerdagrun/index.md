---
title: triggerDagRun
kind: function
longname: module:Authoring.triggerDagRun
description: "A task that triggers another Dag's run, passed to dag.task in place of a handler. dag.task(triggerDagRun({ dagId: \"downstream_etl\" }), { taskId: \"trigger_downstream\" })();"
---

# triggerDagRun

<Signature code="triggerDagRun(spec: TriggerDagRunSpec): TriggerDagRunTask" />

<SourceLink href="/source/src/sdk/trigger-dag-run-ts/#L129" label="trigger-dag-run.ts:129" />

A task that triggers another Dag's run, passed to `dag.task` in place of a handler.

```ts
dag.task(triggerDagRun({ dagId: "downstream_etl" }), { taskId: "trigger_downstream" })();
```

**Parameters**

- `spec` (TriggerDagRunSpec)

**Returns**

- `TriggerDagRunTask`
