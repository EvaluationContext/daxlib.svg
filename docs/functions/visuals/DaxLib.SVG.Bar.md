---
title: DaxLib.SVG.Bar
nav_order: 3
parent: Visuals
---

	/// Create a bar SVG for a given column
	/// width			INT64	The width of the SVG canvas
	/// height			INT64	The height of the SVG canvas
	/// columnRef		ANYREF	The column to visualize
	/// positiveColor	STRING	The Hex color of the positive bar i.e "#01B8AA"
	/// negativeColor	STRING	The Hex color of the negative bar i.e "#FD625E"
	/// zeroAxisColor	STRING	The Hex color of the zero axis i.e "#A6A6A6"
	function 'DaxLib.SVG.Bar' = 
			(
				width: INT64,
				height: INT64,
				columnRef: ANYREF,
				positiveColor: STRING,
				negativeColor: STRING,
				zeroAxisColor: STRING
			) =>

				// X-axis scale
				VAR XMin = CALCULATE( MIN( columnRef ), ALLSELECTED() ) 
				VAR XMax = CALCULATE( MAX( columnRef ), ALLSELECTED() ) 

				// Map the zero point and the current value to the SVG's coordinate system
				VAR ZeroPoint = DaxLib.SVG.Calc.Normalize( 0, XMin, XMax, 0, width )
				VAR CurrentValue = SUM( columnRef )
				VAR ValuePoint =  DaxLib.SVG.Calc.Normalize( CurrentValue, XMin, XMax, 0, width )

				// Style
				VAR _PositiveColor = IF( NOT ISBLANK( positiveColor ), positiveColor, "#01B8AA" )
				VAR _NegativeColor = IF( NOT ISBLANK( negativeColor ), negativeColor, "#FD625E" )
				VAR _ZeroAxisColor = IF( NOT ISBLANK( zeroAxisColor ), zeroAxisColor, "#A6A6A6" )
				VAR ZeroAxisStyle =
					DaxLib.SVG.Style.Common(
						BLANK(),			// Fill
						BLANK(),			// FillOpacity
						_ZeroAxisColor,		// Stroke
						1,					// StrokeWidth
						BLANK(),			// StrokeOpacity
						BLANK()				// Opacity
					)
				VAR RectColour = IF( CurrentValue >= 0, _PositiveColor, _NegativeColor )
				VAR RectStyle =
					DaxLib.SVG.Style.Common(
						RectColour,			// Fill
						BLANK(),			// FillOpacity
						RectColour,			// Stroke
						BLANK(),			// StrokeWidth
						BLANK(),			// StrokeOpacity
						BLANK()				// Opacity
					)

				// Rect
				VAR RectWidth =  ABS( ValuePoint - ZeroPoint )
				VAR RectX =		 IF( ValuePoint > ZeroPoint, ZeroPoint, ValuePoint )
				VAR Rect = 
					DaxLib.SVG.Element.Rect(
						RectX,             // X
						height / 4,        // Y
						RectWidth,         // Width
						height / 2,        // Height
						0,                 // RX
						0,                 // RY
						RectStyle,         // Style
						BLANK(),           // Class
						BLANK()            // Transform
					)

				// Zero Axis Line
				VAR ZeroAxis = 
					DaxLib.SVG.Element.Line(
						ZeroPoint,         	// X1
						0,                	// Y1
						ZeroPoint,          // X2
						height,				// Y2
						ZeroAxisStyle,    	// Style
						BLANK(),            // Class
						BLANK()             // Transform
					)

				RETURN 
				
					DaxLib.SVG.SVG(
						width,
						height,
						BLANK(),
						ZeroAxis &
						Rect,
						BLANK()
					)