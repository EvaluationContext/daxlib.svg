---
comments: true
---

# Scale.Normalize

Maps a value from one scale to another. Used for scaling values to fit within SVG dimensions

=== "Syntax"

    ```dax
    DaxLib.SVG.Scale.Normalize( inputValue, fromMin, fromMax, toMin, toMax )
    ```

    | Name       | Type        | Required | Description                         |
    |:---:|:---:|:---:|---|
    | inputValue | <span class="type-label numeric">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | The value to map                    |
    | fromMin    | <span class="type-label numeric">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | The minimum value of the original scale |
    | fromMax    | <span class="type-label numeric">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | The maximum value of the original scale |
    | toMin      | <span class="type-label numeric">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | The minimum value of the new scale  |
    | toMax      | <span class="type-label numeric">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | The maximum value of the new scale  |

    <span class="type-label numeric">NUMERIC</span> mapped value

=== "Example"

    ```dax
    DaxLib.SVG.Scale.Normalize(50, 0, 200, 0, 100) 
    // Returns 25
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Scale.Normalize' =
        (
            inputValue: NUMERIC VAL,
            fromMin: NUMERIC VAL,
            fromMax: NUMERIC VAL,
            toMin: NUMERIC VAL,
            toMax: NUMERIC VAL
        ) =>

            ( ( inputValue - fromMin ) / ( fromMax - fromMin ) ) * ( toMax - toMin ) + toMin
    ```
