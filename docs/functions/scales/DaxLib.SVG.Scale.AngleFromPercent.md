---
title: Scale.AngleFromPercent
nav_order: 7.1
parent: Scales
---

# DaxLib.SVG.Scale.AngleFromPercent

Converts a percentage value to an angle for circular visualizations, such as gauges or donut charts

## Syntax

```dax
DaxLib.SVG.Scale.AngleFromPercent(perc, startAngle, sweepAngle)
```

## Parameters

| Name        | Type               | Description                                                      |
|:---:|:---:|:---:|
| perc        | SCALAR INT64 VAL   | Percentage value (0-100)                                         |
| startAngle  | SCALAR INT64 VAL   | Starting angle in degrees (default -90 for top)                  |
| sweepAngle  | SCALAR int64 VAL   | Total sweep angle in degrees (default 360 for full circle)       |

## Returns

(*NUMERIC*) Angle in degrees

## Example

```dax
DaxLib.SVG.Scale.AngleFromPercent(50, -90, 360)
// Returns: 90 (the angle halfway through a full circle starting at the top)
```

## Definition

```dax
function 'DaxLib.SVG.Scale.AngleFromPercent' = 
	(
		perc : SCALAR Double VAL,
		startAngle : SCALAR int64 VAL,
		sweepAngle : SCALAR int64 VAL
	) =>

		startAngle + ( perc / 100 * sweepAngle )
```