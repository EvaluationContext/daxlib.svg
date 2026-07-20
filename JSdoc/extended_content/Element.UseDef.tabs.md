=== "Example"

    ```dax hl_lines="59-101"
    VAR _Defs =
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.Circle(
                "Circle1",      // defId
                0,              // cx
                0,              // cy
                8,              // r
                DaxLib.SVG.Attr.Shapes(
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        25
                    ),          // fill
                    0.8,        // fillOpacity
                    BLANK(),    // fillRule
                    "black",    // stroke
                    1,          // strokeWidth
                    0.8,        // strokeOpacity
                    BLANK()     // opacity
                ),              // attributes
                BLANK()         // transforms
            ) &
            DaxLib.SVG.Def.Circle(
                "Circle2",      // defId
                0,              // cx
                0,              // cy
                8,              // r
                DaxLib.SVG.Attr.Shapes(
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        26
                    ),          // fill
                    0.8,        // fillOpacity
                    BLANK(),    // fillRule
                    "black",    // stroke
                    1,          // strokeWidth
                    0.8,        // strokeOpacity
                    BLANK()     // opacity
                ),              // attributes
                BLANK()         // transforms
            ) &
            DaxLib.SVG.Def.Paths(
                "myPath",       // defId
                "M10 10 L30 5 L90 15 L100 0", // d
                DaxLib.SVG.Attr.Shapes(
                    "none",     // fill
                    0.8,        // fillOpacity
                    BLANK(),    // fillRule
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        25
                    ),          // stroke
                    BLANK(),    // strokeWidth
                    BLANK(),    // strokeOpacity
                    BLANK()     // opacity
                ),              // attributes
                BLANK()         // transforms
            )
        )
    VAR _Contents = 
        _Defs &
        DaxLib.SVG.Element.UseDef(
            "Circle1",   // defId
            20,             // x
            10,             // y
            DaxLib.SVG.Transforms(
                BLANK(),    // translate
                30,         // rotate
                BLANK(),    // scale
                BLANK(),    // skewX
                BLANK()     // skewY
            )               // transforms
        ) &
        DaxLib.SVG.Element.UseDef(
            "Circle2",      // defId
            50,             // x
            10,             // y
            BLANK()         // transforms
        ) &
        DaxLib.SVG.Element.UseDef(
            "Circle1",      // defId
            80,             // x
            10,             // y
            BLANK()         // transforms
        ) &
        DaxLib.SVG.Element.UseDef(
            "myPath",       // defId
            BLANK(),        // x
            5,              // y
            BLANK()         // transforms
        ) &
        DaxLib.SVG.Element.UseDef(
            "myPath",       // defId
            BLANK(),        // x
            10,             // y
            DaxLib.SVG.Transforms(
                BLANK(),    // translate
                -10,        // rotate
                BLANK(),    // scale
                BLANK(),    // skewX
                BLANK()     // skewY
            )               // transforms
        )

    RETURN
    DaxLib.SVG.SVG(
        500,                // width
        100,                // height
        _Contents,          // contents
        "0 0 100 20",       // viewbox
        BLANK()             // sortValue
    )
    ```