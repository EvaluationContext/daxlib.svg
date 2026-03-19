=== "Example"

    ```dax hl_lines="6-38"
    DaxLib.SVG.SVG(
        500,                    // width
        100,                    // height
        "0 0 100 20",           // viewbox
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.RadialGradient(
                "myGradient",   // id
                DaxLib.SVG.Def.GradientStop( 
                    "10%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        25
                    ),          // colour
                    BLANK()     // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "80%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        26
                    ),          // colour
                    0.5         // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "95%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        27
                    ),          // colour
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
        BLANK()                 // sortODer
    )
    ```