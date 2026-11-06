---
title: hitl
kind: function
longname: module:HITL.hitl
description: "A task that asks a human to choose, passed to dag.task in place of a handler. Its first run creates the request and parks the task in awaiting_input , freeing the worker; a later run resumes with the response, pushes it to XCom as a {@link module:HITL.HITLResult|HITLResult}, and succeeds. The choice never skips or fails anything by itself. dag.task(\"choose_region\", hitl({ subject: ({ report }: { report: Report }) => `Pick a region for ${report.version}`, options: [\"us\", \"eu\"], }))({ report });"
---

# hitl

<Signature
  code="hitl<
	TSubjectArgs extends void | object = void,
	TBodyArgs extends void | object = TSubjectArgs,
>(
	spec: HITLSpec<TSubjectArgs, TBodyArgs>,
): HITLTask<HITLTextArgs<TSubjectArgs, TBodyArgs>>"
/>

<SourceLink href="/source/src/hitl/spec-ts/#L195" label="spec.ts:195" />

A task that asks a human to choose, passed to `dag.task` in place of a handler.

Its first run creates the request and parks the task in `awaiting_input`, freeing the worker; a later run resumes with the response, pushes it to XCom as a [HITLResult](/module/hitl/hitlresult), and succeeds. The choice never skips or fails anything by itself.

```ts
dag.task("choose_region", hitl({
  subject: ({ report }: { report: Report }) => `Pick a region for ${report.version}`,
  options: ["us", "eu"],
}))({ report });
```

**Type Parameters**

- `TSubjectArgs` extends `void | object` = `void`
- `TBodyArgs` extends `void | object` = `TSubjectArgs`

**Parameters**

- `spec` ([HITLSpec](/module/hitl/hitlspec)\<TSubjectArgs, TBodyArgs>)

**Returns**

- [`HITLTask`](/module/hitl/hitltask)`<`[`HITLTextArgs`](/module/hitl/hitltextargs)`<TSubjectArgs, TBodyArgs>>`
