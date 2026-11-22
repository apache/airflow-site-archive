---
title: TaskStateStore
kind: interface
longname: module:Authoring.TaskStateStore
description: "Key/value state private to one task instance, kept across its retries within the same Dag run. Reach it through {@link module:Authoring.TaskClient#taskStateStore|TaskClient.taskStateStore}: const store = getClient().taskStateStore; let jobId = await store.get&#x3C;string>(\"job_id\"); if (jobId == null) { jobId = await submit(); await store.set(\"job_id\", jobId, { retention: NEVER_EXPIRE }); } Values are stored in the metadata database as-is; the [workers] state_store_backend that Python tasks can configure is not applied here."
---

# TaskStateStore

<Signature
  code="interface TaskStateStore {
	clear(): Promise<void>;
	delete(key: string): Promise<void>;
	get<T = unknown>(key: string): Promise<T | null>;
	set(key: string, value: NonNullable<JsonValue>, opts?: TaskStateStoreSetOpts): Promise<void>;
}"
/>

<SourceLink href="/source/src/sdk/client-ts/#L143" label="client.ts:143" />

Key/value state private to one task instance, kept across its retries within the same Dag run.

Reach it through [TaskClient.taskStateStore](/module/authoring/taskclient#taskstatestore):

```ts
const store = getClient().taskStateStore;
let jobId = await store.get<string>("job_id");
if (jobId == null) {
  jobId = await submit();
  await store.set("job_id", jobId, { retention: NEVER_EXPIRE });
}
```

Values are stored in the metadata database as-is; the `[workers] state_store_backend` that Python tasks can configure is not applied here.

---

## Methods

<MemberHeading id="clear" depth="3" name="clear" sig="clear(): Promise<void>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L183" sourceLabel="client.ts:183" />

Delete every key stored for this task instance.

**Returns**

- `Promise<void>`

<MemberHeading id="delete" depth="3" name="delete" sig="delete(key: string): Promise<void>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L180" sourceLabel="client.ts:180" />

Delete a key.

Resolves even when the key does not exist — the Execution API's delete route is idempotent and does not report a missing key as an error.

**Parameters**

- `key` (string)

**Returns**

- `Promise<void>`

**Throws**

- `TypeError` when `key` is not a string.
- `RangeError` when `key` is empty.

<MemberHeading id="get" depth="3" name="get" sig="get<T = unknown>(key: string): Promise<T | null>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L155" sourceLabel="client.ts:155" />

Look up a value.

Returns `null` when the key is missing. Throws on any other error.

The generic `T` lets callers narrow the return type when the shape is known.

**Type Parameters**

- `T` = `unknown`

**Parameters**

- `key` (string)

**Returns**

- `Promise<T | null>`

**Throws**

- `TypeError` when `key` is not a string.
- `RangeError` when `key` is empty.

<MemberHeading
  id="set"
  depth="3"
  name="set"
  sig="set(
	key: string,
	value: NonNullable<JsonValue>,
	opts?: TaskStateStoreSetOpts,
): Promise<void>"
/>

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L169" sourceLabel="client.ts:169" />

Store a value, replacing any existing value for the key.

`opts.retention` is how long to keep the key, in seconds.

**Parameters**

- `key` (string)
- `value` (NonNullable\<[JsonValue](/module/types/jsonvalue)>)
- `opts` ([TaskStateStoreSetOpts](/module/types/taskstatestoresetopts), optional)

**Returns**

- `Promise<void>`

**Throws**

- `TypeError` when `key` is not a string, or `value` is null, undefined, NaN, or Infinity.
- `RangeError` when `key` is empty; when `retention` is negative, NaN, or Infinity; when the deployment's `[state_store] default_retention_days` is invalid; or when the resolved expiry would overflow the wire timestamp (year 9999).
