# Viz.Pill

Renders a pill-shaped badge as an SVG data URI with centered text

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><rect x='1' y='1' width='93.1' height='18.032' rx='10' ry='10' fill='#EC008C' fill-opacity='0.2' stroke='#EC008C' stroke-width='1'  /><text x='47.5' y='11.368' dx='0' dy='0' fill='#EC008C' font-family='Segoe UI' font-size='12' text-anchor='middle' dominant-baseline='middle'  >DaxLib</text></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Viz.Pill( txt, color, width, height )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | txt | <span class="type-label string">STRING</span> | :material-check: | The text to display |
    | color | <span class="type-label string">STRING</span> | :material-close: | Optional pill color. Defaults to Power BI theme color |
    | width | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG width. Defaults to 120 |
    | height | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG height. Defaults to 48 |

    <span class="type-label string">STRING</span> SVG Pill

=== "Example"

    ```dax
    DaxLib.SVG.Viz.Pill(
        "Active",           // txt
        "#EC008C",          // color
        120,                // width
        28                  // height
    )
    // Returns an SVG data URI with a pill-shaped badge
    // Set as a measure with DataCategory = "ImageUrl"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Viz.Pill' =
    		(
    			txt: STRING,
    			color: STRING,
    			width: INT64,
    			height: INT64
    		) =>
    
    			VAR _W = IF( ISBLANK( width ), 120, width )
    			VAR _H = IF( ISBLANK( height ), 48, height )
    			VAR _Color = IF( NOT ISBLANK( color ), color, DaxLib.SVG.Color.Theme( "Power BI", 1 ) )
    			VAR _Marks =
    				DaxLib.SVG.Compound.Pill(
    					0, 0, _W, _H, 0, 0, txt, _Color
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Marks ), DaxLib.SVG.SVG( "100%", "100%", "0 0 " & _W & " " & _H, _Marks, BLANK() ) )
    ```