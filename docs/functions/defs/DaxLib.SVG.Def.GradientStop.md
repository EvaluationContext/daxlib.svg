---
title: Def.GradientStop
nav_order: 7
parent: Defs
---

# DaxLib.SVG.Def.GradientStop

Generates a gradient `<stop>`{:.xml} element for use in SVG gradients

## Syntax

```dax
DaxLib.SVG.Def.GradientStop( offset, color, opacity )
```

| Name    | Type   | Required | Description                      |
|:---:|:---:|:---:|---|
| offset  | <span class="type-label string">STRING</span> | Yes      | Stop position                   |
| color   | <span class="type-label string">STRING</span> | Yes      | color value (hex or named color) |
| opacity | <span class="type-label string">STRING</span> | No       | opacity value         |

## Returns

<span class="type-label string">**STRING**</span> `<stop>`{:.xml} element

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
        color: STRING,
        opacity: STRING
    ) =>

        "<stop offset='" & offset & 
        "' stop-color='" & color & "'" &
        IF( NOT ISBLANK( opacity ), " stop-opacity='" & opacity & "'" ) &
        "/>"
```