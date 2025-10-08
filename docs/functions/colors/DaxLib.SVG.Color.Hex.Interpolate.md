---
title: Color.Hex.Interpolate
nav_order: 7.6
parent: Colors
---

# DaxLib.SVG.Color.Hex.Interpolate

Interpolate between two Hex colors by a given percentage

## Syntax

```dax
DaxLib.SVG.Color.Hex.Interpolate( startHexColor, endHexColor, percentage )
```

| Name          | Type   | Required | Description                                                    |
|:---:|:---:|:---:|---|
| startHexColor | <span class="type-label string">STRING</span> | Yes      | The starting Hex color (e.g., "#FF0000")                     |
| endHexColor   | <span class="type-label string">STRING</span> | Yes      | The ending Hex color (e.g., "#0000FF")                       |
| percentage    | <span class="type-label number">DOUBLE</span> | Yes      | The interpolation percentage (0.0 = startColor, 1.0 = endColor) |

## Returns

<span class="type-label string">**STRING**</span> Interpolated hex color code

## Example

```dax
DaxLib.SVG.Color.Hex.Interpolate("#FF0000", "#0000FF", 0.5)
// Returns: "#800080" (purple)
```

## Definition

```dax
function 'DaxLib.SVG.Color.Hex.Interpolate' =
    (
        startHexColor: STRING,
        endHexColor: STRING,
        percentage: DOUBLE
    ) =>
    
        // Clamp percentage between 0 and 1
        VAR _ClampedPercentage = MIN( MAX( percentage, 0 ), 1 )
    
        // Clean Hex codes
        VAR _StartHex = SUBSTITUTE( startHexColor, "#", "" )
        VAR _EndHex = 	SUBSTITUTE( endHexColor, "#", "" )
    
        // Extract and convert RGB components using your existing Hex.ToInt function
        VAR _StartR = 	DaxLib.SVG.Color.Hex.ToInt( MID( _StartHex, 1, 2 ) )
        VAR _StartG = 	DaxLib.SVG.Color.Hex.ToInt( MID( _StartHex, 3, 2 ) )
        VAR _StartB = 	DaxLib.SVG.Color.Hex.ToInt( MID( _StartHex, 5, 2 ) )
    
        VAR _EndR = 	DaxLib.SVG.Color.Hex.ToInt( MID( _EndHex, 1, 2 ) )
        VAR _EndG = 	DaxLib.SVG.Color.Hex.ToInt( MID( _EndHex, 3, 2 ) )
        VAR _EndB = 	DaxLib.SVG.Color.Hex.ToInt( MID( _EndHex, 5, 2 ) )
    
        // Interpolate RGB values
        VAR _InterpolatedR = ROUND( _StartR + ( _EndR - _StartR ) * _ClampedPercentage, 0 )
        VAR _InterpolatedG = ROUND( _StartG + ( _EndG - _StartG ) * _ClampedPercentage, 0 )
        VAR _InterpolatedB = ROUND( _StartB + ( _EndB - _StartB ) * _ClampedPercentage, 0 )
    
        VAR result =
            DaxLib.SVG.Color.RGB.ToHex(
                _InterpolatedR,
                _InterpolatedG,
                _InterpolatedB,
                BLANK()  // No alpha
            )
    
        RETURN result
```