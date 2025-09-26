---
title: DaxLib.SVG.Element.Ellipse
nav_order: 3
has_children: true
parent: Elements
---

	/// Generates an ellipse SVG element
	/// cx			STRING	The x position of the center
	/// cy			STRING	The y position of the center
	/// rx			STRING	The x radius
	/// ry			STRING	The y radius
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: transformation to apply
	function 'DaxLib.SVG.Element.Ellipse' = 
			(
				cx: STRING,
				cy: STRING,
				rx: STRING,
				ry: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN

					"<ellipse" &
					" cx='" & cx & "'" &
					" cy='" & cy & "'" &
					" rx='" & rx & "'" &
					" ry='" & ry & "'" &
					_OCE & 
					"/>"