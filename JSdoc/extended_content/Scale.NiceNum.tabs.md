=== "Example"

    ```dax
    DaxLib.SVG.Scale.NiceNum( 17.3, TRUE )
    // Returns 20 (rounds to nearest nice number)

    DaxLib.SVG.Scale.NiceNum( 17.3, FALSE )
    // Returns 20 (ceiling to next nice number for range extents)

    DaxLib.SVG.Scale.NiceNum( 0.73, TRUE )
    // Returns 1
    ```
