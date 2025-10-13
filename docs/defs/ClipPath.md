---
comments: true
---

# Def.ClipPath

Generates a reusable `#!xml <clipPath>` definition

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><clipPath id='clip-circle'><circle cx='50%' cy='80%' r='8'/></clipPath></defs><rect x='0%' y='0%' width='100%' height='80%' fill='#EC008C' clip-path='url(#clip-circle)' /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.ClipPath( defId, contents )
    ```

    | Name     | Type   | Required | Description                                                        |
    |:---:|:---:|:---:|---|
    | defId    | <span class="type-label string">STRING</span> | Yes      | The unique identifier for the clip path. (Example: "cut-top", "mask-circle") |
    | contents | <span class="type-label string">STRING</span> | Yes      | The SVG element(s) that make up the clipping path (typically a single shape) |

    <span class="type-label string">**STRING**</span> `#!xml <clipPath>` definition

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

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.ClipPath' =
        (
            defId : STRING,
            contents: STRING
        ) =>
            
            "<clipPath id='" & defId & "'>" &
            contents &
            "</clipPath>"
    ```