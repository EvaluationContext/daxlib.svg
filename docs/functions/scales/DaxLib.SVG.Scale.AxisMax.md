---
title: Scale.AxisMax
nav_order: 7.3
parent: Scales
---

# DaxLib.SVG.Scale.AxisMax

Calculates the maximum value for a measure evaluated against a given column Handles both category crossfiltering and (sub)totals

TODO buffer and axisBuffer are not on the same scale, would you not to have a % buffer? 

## Syntax

```dax
DaxLib.SVG.Scale.AxisMax(measureValue, columnOne, axisBuffer)
```

## Parameters

| Name         | Type        | Required | Description                                              |
|:---:|:---:|:---:|:---:|
| measureValue | EXPR        | Yes      | The actual you will measure (expects a measure reference)|
| columnOne    | ANYREF EXPR | Yes      | The data scope for the SVG (expects a table expression)  |
| axisBuffer   | NUMERIC VAL | Yes      | Buffer between axis max and end of the visual            |

## Returns

(*NUMERIC*) maximum value with buffer

## Example

```dax
DaxLib.SVG.Scale.AxisMax([Sales], 'Customers', 1.1)
```

## Definition

```dax
function 'DaxLib.SVG.Scale.AxisMax' = 
    (
        measureValue : EXPR,
        columnOne : ANYREF EXPR,
        axisBuffer : NUMERIC VAL
    ) =>

        VAR _TotalScope = ALL ( columnOne )
        // Calculates the highest value in the data scope
        VAR _MaxInScope =
            CALCULATE(
                MAXX( _TotalScope, measureValue ),
                _TotalScope
            )
        // Calculates the total for the data scope
        VAR _MaxOverall =
            CALCULATE (
                measureValue,
                _TotalScope
            )
        // Configures axis for categories if one is selected, otherwise for the total
        VAR _Max =
            IF (
                HASONEVALUE ( columnOne ),
                _MaxInScope,
                _MaxOverall
            )

        RETURN 
		
			_Max * axisBuffer
```
