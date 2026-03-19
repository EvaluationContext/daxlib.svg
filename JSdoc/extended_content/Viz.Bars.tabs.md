=== "Example"

    ```dax
    DaxLib.SVG.Viz.Bars(
        Dates[Date],        // axisRefColumn
        [Total Cost],       // measureRefExpr
        BLANK(),            // color (uses default theme)
        BLANK(),            // minMarkColor
        BLANK(),            // maxMarkColor
        TRUE,               // showAxis
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded bar chart
    // Set as a measure with DataCategory = "ImageUrl"
    ```
