=== "Example"

    ```dax hl_lines="5-23"
    DaxLib.SVG.SVG( 
        500,                // width
        100,                // height
        "0 0 100 20",       // viewbox
        DaxLib.SVG.Element.Txt(
            10,             // x
            10, 	        // y
            "DaxLib",       // txt
            0,              // dx
            0,              // dy
            DaxLib.SVG.Attr.Txt(
                "Arial",    // fontFamily
                12,         // fontSize
                BLANK(),    // fontWeight
                BLANK(),    // fontStyle
                BLANK(),    // textAnchor
                BLANK(),    // baseline
                BLANK(),    // textDecoration
                BLANK(),    // letterSpacing
                BLANK()     // wordSpacing
            ),              // attributes
            BLANK()         // transforms
        ),                  // contents
        BLANK()             // sortValue
    )
    ```