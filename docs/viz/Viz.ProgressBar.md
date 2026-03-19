# Viz.ProgressBar

Renders a progress bar as an SVG data URI showing value progression

<svg width='500' height='50' xmlns='http://www.w3.org/2000/svg'><rect x='12.5' y='0.5' width='475' height='49' rx='3' ry='3' fill='#E1DFDD' fill-opacity='1' stroke='#E1DFDD' stroke-width='1'  /><rect x='12.5' y='0.5' width='380' height='49' rx='3' ry='3' fill='#E044A7' fill-opacity='0.95' stroke='#E044A7' stroke-width='1'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Viz.ProgressBar( valueRefExpr, trackRefExpr, color, orientation, width, height )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | valueRefExpr | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: | Value expression |
    | trackRefExpr | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: | Track measure (maximum value) |
    | color | <span class="type-label string">STRING</span> | :material-close: | Optional fill color. Defaults to Power BI theme color |
    | orientation | <span class="type-label string">STRING</span> | :material-close: | Optional orientation: "Horizontal" or "Vertical". Defaults to "Horizontal" |
    | width | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG width. Defaults to 120 |
    | height | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG height. Defaults to 48 |

    <span class="type-label string">STRING</span> SVG Progress Bar

=== "Example"

    ```dax
    DaxLib.SVG.Viz.ProgressBar(
        [Completed],        // valueRefExpr
        [Target],           // trackRefExpr
        BLANK(),            // color (uses default theme)
        "Horizontal",       // orientation
        200,                // width
        20                  // height
    )
    // Returns an SVG data URI with an embedded progress bar
    // Set as a measure with DataCategory = "ImageUrl"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Viz.ProgressBar' =
    		(
    			valueRefExpr: NUMERIC EXPR,
    			trackRefExpr: NUMERIC EXPR,
    			color: STRING,
    			orientation: STRING,
    			width: INT64,
    			height: INT64
    		) =>
    
    			VAR _W = IF( ISBLANK( width ), 120, width )
    			VAR _H = IF( ISBLANK( height ), 48, height )
    			VAR _Color = IF( NOT ISBLANK( color ), color, DaxLib.SVG.Color.Theme( "Power BI", 1 ) )
    			VAR _Marks =
    				DaxLib.SVG.Compound.ProgressBar(
    					0, 0, _W, _H, 0, 0,
    					valueRefExpr, trackRefExpr, _Color, "#E1DFDD", orientation
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Marks ), DaxLib.SVG.SVG( "100%", "100%", "0 0 " & _W & " " & _H, _Marks, BLANK() ) )
    ```