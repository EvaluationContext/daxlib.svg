=== "Example"

    ```dax hl_lines="5-18"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Boxplot(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            "#EC008C",          // fillColor
            "#605E5C",          // strokeColor
            TRUE,               // showOutliers
            "Horizontal",       // orientation
            0.05,               // paddingX
            0.02                // paddingY
        ),
        BLANK()
    )
    ```