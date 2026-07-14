=== "Example"

    ```dax hl_lines="5-18"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Violin(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            MAX( Samples[Samples] ), // samples
            MAX( Bandwidth[Bandwidth] ), // bandwidth
            "#EC008C",          // color
            "Horizontal",       // orientation
            0.05,               // paddingX
            0.02                // paddingY
        ),
        BLANK()
    )
    ```