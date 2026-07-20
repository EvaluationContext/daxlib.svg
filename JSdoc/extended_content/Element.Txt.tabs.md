=== "Example"

    ```dax hl_lines="4-22"
    DaxLib.SVG.SVG( 
        500,                // width
        100,                // height
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
        "0 0 100 20",       // viewbox
        BLANK()             // sortValue
    )
    ```