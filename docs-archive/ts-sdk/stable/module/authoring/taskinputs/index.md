---
title: TaskInputs
kind: typedef
longname: module:Authoring.TaskInputs
description: The inputs of a task, keyed by the name of the argument each one supplies.
---

# TaskInputs

<Signature code="TaskInputs<TArgs> = { [K in keyof TArgs]: TaskRef | JsonCompatible<TArgs[K]> }" />

<SourceLink href="/source/src/sdk/dag-ts/#L514" label="dag.ts:514" />

The inputs of a task, keyed by the name of the argument each one supplies.

**Type Parameters**

- `TArgs`
