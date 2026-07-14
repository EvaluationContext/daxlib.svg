# Viz.ProgressBar

Renders a progress bar as an SVG data URI showing value progression

<svg width='500' height='50' xmlns='http://www.w3.org/2000/svg'><rect x='12.5' y='0.5' width='475' height='49' rx='3' ry='3' fill='#E1DFDD' fill-opacity='1' stroke='#E1DFDD' stroke-width='1'  /><rect x='12.5' y='0.5' width='380' height='49' rx='3' ry='3' fill='#E044A7' fill-opacity='0.95' stroke='#E044A7' stroke-width='1'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Viz.ProgressBar( valueRefExpr, trackRefExpr, color, orientation, width, height )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | valueRefExpr | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: |  | Value expression |
    | trackRefExpr | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: |  | Track measure (maximum value) |
    | color | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional fill color. Defaults to Power BI theme color |
    | orientation | <span class="type-label string">STRING</span> | :material-close: | `#!dax "Horizontal"` | Optional orientation: "Horizontal" or "Vertical". Defaults to "Horizontal" |
    | width | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 120` | Optional: SVG width. Defaults to 120 |
    | height | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 48` | Optional: SVG height. Defaults to 48 |

    <span class="type-label string">STRING</span> SVG Progress Bar

=== "Example"

    ```dax
    DaxLib.SVG.Viz.ProgressBar(
        [Completed],        // valueRefExpr
        [Target],           // trackRefExpr
        ,                   // color
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
    			color: STRING = BLANK(),
    			orientation: STRING = "Horizontal",
    			width: INT64 = 120,
    			height: INT64 = 48
    		) =>
    
    			VAR _Marks =
    				DaxLib.SVG.Compound.ProgressBar(
    					0, 
                        0, 
                        width, 
                        height,
    					valueRefExpr,
                        trackRefExpr, 
                        color, 
                        "#E1DFDD",
                        orientation
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Marks ), DaxLib.SVG.SVG( "100%", "100%", _Marks, "0 0 " & width & " " & height ) )
    ```