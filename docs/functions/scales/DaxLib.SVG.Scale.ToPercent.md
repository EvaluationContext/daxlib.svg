---
title: DaxLib.SVG.Scale.ToPercent
nav_order: 3
parent: Styles
---

	/// Converts a value to percentage (0-100%) based on original scale
	/// inputValue		NUMERIC	VAL		The value to map
	/// fromMin			NUMERIC	VAL		The minimum value of the original scale
	/// fromMax			NUMERIC	VAL		The maximum value of the original scale
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
