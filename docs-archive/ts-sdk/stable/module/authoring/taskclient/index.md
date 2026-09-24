---
title: TaskClient
kind: interface
longname: module:Authoring.TaskClient
description: Client for reading and writing Airflow task-time data from a task handler. The active runtime selects the concrete transport and implements this interface for the current task attempt.
---

# TaskClient

<Signature
  code="interface TaskClient {
	getConnection(connId: string): Promise<ConnectionResult | null>;
	getConnectionOrThrow(connId: string): Promise<ConnectionResult>;
	getVariable(key: string): Promise<string | null>;
	getVariableOrThrow(key: string): Promise<string>;
	getXCom<T = unknown>(opts: GetXComOpts): Promise<T | null>;
	setXCom(opts: SetXComOpts): Promise<void>;
}"
/>

<SourceLink href="/source/src/sdk/client-ts/#L28" label="client.ts:28" />

Client for reading and writing Airflow task-time data from a task handler.

The active runtime selects the concrete transport and implements this interface for the current task attempt.

---

## Methods

<MemberHeading id="getconnection" depth="3" name="getConnection" sig="getConnection(connId: string): Promise<ConnectionResult | null>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L82" sourceLabel="client.ts:82" />

Look up an Airflow Connection by ID.

Returns `null` when the connection does not exist. Throws on any other error.

This is intentionally JS-friendly behavior. Use [getConnectionOrThrow](/module/authoring/taskclient#getconnectionorthrow) when missing connections should raise.

**Parameters**

- `connId` (string)

**Returns**

- `Promise<`[`ConnectionResult`](/module/types/connectionresult)` | null>`

<MemberHeading id="getconnectionorthrow" depth="3" name="getConnectionOrThrow" sig="getConnectionOrThrow(connId: string): Promise<ConnectionResult>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L91" sourceLabel="client.ts:91" />

Look up an Airflow Connection by ID and raise when it is missing.

This matches Python `BaseHook.get_connection` behavior.

**Parameters**

- `connId` (string)

**Returns**

- `Promise<`[`ConnectionResult`](/module/types/connectionresult)`>`

**Throws**

- [ConnectionNotFoundError](/module/exceptions/connectionnotfounderror) when the connection does not exist.

<MemberHeading id="getvariable" depth="3" name="getVariable" sig="getVariable(key: string): Promise<string | null>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L38" sourceLabel="client.ts:38" />

Look up an Airflow Variable.

Returns `null` when the key is missing or stored with a null value. Throws on any other error.

This is intentionally JS-friendly behavior. Use [getVariableOrThrow](/module/authoring/taskclient#getvariableorthrow) when missing variables should raise.

**Parameters**

- `key` (string)

**Returns**

- `Promise<string | null>`

<MemberHeading id="getvariableorthrow" depth="3" name="getVariableOrThrow" sig="getVariableOrThrow(key: string): Promise<string>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L48" sourceLabel="client.ts:48" />

Look up an Airflow Variable and raise when it is missing.

This matches Python `Variable.get` behavior when no default value is supplied.

**Parameters**

- `key` (string)

**Returns**

- `Promise<string>`

**Throws**

- [VariableNotFoundError](/module/exceptions/variablenotfounderror) when the key is missing.

<MemberHeading id="getxcom" depth="3" name="getXCom" sig="getXCom<T = unknown>(opts: GetXComOpts): Promise<T | null>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L64" sourceLabel="client.ts:64" />

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

<MemberHeading id="setxcom" depth="3" name="setXCom" sig="setXCom(opts: SetXComOpts): Promise<void>" />

<MemberMeta badges="async" sourceHref="/source/src/sdk/client-ts/#L71" sourceLabel="client.ts:71" />

Push an XCom value.

Target fields default to the current task's context.

**Parameters**

- `opts` ([SetXComOpts](/module/types/setxcomopts))

**Returns**

- `Promise<void>`
