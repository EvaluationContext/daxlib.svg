---
title: Scale.StringByThreshold
nav_order: 3
parent: Scales
---

# DaxLib.SVG.Scale.StringByThreshold

Returns a string based on where a value falls within defined thresholds

## Syntax

```dax
DaxLib.SVG.Scale.StringByThreshold(inputValue, thresholdLow, thresholdHigh, low, mid, high)
```

## Parameters

| Name          | Type       | Description                                                        |
|:---:|:---:|:---:|
| inputValue    | SCALAR VAL | The value to evaluate                                              |
| thresholdLow  | SCALAR VAL | Lower threshold value                                              |
| thresholdHigh | SCALAR VAL | Upper threshold value                                              |
| low     		| SCALAR VAL | String returned when value <= thresholdLow                         |
| mid     		| SCALAR VAL | String returned when value between thresholds                      |
| high    		| SCALAR VAL | String returned when values >= thresholdHigh                       |

## Returns

(*STRING*) result

## Example

```dax
DaxLib.SVG.Scale.StringByThreshold(75, 50, 100, "red", "yellow", "green")
// Returns: "yellow"
```

## Definition

```dax
function 'DaxLib.SVG.Scale.StringByThreshold' =
    (
        inputValue : SCALAR VAL,
        thresholdLow : SCALAR VAL,
        thresholdHigh : SCALAR VAL,
        colourLow : SCALAR VAL,
        colourMid : SCALAR VAL,
        colourHigh : SCALAR VAL
    ) =>

        SWITCH(
            true,
            inputValue <= thresholdLow, 
                low,
            inputValue >= thresholdHigh, 
                high,
            mid
        )
```
