---
title: Label
kind: class
longname: module:Authoring.Label
description: "A text label for an edge. The Airflow UI shows the label on the edge in the graph, as it does for Python's Label . The text comes before the task that the label is put on. That way the text sits between the two tasks of the edge in the code, just as the label sits between them in the graph: // load >> Label(\"when empty\") >> report_empty loaded.before(Label.of(\"when empty\").on(reportedEmpty)); // load >> Label(\"always\") >> cleanup cleaned.after(Label.of(\"always\").on(loaded));"
---

# Label

<SourceLink href="/source/src/sdk/dag-ts/#L364" label="dag.ts:364" />

A text label for an edge. The Airflow UI shows the label on the edge in the graph, as it does for Python's `Label`. The text comes before the task that the label is put on. That way the text sits between the two tasks of the edge in the code, just as the label sits between them in the graph:

```ts
// load >> Label("when empty") >> report_empty
loaded.before(Label.of("when empty").on(reportedEmpty));
// load >> Label("always") >> cleanup
cleaned.after(Label.of("always").on(loaded));
```

---

## Constructors

<MemberHeading id="constructor" depth="3" name="constructor" sig="new Label(): Label" />

**Returns**

`Label`

---

## Methods

<MemberHeading id="on" depth="3" name="on" sig="on(node: Node, ...more: readonly Node[]): Node" />

<MemberMeta sourceHref="/source/src/sdk/dag-ts/#L408" sourceLabel="dag.ts:408" />

Put the label on each edge that a `before` or `after` call draws between its receiver and `node` or a node in `more`.

So each edge of a fan-out can have its own label, and one label can go on several edges:

```ts
checked.before(Label.of("rows found").on(processed), Label.of("no rows").on(reportedEmpty));
// load >> Label("forks") >> [report_empty, notify]
loaded.before(Label.of("forks").on(reportedEmpty, notified));
```

Pass the value that `on` returns to `before` or `after`. Calling `before` or `after` on that value throws an error.

**Parameters**

- `node` (Node)
- `more` (readonly Node\[])

**Returns**

- `Node`

## Static Methods

<MemberHeading id="of" depth="3" name="of" sig="of(text: string): Label" />

<MemberMeta badges="static" sourceHref="/source/src/sdk/dag-ts/#L389" sourceLabel="dag.ts:389" />

Make a label with the given `text`. Use `on` to put the label on edges. `text` must not be empty or only whitespace.

**Parameters**

- `text` (string)

**Returns**

- [`Label`](/module/authoring/label)
