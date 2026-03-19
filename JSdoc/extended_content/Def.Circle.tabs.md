=== "Example"

    ```dax
    DaxLib.SVG.Def.Circle(
        "myCircle", 
        "50", 
        "50", 
        "40", 
        DaxLib.SVG.Attr.Shapes(
            "red",      // fill
            BLANK(),    // fillOpacity
            BLANK(),    // fillRule
            "blue",     // stroke
            2,          // strokeWidth
            BLANK(),    // strokeOpacity
            BLANK()     // opacity
        ), 
        BLANK()
    )
    // Returns: <circle id='myCircle' cx='50' cy='50' r='40' fill='red' stroke='blue' stroke-width='2' />
    ```
