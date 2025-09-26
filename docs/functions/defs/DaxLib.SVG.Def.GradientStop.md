---
title: Def.GradientStop
nav_order: 5.3
parent: Defs
---

# DaxLib.SVG.Def.GradientStop

Creates a gradient `<stop>`{:.xml} element for use in SVG gradients

## Syntax

```dax
DaxLib.SVG.Def.GradientStop(offset, colour, opacity)
```

## Parameters

| Name    | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| offset  | STRING | Yes      | Stop position (e.g., "0%", "100%")                                 |
| colour  | STRING | Yes      | Colour value (hex or named colour)                                 |
| opacity | STRING | No       | Opacity value                                            		   |

## Returns

(*STRING*) `<stop>`{:.xml} element

## Example

```dax

DaxLib.SVG.Def.GradientStop("0%", "red", "1")
// Returns: <stop offset='0%' stop-color='red' stop-opacity='1'/>

```

## Definition

```dax
function 'DaxLib.SVG.Def.GradientStop' =
    (
        offset: STRING,
        colour: STRING,
        opacity: STRING
    ) =>

        "<stop offset='" & offset &
        "' stop-color='" & colour & "'" &
        IF( NOT ISBLANK( opacity ), " stop-opacity='" & opacity & "'" ) &
        "/>"
```