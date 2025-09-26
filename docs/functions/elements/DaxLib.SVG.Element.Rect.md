---
title: DaxLib.SVG.Element.Line
nav_order: 3
has_children: true
parent: Elements
---

	/// Generates SVG line element
	/// x1			STRING	Starting X position (left edge is 0)
	/// y1			STRING	Starting Y position (top edge is 0)
	/// x2			STRING	Ending X position (left edge is 0)
	/// y2			STRING	Ending Y position (top edge is 0)
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: CSS class to apply
	/// transform	STRING	Optional: transformation to apply
	function 'DaxLib.SVG.Element.Line' =
			(
				x1: STRING,
				y1: STRING,
				x2: STRING,
				y2: STRING,
				style: STRING,
				class: STRING,
				transform: STRING
			) =>  
				
				VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

				RETURN

					"<line" &
					" x1='" & x1 & "'" &
					" y1='" & y1 & "'" &
					" x2='" & x2 & "'" &
					" y2='" & y2 & "'" &
					_OCE & 
					"/>"