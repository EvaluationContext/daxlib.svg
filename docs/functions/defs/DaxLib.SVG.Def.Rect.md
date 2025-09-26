---
title: DaxLib.SVG.Def.Rect
nav_order: 3
parent: Defs
---

	/// Create a reusable rectangle definition
	/// defId		STRING		The unique identifier for the rectangle
	/// width		STRING		The width of the rectangle (pixels or percentage)
	/// height		STRING		The height of the rectangle	(pixels or percentage)
	/// rx			STRING		Optional: x radius for rounded corners
	/// ry			STRING		Optional: y radius for rounded corners
	/// style		STRING		Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING		Optional: CSS class to apply
	/// transform	STRING		Optional: transformation to apply
	function 'DaxLib.SVG.Def.Rect' = 
			(
				defId: STRING,
				width: STRING,
				height: STRING,
				rx: STRING,
				ry: STRING,
				style: STRING,
				class: STRING,
				Transform: STRING
			) =>

				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )
				
				RETURN

					"<rect id='" & defId & "'" &
					" width='" & width & "'" &
					" height='" & height & "'" &
					IF(NOT ISBLANK(RX), " rx='" & RX & "'" ) & 
					IF(NOT ISBLANK(RY), " ry='" & RY & "'" ) &
					_OCE &
					"/>"	