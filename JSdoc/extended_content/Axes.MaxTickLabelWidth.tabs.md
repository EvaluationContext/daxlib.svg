=== "Example"

    ```dax
    DaxLib.SVG.Axes.MaxTickLabelWidth(
        0,              // axisMin
        1000,           // axisMax
        5,              // tickCount
        10,             // axisFontSize
        0.56,           // labelWidthFactor (Segoe UI default)
        FALSE           // axisIsDate
    )
    // Returns estimated max label width in pixels
    // Used to reserve space for Y-axis labels in Axes.Layout
    ```
