---
title: TaskStateStoreSetOpts
kind: interface
longname: module:Types.TaskStateStoreSetOpts
description: Options for a task state store write.
---

# TaskStateStoreSetOpts

<Signature
  code="interface TaskStateStoreSetOpts {
	retention?: number | typeof NEVER_EXPIRE;
}"
/>

<SourceLink href="/source/src/sdk/client-types-ts/#L64" label="client-types.ts:64" />

Options for a task state store write.

---

## Properties

<MemberHeading id="retention" depth="3" name="retention" sig="retention: number | typeof NEVER_EXPIRE" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L73" sourceLabel="client-types.ts:73" />

How long to keep the key, in seconds, counted from the write; `0` expires it immediately.

Omitting it follows the deployment's `[state_store] default_retention_days`, which the coordinator passes to the runtime. Pass [NEVER\_EXPIRE](/module/authoring/never-expire) to store the key with no expiry regardless of that default.
