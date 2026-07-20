=== "Example"

    ```dax hl_lines="4-22"
    DaxLib.SVG.SVG(
        500,                // width
        100,                // height
        DaxLib.SVG.Element.Line(
            1,              // x1
            5,              // y1
            80,             // x2
            5,              // y2
            DaxLib.SVG.Attr.Shapes(
                BLANK(),    // fill
                BLANK(),    // fillOpacity
                BLANK(),    // fillRule
                DaxLib.SVG.Color.Theme(
                    "Power BI",
                    25
                ),          // stroke
                2,          // strokeWidth
                BLANK(),    // strokeOpacity
                BLANK()     // opacity
            ),              // attributes
            BLANK()         // transforms
        ),                  // contents
        "0 0 100 20",       // viewbox
        BLANK()             // sortValue
    )
    ```