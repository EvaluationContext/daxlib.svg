=== "Example"

    ```dax hl_lines="3-12"
    VAR _Defs = 
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.ClipPath(
                "clip-circle",      // id
                DaxLib.SVG.Element.Circle(
                    "50%",          // cx 
                    "80%",          // cy
                    8,              // r
                    BLANK(),        // attributes
                    BLANK()         // transforms
                )                   // elements
            )
        )

    VAR _Rectangle = 
        DaxLib.SVG.Element.Rect(
            "0%",           // x
            "0%",           // y
            "100%",         // width
            "80%",          // height
            BLANK(),        // rx
            BLANK(),        // ry
            DaxLib.SVG.Attr.Shapes(
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // fill
                BLANK(),    // fillOpacity
                BLANK(),    // fillRule   
                BLANK(),    // stroke
                BLANK(),    // strokeWidth
                BLANK(),    // strokeOpacity
                BLANK()     // opacity
            ) &
            "clip-path='url(#clip-circle)'",  // Add clip-path reference
            BLANK()         // transforms
        )

    RETURN
    DaxLib.SVG.SVG(
        500,
        100,
        "0 0 100 20",
        _Defs &          
        _Rectangle,    
        BLANK()         
    )
    ```