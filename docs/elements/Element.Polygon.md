# Element.Polygon

Creates a polygon (closed shape)

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.Polygon( points, attributes, transforms )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | points | <span class="type-label string">STRING</span> | :material-check: |  | Space-separated x,y coordinate pairs (e.g., "0,10 20,30 40,15") |
    | attributes | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Direct SVG attributes to apply (e.g., "fill-rule='nonzero' vector-effect='non-scaling-stroke'"), can generate with `DaxLib.SVG.Attr.*` or manually |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Transformation to apply (can be generated with `DaxLib.SVG.Transforms`) |

    <span class="type-label string">STRING</span> <polygon> element

=== "Example"

	```dax
	DaxLib.SVG.Element.Polygon(
		"0,10 20,30 40,15",
		DaxLib.SVG.Attr.Shapes("#32CD32", "#800080", "1", BLANK(), BLANK(), BLANK(), BLANK()),
		"rotate(10)"
	)
	// Returns: <polygon points='0,10 20,30 40,15' fill='#32CD32' stroke='#800080' stroke-width='1' transform='rotate(10)' />
	```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Element.Polygon' =
    		(
    			points: STRING,
    			attributes: STRING = BLANK(),
    			transforms: STRING = BLANK()
    		) =>
    
    			"<polygon" &
    			" points='" & points & "'" &
    			IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
    			IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
    			"/>"
    ```