# Transforms

Generates transform string for SVG elements

=== "Syntax"

    ```dax
    DaxLib.SVG.Transforms( translate, rotate, scale, skewX, skewY )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | translate | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Translation coordinates (e.g., "10,20") |
    | rotate | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Rotation with optional center point (e.g., "45" or "45 50 50") |
    | scale | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Scale factors (e.g., "2" or "2,1.5") |
    | skewX | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Horizontal skew angle in degrees |
    | skewY | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Vertical skew angle in degrees |

    <span class="type-label string">STRING</span> A transform attribute value that can be used with the transform attribute of SVG elements.

=== "Example"

    ```dax
    DaxLib.SVG.Transforms("10,20", "45", "1.5", "", "")
    // Returns: "translate(10,20) rotate(45) scale(1.5)"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Transforms' =
    		(
    			translate: STRING = BLANK(),
    			rotate: STRING = BLANK(),
    			scale: STRING = BLANK(),
    			skewX: STRING = BLANK(),
    			skewY: STRING = BLANK()
    		) =>
    
    			IF(NOT ISBLANK(translate), "translate(" & translate & ") ") &
    			IF(NOT ISBLANK(rotate), "rotate(" & rotate & ") ") &
    			IF(NOT ISBLANK(scale), "scale(" & scale & ") ") &
    			IF(NOT ISBLANK(skewX), "skewX(" & skewX & ") ") &
    			IF(NOT ISBLANK(skewY), "skewY(" & skewY & ") ")
    ```