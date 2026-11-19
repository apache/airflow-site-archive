---
title: withArgNames
kind: function
longname: module:Authoring.withArgNames
description: "Bind an argument explicitly, naming it on both sides. Mapping first, handler second. An entry takes precedence over folding, and everything the map does not mention still folds: interface ReportArgs { label: string; // Python calls this `run_label` threshold: number; } const report = withArgNames({ label: \"run_label\" }, async ({ label, threshold }: ReportArgs) => { // `label` is the call's `run_label`; `threshold` folded as usual. }); bundle.register(new TaskHandler(\"etl\", \"report\", report)); Folding absorbs ordinary spelling differences, so this is for a name that genuinely differs: a clearer word than the Dag chose, or a TypeScript reserved word like enum . It should be rare in a real Dag. The map's keys are checked against the handler's own parameter type, so { labl: \"run_label\" } is a compile error. Its values are Python names, which tsc cannot check."
---

# withArgNames

<Signature
  code="withArgNames<
	TArgs,
	TReturn,
>(
	names: ArgNameMap<NoInfer<TArgs>>,
	handler: TaskFunction<TArgs, TReturn>,
): TaskFunction<TArgs, TReturn>"
/>

<SourceLink href="/source/src/sdk/arg-names-ts/#L88" label="arg-names.ts:88" />

Bind an argument explicitly, naming it on both sides.

Mapping first, handler second. An entry takes precedence over folding, and everything the map does not mention still folds:

```ts
interface ReportArgs {
  label: string; // Python calls this `run_label`
  threshold: number;
}

const report = withArgNames({ label: "run_label" }, async ({ label, threshold }: ReportArgs) => {
  // `label` is the call's `run_label`; `threshold` folded as usual.
});

bundle.register(new TaskHandler("etl", "report", report));
```

Folding absorbs ordinary spelling differences, so this is for a name that genuinely differs: a clearer word than the Dag chose, or a TypeScript reserved word like `enum`. It should be rare in a real Dag.

The map's keys are checked against the handler's own parameter type, so `{ labl: "run_label" }` is a compile error. Its values are Python names, which `tsc` cannot check.

**Type Parameters**

- `TArgs`
- `TReturn`

**Parameters**

- `names` ([ArgNameMap](/module/authoring/argnamemap)\<NoInfer\<TArgs>>)
- `handler` ([TaskFunction](/module/authoring/taskfunction)\<TArgs, TReturn>)

**Returns**

- [`TaskFunction`](/module/authoring/taskfunction)`<TArgs, TReturn>`
