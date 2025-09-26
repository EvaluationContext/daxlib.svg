---
title: Style.Common
nav_order: 6.1
parent: Styles
---

# DaxLib.SVG.Style.Common

Style properties common to all SVG elements

## Syntax

```dax
DaxLib.SVG.Style.Common(fill, fillOpacity, stroke, strokeWidth, strokeOpacity, opacity)
```

## Parameters

| Name         | Type   | Required | Description                          |
|:---:|:---:|:---:|:---:|
| fill         | STRING | No       | Fill color or gradient reference     |
| fillOpacity  | DOUBLE | No       | Fill opacity (0-1)                   |
| stroke       | STRING | No       | Stroke color                         |
| strokeWidth  | INT64  | No       | Stroke width                         |
| strokeOpacity| DOUBLE | No       | Stroke opacity (0-1)                 |
| opacity      | DOUBLE | No       | Overall opacity (0-1)                |

## Returns

(*STRING*) style string

## Example

```dax
DaxLib.SVG.Style.Common(
	"#01B8AA", 
	0.8, 
	"#000", 
	2, 
	1, 
	0.9
)
// Returns: fill:#01B8AA;fill-opacity:0.8;stroke:#000;stroke-width:2;stroke-opacity:1;opacity:0.9;
```

## Definition

```dax
function 'DaxLib.SVG.Style.Common' = 
    (
        fill: STRING,
        fillOpacity: DOUBLE,
        stroke: STRING,
        strokeWidth: INT64,
        strokeOpacity: DOUBLE,
        opacity: DOUBLE
    ) =>

        VAR _Fill =          IF( NOT ISBLANK( fill ),          "fill:" & fill & ";" )
        VAR _FillOpacity =   IF( NOT ISBLANK( fillOpacity ),   "fill-opacity:" & fillOpacity & ";" )
        VAR _Stroke =        IF( NOT ISBLANK( stroke ),        "stroke:" & stroke & ";" )
        VAR _StrokeWidth =   IF( NOT ISBLANK( strokeWidth ),   "stroke-width:" & strokeWidth & ";" )
        VAR _StrokeOpacity = IF( NOT ISBLANK( strokeOpacity ), "stroke-opacity:" & strokeOpacity & ";" )
        VAR _Opacity =       IF( NOT ISBLANK( opacity ),       "opacity:" & opacity & ";" )

        RETURN

            _Fill &
            _FillOpacity &
            _Stroke &
            _StrokeWidth &
            _StrokeOpacity &
            _Opacity 
```
