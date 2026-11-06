---
title: ArgNameMap
kind: typedef
longname: module:Authoring.ArgNameMap
description: A rename per argument, keyed by the handler's own parameter names. Every key is checked against the handler's parameter type, so a typo is a compile error naming the right key. The values are Python names, which tsc cannot see and does not check.
---

# ArgNameMap

<Signature code="ArgNameMap<TArgs> = { readonly [K in keyof TArgs]?: string }" />

<SourceLink href="/source/src/sdk/arg-names-ts/#L31" label="arg-names.ts:31" />

A rename per argument, keyed by the handler's own parameter names.

Every key is checked against the handler's parameter type, so a typo is a compile error naming the right key. The values are Python names, which `tsc` cannot see and does not check.

**Type Parameters**

- `TArgs`
