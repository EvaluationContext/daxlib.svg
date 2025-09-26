---
title: DaxLib.SVG.Style.Line
nav_order: 3
parent: Styles
---

	/// Line and stroke style properties
	/// strokeDasharray    STRING    Line: Stroke dasharray (e.g., "5,5" for dashed)
	/// strokeDashoffset   INT64     Line: Stroke dashoffset
	/// strokeLinecap      STRING    Line: Stroke linecap ("butt", "round", "square")
	/// strokeLinejoin     STRING    Line: Stroke linejoin ("miter", "round", "bevel")
	/// strokeMiterlimit   INT64     Line: Miter limit for stroke joins
	function 'DaxLib.SVG.Style.Line' = 
			(
				strokeDasharray: STRING,
				strokeDashoffset: INT64,
				strokeLinecap: STRING,
				strokeLinejoin: STRING,
				strokeMiterlimit: INT64
			) =>

				VAR _StrokeDasharray =  IF( NOT ISBLANK( strokeDasharray ),  "stroke-dasharray:" & strokeDasharray & ";" )
				VAR _StrokeDashoffset = IF( NOT ISBLANK( strokeDashoffset ), "stroke-dashoffset:" & strokeDashoffset & ";" )
				VAR _StrokeLinecap =    IF( NOT ISBLANK( strokeLinecap ),    "stroke-linecap:" & strokeLinecap & ";" )
				VAR _StrokeLinejoin =   IF( NOT ISBLANK( strokeLinejoin ),   "stroke-linejoin:" & strokeLinejoin & ";" )
				VAR _StrokeMiterlimit = IF( NOT ISBLANK( strokeMiterlimit ), "stroke-miterlimit:" & strokeMiterlimit & ";" )

				RETURN
					_Stroke &
					_StrokeWidth &
					_StrokeOpacity &
					_StrokeDasharray &
					_StrokeDashoffset &
					_StrokeLinecap &
					_StrokeLinejoin &
					_StrokeMiterlimit
