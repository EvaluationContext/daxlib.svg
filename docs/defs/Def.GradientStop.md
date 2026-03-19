# Def.GradientStop

Create a gradient stop element

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.GradientStop( offset, color, opacity )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | offset | <span class="type-label string">STRING</span> | :material-check: | Stop position |
    | color | <span class="type-label string">STRING</span> | :material-check: | Color value (hex or named color) |
    | opacity | <span class="type-label string">STRING</span> | :material-close: | Optional: Opacity value |

    <span class="type-label string">STRING</span> <stop> element

=== "Example"

    ```dax
    DaxLib.SVG.Def.GradientStop("0%", "red", "1")
    // Returns: <stop offset='0%' stop-color='red' stop-opacity='1'/>
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.GradientStop' =
    		(
    			offset: STRING,
    			color: STRING,
    			opacity: STRING
    		) =>
    
    			"<stop offset='" & offset & 
    			"' stop-color='" & color & "'" &
    			IF( NOT ISBLANK( opacity ), " stop-opacity='" & opacity & "'" ) &
    			"/>"
    ```