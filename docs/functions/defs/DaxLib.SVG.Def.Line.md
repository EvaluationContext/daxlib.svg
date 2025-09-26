---
title: DaxLib.SVG.Def.Paths
nav_order: 3
parent: Defs
---

	/// Create a reusable path definition
	/// defId		STRING	The unique identifier for the path
	/// d			STRING	The path data string (e.g., "M10 10 L90 90")
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: transformation to apply
	function 'DaxLib.SVG.Def.Paths' =
			(
				defId: STRING,
				d: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN

					"<path id='" & defId & "'" &
					" d='" & d & "'" &
					_OCE &
					"/>"