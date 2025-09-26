---
title: DaxLib.SVG.Scale.AngleFromPercent
nav_order: 3
parent: Styles
---

	/// Converts percentage to angle for circular visualizations
	/// perc			SCALAR Double VAL	Percentage value (0-100)
	/// startAngle 		SCALAR VAL int64	Starting angle in degrees (default -90 for top)
	/// sweepAngle		SCALAR VAL int64	Total sweep angle in degrees (default 360 for full circle)
	function 'DaxLib.SVG.Scale.AngleFromPercent' = 
			(
				perc : SCALAR Double VAL,
				startAngle : SCALAR int64 VAL,
				sweepAngle : SCALAR int64 VAL
			) =>
				
				startAngle + ( perc / 100 * sweepAngle )
