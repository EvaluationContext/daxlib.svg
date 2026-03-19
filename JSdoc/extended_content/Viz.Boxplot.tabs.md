=== "Example"

    ```dax
    DaxLib.SVG.Viz.Boxplot(
        Products[Product],  // axisRefColumn
        [Total Cost],       // measureRefExpr
        BLANK(),            // color (uses default theme)
        TRUE,               // showOutliers
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded box plot
    // Set as a measure with DataCategory = "ImageUrl"
    ```
