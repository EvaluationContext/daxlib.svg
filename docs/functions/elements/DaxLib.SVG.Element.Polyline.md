---
title: DaxLib.SVG.Element.Polyline
nav_order: 3
has_children: true
parent: Elements
---

	/// Creates a polyline (connected points)
	/// points		STRING		Space-separated x,y coordinate pairs (e.g., "0,10 20,30 40,15")
	/// style		STRING		Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING		Optional: CSS class to apply
	/// transform	STRING		Optional: transformation to apply
	function 'DaxLib.SVG.Element.Polyline' =
			(
				points: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>
				
				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN

					"<polyline" &
					" points='" & points & "'" &
					_OCE & 
					"/>"