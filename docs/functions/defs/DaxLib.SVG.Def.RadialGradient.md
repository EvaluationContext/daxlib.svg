---
title: DaxLib.SVG.Def.RadialGradient
nav_order: 3
parent: Defs
---

	/// Create a radial gradient definition
	/// defId		STRING	The unique identifier for the gradient
	/// stops		STRING	Concatinated list of one or more DaxLib.SVG.Def.GradientStop Elements
	/// cx			STRING	Optional: Center X position
	/// cy			STRING	Optional: Center Y position
	/// r			STRING	Optional: Radius
	/// fx			STRING	Optional: Focus X position
	/// fy			STRING	Optional: Focus Y position
	/// fr			STRING	Optional: Focus radius
	function 'DaxLib.SVG.Def.RadialGradient' = 
			(
				defId: STRING,
				stops: STRING,
				cx: STRING,
				cy: STRING,
				r: STRING,
				fx: STRING,
				fy: STRING,
				fr: STRING
			) =>

				"<radialGradient" & 
				" id='" & defId & "'" &
				IF( NOT ISBLANK( cx ), " cx='" & cx & "'" ) &
				IF( NOT ISBLANK( cy ), " cy='" & cy & "'" ) &
				IF( NOT ISBLANK( r ),  " r='" & r & "'" ) &
				IF( NOT ISBLANK( fx ), " fx='" & fx & "'" ) &
				IF( NOT ISBLANK( fy ), " fy='" & fy & "'" ) &
				IF( NOT ISBLANK( fr ), " fr='" & fr & "'" ) &
				">" &
				stops &
				"</radialGradient>"