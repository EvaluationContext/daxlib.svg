# SVG

Wraps content in SVG container for Power BI visualization

!!! Tip
	Any measures use these UDFs must have `DataCategory = "ImageUrl"`

=== "Syntax"

    ```dax
    DaxLib.SVG.SVG( width, height, contents, viewbox, sortValue )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | width | <span class="type-label string">STRING</span> | :material-check: |  | width (pixels or percentage) |
    | height | <span class="type-label string">STRING</span> | :material-check: |  | height (pixels or percentage) |
    | contents | <span class="type-label string">STRING</span> | :material-check: |  | To include one or more SVG elements (e.g., from DaxLib.SVG.Element functions) |
    | viewbox | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: viewBox (e.g., "0 0 100 100") |
    | sortValue | <span class="type-label number">NUMERIC</span> | :material-close: | `#!dax BLANK()` | Optional: Sort value for ordering in tables |

    <span class="type-label string">STRING</span> SVG string

=== "Example"

	```dax
	DaxLib.SVG.SVG(
		"100",
		"100",
		DaxLib.SVG.Element.Circle("50", "50", "40", "fill='blue'", BLANK()),
		"0 0 100 100",
		1
	)
	```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.SVG' =
    		(
    			width : STRING,
    			height : STRING, 
    			contents : STRING,
    			viewbox : STRING = BLANK(),
    			sortValue : NUMERIC = BLANK()
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