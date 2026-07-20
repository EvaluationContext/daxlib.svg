=== "Example"

    ```dax
    DaxLib.SVG.Viz.Bars(
        Dates[Date],        // axisRef
        [Total Cost],       // measureRef
        ,                   // color
        ,                   // minMarkColor
        ,                   // maxMarkColor
        TRUE,               // showAxis
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded bar chart
    // Set as a measure with DataCategory = "ImageUrl"
    ```
