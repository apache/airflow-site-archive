---
title: TaskInputs
kind: typedef
longname: module:Authoring.TaskInputs
description: Task references keyed by input name. Stored and validated, but they do not create dependencies or pass values yet — see {@link module:Authoring.TaskOptions#inputs|TaskOptions.inputs}. Each must identify an earlier task in the same Dag. Literal values are not supported.
---

# TaskInputs

<Signature code="TaskInputs = Readonly<Record<string, TaskRef>>" />

<SourceLink href="/source/src/sdk/dag-ts/#L79" label="dag.ts:79" />

Task references keyed by input name.

Stored and validated, but they do not create dependencies or pass values yet — see [TaskOptions.inputs](/module/authoring/taskoptions#inputs). Each must identify an earlier task in the same Dag. Literal values are not supported.
