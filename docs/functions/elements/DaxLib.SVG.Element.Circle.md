---
title: DaxLib.SVG.Element.Circle
nav_order: 3
has_children: true
parent: Elements
---

	/// Generates a circle SVG element
	/// cx			STRING	The x position of the center
	/// cy			STRING	The y position of the center
	/// r			STRING	The radius
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: transformation to apply
	function 'DaxLib.SVG.Element.Circle' = 
			(
				cx: STRING,
				cy: STRING,
				r: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN

					"<circle" &
					" cx='" & cx & "'" &
					" cy='" & cy & "'" &
					" r='" & r & "'" &
					_OCE & 
					"/>"