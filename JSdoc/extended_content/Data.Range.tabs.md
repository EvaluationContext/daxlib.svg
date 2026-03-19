=== "Example"

    ```dax
    DaxLib.SVG.Data.Range( 3.2, 97.8, TRUE )
    // Returns single-row table:
    //   @Min = 3.2
    //   @Max = 97.8
    //   @Baseline = 0     (zero because includeZero = TRUE and min > 0)

    DaxLib.SVG.Data.Range( -10, 50, FALSE )
    // Returns single-row table:
    //   @Min = -10
    //   @Max = 50
    //   @Baseline = -10   (baseline equals min when includeZero = FALSE)
    ```
