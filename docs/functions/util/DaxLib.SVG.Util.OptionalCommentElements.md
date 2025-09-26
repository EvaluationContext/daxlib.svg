---
title: DaxLib.SVG.Util.OptionalCommentElements
nav_order: 3
parent: Utils
---

    /// Util function to generate optional common SVG element attributes
	/// style		STRING	Optional: The style to apply, can generate with DaxLib.SVG.Style.* or manually (e.g., "fill:black;stroke:blue;")
	/// class		STRING	Optional: The CSS class to apply to the element
	/// transform	STRING	Optional: The transform to apply to the element (e.g., "rotate(45)")
	function 'DaxLib.SVG.Util.OptionalCommentElements' = 
			(
				style: STRING,
				class: STRING,
				transform: STRING
			) =>

			VAR _Style = 		
				IF( 
					NOT ISBLANK( style ),
					IF(
						SEARCH( "style=", style, 1, 0 ) > 0,
						" " & style & " ",
						" style='" & style & "' "
					)
				)
			
			VAR _Class = 		
				IF( 
					NOT ISBLANK( class ), 
					IF(
						SEARCH( "class=", class, 1, 0 ) > 0,
						" " & class & " ",
						" class='" & class & "' "
					)
				)
			
			VAR _Transform = 	
				IF( 
					NOT ISBLANK( transform ), 
					IF(
						SEARCH( "transform=", transform, 1, 0 ) > 0,
						" " & transform & " ",
						" transform='" & transform & "' "
					)
				)
				
				RETURN

					_Style &
					_Class &
					_Transform