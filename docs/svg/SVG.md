# SVG

Wraps content in SVG container for Power BI visualization

!!! Tip
	Any measures use these UDFs must have `DataCategory = "ImageUrl"`

=== "Syntax"

    ```dax
    DaxLib.SVG.SVG( width, height, viewbox, contents, sortValue )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | width | <span class="type-label string">STRING</span> | :material-check: | width (pixels or percentage) |
    | height | <span class="type-label string">STRING</span> | :material-check: | height (pixels or percentage) |
    | viewbox | <span class="type-label string">STRING</span> | :material-close: | Optional: viewBox (e.g., "0 0 100 100") |
    | contents | <span class="type-label string">STRING</span> | :material-check: | To include one or more SVG elements (e.g., from DaxLib.SVG.Element functions) |
    | sortValue | <span class="type-label number">NUMERIC</span> | :material-close: | Optional: Sort value for ordering in tables |

    <span class="type-label string">STRING</span> SVG string

=== "Example"

	```dax
	DaxLib.SVG.SVG(
		"100",
		"100",
		"viewBox='0 0 100 100' ",
		DaxLib.SVG.Element.Circle("50", "50", "40", "fill='blue'", BLANK()),
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
    			sortValue : NUMERIC
    		) =>
    
    			"data:image/svg+xml;utf8," &
    			"<svg " & 
    			"width='" & width & "' height='" & height & "' " &
    			IF( NOT ISBLANK( viewbox ), "viewBox='" & viewbox & "' " ) &
    			"xmlns='http://www.w3.org/2000/svg'>" &
    			IF( NOT ISBLANK( sortValue ), "<desc>" & FORMAT( sortValue, "000000000000" ) & "</desc>" ) &
    			contents &
    			"</svg>"
    ```