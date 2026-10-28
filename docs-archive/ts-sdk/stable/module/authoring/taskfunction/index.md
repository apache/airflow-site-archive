---
title: TaskFunction
kind: typedef
longname: module:Authoring.TaskFunction
description: "Function signature for a TypeScript task handler. TArgs describes what the Dag's call site passes. {@link module:Authoring.getContext|getContext} and {@link module:Authoring.getClient|getClient} reach the runtime from inside the call, so neither is a parameter. interface TransformArgs { regionCode: string; threshold: number; } async function transform({ regionCode, threshold }: TransformArgs) { // ... } A handler that takes no arguments declares no parameter. Non- undefined return values are automatically pushed to XCom under the \"return_value\" key, matching Python @task behavior."
---

# TaskFunction

<Signature code="TaskFunction<TArgs = void, TReturn = unknown> = (args: TArgs) => TReturn | Promise<TReturn>" />

<SourceLink href="/source/src/sdk/task-ts/#L154" label="task.ts:154" />

Function signature for a TypeScript task handler.

`TArgs` describes what the Dag's call site passes. [getContext](/module/authoring/getcontext) and [getClient](/module/authoring/getclient) reach the runtime from inside the call, so neither is a parameter.

```ts
interface TransformArgs {
  regionCode: string;
  threshold: number;
}

async function transform({ regionCode, threshold }: TransformArgs) {
  // ...
}
```

A handler that takes no arguments declares no parameter.

Non-`undefined` return values are automatically pushed to XCom under the `"return_value"` key, matching Python `@task` behavior.

**Type Parameters**

- `TArgs` = `void`
- `TReturn` = `unknown`

**Parameters**

- `args` (TArgs)

**Returns**

- `TReturn | Promise<TReturn>`
