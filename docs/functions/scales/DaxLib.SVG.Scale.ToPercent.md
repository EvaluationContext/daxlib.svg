---
title: Scale.ToPercent
nav_order: 3
parent: Scales
---

# DaxLib.SVG.Scale.ToPercent

Converts a value to percentage (0-100%) based on original scale

TODO remove since just a more limited normalize function?

## Syntax

```dax
DaxLib.SVG.Scale.ToPercent(inputValue, fromMin, fromMax)
```

## Parameters

| Name       | Type        | Required | Description                         |
|:---:|:---:|:---:|:---:|
| inputValue | NUMERIC VAL | Yes      | The value to map                    |
| fromMin    | NUMERIC VAL | Yes      | The minimum value of the original scale |
| fromMax    | NUMERIC VAL | Yes      | The maximum value of the original scale |

## Returns

(*DOUBLE*) percentage (0-1)

## Example

```dax
DaxLib.SVG.Scale.ToPercent(50, 0, 200) // Returns 0.25
```

## Definition

```dax
function 'DaxLib.SVG.Scale.ToPercent' =
    (
        inputValue : NUMERIC VAL,
        fromMin : NUMERIC VAL,
        fromMax : NUMERIC VAL
    ) =>

        DaxLib.SVG.Scale.Normalize(
            inputValue,
            fromMin,
            fromMax,
            0,
            100
        ) / 100
```
