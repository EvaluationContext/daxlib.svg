---
comments: true
---

# Def.LinearGradient

Generates a reusable `#!xml <linearGradient>` definition

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><linearGradient id='myGradient'><stop offset='20%' stop-color='#EC008C'/><stop offset='80%' stop-color='#533285'/></linearGradient></defs><rect x='2' y='2' width='80%' height='80%' fill='url("#myGradient")'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.LinearGradient( defId, stops, x1, y1, x2, y2 )
    ```

    | Name   | Type   | Required | Description                                                        |
    |:---:|:---:|:---:|---|
    | defId  | <span class="type-label string">STRING</span> | :material-check: | The unique identifier for the gradient                             |
    | stops  | <span class="type-label string">STRING</span> | :material-check: | Concatenated list of one or more `DaxLib.SVG.Def.GradientStop` elements |
    | x1     | <span class="type-label string">STRING</span> | :material-close: | Start X position                                                   |
    | y1     | <span class="type-label string">STRING</span> | :material-close: | Start Y position                                                   |
    | x2     | <span class="type-label string">STRING</span> | :material-close: | End X position                                                     |
    | y2     | <span class="type-label string">STRING</span> | :material-close: | End Y position                                                     |

    <span class="type-label string">**STRING**</span> `#!xml <linearGradient>` definition

=== "Example"

    ```dax hl_lines="6-29"
    DaxLib.SVG.SVG(
        500,
        100,
        "0 0 100 20",
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.LinearGradient(
                "myGradient",   // id
                DaxLib.SVG.Def.GradientStop(
                    "20%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        25
                    ),          // colour
                    BLANK()     // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "80%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        26
                    ),           // colour
                    BLANK()     // opacity
                ),              // stops
                BLANK(),        // x1
                BLANK(),        // y1
                BLANK(),        // x2
                BLANK()         // y2
            )                   // contents
        ) &
        DaxLib.SVG.Element.Rect(
            2,                  // x
            2,                  // y
            "80%",              // width
            "80%",              // height
            BLANK(),            // rx
            BLANK(),            // ry
            DaxLib.SVG.Attr.Shapes(
                "url(""" & "#myGradient" & """)", // fill
                BLANK(),        // fillOpacity
                BLANK(),        // fillRule   
                BLANK(),        // stroke
                BLANK(),        // strokeWidth
                BLANK(),        // strokeOpacity
                BLANK()         // opacity
            ),                  // attributes
            BLANK()             // transforms
        ),
        BLANK()                 // sortValue               
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.LinearGradient' =
        (
            defId: STRING,
            stops: STRING,
            x1: STRING,
            y1: STRING,
            x2: STRING,
            y2: STRING
        ) =>

            "<linearGradient" &
            " id='" & defId & "'" &
            IF( NOT ISBLANK( x1 ), " x1='" & x1 & "'" ) &
            IF( NOT ISBLANK( y1 ), " y1='" & y1 & "'" ) &
            IF( NOT ISBLANK( x2 ), " x2='" & x2 & "'" ) &
            IF( NOT ISBLANK( y2 ), " y2='" & y2 & "'" ) &
            ">" &
            stops &
            "</linearGradient>"
    ```