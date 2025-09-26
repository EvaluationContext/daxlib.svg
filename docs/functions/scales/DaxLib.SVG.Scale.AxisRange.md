---
title: Scale.AxisRange
nav_order: 7.5
parent: Scales
---

# DaxLib.SVG.Scale.AxisRange

Determines the axis range by subtracting the minimum from the maximum.

TODO is it worth having a function for this? also with the buffer it gets a bit werid. Maybe remove this and have buffer on normalize, which will just adjust the svg scale.

## Syntax

```dax
DaxLib.SVG.Scale.AxisRange(maxValue, minValue)
```

## Parameters

| Name     | Type        | Required | Description                                 |
|:---:|:---:|:---:|:---:|
| maxValue | NUMERIC VAL | Yes      | The highest expected value (use AxisMax)    |
| minValue | NUMERIC VAL | Yes      | The lowest expected value (typically fixed) |

## Returns

(*NUMERIC*) range

## Example

```dax
DaxLib.SVG.Scale.AxisRange(200, 50) // Returns 150
```

## Definition

```dax
function 'DaxLib.SVG.Scale.AxisRange' =
    (
        maxValue : NUMERIC VAL,
        minValue : NUMERIC VAL
    ) =>

        maxValue - minValue
```
