---
title: DaxLib.SVG.Scale.AxisMin
nav_order: 3
parent: Styles
---

	/// Calculate the minimum for a value plotted on an SVG
	/// measureValue	EXPR			The actual you will measure, expects a measure reference
	/// columnOne		ANYREF			The scope of the data for which the SVG will be used, Expects a table expression
	/// axisBuffer		NUMERIC VAL		How much buffer should exist between the axis min and the end of the visual
	function 'DaxLib.SVG.Scale.AxisMin' =
			(
				measureValue : EXPR,
				columnOne : ANYREF,
				axisBuffer : NUMERIC VAL
			) =>  
			
				VAR _TotalScope = ALL ( columnOne )
				VAR _MinInScope =
					CALCULATE(
						MINX(
							_TotalScope,
							measureValue
						),
						_TotalScope
					)

				RETURN  _MinInScope * axisBuffer
