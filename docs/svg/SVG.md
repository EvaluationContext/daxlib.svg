---
comments: true
---

# SVG

Wraps content in an SVG container for Power BI visualization

!!! Tip
	Any measures use these UDFs must have `DataCategory = "ImageUrl"`{:.txt}

=== "Syntax"

	```dax
	DaxLib.SVG.SVG( width, height, viewbox, contents, sortValue)
	```

	| Name      | Type   | Required | Description                                                                 |
	|:---:|:---:|:---:|---|
	| width     | <span class="type-label string">STRING</span> | :material-close: | Width (pixels or percentage)                                                |
	| height    | <span class="type-label string">STRING</span> | :material-close: | Height (pixels or percentage)                                               |
	| viewbox   | <span class="type-label string">STRING</span> | :material-close: | viewBox (e.g., "0 0 100 100")                                               |
	| contents  | <span class="type-label string">STRING</span> | :material-check: | SVG elements to include (e.g., from DaxLib.SVG.Element functions)           |
	| sortValue | <span class="type-label expr">EXPR</span> | :material-close: | Sort value for ordering in tables                                           |

	<span class="type-label string">STRING</span> SVG string

=== "Example"

	```dax
	DaxLib.SVG.SVG(
		"100",
		"100",
		"viewBox='0 0 100 100' ",
		DaxLib.SVG.Element.Circle("50", "50", "40", "fill:blue;", BLANK(), BLANK()),
		1
	)
	```

=== "Definition"

	```dax
	function 'DaxLib.SVG.SVG' =
		(
			width : STRING,
			height : STRING,
			viewbox : STRING,
			contents : STRING,
			sortValue : EXPR
		) =>

			VAR _Canvas = 	IF( NOT ISBLANK( width ) && NOT ISBLANK( height ), "width='" & width & "' height='" & height & "' " )
			VAR _SortDesc = IF( NOT ISBLANK( sortValue ), "<desc>" & FORMAT( sortValue, "000000000000" ) & "</desc>" )

			RETURN 
			
				"data:image/svg+xml;utf8," &
				"<svg " &
				_Canvas &
				viewbox &
				"xmlns='http://www.w3.org/2000/svg'>" &
				_SortDesc &
				contents &
				"</svg>"
	```