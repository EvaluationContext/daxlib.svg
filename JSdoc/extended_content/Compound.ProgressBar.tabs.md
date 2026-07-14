=== "Example"

    ```dax hl_lines="5-17"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.ProgressBar(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            [Completed],        // valueRef
            [Target],           // trackRef
            "#EC008C",          // fillColor
            "#E1DFDD",          // trackColor
            "Horizontal",       // orientation
            0.02,               // paddingX
            0.05                // paddingY
        ),
        BLANK()
    )
    ```
