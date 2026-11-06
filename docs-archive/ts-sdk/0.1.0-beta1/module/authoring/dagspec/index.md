---
title: DagSpec
kind: typedef
longname: module:Authoring.DagSpec
description: "Dag-level options. No fields yet, so only {} is accepted: a field that would be silently dropped — new Dag(\"d\", { schedule: \"@daily\" }) — is a compile error. Native Dag declaration will add optional fields here, generated from the serialized-Dag JSON schema as src/generated/supervisor.ts is."
---

# DagSpec

<Signature code="DagSpec = Record<string, never>" />

<SourceLink href="/source/src/sdk/dag-ts/#L46" label="dag.ts:46" />

Dag-level options.

No fields yet, so only `{}` is accepted: a field that would be silently dropped — `new Dag("d", { schedule: "@daily" })` — is a compile error.

Native Dag declaration will add optional fields here, generated from the serialized-Dag JSON schema as `src/generated/supervisor.ts` is.
