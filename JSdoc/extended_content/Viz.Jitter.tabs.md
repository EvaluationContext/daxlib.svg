=== "Example"

    ```dax
    DaxLib.SVG.Viz.Jitter(
        Products[Product],  // axisRef
        [Total Cost],       // measureRef
        ,                   // color
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded jitter plot
    // Set as a measure with DataCategory = "ImageUrl"
    ```
