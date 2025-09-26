---
title: DaxLib.SVG.Def.Circle
nav_order: 3
parent: Defs
---

	/// Create a reusable circle definition
	/// defId		STRING	The unique identifier for the circle
	/// cx			STRING	X center coordinate
	/// cy			STRING	Y center coordinate
	/// r			STRING	Radius
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: transformation to apply
	function 'DaxLib.SVG.Def.Circle' = 
			(
				defId: STRING,
				cx: STRING,
				cy: STRING,  
				r: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN
					"<circle id='" & defId & "'" &
					" cx='" & cx & "'" &
					" cy='" & cy & "'" &
					" r='" & r & "'" &
					_OCE &
					"/>"