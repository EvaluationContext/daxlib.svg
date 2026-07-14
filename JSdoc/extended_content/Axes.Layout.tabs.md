=== "Example"

    ```dax
    DaxLib.SVG.Axes.Layout(
        0,              // x
        0,              // y
        500,            // width
        300,            // height
        35,             // maxTickLabelWidth
        TRUE,           // showAxis
        10              // axisFontSize
    )
    // Returns single-row table:
    //   @PlotX     – left edge of plot area (after Y-axis reservation)
    //   @PlotY     – top edge of plot area (after top padding)
    //   @PlotWidth – available plot width
    //   @PlotHeight – available plot height
    ```
