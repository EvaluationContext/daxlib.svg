=== "Example"

    ```dax
    DaxLib.SVG.Def.Line(
        "myLine",
        "0",
        "0",
        "100",
        "100",
        DaxLib.SVG.Attr.Stroke(
            "black",    // stroke
            2,          // strokeWidth
            BLANK(),    // strokeOpacity
            BLANK(),    // strokeDasharray
            BLANK(),    // strokeDashoffset
            BLANK(),    // strokeLinecap
            BLANK(),    // strokeLinejoin
            BLANK(),    // strokeMiterlimit
            BLANK(),    // markerStart
            BLANK(),    // markerMid
            BLANK()     // markerEnd
        ),
        BLANK()
    )
    // Returns: <line id='myLine' x1='0' y1='0' x2='100' y2='100' stroke='black' stroke-width='2' />
    ```
