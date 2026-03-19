=== "Example"

    ```dax hl_lines="5-16"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Jitter(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            0.05,               // paddingX
            0.02,               // paddingY
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            "#EC008C",          // pointColor
            0.5                 // jitterAmount
        ),
        BLANK()
    )
    ```