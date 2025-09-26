---
title: DaxLib.SVG.Def.GradientStop
nav_order: 3
parent: Defs
---

	/// Create a gradient stop element
	/// offset		STRING	Stop position
	/// colour		STRING	Colour value (hex or named Colour)
	/// opacity		STRING	Optional: opacity value
	function 'DaxLib.SVG.Def.GradientStop' = 
			(
				offset: STRING,
				colour: STRING,
				opacity: STRING
			) =>

				"<stop offset='" & offset & 
				"' stop-color='" & colour & "'" &
				IF( NOT ISBLANK( opacity ), " stop-opacity='" & opacity & "'" ) &
				"/>"