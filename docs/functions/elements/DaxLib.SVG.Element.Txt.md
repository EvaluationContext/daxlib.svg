---
title: DaxLib.SVG.Element.Txt
nav_order: 3
has_children: true
parent: Elements
---

	/// Creates a text SVG element
	/// x			STRING	The x position of the text
	/// y			STRING	The y position of the text
	/// txt			STRING	The text content
	/// dx			STRING	Optional: x offset from position
	/// dy			STRING	Optional: y offset from position
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: additional transforms (e.g. "scale(1.2) translate(10,10)")
	function 'DaxLib.SVG.Element.Txt' =
			(
				x: STRING,
				y: STRING,
				txt: STRING,
				dx: STRING,
				dy: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

				VAR _DX = IF(NOT ISBLANK( dx ), " dx='" & dx & "'" )
				VAR _DY = IF(NOT ISBLANK( dy ), " dy='" & dy & "'" )
				
				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN

					"<text" &
					" x='" & x & "'" &
					" y='" & y & "'" &
					_DX & 
					_DY &
					_OCE &
					">" & txt & 
					"</text>"