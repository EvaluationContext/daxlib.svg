---
title: DaxLib.SVG.Def.LinearGradient
nav_order: 3
parent: Defs
---

	/// Create a linear gradient definition
	/// defId		STRING	The unique identifier for the gradient
	/// stops		STRING	Concatinated list of one or more DaxLib.SVG.Def.GradientStop Elements
	/// x1			STRING	Optional: Start X position
	/// y1			STRING	Optional: Start Y position
	/// x2			STRING	Optional: End X position
	/// y2			STRING	Optional: End Y position
	function 'DaxLib.SVG.Def.LinearGradient' = 
			(
				defId: STRING,
				stops: STRING,
				x1: STRING,
				y1: STRING,
				x2: STRING,
				y2: STRING
			) =>
				
				"<linearGradient" & 
				" id='" & defId & "'" &
				IF( NOT ISBLANK( x1 ), " x1='" & x1 & "'" ) &
				IF( NOT ISBLANK( y1 ), " y1='" & y1 & "'" ) &
				IF( NOT ISBLANK( x2 ), " x2='" & x2 & "'" ) &
				IF( NOT ISBLANK( y2 ), " y2='" & y2 & "'" ) &
				">" &
				stops &
				"</linearGradient>"