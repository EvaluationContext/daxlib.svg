=== "Example"

    ```dax
    DaxLib.SVG.Viz.Violin(
        Products[Product],  // axisRef
        [Total Cost],       // measureRef
        ,                   // color (uses default theme)
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded violin plot
    // Set as a measure with DataCategory = "ImageUrl"
    ```
