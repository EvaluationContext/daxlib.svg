=== "Example"

    ```dax hl_lines="5-23"
     DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Area(
            0,                  // x
            0,                  // y
            100,                // width
            20,                 // height
            0.05,               // paddingX
            0.02,               // paddingY
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            "#EC008C",          // fillColor
            0.2,                // fillOpacity
            "#EC008C",          // strokeColor
            "#D04848",          // minMarkColor
            "#2E8B57",          // maxMarkColor
            TRUE,               // showAxis
            8                   // axisFontSize
        ),
        BLANK()
    )
    ```