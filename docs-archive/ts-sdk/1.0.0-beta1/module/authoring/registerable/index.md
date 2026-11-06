---
title: Registerable
kind: typedef
longname: module:Authoring.Registerable
description: "What {@link module:Authoring.Bundle#register|Bundle.register} and the {@link module:Authoring.Bundle|Bundle} constructor accept: a {@link module:Authoring.TaskHandler|TaskHandler} for a task that a Python Dag declares, or a {@link module:Authoring.Dag|Dag} declared in TypeScript."
---

# Registerable

<Signature code="Registerable = Dag | TaskHandler<never, unknown>" />

<SourceLink href="/source/src/sdk/bundle-ts/#L40" label="bundle.ts:40" />

What [Bundle.register](/module/authoring/bundle#register) and the [Bundle](/module/authoring/bundle) constructor accept: a [TaskHandler](/module/authoring/taskhandler) for a task that a Python Dag declares, or a [Dag](/module/authoring/dag) declared in TypeScript.
