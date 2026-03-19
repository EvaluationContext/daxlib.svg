=== "Example"

    ```dax hl_lines="5-34"
    DaxLib.SVG.SVG( 
        500,                // width
        100,                // height
        "0 0 100 20",       // viewbox
        DaxLib.SVG.Element.Rect(
            "50%",          // x
            "0%",           // y
            "40%",          // width
            8,              // height
            blank(),        // rx
            blank(),        // ry
            DaxLib.SVG.Attr.Shapes(
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // fill
                0.3,        // fillOpacity
                BLANK(),    // fillRule
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // stroke
                2,          // strokeWidth
                0.9,        // strokeOpacity
                BLANK()     // opacity
            ),              // attributes
            DaxLib.SVG.Transforms(
                -15,        // translate
                5,          // rotate
                BLANK(),    // scale
                -20,        // skewX
                BLANK()     // skewY
            )               // transforms
        ),                  // contents
        BLANK()             // sortValue
    )
    ```