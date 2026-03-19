=== "Example"

    ```dax
    DaxLib.SVG.Axes.Baseline(
        "Vertical",     // orientation
        0,              // yMin
        500,            // yMax
        40,             // plotX
        5,              // plotY
        460,            // plotWidth
        270             // plotHeight
    )
    // Returns single-row table: { @BaseX, @BaseY }
    // Maps the numeric baseline (yMin) to plot coordinates
    ```
