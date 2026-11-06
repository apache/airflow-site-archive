---
title: NEVER_EXPIRE
kind: variable
longname: module:Authoring.NEVER_EXPIRE
description: Pass as {@link module:Types.TaskStateStoreSetOpts#retention|TaskStateStoreSetOpts.retention} to store a task state store key with no expiry, regardless of the deployment default. A symbol rather than a number, so a retention that reaches Infinity by accident (a division by zero, for example) is rejected instead of silently storing a key forever.
---

# NEVER\_EXPIRE

<Signature code="NEVER_EXPIRE: unique symbol" />

<SourceLink href="/source/src/sdk/client-types-ts/#L61" label="client-types.ts:61" />

Pass as [TaskStateStoreSetOpts.retention](/module/types/taskstatestoresetopts#retention) to store a task state store key with no expiry, regardless of the deployment default.

A symbol rather than a number, so a retention that reaches `Infinity` by accident (a division by zero, for example) is rejected instead of silently storing a key forever.

**Type**

`unique symbol`
