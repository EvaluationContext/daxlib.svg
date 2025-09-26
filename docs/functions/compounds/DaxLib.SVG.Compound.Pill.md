---
title: DaxLib.SVG.Compound.Pill
nav_order: 3
has_children: true
parent: Compounds
---

/// Create a pill SVG Compound element (rounded rectangle with text centered inside)
	/// width 		STRING  	The width of the SVG canvas
	/// Height 		STRING  	The height of the SVG canvas
	/// txt 		STRING  The text to display
	/// pillColour 	STRING  The Hex color of the fill i.e "#01B8AA80"
	/// txtColor 	STRING  The Hex color of the text i.e "#FFFFFF"
	function 'DaxLib.SVG.Compound.Pill' = 
			(
				width: STRING,
				height: STRING,
				txt: STRING,
				pillColour: STRING,
				txtColour: STRING
			) =>

			VAR Pill = 
				DaxLib.SVG.Element.Rect(
					1,                 	// X
					1,                 	// Y
					width,      		// Width
					height,     		// Height
					10,               	// RX
					10,               	// RY
					DaxLib.SVG.Style.Common(
						pillColour,
						BLANK(),
						txtColour,
						1,
						BLANK(),
						BLANK()
					),         			// Style
					BLANK(),           	// Class
					BLANK()           	// Transform
				)

			VAR TextElement = 
				DaxLib.SVG.Element.Txt(
					width * 0.50,      	// X
					height * 0.58,     	// Y
					txt,              	// Text content
					0,                	// DX
					0,                	// DY
					DaxLib.SVG.Style.Common(
						txtColour,
						BLANK(),
						BLANK(),
						BLANK(),
						BLANK(),
						BLANK()
					) &
					DaxLib.SVG.Style.Txt(
						"Segoe UI",
						12,
						BLANK(),
						BLANK(),
						"middle",
						"middle",
						BLANK(),
						BLANK(),
						BLANK()
					),         			// Style
					BLANK(),			// Class
					BLANK()				// Transform
				)

			RETURN
			
				Pill & 
				TextElement