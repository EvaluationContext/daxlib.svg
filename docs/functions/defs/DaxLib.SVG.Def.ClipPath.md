---
title: Def.ClipPath
nav_order: 5.2
parent: Defs
---

# DaxLib.SVG.Def.ClipPath

Creates a reusable `<clipPath>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.ClipPath(defId, elements)
```

## Parameters

| Name     | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| defId    | STRING | Yes      | The unique identifier for the clip path (e.g., "cut-top")          |
| elements | STRING | Yes      | The SVG element(s) that make up the clipping path                  |

## Returns

(*STRING*) `<clipPath>`{:.xml} definition

## Example

```dax
DaxLib.SVG.Def.ClipPath(
    "cut-bottom",
    "<rect x='0' y='50' width='100' height='50'/>"
)
// Returns: <clipPath id='cut-bottom'><rect x='0' y='50' width='100' height='50'/></clipPath>
```

## Definition

```dax
function 'DaxLib.SVG.Def.ClipPath' =
    (
        defId: STRING,
        elements: STRING
    ) =>

        "<clipPath id='" & defId & "'>" &
        elements &
        "</clipPath>"
```