---
title: TaskOptions
kind: typedef
longname: module:Authoring.TaskOptions
description: "The trailing argument of dag.task() : the task's own {@link module:Authoring.TaskSpec|TaskSpec}. Every field is optional, and an unknown key is rejected, so a misspelled field is an error rather than a task that quietly ignores it."
---

# TaskOptions

<Signature code="TaskOptions = TaskSpec" />

<SourceLink href="/source/src/sdk/dag-ts/#L552" label="dag.ts:552" />

The trailing argument of `dag.task()`: the task's own [TaskSpec](/module/authoring/taskspec).

Every field is optional, and an unknown key is rejected, so a misspelled field is an error rather than a task that quietly ignores it.
