---
title: Scale.AxisMin
nav_order: 7.4
parent: Scales
---

# DaxLib.SVG.Scale.AxisMin

Calculates the maximum value for a measure evaluated against a given column Handles both category crossfiltering and (sub)totals

TODO buffer and axisBuffer are not on the same scale, would you not to have a % buffer? 

## Syntax

```dax
DaxLib.SVG.Scale.AxisMin(measureValue, columnOne, axisBuffer)
```

## Parameters

| Name         | Type        | Required | Description                                              |
|:---:|:---:|:---:|:---:|
| measureValue | EXPR        | Yes      | The actual you will measure (expects a measure reference)|
| columnOne    | ANYREF      | Yes      | The data scope for the SVG (expects a table expression)  |
| axisBuffer   | NUMERIC VAL | Yes      | Buffer between axis min and end of the visual            |

## Returns

(*NUMERIC*) minimum value with buffer

## Example

```dax
DaxLib.SVG.Scale.AxisMin([Sales], 'Customers', 0.9)
```

## Definition

```dax
function 'DaxLib.SVG.Scale.AxisMin' =
    (
        measureValue : EXPR,
        columnOne : ANYREF,
        axisBuffer : NUMERIC VAL
    ) =>  

        VAR _TotalScope = ALL ( columnOne )
        VAR _MinInScope =
            CALCULATE(
                MINX(
                    _TotalScope,
                    measureValue
                ),
                _TotalScope
            )

        RETURN  

			_MinInScope * axisBuffer
```
