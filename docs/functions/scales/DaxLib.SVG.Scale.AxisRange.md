---
title: DaxLib.SVG.Scale.AxisRange
nav_order: 3
parent: Styles
---

	/// Determines the axis range by subtracting the minimum from the maximum
	/// maxValue	NUMERIC VAL	The highest expected value (Recommended: Use SVG.Scale.AxisMax)
	/// minValue	NUMERIC VAL	The lowest expected value. Typically a fixed value
	function 'DaxLib.SVG.Scale.AxisRange' =
			(
				maxValue : NUMERIC VAL,
				minValue : NUMERIC VAL
			) =>
				
				maxValue - minValue
