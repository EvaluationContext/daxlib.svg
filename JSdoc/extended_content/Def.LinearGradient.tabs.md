=== "Example"

    ```dax hl_lines="6-29"
    DaxLib.SVG.SVG(
        500,
        100,
        "0 0 100 20",
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.LinearGradient(
                "myGradient",   // defId
                DaxLib.SVG.Def.GradientStop(
                    "20%",      // offset
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        25
                    ),          // color
                    BLANK()     // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "80%",      // offset
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        26
                    ),           // color
                    BLANK()     // opacity
                ),              // stops
                BLANK(),        // x1
                BLANK(),        // y1
                BLANK(),        // x2
                BLANK()         // y2
            )                   // defs
        ) &
        DaxLib.SVG.Element.Rect(
            2,                  // x
            2,                  // y
            "80%",              // width
            "80%",              // height
            BLANK(),            // rx
            BLANK(),            // ry
            DaxLib.SVG.Attr.Shapes(
                "url(""" & "#myGradient" & """)", // fill
                BLANK(),        // fillOpacity
                BLANK(),        // fillRule   
                BLANK(),        // stroke
                BLANK(),        // strokeWidth
                BLANK(),        // strokeOpacity
                BLANK()         // opacity
            ),                  // attributes
            BLANK()             // transforms
        ),
        BLANK()                 // sortValue               
    )
    ```