---
title: GetXComOpts
kind: interface
longname: module:Types.GetXComOpts
description: Options for pulling an XCom value. dagId , taskId , and runId default to the running task's context. Pass them only when pulling an XCom value from another task or run.
---

# GetXComOpts

<Signature
  code="interface GetXComOpts {
	dagId?: string;
	includePriorDates?: boolean;
	key: string;
	mapIndex?: number | null;
	runId?: string;
	taskId?: string;
}"
/>

<SourceLink href="/source/src/sdk/client-types-ts/#L30" label="client-types.ts:30" />

Options for pulling an XCom value.

`dagId`, `taskId`, and `runId` default to the running task's context. Pass them only when pulling an XCom value from another task or run.

---

## Properties

<MemberHeading id="dagid" depth="3" name="dagId" sig="dagId: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L32" sourceLabel="client-types.ts:32" />

<MemberHeading id="includepriordates" depth="3" name="includePriorDates" sig="includePriorDates: boolean" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L36" sourceLabel="client-types.ts:36" />

<MemberHeading id="key" depth="3" name="key" sig="key: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L31" sourceLabel="client-types.ts:31" />

<MemberHeading id="mapindex" depth="3" name="mapIndex" sig="mapIndex: number | null" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L35" sourceLabel="client-types.ts:35" />

<MemberHeading id="runid" depth="3" name="runId" sig="runId: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L33" sourceLabel="client-types.ts:33" />

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta sourceHref="/source/src/sdk/client-types-ts/#L34" sourceLabel="client-types.ts:34" />
