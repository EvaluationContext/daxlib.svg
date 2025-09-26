---
title: BulletChart.ActionDot
nav_order: 1.2
parent: Visuals
---

# DaxLib.SVG.BulletChart.ActionDot

Generates an SVG performance bar with a target line and status indicator. Returns an SVG string for use in Table/Matrix visuals (set Image size: Height 25px, Width 100px)

TODO threshold vals should be DOUBLE?
TODO mention actual for bar, target for line, and threshold for dot colour?

## Syntax

```dax
DaxLib.SVG.BulletChart.ActionDot(actual, target, columnOne, thresholdVeryBad, thresholdBad, thresholdGood, thresholdVeryGood, colourBadLow, colourBadHigh, colourGoodLow, colourGoodHigh)
```

## Parameters

| Name             | Type         | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| actual           | EXPR         | Yes      | Actual measure to evaluate                                         |
| target           | EXPR         | Yes      | Target measure to evaluate                                         |
| columnOne        | ANYREF EXPR  | Yes      | Table scope for calculating axis max (e.g., 'Customers'[Key Account Name]) |
| thresholdVeryBad | NUMERIC VAL  | Yes      | Performance threshold (Percentage)                                 |
| thresholdBad     | NUMERIC VAL  | Yes      | Performance threshold (Percentage)                                 |
| thresholdGood    | NUMERIC VAL  | Yes      | Performance threshold (Percentage)                                 |
| thresholdVeryGood| NUMERIC VAL  | Yes      | Performance threshold (Percentage)                                 |
| colourBadLow     | STRING VAL   | Yes      | Status colour                                                      |
| colourBadHigh    | STRING VAL   | Yes      | Status colour                                                      |
| colourGoodLow    | STRING VAL   | Yes      | Status colour                                                      |
| colourGoodHigh   | STRING VAL   | Yes      | Status colour                                                      |

## Returns

(*STRING*) SVG

## Example

```dax
DaxLib.SVG.BulletChart.ActionDot(
    [Actual], 
    [Target], 
    'Customers'[Key Account Name], 
    -0.2, 
    -0.1, 
    0.1, 
    0.2, 
    "#FF0000", 
    "#FFA500", 
    "#90EE90", 
    "#008000"
)
```

## Definition

```dax
function 'DaxLib.SVG.BulletChart.ActionDot' =
    (
        actual: EXPR,
        target: EXPR,
        columnOne: ANYREF EXPR,
        thresholdVeryBad: NUMERIC VAL,
        thresholdBad: NUMERIC VAL,
        thresholdGood: NUMERIC VAL,
        thresholdVeryGood: NUMERIC VAL,
        colourBadLow: STRING VAL,
        colourBadHigh: STRING VAL,
        colourGoodLow: STRING VAL,
        colourGoodHigh: STRING VAL
    ) =>
        // Chart dimensions
        VAR _BarMax = 100
        VAR _BarMin = 20
        // Fixed colour config
        VAR _ColourBackground = "#F5F5F5"
        VAR _ColourBaseline = "#797979"
        VAR _ColourTarget = "black"
        // Get current values
        VAR _Actual = actual
        VAR _Target = target
        // Calculate performance
        VAR _Performance = DIVIDE( _Actual - _Target, _Target )
        // Determine performance colour
        VAR _PerformanceColour =
            SWITCH(
                true,
                _Performance < thresholdVeryBad,  colourBadLow,
                _Performance < thresholdBad,      colourBadHigh,
                _Performance > thresholdVeryGood, colourGoodHigh,
                _Performance > thresholdGood,     colourGoodLow,
                "#CFCFCF"  // Default grey
            )
        // Action dot fill color
        VAR _ActionDotFill =
            IF(
                _Performance >= thresholdBad && _Performance <= thresholdGood,
                "#FFFFFF00",  // Transparent
                _PerformanceColour
            )
        // Scale
        VAR _AxisMax =
            MAX(
                DaxLib.SVG.Calc.AxisMax( actual, columnOne, 1.1 ),
                DaxLib.SVG.Calc.AxisMax( target, columnOne, 1.1 )
            )
        VAR _AxisRange = DaxLib.SVG.Calc.AxisRange( _AxisMax, 0 )
        VAR _ActualNormalized = DaxLib.SVG.Calc.Normalize( _Actual, 0, _AxisMax, _BarMin, _BarMax )
        VAR _TargetNormalized = DaxLib.SVG.Calc.Normalize( _Target, 0, _AxisMax, _BarMin, _BarMax )
        // Create SVG Elements
        VAR _ActionDot = 
            DaxLib.SVG.Element.Circle(
                10, 10, 5,
                DaxLib.SVG.Style.Common(_ActionDotFill, BLANK(), BLANK(), BLANK(), BLANK(), BLANK()),
                BLANK(), BLANK()
            )
        VAR _BarBackground =
            DaxLib.SVG.Element.Rect(
                _BarMin, 2, _BarMax, 16, BLANK(), BLANK(),
                DaxLib.SVG.Style.Common(_ColourBackground, BLANK(), BLANK(), BLANK(), BLANK(), BLANK()),
                BLANK(), BLANK()
            )
        VAR _ActualBar =
            DaxLib.SVG.Element.Rect(
                _BarMin, 5, _ActualNormalized, 10, BLANK(), BLANK(),
                DaxLib.SVG.Style.Common("#CFCFCF", BLANK(), BLANK(), BLANK(), BLANK(), BLANK()),
                BLANK(), BLANK()
            )
        VAR _TargetLine =
            DaxLib.SVG.Element.Rect(
                _TargetNormalized, 2, 2, 16, BLANK(), BLANK(),
                DaxLib.SVG.Style.Common(_ColourTarget, BLANK(), BLANK(), BLANK(), BLANK(), BLANK()),
                BLANK(), BLANK()
            )
        VAR _BarBaseline =
            DaxLib.SVG.Element.Rect(
                _BarMin, 4, 1, 12, BLANK(), BLANK(),
                DaxLib.SVG.Style.Common(_ColourBaseline, BLANK(), BLANK(), BLANK(), BLANK(), BLANK()),
                BLANK(), BLANK()
            )
        RETURN
            DaxLib.SVG.SVG(
                100, 20, BLANK(),
                _ActionDot & _BarBackground & _ActualBar & _TargetLine & _BarBaseline,
                _Actual
            )
```