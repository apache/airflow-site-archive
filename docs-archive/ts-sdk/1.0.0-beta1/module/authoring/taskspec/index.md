---
title: TaskSpec
kind: interface
longname: module:Authoring.TaskSpec
description: "Task-level options: the retries, the pool, the trigger rule, and the rest of what an operator takes in Python. The task id is here too, for a handler whose id is not given positionally. Optional and record-only on the same terms as {@link module:Authoring.DagSpec|DagSpec}."
---

# TaskSpec

<Signature
  code="interface TaskSpec extends GeneratedTaskFields {
	dependsOnPast?: boolean;
	docMd?: string;
	doXcomPush?: boolean;
	emailOnFailure?: boolean;
	emailOnRetry?: boolean;
	endDate?: Date;
	executionTimeout?: number;
	executor?: string;
	ignoreFirstDependsOnPast?: boolean;
	mapIndexTemplate?: string;
	maxActiveTisPerDag?: number;
	maxActiveTisPerDagrun?: number;
	maxRetryDelay?: number;
	owner?: string;
	pool?: string;
	poolSlots?: number;
	priorityWeight?: number;
	queue?: string;
	retries?: number;
	retryDelay?: number;
	retryExponentialBackoff?: number;
	startDate?: Date;
	taskId?: string;
	triggerRule?: string;
	waitForDownstream?: boolean;
	waitForPastDependsBeforeSkipping?: boolean;
	weightRule?: string;
}"
/>

<SourceLink href="/source/src/sdk/dag-ts/#L125" label="dag.ts:125" />

Task-level options: the retries, the pool, the trigger rule, and the rest of what an operator takes in Python.

The task id is here too, for a handler whose id is not given positionally. Optional and record-only on the same terms as [DagSpec](/module/authoring/dagspec).

#### Hierarchy

- `GeneratedTaskFields`
- `TaskSpec`

---

## Properties

<MemberHeading id="dependsonpast" depth="3" name="dependsOnPast" sig="dependsOnPast: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L85" sourceLabel="dag-schema-fields.ts:85" />

_Inherited from&#x20;_`dependsOnPast`

Maps to the schema key `depends_on_past` (schema default `false`).

<MemberHeading id="docmd" depth="3" name="docMd" sig="docMd: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L121" sourceLabel="dag-schema-fields.ts:121" />

_Inherited from&#x20;_`docMd`

Maps to the schema key `doc_md`.

<MemberHeading id="doxcompush" depth="3" name="doXcomPush" sig="doXcomPush: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L115" sourceLabel="dag-schema-fields.ts:115" />

_Inherited from&#x20;_`doXcomPush`

Maps to the schema key `do_xcom_push` (schema default `true`).

<MemberHeading id="emailonfailure" depth="3" name="emailOnFailure" sig="emailOnFailure: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L117" sourceLabel="dag-schema-fields.ts:117" />

_Inherited from&#x20;_`emailOnFailure`

Maps to the schema key `email_on_failure` (schema default `true`).

<MemberHeading id="emailonretry" depth="3" name="emailOnRetry" sig="emailOnRetry: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L119" sourceLabel="dag-schema-fields.ts:119" />

_Inherited from&#x20;_`emailOnRetry`

Maps to the schema key `email_on_retry` (schema default `true`).

<MemberHeading id="enddate" depth="3" name="endDate" sig="endDate: Date" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L81" sourceLabel="dag-schema-fields.ts:81" />

_Inherited from&#x20;_`endDate`

Maps to the schema key `end_date`.

<MemberHeading id="executiontimeout" depth="3" name="executionTimeout" sig="executionTimeout: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L101" sourceLabel="dag-schema-fields.ts:101" />

_Inherited from&#x20;_`executionTimeout`

Maps to the schema key `execution_timeout`, in seconds.

<MemberHeading id="executor" depth="3" name="executor" sig="executor: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L113" sourceLabel="dag-schema-fields.ts:113" />

_Inherited from&#x20;_`executor`

Maps to the schema key `executor`.

<MemberHeading id="ignorefirstdependsonpast" depth="3" name="ignoreFirstDependsOnPast" sig="ignoreFirstDependsOnPast: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L87" sourceLabel="dag-schema-fields.ts:87" />

_Inherited from&#x20;_`ignoreFirstDependsOnPast`

Maps to the schema key `ignore_first_depends_on_past` (schema default `false`).

<MemberHeading id="mapindextemplate" depth="3" name="mapIndexTemplate" sig="mapIndexTemplate: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L123" sourceLabel="dag-schema-fields.ts:123" />

_Inherited from&#x20;_`mapIndexTemplate`

Maps to the schema key `map_index_template`.

<MemberHeading id="maxactivetisperdag" depth="3" name="maxActiveTisPerDag" sig="maxActiveTisPerDag: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L125" sourceLabel="dag-schema-fields.ts:125" />

