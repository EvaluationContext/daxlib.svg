=== "Example"

    ```dax
    DaxLib.SVG.Viz.Jitter(
        Products[Product],  // axisRefColumn
        [Total Cost],       // measureRefExpr
        BLANK(),            // color (uses default theme)
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded jitter plot
    // Set as a measure with DataCategory = "ImageUrl"
    ```
