---
title: TaskClient
kind: interface
longname: module:Authoring.TaskClient
description: Client for reading and writing Airflow task-time data from a task handler. The active runtime selects the concrete transport and implements this interface for the current task attempt.
---

# TaskClient

<Signature
  code="interface TaskClient {
	taskStateStore: TaskStateStore;
	deleteVariable(key: string): Promise<void>;
	getConnection(connId: string): Promise<ConnectionResult | null>;
	getConnectionOrThrow(connId: string): Promise<ConnectionResult>;
	getVariable(key: string): Promise<string | null>;
	getVariableOrThrow(key: string): Promise<string>;
	getXCom<T = unknown>(opts: GetXComOpts): Promise<T | null>;
	setVariable(key: string, value: string, description?: string | null): Promise<void>;
	setXCom(opts: SetXComOpts): Promise<void>;
}"
/>

<SourceLink href="/source/src/sdk/client-ts/#L34" label="client.ts:34" />

Client for reading and writing Airflow task-time data from a task handler.

The active runtime selects the concrete transport and implements this interface for the current task attempt.

---

## Properties

<MemberHeading id="taskstatestore" depth="3" name="taskStateStore" sig="taskStateStore: TaskStateStore" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/client-ts/#L102" sourceLabel="client.ts:102" />

Key/value state private to this task instance.

See [TaskStateStore](/module/authoring/taskstatestore).

## Methods

<MemberHeading id="deletevariable" depth="3" name="deleteVariable" sig="deleteVariable(key: string): Promise<void>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L72" sourceLabel="client.ts:72" />

Delete an Airflow Variable.

Resolves even when the key does not exist — the Execution API's delete route is idempotent and does not report a missing key as an error.

**Parameters**

- `key` (string)

**Returns**

- `Promise<void>`

<MemberHeading id="getconnection" depth="3" name="getConnection" sig="getConnection(connId: string): Promise<ConnectionResult | null>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L113" sourceLabel="client.ts:113" />

Look up an Airflow Connection by ID.

Returns `null` when the connection does not exist. Throws on any other error.

This is intentionally JS-friendly behavior. Use [getConnectionOrThrow](/module/authoring/taskclient#getconnectionorthrow) when missing connections should raise.

**Parameters**

- `connId` (string)

**Returns**

- `Promise<`[`ConnectionResult`](/module/types/connectionresult)` | null>`

<MemberHeading id="getconnectionorthrow" depth="3" name="getConnectionOrThrow" sig="getConnectionOrThrow(connId: string): Promise<ConnectionResult>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L122" sourceLabel="client.ts:122" />

Look up an Airflow Connection by ID and raise when it is missing.

This matches Python `BaseHook.get_connection` behavior.

**Parameters**

- `connId` (string)

**Returns**

- `Promise<`[`ConnectionResult`](/module/types/connectionresult)`>`

**Throws**

- [ConnectionNotFoundError](/module/exceptions/connectionnotfounderror) when the connection does not exist.

<MemberHeading id="getvariable" depth="3" name="getVariable" sig="getVariable(key: string): Promise<string | null>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L44" sourceLabel="client.ts:44" />

Look up an Airflow Variable.

Returns `null` when the key is missing or stored with a null value. Throws on any other error.

This is intentionally JS-friendly behavior. Use [getVariableOrThrow](/module/authoring/taskclient#getvariableorthrow) when missing variables should raise.

**Parameters**

- `key` (string)

**Returns**

- `Promise<string | null>`

<MemberHeading id="getvariableorthrow" depth="3" name="getVariableOrThrow" sig="getVariableOrThrow(key: string): Promise<string>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L54" sourceLabel="client.ts:54" />

Look up an Airflow Variable and raise when it is missing.

This matches Python `Variable.get` behavior when no default value is supplied.

**Parameters**

- `key` (string)

**Returns**

- `Promise<string>`

**Throws**

- [VariableNotFoundError](/module/exceptions/variablenotfounderror) when the key is missing.

<MemberHeading id="getxcom" depth="3" name="getXCom" sig="getXCom<T = unknown>(opts: GetXComOpts): Promise<T | null>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L88" sourceLabel="client.ts:88" />

Pull an XCom value.

Returns `null` when the row is missing. Locator fields default to the current task's context.

The generic `T` lets callers narrow the return type when the shape is known:

```ts
const data = await client.getXCom<{ count: number }>({ key: "result" });
// data is { count: number } | null
```

**Type Parameters**

- `T` = `unknown`

**Parameters**

- `opts` ([GetXComOpts](/module/types/getxcomopts))

**Returns**

- `Promise<T | null>`

<MemberHeading
  id="setvariable"
  depth="3"
  name="setVariable"
  sig="setVariable(
	key: string,
	value: string,
	description?: string | null,
): Promise<void>"
/>

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L64" sourceLabel="client.ts:64" />

Store an Airflow Variable, replacing any existing value.

The value is stored as a string. Serialize structured data (for example with `JSON.stringify`) before storing it.

Omitting `description` clears the description the Variable had.

**Parameters**

- `key` (string)
- `value` (string)
- `description` (string | null, optional)

**Returns**

- `Promise<void>`

<MemberHeading id="setxcom" depth="3" name="setXCom" sig="setXCom(opts: SetXComOpts): Promise<void>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L95" sourceLabel="client.ts:95" />

Push an XCom value.

Target fields default to the current task's context.

**Parameters**

- `opts` ([SetXComOpts](/module/types/setxcomopts))

**Returns**

- `Promise<void>`
