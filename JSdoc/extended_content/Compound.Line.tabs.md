=== "Example"

    ```dax hl_lines="5-19"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Line(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            0.05,               // paddingX
            0.04,               // paddingY
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            "#EC008C",          // lineColor
            BLANK(),            // minMarkColor
            BLANK(),            // maxMarkColor
            TRUE,               // showAxis
            10                  // axisFontSize
        ),
        BLANK()
    )
    ```