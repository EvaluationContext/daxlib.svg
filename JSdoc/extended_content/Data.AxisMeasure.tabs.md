=== "Example"

    ```dax
    DaxLib.SVG.Data.AxisMeasure(
        Dates[Date],        // axisRefColumn
        [Total Cost],       // measureRefExpr
        "Auto"              // axisMode
    )
    // Returns table with columns:
    //   @AxisValue – the raw axis value
    //   @AxisIndex – numeric index (or value itself for numeric axes)
    //   @Value     – the evaluated measure
    // Sorted by @AxisIndex ascending
    ```
