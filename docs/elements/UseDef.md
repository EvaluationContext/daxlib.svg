---
comments: true
---

# Element.UseDef

Applies a previously defined `DaxLib.SVG.Def.*` shape element (ie. `#!xml <rect>`, `#!xml <circle>`, `#!xml <line>`, via `#!xml <use>`

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><circle id='Circle1' cx='0' cy='0' r='8' fill='#EC008C' fill-opacity='0.8' stroke='black' stroke-width='1' stroke-opacity='0.8'  /><circle id='Circle2' cx='0' cy='0' r='8' fill='#533285' fill-opacity='0.8' stroke='black' stroke-width='1' stroke-opacity='0.8'  /><path id='myPath' d='M10 10 L30 5 L90 15 L100 0' fill='none' fill-opacity='0.8' stroke='#EC008C'  /></defs><use href='#Circle1' x='20' y='10' transform='rotate(30) '/><use href='#Circle2' x='50' y='10'/><use href='#Circle1' x='80' y='10'/><use href='#myPath' y='5'/><use href='#myPath' y='10' transform='rotate(-10) '/></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.UseDef( defId, x, y, transforms )
    ```

    | Name       | Type   | Required | Description                                                        |
    |:---:|:---:|:---:|---|
    | defId      | <span class="type-label string">STRING</span> | :material-check: | The identifier of the defined element to use                      |
    | x          | <span class="type-label string">STRING</span> | :material-close: | X position where the element should be placed                     |
    | y          | <span class="type-label string">STRING</span> | :material-close: | Y position where the element should be placed                     |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`) |

    <span class="type-label string">**STRING**</span> `#!xml <use>` element

=== "Example"

    ```dax hl_lines="59-101"
    VAR _Defs =
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.Circle(
                "Circle1",      // id
                0,              // cx
                0,              // cy
                8,              // r
                DaxLib.SVG.Attr.Shapes(
                    DaxLib.SVG.Colour.Theme(
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
                "Circle2",      // id
                0,              // cx
                0,              // cy
                8,              // r
                DaxLib.SVG.Attr.Shapes(
                    DaxLib.SVG.Colour.Theme(
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
                "myPath",       // id
                "M10 10 L30 5 L90 15 L100 0", // d
                DaxLib.SVG.Attr.Shapes(
                    "none",     // fill
                    0.8,        // fillOpacity
                    BLANK(),    // fillRule
                    DaxLib.SVG.Colour.Theme(
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
            "Circle1",   // id
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
            "Circle2",      // id
            50,             // x
            10,             // y
            BLANK()         // transforms
        ) &
        DaxLib.SVG.Element.UseDef(
            "Circle1",      // id
            80,             // x
            10,             // y
            BLANK()         // transforms
        ) &
        DaxLib.SVG.Element.UseDef(
            "myPath",       // id
            BLANK(),        // x
            5,              // y
            BLANK()         // transforms
        ) &
        DaxLib.SVG.Element.UseDef(
            "myPath",       // id
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
        "0 0 100 20",       // viewbox
        _Contents,          // contents
        BLANK()             // sortValue
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Element.UseDef' = 
        (
            defId: STRING,
            x: STRING,
            y: STRING,
            transforms: STRING
        ) =>

            "<use" &
            " href='#" & defId & "'" &
            IF( NOT ISBLANK( x ), " x='" & x & "'" ) &
            IF( NOT ISBLANK( y ), " y='" & y & "'" ) &
            IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
            "/>"
    ```