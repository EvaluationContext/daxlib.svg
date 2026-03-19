=== "Example"

    ```dax
    DaxLib.SVG.Element.Defs(
        DaxLib.SVG.Def.Circle(
            "myCircle",        // defId
            "50",              // cx
            "50",              // cy
            "20",              // r
            "fill='red'",      // attributes
            BLANK()            // transforms
        ) &
        DaxLib.SVG.Def.Rect(
            "myRect",          // defId
            "100",             // width
            "60",              // height
            "5",               // rx
            "5",               // ry
            "fill='blue'",     // attributes
            BLANK()            // transforms
        )
    )
    // Returns: <defs><circle id='myCircle' cx='50' cy='50' r='20' fill='red' /><rect id='myRect' width='100' height='60' rx='5' ry='5' fill='blue' /></defs>
    ```
