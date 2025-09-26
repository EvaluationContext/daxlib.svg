---
title: DaxLib.SVG.Style.Txt
nav_order: 3
parent: Styles
---

	/// Text-specific style properties
	/// fontFamily      STRING      Font family for text
	/// fontSize        INT64       Font size for text
	/// fontWeight      STRING      Weight ("normal", "bold", "lighter", "100-900")
	/// fontStyle       STRING      Style ("normal", "italic", "oblique")
	/// textAnchor      STRING      Anchor ("start", "middle", "end")
	/// baseline        STRING      Dominant baseline
	/// textDecoration  STRING      Decoration ("none", "underline", "overline", "line-through")
	/// letterSpacing   STRING      Space between letters
	/// wordSpacing     STRING      Space between words
	function 'DaxLib.SVG.Style.Txt' = 
			(
				fontFamily: STRING,
				fontSize: INT64,
				fontWeight: STRING,
				fontStyle: STRING,
				textAnchor: STRING,
				baseline: STRING,
				textDecoration: STRING,
				letterSpacing: STRING,
				wordSpacing: STRING
			) =>

				VAR _FontFamily =     IF( NOT ISBLANK( fontFamily ),     "font-family:" & fontFamily & ";" )
				VAR _FontSize =       IF( NOT ISBLANK( fontSize ),       "font-size:" & fontSize & ";" )
				VAR _FontWeight =     IF( NOT ISBLANK( fontWeight ),     "font-weight:" & fontWeight & ";" )
				VAR _FontStyle =      IF( NOT ISBLANK( fontStyle ),      "font-style:" & fontStyle & ";" )
				VAR _TextAnchor =     IF( NOT ISBLANK( textAnchor ),     "text-anchor:" & textAnchor & ";" )
				VAR _Baseline =       IF( NOT ISBLANK( baseline ),       "dominant-baseline:" & baseline & ";" )
				VAR _TextDecoration = IF( NOT ISBLANK( textDecoration ), "text-decoration:" & textDecoration & ";" )
				VAR _LetterSpacing =  IF( NOT ISBLANK( letterSpacing ),  "letter-spacing:" & letterSpacing & ";" )
				VAR _WordSpacing =    IF( NOT ISBLANK( wordSpacing ),    "word-spacing:" & wordSpacing & ";" )

				RETURN

					_FontFamily &
					_FontSize &
					_FontWeight &
					_FontStyle &
					_TextAnchor &
					_Baseline &
					_TextDecoration &
					_LetterSpacing &
					_WordSpacing