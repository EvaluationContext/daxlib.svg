=== "Example"

    ```dax
    DaxLib.SVG.Def.Rect(
        "myRect",
        "100",
        "50",
        "10",
        "10",
        DaxLib.SVG.Attr.Shapes(
            "blue",     // fill
            BLANK(),    // fillOpacity
            BLANK(),    // fillRule
            "black",    // stroke
            2,          // strokeWidth
            BLANK(),    // strokeOpacity
            BLANK()     // opacity
        ),
        BLANK()
    )
    // Returns: <rect id='myRect' width='100' height='50' rx='10' ry='10' fill='blue' stroke='black' stroke-width='2' />
    ```
