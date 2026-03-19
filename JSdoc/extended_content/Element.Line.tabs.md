=== "Example"

    ```dax hl_lines="5-23"
    DaxLib.SVG.SVG(
        500,                // width
        100,                // height
        "0 0 100 20",       // viewbox
        DaxLib.SVG.Element.Line(
            1,              // x1
            5,              // y1
            80,             // x2
            5,              // y2
            DaxLib.SVG.Attr.Shapes(
                BLANK(),    // fill
                BLANK(),    // fillOpacity
                BLANK(),    // fillRule
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // stroke
                2,          // strokeWidth
                BLANK(),    // strokeOpacity
                BLANK()     // opacity
            ),              // attributes
            BLANK()         // transforms
        ),                  // contents
        BLANK()             // sortValue
    )
    ```