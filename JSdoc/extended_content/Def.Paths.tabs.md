=== "Example"

    ```dax
    DaxLib.SVG.Def.Paths(
        "myPath",
        "M10 10 L90 90",
        DaxLib.SVG.Attr.Shapes(
            "none",     // fill
            BLANK(),    // fillOpacity
            BLANK(),    // fillRule
            "black",    // stroke
            2,          // strokeWidth
            BLANK(),    // strokeOpacity
            BLANK()     // opacity
        ),
        BLANK()
    )
    // Returns: <path id='myPath' d='M10 10 L90 90' fill='none' stroke='black' stroke-width='2' />
    ```
