=== "Example"

    ```dax
    DaxLib.SVG.Viz.Line(
        Dates[Date],        // axisRef
        [Total Cost],       // measureRef
        ,                   // color
        TRUE,               // showAxis
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded line chart
    // Set as a measure with DataCategory = "ImageUrl"
    ```
