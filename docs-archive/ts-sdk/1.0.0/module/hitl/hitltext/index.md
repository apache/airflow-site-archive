---
title: HITLText
kind: typedef
longname: module:HITL.HITLText
description: "Text shown to the responder: fixed, or computed from the task's inputs on its first run."
---

# HITLText

<Signature code="HITLText<TArgs, TText extends string | null = string> = TText | ((args: TArgs) => TText | Promise<TText>)" />

<SourceLink href="/source/src/hitl/spec-ts/#L38" label="spec.ts:38" />

Text shown to the responder: fixed, or computed from the task's inputs on its first run.

**Type Parameters**

- `TArgs`
- `TText` extends `string | null` = `string`
