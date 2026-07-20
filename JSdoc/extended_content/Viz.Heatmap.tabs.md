=== "Example"

    ```dax
    DaxLib.SVG.Viz.Heatmap(
        Products[Product],  // axisRef
        [Total Cost],       // measureRef
        ,                   // color
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded heatmap
    // Set as a measure with DataCategory = "ImageUrl"
    ```
