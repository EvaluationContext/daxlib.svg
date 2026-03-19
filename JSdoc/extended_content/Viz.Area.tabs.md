=== "Example"

    ```dax
    DaxLib.SVG.Viz.Area(
        Dates[Date],        // axisRefColumn
        [Total Cost],       // measureRefExpr
        BLANK(),            // color (uses default theme)
        TRUE,               // showAxis
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded area chart
    // Set as a measure with DataCategory = "ImageUrl"
    ```