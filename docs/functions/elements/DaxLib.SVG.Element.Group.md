---
title: DaxLib.SVG.Element.Group
nav_order: 3
has_children: true
parent: Elements
---

	/// Generates SVG group element
	/// Transformations applied to the <g> element are performed on its child elements, and its attributes are inherited by its children. It can also group multiple elements to be referenced later with the <use> element.
	/// contents	SCALAR VAL	Content to group (recommend including all content in a single _SvgGroup variable defined upstream)
	/// transform	SCALAR VAL	Optional: Transform (e.g., "translate(50,50) rotate(45)")
	/// opacity		SCALAR VAL	Optional: Opacity for entire group (0-1, optional)
	function 'DaxLib.SVG.Element.Group' =
			(
				contents : SCALAR VAL,
				transform : SCALAR VAL,
				opacity : SCALAR VAL
			) =>

				"<g" &
				" transform='" & transform & "'" &
				" opacity='" & opacity & "'" &
				">" & contents & "</g>"