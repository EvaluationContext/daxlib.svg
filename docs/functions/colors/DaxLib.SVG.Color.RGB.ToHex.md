---
title: Color.RGB.ToHex
nav_order: 7.5
parent: Colors
---

# DaxLib.SVG.Color.RGB.ToHex

RGB to Hex conversion

## Syntax

```dax
DaxLib.SVG.Color.RGB.ToHex(
    red, 
    green, 
    blue, 
    alpha
)
```

| Name  | Type   | Required | Description                        |
|:-----:|:------:|:--------:|:-----------------------------------|
| red   | INT64  | Yes      | The red value (0-255)             |
| green | INT64  | Yes      | The green value (0-255)           |
| blue  | INT64  | Yes      | The blue value (0-255)            |
| alpha | DOUBLE | No       | Optional: The alpha value (0-1)   |

## Returns

**STRING** Hex color code (e.g., "#FF0000" or "#FF0000FF" with alpha)

## Example

```dax
DaxLib.SVG.Color.RGB.ToHex(255, 0, 0, BLANK())
// Returns: "#FF0000" (red)
```

## Definition

```dax
function 'DaxLib.SVG.Color.RGB.ToHex' =
    (
        red: INT64,
        green: INT64,
        blue: INT64,
        alpha: DOUBLE
    ) =>
    
        "#" &
        DaxLib.SVG.Color.Int.ToHex( red, 2 ) &
        DaxLib.SVG.Color.Int.ToHex( green, 2 ) &
        DaxLib.SVG.Color.Int.ToHex( blue, 2 ) &
        IF( NOT ISBLANK( alpha ), DaxLib.SVG.Color.Int.ToHex( alpha * 255, 2 ) )
```