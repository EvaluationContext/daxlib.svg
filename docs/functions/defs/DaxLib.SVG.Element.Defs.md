---
title: Element.Defs
nav_order: 1
parent: Defs
---

# DaxLib.SVG.Element.Defs

Creates a `<defs>`{:.xml} element from one or more `DaxLib.SVG.Def.*` elements

## Syntax

```dax
DaxLib.SVG.Element.Defs(defs)
```

## Parameters

| Name | Type   | Required | Description                                                    |
|------|--------|----------|----------------------------------------------------------------|
| defs | STRING | Yes      | Concatenated list of def elements to include in a defs block   |

## Returns

(*STRING*) `<defs>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Defs(
	DaxLib.SVG.Def.Circle(...) &
	DaxLib.SVG.Def.Rect(...)
)
// Returns: <defs>...</defs>
```

## Definition

```dax
function 'DaxLib.SVG.Element.Defs' = 
    (
        defs: STRING
    ) =>

        "<defs>" &
        defs &
        "</defs>"
```