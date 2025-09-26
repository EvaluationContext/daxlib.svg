---
title: Style.Line
nav_order: 6.2
parent: Styles
---

# DaxLib.SVG.Style.Line

Line and stroke style properties for SVG elements

## Syntax

```dax
DaxLib.SVG.Style.Line(strokeDasharray, strokeDashoffset, strokeLinecap, strokeLinejoin, strokeMiterlimit)
```

## Parameters

| Name            | Type   | Required | Description                                 |
|:---:|:---:|:---:|:---:|
| strokeDasharray | STRING | No       | Stroke dasharray (e.g., "5,5" for dashed)   |
| strokeDashoffset| INT64  | No       | Stroke dashoffset                           |
| strokeLinecap   | STRING | No       | Stroke linecap ("butt", "round", "square")  |
| strokeLinejoin  | STRING | No       | Stroke linejoin ("miter", "round", "bevel") |
| strokeMiterlimit| INT64  | No       | Miter limit for stroke joins                |

## Returns

(*STRING*) style string

## Example

```dax
DaxLib.SVG.Style.Line(
	"5,5", 
	0, 
	"round", 
	"miter", 
	4
)
// Returns: stroke-dasharray:5,5;stroke-dashoffset:0;stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:4;
```

## Definition
```dax
function 'DaxLib.SVG.Style.Line' = 
    (
        strokeDasharray: STRING,
        strokeDashoffset: INT64,
        strokeLinecap: STRING,
        strokeLinejoin: STRING,
        strokeMiterlimit: INT64
    ) =>

        VAR _StrokeDasharray =  IF( NOT ISBLANK( strokeDasharray ),  "stroke-dasharray:" & strokeDasharray & ";" )
        VAR _StrokeDashoffset = IF( NOT ISBLANK( strokeDashoffset ), "stroke-dashoffset:" & strokeDashoffset & ";" )
        VAR _StrokeLinecap =    IF( NOT ISBLANK( strokeLinecap ),    "stroke-linecap:" & strokeLinecap & ";" )
        VAR _StrokeLinejoin =   IF( NOT ISBLANK( strokeLinejoin ),   "stroke-linejoin:" & strokeLinejoin & ";" )
        VAR _StrokeMiterlimit = IF( NOT ISBLANK( strokeMiterlimit ), "stroke-miterlimit:" & strokeMiterlimit & ";" )

        RETURN
		
            _StrokeDasharray &
            _StrokeDashoffset &
            _StrokeLinecap &
            _StrokeLinejoin &
            _StrokeMiterlimit
```
