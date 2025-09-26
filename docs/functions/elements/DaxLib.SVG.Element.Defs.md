---
title: DaxLib.SVG.Element.Defs
nav_order: 3
has_children: true
parent: Elements
---

    /// Create a <def> element from one or more DaxLib.SVG.Def.* Elements
	/// defs	STRING	Concatenated lists of def Elements to include in a def block
	function 'DaxLib.SVG.Element.Defs' = 
			(
				defs: STRING    // concatenated lists of elements to include in a def block
			) =>

				"<defs>" &
				defs &  
				"</defs>"