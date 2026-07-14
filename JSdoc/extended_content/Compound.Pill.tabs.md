=== "Example"

    ```dax hl_lines="5-14"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Pill(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            MAX( Products[Brand] ), // txt
            "#EC008C",          // color
            0.05,               // paddingX
            0.02                // paddingY
        ),
        BLANK()
    )
    ```