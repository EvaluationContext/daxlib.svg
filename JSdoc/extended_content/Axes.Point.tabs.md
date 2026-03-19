=== "Example"

    ```dax
    DaxLib.SVG.Axes.Point(
        "Vertical",     // orientation
        50,             // axisIndex
        250,            // measureValue
        0,              // xMin
        100,            // xMax
        0,              // yMin
        500,            // yMax
        40,             // plotX
        5,              // plotY
        460,            // plotWidth
        270             // plotHeight
    )
    // Returns single-row table: { @X, @Y }
    // Coordinates mapped to plot pixel space
    ```
