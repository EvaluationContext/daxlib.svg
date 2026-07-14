# Attr.Shapes

Generates a STRING of common shape attributes that can be passed to `DaxLib.SVG.Element.*` or `DaxLib.SVG.Def.*` functions

=== "Syntax"

    ```dax
    DaxLib.SVG.Attr.Shapes( fill, fillOpacity, fillRule, stroke, strokeWidth, strokeOpacity, opacity )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | fill | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Fill color or gradient reference. Omitted if not specified |
    | fillOpacity | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax BLANK()` | Fill opacity (0-1). Omitted if not specified |
    | fillRule | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Fill rule ("nonzero" or "evenodd"). Omitted if not specified |
    | stroke | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Stroke color. Omitted if not specified |
    | strokeWidth | <span class="type-label int64">INT64</span> | :material-close: | `#!dax BLANK()` | Stroke width. Omitted if not specified |
    | strokeOpacity | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax BLANK()` | Stroke opacity (0-1). Omitted if not specified |
    | opacity | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax BLANK()` | Overall opacity (0-1). Omitted if not specified |

    <span class="type-label string">STRING</span> An attribute string that can be used directly in SVG elements

=== "Example"

    ```dax
    DaxLib.SVG.Attr.Shapes("#FF0000", 0.8, "nonzero", "#000000", 2, 1, 1)
    // Returns "fill='#FF0000' fill-opacity='0.8' fill-rule='nonzero' stroke='#000000' stroke-width='2' stroke-opacity='1' opacity='1' "
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Attr.Shapes' =
    		(
    			fill: STRING = BLANK(),
    			fillOpacity: DOUBLE = BLANK(),
    			fillRule: STRING = BLANK(),
    			stroke: STRING = BLANK(),
    			strokeWidth: INT64 = BLANK(),
    			strokeOpacity: DOUBLE = BLANK(),
    			opacity: DOUBLE = BLANK()
    		) =>
    
    			IF( NOT ISBLANK( fill ),          "fill='" & fill & "' ") &
    			IF( NOT ISBLANK( fillOpacity ),   "fill-opacity='" & fillOpacity & "' ") &
    			IF( NOT ISBLANK( fillRule ),      "fill-rule='" & fillRule & "' ") &
    			IF( NOT ISBLANK( stroke ),        "stroke='" & stroke & "' ") &
    			IF( NOT ISBLANK( strokeWidth ),   "stroke-width='" & strokeWidth & "' ") &
    			IF( NOT ISBLANK( strokeOpacity ), "stroke-opacity='" & strokeOpacity & "' ") &
    			IF( NOT ISBLANK( opacity ),       "opacity='" & opacity & "' ")
    ```