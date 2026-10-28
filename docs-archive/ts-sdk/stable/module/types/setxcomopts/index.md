---
title: SetXComOpts
kind: interface
longname: module:Types.SetXComOpts
description: Options for pushing an XCom value. dagId , taskId , and runId default to the running task's context.
---

# SetXComOpts

<Signature
  code="interface SetXComOpts {
	dagId?: string;
	key: string;
	mapIndex?: number | null;
	runId?: string;
	taskId?: string;
	value: JsonValue;
}"
/>

<SourceLink href="/source/src/sdk/client-types-ts/#L44" label="client-types.ts:44" />

Options for pushing an XCom value.

`dagId`, `taskId`, and `runId` default to the running task's context.

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L47" sourceLabel="client-types.ts:47" />

<MemberHeading id="key" depth="3" name="key" sig="key: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L45" sourceLabel="client-types.ts:45" />

<MemberHeading id="mapindex" depth="3" name="mapIndex" sig="mapIndex: number | null" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L50" sourceLabel="client-types.ts:50" />

<MemberHeading id="runid" depth="3" name="runId" sig="runId: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L48" sourceLabel="client-types.ts:48" />

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L49" sourceLabel="client-types.ts:49" />

<MemberHeading id="value" depth="3" name="value" sig="value: JsonValue" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L46" sourceLabel="client-types.ts:46" />
