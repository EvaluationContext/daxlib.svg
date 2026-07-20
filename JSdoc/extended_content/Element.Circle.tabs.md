=== "Example"

    ```dax hl_lines="4-24"
    DaxLib.SVG.SVG(
        500,                // width
        100,                // height
        DaxLib.SVG.Element.Circle(
            50,             // cx
            10,             // cy
            "10%",          // r
            DaxLib.SVG.Attr.Shapes(
                DaxLib.SVG.Color.Theme(
                    "Power BI",
                    25
                ),              // fill
                0.5,            // fillOpacity
                BLANK(),        // fillRule   
                DaxLib.SVG.Color.Theme(
                    "Power BI",
                    25
                ),              // stroke
                1,              // strokeWidth
                BLANK(),        // strokeOpacity
                BLANK()         // opacity
            ),              // attributes
            BLANK()         // transforms
        ),                  // contents
        "0 0 100 20",       // viewbox
        BLANK()             // sortValue
    )
    ```