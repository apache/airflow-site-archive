---
title: getContext
kind: function
longname: module:Authoring.getContext
description: Runtime metadata for the task currently running. async function transform() { throw new Error(`task ${getContext().taskId} has nothing to transform`); }
---

# getContext

<Signature code="getContext(): TaskContext" />

<SourceLink href="/source/src/sdk/task-ts/#L105" label="task.ts:105" />

Runtime metadata for the task currently running.

```ts
async function transform() {
  throw new Error(`task ${getContext().taskId} has nothing to transform`);
}
```

**Returns**

- [`TaskContext`](/module/authoring/taskcontext)

**Throws**

- when called outside a task handler.
