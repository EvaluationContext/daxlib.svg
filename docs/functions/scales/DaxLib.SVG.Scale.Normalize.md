---
title: DaxLib.SVG.Scale.Normalize
nav_order: 3
parent: Styles
---

	/// Map a value from one value scale to another
	/// Used for scaling values to fit within SVG dimensions
	/// inputValue		NUMERIC	VAL		The value to map
	/// fromMin			NUMERIC	VAL		The minimum value of the original scale
	/// fromMax			NUMERIC	VAL		The maximum value of the original scale
	/// toMin			NUMERIC	VAL		The minimum value of the new scale
	/// toMax			NUMERIC	VAL		The maximum value of the new scale
	function 'DaxLib.SVG.Scale.Normalize' =
			(
				inputValue: NUMERIC VAL,
				fromMin: NUMERIC VAL,
				fromMax: NUMERIC VAL,
				toMin: NUMERIC VAL,
				toMax: NUMERIC VAL
			) =>
				
				( ( inputValue - fromMin ) / ( fromMax - fromMin ) ) * ( toMax - toMin ) + toMin
