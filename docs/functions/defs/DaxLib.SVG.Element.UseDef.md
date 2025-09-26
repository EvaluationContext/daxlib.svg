---
title: DaxLib.SVG.Element.UseDef
nav_order: 3
parent: Defs
---

	/// Reference a previously defined SVG element with optional positioning and styling
	/// This function is used to reuse elements that have been defined using DaxLib.SVG.Def.* functions
	/// (e.g., DEFCIRCLE, DEFRECT, DEFPATH, etc.). Instead of duplicating element definitions,
	/// use the appropriate DEF* function once and then reference it multiple times with USE.
	/// defId		STRING	The identifier of the defined element to use
	/// x			STRING	X position where the element should be placed
	/// y			STRING	Y position where the element should be placed
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: transformation to apply
	function 'DaxLib.SVG.Element.UseDef' = 
			(
				defId: STRING,
				X: STRING,
				Y: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )
				
				RETURN

					"<use" &
					" href='#" & defId & "'" &
					IF( NOT ISBLANK( x ), " x='" & x & "'" ) &
					IF( NOT ISBLANK( y ), " y='" & y & "'" ) &
					_OCE & 
					"/>"