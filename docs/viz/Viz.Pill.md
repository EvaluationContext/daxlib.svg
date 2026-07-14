# Viz.Pill

Renders a pill-shaped badge as an SVG data URI with centered text

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><rect x='1' y='1' width='93.1' height='18.032' rx='10' ry='10' fill='#EC008C' fill-opacity='0.2' stroke='#EC008C' stroke-width='1'  /><text x='47.5' y='11.368' dx='0' dy='0' fill='#EC008C' font-family='Segoe UI' font-size='12' text-anchor='middle' dominant-baseline='middle'  >DaxLib</text></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Viz.Pill( txt, color, width, height )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | txt | <span class="type-label string">STRING</span> | :material-check: |  | The text to display |
    | color | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional pill color. Defaults to Power BI theme color |
    | width | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 120` | Optional: SVG width. Defaults to 120 |
    | height | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 48` | Optional: SVG height. Defaults to 48 |

    <span class="type-label string">STRING</span> SVG Pill

=== "Example"

    ```dax
    DaxLib.SVG.Viz.Pill(
        "Active",           // txt
        "#EC008C",        // color
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
    			color: STRING = BLANK(),
    			width: INT64 = 120,
    			height: INT64 = 48
    		) =>
    
    			VAR _Marks =
    				DaxLib.SVG.Compound.Pill(
    					0, 
                        0, 
                        width, 
                        height, 
                        txt, 
                        color
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Marks ), DaxLib.SVG.SVG( "100%", "100%", _Marks, "0 0 " & width & " " & height ) )
    ```