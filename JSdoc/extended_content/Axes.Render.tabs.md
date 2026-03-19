=== "Example"

    ```dax
    DaxLib.SVG.Axes.Render(
        40,             // plotX
        5,              // plotY
        460,            // plotWidth
        270,            // plotHeight
        0,              // xAxisMin
        100,            // xAxisMax
        0,              // yAxisMin
        500,            // yAxisMax
        TRUE,           // showAxis
        10,             // axisFontSize
        FALSE,          // xAxisIsDate
        FALSE,          // yAxisIsDate
        5,              // tickCountX
        4               // tickCountY
    )
    // Returns SVG string with axis lines, ticks, and labels
    // Returns BLANK when showAxis = FALSE
    ```
