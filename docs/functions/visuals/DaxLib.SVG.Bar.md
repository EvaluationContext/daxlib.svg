---
title: Bar
nav_order: 1.1
parent: Visuals
---

# DaxLib.SVG.Bar

Creates a bar SVG for a given column, with configurable colors for positive, negative, and zero axis values.

## Syntax

```dax
DaxLib.SVG.Bar(width, height, columnRef, positiveColor, negativeColor, zeroAxisColor)
```

## Parameters

| Name          | Type   | Required | Description                                      |
|:---:|:---:|:---:|:---:|
| width         | INT64  | Yes      | The width of the SVG canvas                      |
| height        | INT64  | Yes      | The height of the SVG canvas                     |
| columnRef     | ANYREF | Yes      | The column to visualize                          |
| positiveColor | STRING | Yes      | Hex color of the positive bar (e.g. "#01B8AA") |
| negativeColor | STRING | Yes      | Hex color of the negative bar (e.g. "#FD625E") |
| zeroAxisColor | STRING | Yes      | Hex color of the zero axis (e.g. "#A6A6A6")    |

## Returns

(*STRING*) SVG

## Example

```dax
DaxLib.SVG.Bar(100, 20, [Sales], "#01B8AA", "#FD625E", "#A6A6A6")
```

## Definition

```dax
function 'DaxLib.SVG.Bar' = 
    (
        width: INT64,
        height: INT64,
        columnRef: ANYREF,
        positiveColor: STRING,
        negativeColor: STRING,
        zeroAxisColor: STRING
    ) =>

        // X-axis scale
        VAR XMin = CALCULATE( MIN( columnRef ), ALLSELECTED() ) 
        VAR XMax = CALCULATE( MAX( columnRef ), ALLSELECTED() ) 

        // Map the zero point and the current value to the SVG's coordinate system
        VAR ZeroPoint = DaxLib.SVG.Calc.Normalize( 0, XMin, XMax, 0, width )
        VAR CurrentValue = SUM( columnRef )
        VAR ValuePoint =  DaxLib.SVG.Calc.Normalize( CurrentValue, XMin, XMax, 0, width )

        // Style
        VAR _PositiveColor = IF( NOT ISBLANK( positiveColor ), positiveColor, "#01B8AA" )
        VAR _NegativeColor = IF( NOT ISBLANK( negativeColor ), negativeColor, "#FD625E" )
        VAR _ZeroAxisColor = IF( NOT ISBLANK( zeroAxisColor ), zeroAxisColor, "#A6A6A6" )
        VAR ZeroAxisStyle =
            DaxLib.SVG.Style.Common(
                BLANK(), BLANK(), _ZeroAxisColor, 1, BLANK(), BLANK()
            )
        VAR RectColour = IF( CurrentValue >= 0, _PositiveColor, _NegativeColor )
        VAR RectStyle =
            DaxLib.SVG.Style.Common(
                RectColour, BLANK(), RectColour, BLANK(), BLANK(), BLANK()
            )

        // Rect
        VAR RectWidth =  ABS( ValuePoint - ZeroPoint )
        VAR RectX =      IF( ValuePoint > ZeroPoint, ZeroPoint, ValuePoint )
        VAR Rect = 
            DaxLib.SVG.Element.Rect(
                RectX, height / 4, RectWidth, height / 2, 0, 0, RectStyle, BLANK(), BLANK()
            )

        // Zero Axis Line
        VAR ZeroAxis = 
            DaxLib.SVG.Element.Line(
                ZeroPoint, 0, ZeroPoint, height, ZeroAxisStyle, BLANK(), BLANK()
            )

        RETURN 

        DaxLib.SVG.SVG(
            width, 
            height, 
            BLANK(),
            ZeroAxis & Rect,
            BLANK()
        )
```