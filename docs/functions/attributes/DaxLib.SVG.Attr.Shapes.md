---
title: Attr.Shape
parent: Attributes
grand_parent: Functions
nav_order: 1
---

# DaxLib.SVG.Attr.Shapes

Creates SVG attribute strings for common shape styling properties

## Syntax

```dax
DaxLib.SVG.Attr.Shapes( fill, fillOpacity, fillRule, stroke, strokeWidth, strokeOpacity, opacity )
```

| Parameter     | Type      | Required  | Description                                   |
|:---:|:---:|:---:|---|
| fill          | <span class="type-label string">STRING</span>    |  No       | Fill color (e.g., "#FF0000", "red")         |
| fillOpacity   | <span class="type-label number">DOUBLE</span>    |  No       | Fill opacity value between 0 and 1            |
| fillRule      | <span class="type-label string">STRING</span>    |  No       | Fill rule ("nonzero", "evenodd")              |
| stroke        | <span class="type-label string">STRING</span>    |  No       | Stroke color (e.g., "#000000", "black")     |
| strokeWidth   | <span class="type-label int64">INT64</span>     |  No       | Width of the stroke                           |
| strokeOpacity | <span class="type-label number">DOUBLE</span>    |  No       | Stroke opacity value between 0 and 1          |
| opacity       | <span class="type-label number">DOUBLE</span>    |  No       | Overall opacity value between 0 and 1         |

## Returns

<span class="type-label string">STRING</span> An attribute string that can be used directly in SVG elements

## Example

```dax
DaxLib.SVG.Attr.Shapes("#FF0000", 0.8, "nonzero", "#000000", 2, 1, 1)
// Returns "fill='#FF0000' fill-opacity='0.8' fill-rule='nonzero' stroke='#000000' stroke-width='2' stroke-opacity='1' opacity='1' "
```

## Definition

```dax
function 'DaxLib.SVG.Attr.Shapes' = 
    (
        fill: STRING,
        fillOpacity: DOUBLE,
        fillRule: STRING,
        stroke: STRING,
        strokeWidth: INT64,
        strokeOpacity: DOUBLE,
        opacity: DOUBLE
    ) =>

        IF( NOT ISBLANK( fill ),          "fill='" & fill & "' ") &
        IF( NOT ISBLANK( fillOpacity ),   "fill-opacity='" & fillOpacity & "' ") &
        IF( NOT ISBLANK( fillRule ),      "fill-rule='" & fillRule & "' ") &
        IF( NOT ISBLANK( stroke ),        "stroke='" & stroke & "' ") &
        IF( NOT ISBLANK( strokeWidth ),   "stroke-width='" & strokeWidth & "' ") &
        IF( NOT ISBLANK( strokeOpacity ), "stroke-opacity='" & strokeOpacity & "' ") &
        IF( NOT ISBLANK( opacity ),       "opacity='" & opacity & "' ")
```