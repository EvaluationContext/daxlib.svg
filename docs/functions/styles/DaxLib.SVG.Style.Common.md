---
title: DaxLib.SVG.Style.Common
nav_order: 3
parent: Styles
---

	/// Style properties common to all SVG elements
	/// fill             STRING      Fill color or gradient reference
	/// fillOpacity      DOUBLE      Fill opacity (0-1)
	/// stroke           STRING      Stroke color
	/// strokeWidth      INT64       Stroke width
	/// strokeOpacity    DOUBLE      Stroke opacity (0-1)
	/// opacity          DOUBLE      Overall opacity (0-1)
	function 'DaxLib.SVG.Style.Common' = 
			(
				fill: STRING,
				fillOpacity: DOUBLE,
				stroke: STRING,
				strokeWidth: INT64,
				strokeOpacity: DOUBLE,
				opacity: DOUBLE
			) =>

				VAR _Fill =          IF( NOT ISBLANK( fill ),          "fill:" & fill & ";" )
				VAR _FillOpacity =   IF( NOT ISBLANK( fillOpacity ),   "fill-opacity:" & fillOpacity & ";" )
				VAR _Stroke =        IF( NOT ISBLANK( stroke ),        "stroke:" & stroke & ";" )
				VAR _StrokeWidth =   IF( NOT ISBLANK( strokeWidth ),   "stroke-width:" & strokeWidth & ";" )
				VAR _StrokeOpacity = IF( NOT ISBLANK( strokeOpacity ), "stroke-opacity:" & strokeOpacity & ";" )
				VAR _Opacity =       IF( NOT ISBLANK( opacity ),       "opacity:" & opacity & ";" )

				RETURN

					_Fill &
					_FillOpacity &
					_Stroke &
					_StrokeWidth &
					_StrokeOpacity &
					_Opacity 
