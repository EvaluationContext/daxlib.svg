=== "Example"

    ```dax
    DaxLib.SVG.Viz.ProgressBar(
        [Completed],        // valueRefExpr
        [Target],           // trackRefExpr
        BLANK(),            // color (uses default theme)
        "Horizontal",       // orientation
        200,                // width
        20                  // height
    )
    // Returns an SVG data URI with an embedded progress bar
    // Set as a measure with DataCategory = "ImageUrl"
    ```
