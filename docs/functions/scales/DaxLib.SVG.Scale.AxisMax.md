---
title: DaxLib.SVG.Scale.AxisMax
nav_order: 3
parent: Styles
---

	/// Calculate the maximum for a value plotted on an SVG Chart
	/// Handles both category crossfiltering and (sub) totals
	/// measureValue	EXPR,			The actual you will measure, expects a measure reference
	/// columnOne		ANYREF EXPR		The scope of the data for which the SVG will be used, Expects a table expression
	/// axisBuffer		NUMERIC VAL		How much buffer should exist between the axis max and the end of the visual
	function 'DaxLib.SVG.Scale.AxisMax' = 
			(
				measureValue : EXPR,
				columnOne : ANYREF EXPR,
				axisBuffer : NUMERIC VAL
			) =>
				
				VAR _TotalScope = ALL ( columnOne )

				-- Calculates the highest value in the data scope
				VAR _MaxInScope =
					CALCULATE(
						MAXX( _TotalScope, measureValue ),
						_TotalScope
					)

				-- Calculates the total for the data scope
				VAR _MaxOverall =
					CALCULATE (
						measureValue,
						_TotalScope
					)

				-- Configures axis for categories if one is selected, otherwise for the total
				VAR _Max =
					IF (
						HASONEVALUE ( columnOne ),
						_MaxInScope,
						_MaxOverall
					)

				RETURN _Max * axisBuffer
