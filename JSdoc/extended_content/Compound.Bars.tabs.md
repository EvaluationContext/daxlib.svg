=== "Example"

    ```dax hl_lines="5-19"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Bars(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            "#EC008C",          // barColor
            BLANK(),            // minMarkColor
            BLANK(),            // maxMarkColor
            FALSE,              // showAxis
            10,                 // axisFontSize
            0.05,               // paddingX
            0.04                // paddingY
        ),
        BLANK()
    )
    ```
