=== "Example"

    ```dax hl_lines="5-25"
    DaxLib.SVG.SVG(
        500,                // width
        100,                // height
        "0 0 100 20",       // viewbox
        DaxLib.SVG.Element.Circle(
            50,             // cx
            10,             // cy
            "10%",          // r
            DaxLib.SVG.Attr.Shapes(
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),              // fill
                0.5,            // fillOpacity
                BLANK(),        // fillRule   
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),              // stroke
                1,              // strokeWidth
                BLANK(),        // strokeOpacity
                BLANK()         // opacity
            ),              // attributes
            BLANK()         // transforms
        ),                  // contents
        BLANK()             // sortValue
    )
    ```