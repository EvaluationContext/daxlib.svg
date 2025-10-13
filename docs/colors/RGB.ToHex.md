---
comments: true
---

# Color.RGB.ToHex

RGB to Hex conversion

=== "Syntax"

    ```dax
    DaxLib.SVG.Color.RGB.ToHex( red, green, blue, alpha )
    ```

    | Name  | Type   | Required | Description                        |
    |:---:|:---:|:---:|---|
    | red   | <span class="type-label int64">INT64</span>   | :material-check: | The red value (0-255)             |
    | green | <span class="type-label int64">INT64</span>   | :material-check: | The green value (0-255)           |
    | blue  | <span class="type-label int64">INT64</span>  | :material-check: | The blue value (0-255)            |
    | alpha | <span class="type-label number">DOUBLE</span> | :material-close: | The alpha value (0-1)   |

    <span class="type-label string">STRING</span> Hex color code

=== "Example"

    ```dax
    DaxLib.SVG.Color.RGB.ToHex(255, 0, 0, BLANK())
    // Returns: "#FF0000" (red)
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Color.RGB.ToHex' =
        (
            red: INT64,
            green: INT64,
            blue: INT64,
            alpha: DOUBLE
        ) =>
        
            "#" &
            DaxLib.SVG.Color.Int.ToHex( red, 2 ) &
            DaxLib.SVG.Color.Int.ToHex( green, 2 ) &
            DaxLib.SVG.Color.Int.ToHex( blue, 2 ) &
            IF( NOT ISBLANK( alpha ), DaxLib.SVG.Color.Int.ToHex( alpha * 255, 2 ) )
    ```