_Inherited from&#x20;_`maxActiveTisPerDag`

Maps to the schema key `max_active_tis_per_dag`.

<MemberHeading id="maxactivetisperdagrun" depth="3" name="maxActiveTisPerDagrun" sig="maxActiveTisPerDagrun: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L127" sourceLabel="dag-schema-fields.ts:127" />

_Inherited from&#x20;_`maxActiveTisPerDagrun`

Maps to the schema key `max_active_tis_per_dagrun`.

<MemberHeading id="maxretrydelay" depth="3" name="maxRetryDelay" sig="maxRetryDelay: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L107" sourceLabel="dag-schema-fields.ts:107" />

_Inherited from&#x20;_`maxRetryDelay`

Maps to the schema key `max_retry_delay`, in seconds.

<MemberHeading id="owner" depth="3" name="owner" sig="owner: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L77" sourceLabel="dag-schema-fields.ts:77" />

_Inherited from&#x20;_`owner`

Maps to the schema key `owner` (schema default `"airflow"`).

<MemberHeading id="pool" depth="3" name="pool" sig="pool: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L97" sourceLabel="dag-schema-fields.ts:97" />

_Inherited from&#x20;_`pool`

Maps to the schema key `pool` (schema default `"default_pool"`).

<MemberHeading id="poolslots" depth="3" name="poolSlots" sig="poolSlots: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L99" sourceLabel="dag-schema-fields.ts:99" />

_Inherited from&#x20;_`poolSlots`

Maps to the schema key `pool_slots` (schema default `1`).

<MemberHeading id="priorityweight" depth="3" name="priorityWeight" sig="priorityWeight: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L109" sourceLabel="dag-schema-fields.ts:109" />

_Inherited from&#x20;_`priorityWeight`

Maps to the schema key `priority_weight` (schema default `1`).

<MemberHeading id="queue" depth="3" name="queue" sig="queue: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L95" sourceLabel="dag-schema-fields.ts:95" />

_Inherited from&#x20;_`queue`

Maps to the schema key `queue` (schema default `"default"`).

<MemberHeading id="retries" depth="3" name="retries" sig="retries: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L93" sourceLabel="dag-schema-fields.ts:93" />

_Inherited from&#x20;_`retries`

Maps to the schema key `retries` (schema default `0`).

<MemberHeading id="retrydelay" depth="3" name="retryDelay" sig="retryDelay: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L103" sourceLabel="dag-schema-fields.ts:103" />

_Inherited from&#x20;_`retryDelay`

Maps to the schema key `retry_delay`, in seconds (schema default `300`).

<MemberHeading id="retryexponentialbackoff" depth="3" name="retryExponentialBackoff" sig="retryExponentialBackoff: number" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L105" sourceLabel="dag-schema-fields.ts:105" />

_Inherited from&#x20;_`retryExponentialBackoff`

Maps to the schema key `retry_exponential_backoff` (schema default `0`).

<MemberHeading id="startdate" depth="3" name="startDate" sig="startDate: Date" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L79" sourceLabel="dag-schema-fields.ts:79" />

_Inherited from&#x20;_`startDate`

Maps to the schema key `start_date`.

<MemberHeading id="taskid" depth="3" name="taskId" sig="taskId: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/sdk/dag-ts/#L133" sourceLabel="dag.ts:133" />

Airflow task ID, when it should not be the handler's function name.

`dag.task(handler)` takes the id from the handler's name. Set this for an id that has to outlive that name, or for an anonymous handler, which has no name to take one from.

<MemberHeading id="triggerrule" depth="3" name="triggerRule" sig="triggerRule: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L83" sourceLabel="dag-schema-fields.ts:83" />

_Inherited from&#x20;_`triggerRule`

Maps to the schema key `trigger_rule` (schema default `"all_success"`).

<MemberHeading id="waitfordownstream" depth="3" name="waitForDownstream" sig="waitForDownstream: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L91" sourceLabel="dag-schema-fields.ts:91" />

_Inherited from&#x20;_`waitForDownstream`

Maps to the schema key `wait_for_downstream` (schema default `false`).

<MemberHeading id="waitforpastdependsbeforeskipping" depth="3" name="waitForPastDependsBeforeSkipping" sig="waitForPastDependsBeforeSkipping: boolean" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L89" sourceLabel="dag-schema-fields.ts:89" />

_Inherited from&#x20;_`waitForPastDependsBeforeSkipping`

Maps to the schema key `wait_for_past_depends_before_skipping` (schema default `false`).

<MemberHeading id="weightrule" depth="3" name="weightRule" sig="weightRule: string" />

<MemberMeta badges="readonly" sourceHref="/source/src/generated/dag-schema-fields-ts/#L111" sourceLabel="dag-schema-fields.ts:111" />

_Inherited from&#x20;_`weightRule`

Maps to the schema key `weight_rule` (schema default `"downstream"`).
