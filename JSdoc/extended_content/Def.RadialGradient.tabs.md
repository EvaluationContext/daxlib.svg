=== "Example"

    ```dax hl_lines="5-37"
    DaxLib.SVG.SVG(
        500,                    // width
        100,                    // height
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.RadialGradient(
                "myGradient",   // defId
                DaxLib.SVG.Def.GradientStop( 
                    "10%",      // offset
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
                    ),          // color
                    0.5         // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "95%",      // offset
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        27
                    ),          // color
                    BLANK()     // opacity
                ),              // stops
                BLANK(),        // cx
                BLANK(),        // cy
                BLANK(),        // r
                BLANK(),        // fx
                BLANK(),        // fy
                BLANK()         // fr
            )
        ) &
        DaxLib.SVG.Element.Circle(
            "50%",              // cx
            "50%",              // cy
            15,                 // r
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
        ),                      // contents
        "0 0 100 20",           // viewbox
        BLANK()                 // sortValue
    )
    ```