---
title: getClient
kind: function
longname: module:Authoring.getClient
description: "Client for reading and writing Airflow task-time data for the task currently running. async function transform() { const client = getClient(); return await client.getXCom&#x3C;number>({ key: \"return_value\", taskId: \"extract\" }); } Work that outlives the handler is the one gap. Async context propagates into a promise created inside the handler, so one it never awaits still resolves, but it runs after the task's terminal state has been reported and writes to a finished task. Await everything a handler starts."
---

# getClient

<Signature code="getClient(): TaskClient" />

<SourceLink href="/source/src/sdk/task-ts/#L127" label="task.ts:127" />

Client for reading and writing Airflow task-time data for the task currently running.

```ts
async function transform() {
  const client = getClient();
  return await client.getXCom<number>({ key: "return_value", taskId: "extract" });
}
```

Work that outlives the handler is the one gap. Async context propagates into a promise created inside the handler, so one it never awaits still resolves, but it runs after the task's terminal state has been reported and writes to a finished task. Await everything a handler starts.

**Returns**

- [`TaskClient`](/module/authoring/taskclient)

**Throws**

- when called outside a task handler.
