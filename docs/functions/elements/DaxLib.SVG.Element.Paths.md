---
title: DaxLib.SVG.Element.Paths
nav_order: 3
has_children: true
parent: Elements
---

	/// Create a SVG path element	
	/// d			STRING	The path data string (e.g., "M10 10 L90 90")
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: transformation to apply
	function 'DaxLib.SVG.Element.Paths' =
			(
				d: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN

					"<path d='" & d & "'" &
					_OCE & 
					"/>"