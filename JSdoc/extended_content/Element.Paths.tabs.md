=== "Example"

    ```dax hl_lines="4-19"
    DaxLib.SVG.SVG(
        500,                // width
        100,                // height
        DaxLib.SVG.Element.Paths(
            "M10 10 L30 5 C50 0 70 20 90 15 L100 0", // d
            DaxLib.SVG.Attr.Shapes(
                "none",     // fill
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