---
title: Scale.Normalize
nav_order: 1
parent: Scales
---

# DaxLib.SVG.Scale.Normalize

Maps a value from one scale to another. Used for scaling values to fit within SVG dimensions

## Syntax

```dax
DaxLib.SVG.Scale.Normalize(
    inputValue, 
    fromMin, 
    fromMax, 
    toMin, 
    toMax
)
```

| Name       | Type        | Required | Description                         |
|:---:|:---:|:---:|:---:|:---:|:---:|
| inputValue | NUMERIC VAL | Yes      | The value to map                    |
| fromMin    | NUMERIC VAL | Yes      | The minimum value of the original scale |
| fromMax    | NUMERIC VAL | Yes      | The maximum value of the original scale |
| toMin      | NUMERIC VAL | Yes      | The minimum value of the new scale  |
| toMax      | NUMERIC VAL | Yes      | The maximum value of the new scale  |

## Returns

**NUMERIC** mapped value

## Example

```dax
DaxLib.SVG.Scale.Normalize(50, 0, 200, 0, 100) 
// Returns 25
```

## Definition

```dax
function 'DaxLib.SVG.Scale.Normalize' =
    (
        inputValue: NUMERIC VAL,
        fromMin: NUMERIC VAL,
        fromMax: NUMERIC VAL,
        toMin: NUMERIC VAL,
        toMax: NUMERIC VAL
    ) =>

        ( ( inputValue - fromMin ) / ( fromMax - fromMin ) ) * ( toMax - toMin ) + toMin
```
