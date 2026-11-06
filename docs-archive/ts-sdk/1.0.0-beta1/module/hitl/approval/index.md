---
title: approval
kind: function
longname: module:HITL.approval
description: "A task that asks a human to approve or reject, passed to dag.task in place of a handler. Offers exactly \"Approve\" and \"Reject\", which is what the Airflow UI shows as an approval. On \"Reject\" it skips what follows, or fails when {@link module:HITL.ApprovalSpec#failOnReject|ApprovalSpec.failOnReject} is set. dag.task(\"sign_off\", approval({ subject: \"Ship it?\" }))().before(publish());"
---

# approval

<Signature
  code="approval<
	TSubjectArgs extends void | object = void,
	TBodyArgs extends void | object = TSubjectArgs,
>(
	spec: ApprovalSpec<TSubjectArgs, TBodyArgs>,
): HITLTask<HITLTextArgs<TSubjectArgs, TBodyArgs>>"
/>

<SourceLink href="/source/src/hitl/spec-ts/#L232" label="spec.ts:232" />

A task that asks a human to approve or reject, passed to `dag.task` in place of a handler.

Offers exactly "Approve" and "Reject", which is what the Airflow UI shows as an approval. On "Reject" it skips what follows, or fails when [ApprovalSpec.failOnReject](/module/hitl/approvalspec#failonreject) is set.

```ts
dag.task("sign_off", approval({ subject: "Ship it?" }))().before(publish());
```

**Type Parameters**

- `TSubjectArgs` extends `void | object` = `void`
- `TBodyArgs` extends `void | object` = `TSubjectArgs`

**Parameters**

- `spec` ([ApprovalSpec](/module/hitl/approvalspec)\<TSubjectArgs, TBodyArgs>)

**Returns**

- [`HITLTask`](/module/hitl/hitltask)`<`[`HITLTextArgs`](/module/hitl/hitltextargs)`<TSubjectArgs, TBodyArgs>>`
