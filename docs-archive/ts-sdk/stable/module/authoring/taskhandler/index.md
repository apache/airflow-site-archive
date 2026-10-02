---
title: TaskHandler
kind: typedef
longname: module:Authoring.TaskHandler
description: Function signature for a TypeScript task handler. Non- undefined return values are automatically pushed to XCom under the "return_value" key, matching Python @task behavior. Return undefined or omit a return value to skip the automatic XCom push.
---

# TaskHandler

<Signature code="TaskHandler<TReturn = unknown> = (args: TaskHandlerArgs) => TReturn | Promise<TReturn>" />

<SourceLink href="/source/src/sdk/task-ts/#L61" label="task.ts:61" />

Function signature for a TypeScript task handler.

Non-`undefined` return values are automatically pushed to XCom under the `"return_value"` key, matching Python `@task` behavior. Return `undefined` or omit a return value to skip the automatic XCom push.

**Type Parameters**

- `TReturn` = `unknown`

**Parameters**

- `args` ([TaskHandlerArgs](/module/authoring/taskhandlerargs))

**Returns**

- `TReturn | Promise<TReturn>`
