---
title: DagSpec
kind: interface
longname: module:Authoring.DagSpec
description: "Dag-level options: the schedule, the tags, how many runs may be active, and the rest of what DAG(...) takes in Python. Every field is optional, so {} stays valid and a field added later cannot break a call site. An unknown key is rejected, so a misspelled field is an error rather than a Dag that quietly ignores it. queue is the one hand-written field: Airflow's schema has no Dag-level queue, but every task of a native Dag runs on the same coordinator, so the queue that routes them there belongs on the Dag rather than on each task."
---

# DagSpec

<Signature
  code="interface DagSpec extends GeneratedDagFields {
	catchup?: boolean;
	dagDisplayName?: string;
	dagrunTimeout?: number;
	description?: string;
	disableBundleVersioning?: boolean;
	docMd?: string;
	endDate?: Date;
	failFast?: boolean;
	isPausedUponCreation?: boolean;
	maxActiveRuns?: number;
	maxActiveTasks?: number;
	maxConsecutiveFailedDagRuns?: number;
	queue?: string;
	renderTemplateAsNativeObj?: boolean;
	schedule?: string;
	startDate?: Date;
	tags?: readonly string[];
}"
/>

<SourceLink href="/source/src/sdk/dag-ts/#L107" label="dag.ts:107" />

Dag-level options: the schedule, the tags, how many runs may be active, and the rest of what `DAG(...)` takes in Python.

Every field is optional, so `{}` stays valid and a field added later cannot break a call site. An unknown key is rejected, so a misspelled field is an error rather than a Dag that quietly ignores it.

`queue` is the one hand-written field: Airflow's schema has no Dag-level queue, but every task of a native Dag runs on the same coordinator, so the queue that routes them there belongs on the Dag rather than on each task.

#### Hierarchy

- `GeneratedDagFields`
- `DagSpec`

---

## Properties

<MemberHeading id="catchup" depth="3" name="catchup" sig="catchup: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L58" sourceLabel="dag-schema-fields.ts:58" />

_Inherited from&#x20;_`catchup`

Maps to the schema key `catchup`.

<MemberHeading id="dagdisplayname" depth="3" name="dagDisplayName" sig="dagDisplayName: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L46" sourceLabel="dag-schema-fields.ts:46" />

_Inherited from&#x20;_`dagDisplayName`

Maps to the schema key `dag_display_name`.

<MemberHeading id="dagruntimeout" depth="3" name="dagrunTimeout" sig="dagrunTimeout: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L56" sourceLabel="dag-schema-fields.ts:56" />

_Inherited from&#x20;_`dagrunTimeout`

Maps to the schema key `dagrun_timeout`, in seconds.

<MemberHeading id="description" depth="3" name="description" sig="description: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L38" sourceLabel="dag-schema-fields.ts:38" />

_Inherited from&#x20;_`description`

Maps to the schema key `description`.

<MemberHeading id="disablebundleversioning" depth="3" name="disableBundleVersioning" sig="disableBundleVersioning: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L64" sourceLabel="dag-schema-fields.ts:64" />

_Inherited from&#x20;_`disableBundleVersioning`

Maps to the schema key `disable_bundle_versioning`.

<MemberHeading id="docmd" depth="3" name="docMd" sig="docMd: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L48" sourceLabel="dag-schema-fields.ts:48" />

_Inherited from&#x20;_`docMd`

Maps to the schema key `doc_md`.

<MemberHeading id="enddate" depth="3" name="endDate" sig="endDate: Date" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L42" sourceLabel="dag-schema-fields.ts:42" />

_Inherited from&#x20;_`endDate`

Maps to the schema key `end_date`.

<MemberHeading id="failfast" depth="3" name="failFast" sig="failFast: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L60" sourceLabel="dag-schema-fields.ts:60" />

_Inherited from&#x20;_`failFast`

Maps to the schema key `fail_fast` (schema default `false`).

<MemberHeading id="ispauseduponcreation" depth="3" name="isPausedUponCreation" sig="isPausedUponCreation: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L66" sourceLabel="dag-schema-fields.ts:66" />

_Inherited from&#x20;_`isPausedUponCreation`

Maps to the schema key `is_paused_upon_creation`.

<MemberHeading id="maxactiveruns" depth="3" name="maxActiveRuns" sig="maxActiveRuns: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L52" sourceLabel="dag-schema-fields.ts:52" />

_Inherited from&#x20;_`maxActiveRuns`

Maps to the schema key `max_active_runs`.

<MemberHeading id="maxactivetasks" depth="3" name="maxActiveTasks" sig="maxActiveTasks: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L50" sourceLabel="dag-schema-fields.ts:50" />

_Inherited from&#x20;_`maxActiveTasks`

Maps to the schema key `max_active_tasks`.

<MemberHeading id="maxconsecutivefaileddagruns" depth="3" name="maxConsecutiveFailedDagRuns" sig="maxConsecutiveFailedDagRuns: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L54" sourceLabel="dag-schema-fields.ts:54" />

_Inherited from&#x20;_`maxConsecutiveFailedDagRuns`

Maps to the schema key `max_consecutive_failed_dag_runs`.

<MemberHeading id="queue" depth="3" name="queue" sig="queue: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L115" sourceLabel="dag.ts:115" />

Queue the Dag's tasks run on, unless a task names its own.

A native Dag's tasks are executed by the Node coordinator, which the deployment's `queue_to_coordinator` maps a queue to, so this is what routes them there. `queue` on a [TaskSpec](/module/authoring/taskspec) wins for that task.

<MemberHeading id="rendertemplateasnativeobj" depth="3" name="renderTemplateAsNativeObj" sig="renderTemplateAsNativeObj: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L62" sourceLabel="dag-schema-fields.ts:62" />

_Inherited from&#x20;_`renderTemplateAsNativeObj`

Maps to the schema key `render_template_as_native_obj` (schema default `false`).

<MemberHeading id="schedule" depth="3" name="schedule" sig="schedule: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L36" sourceLabel="dag-schema-fields.ts:36" />

_Inherited from&#x20;_`schedule`

When the Dag runs: `"@once"`, `"@continuous"`, a cron expression, or unset for no schedule. The serializer lowers it onto the schema's `timetable` object.

<MemberHeading id="startdate" depth="3" name="startDate" sig="startDate: Date" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L40" sourceLabel="dag-schema-fields.ts:40" />

_Inherited from&#x20;_`startDate`

Maps to the schema key `start_date`.

<MemberHeading id="tags" depth="3" name="tags" sig="tags: readonly string[]" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L44" sourceLabel="dag-schema-fields.ts:44" />

_Inherited from&#x20;_`tags`

Maps to the schema key `tags`.
