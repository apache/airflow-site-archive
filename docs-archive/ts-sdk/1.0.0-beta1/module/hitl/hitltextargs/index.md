---
title: HITLTextArgs
kind: typedef
longname: module:HITL.HITLTextArgs
description: "The inputs a task takes when its subject reads TSubject and its body reads TBody : both, or whichever is read. Bracketed, so that void is not distributed over."
---

# HITLTextArgs

<Signature code="HITLTextArgs<TSubject, TBody> = [TSubject, TBody] extends [void, void] ? void : [TSubject] extends [void] ? TBody : [TBody] extends [void] ? TSubject : TSubject & TBody" />

<SourceLink href="/source/src/hitl/spec-ts/#L158" label="spec.ts:158" />

The inputs a task takes when its subject reads `TSubject` and its body reads `TBody`: both, or whichever is read. Bracketed, so that `void` is not distributed over.

**Type Parameters**

- `TSubject`
- `TBody`
