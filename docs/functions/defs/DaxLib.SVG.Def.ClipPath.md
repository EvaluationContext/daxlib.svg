---
title: DaxLib.SVG.Def.ClipPath
nav_order: 3
parent: Defs
---

	/// Creates a clipping mask definition 
	///	TODO would the example work, or does a regular shape need to be used? if regular shape, then need to add parameter to shapes <circle cx="50" cy="50" r="50" fill="red" clip-path="url(#cut-bottom)" />
	/// defId		STRING	The unique identifier for the clip path. (Example: "cut-top", "mask-circle")
	/// Elements: 	STRING	The SVG element(s) that make up the clipping path (typically a single shape)
	function 'DaxLib.SVG.Def.ClipPath' =
			(
				defId : STRING,
				elements: STRING
			) =>
				
				"<clipPath id='" & defId & "'>" &
				elements &
				"</clipPath>"