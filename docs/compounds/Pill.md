---
comments: true
---

# Compound.Pill

Generates a pill SVG compound (rounded rectangle with text centered inside)

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><rect x='1' y='1' width='93.1' height='18.032' rx='10' ry='10' fill='#EC008C' fill-opacity='0.2' stroke='#EC008C' stroke-width='1'  /><text x='47.5' y='11.368' dx='0' dy='0' fill='#EC008C' font-family='Segoe UI' font-size='12' text-anchor='middle' dominant-baseline='middle'  >DaxLib</text></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Pill( x, y, width, height, paddingX, paddingY, txt, color )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | x | <span class="type-label int64">INT64</span> | :material-check: | The x position of compound |
    | y | <span class="type-label int64">INT64</span> | :material-check: | The y position of compound |
    | width | <span class="type-label int64">INT64</span> | :material-check: | The width of the compound |
    | height | <span class="type-label int64">INT64</span> | :material-check: | The height of the compound |
    | paddingX | <span class="type-label number">DOUBLE</span> | :material-close: | The horizontal padding percentage (0.0-1.0, e.g., 0.1 = 10% padding) |
    | paddingY | <span class="type-label number">DOUBLE</span> | :material-close: | The vertical padding percentage (0.0-1.0, e.g., 0.1 = 10% padding) |
    | txt | <span class="type-label string">STRING</span> | :material-check: | The text to display |
    | color | <span class="type-label string">STRING</span> | :material-check: | The Hex color of the pill (e.g., "#01B8AA80") |

    <span class="type-label string">STRING</span> A pill-shaped SVG element with rounded corners and centered text

=== "Example"

    ```dax hl_lines="5-17"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Pill(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            0.05,               // paddingX
            0.02,               // paddingY
            MAX( Products[Brand] ), // txt
            DaxLib.SVG.Colour.Theme(
                "Power BI",
                25
            )                   // colour
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Pill' = 
        (
            x: INT64,
            y: INT64,
            width: INT64,
            height: INT64,
            paddingX: DOUBLE,
            paddingY: DOUBLE,
            txt: STRING,
            color: STRING
        ) =>

        // Apply padding to dimensions
        VAR _X =            x + (width * (IF(ISBLANK(paddingX), 0, paddingX) / 2))
        VAR _Y =            y + (height * (IF(ISBLANK(paddingY), 0, paddingY) / 2))
        VAR _Width =        width * (1 - IF(ISBLANK(paddingX), 0, paddingX))
        VAR _Height =       height * (1 - IF(ISBLANK(paddingY), 0, paddingY))

        VAR _Pill = 
            DaxLib.SVG.Element.Rect(
                1,                  // x
                1,                  // y
                _Width * 0.98,      // width
                _Height * 0.92,     // height
                10,                 // rx
                10,                 // ry
                DaxLib.SVG.Attr.Shapes(
                    color,          // fill
                    0.2,            // fillOpacity
                    BLANK(),        // fillRule
                    color,          // stroke
                    1,              // strokeWidth
                    BLANK(),        // strokeOpacity
                    BLANK()         // opacity
                ),                  // attributes
                BLANK()             // transforms
            )

        VAR _TextElement = 
            DaxLib.SVG.Element.Txt(
                _Width * 0.50,      // x
                _Height * 0.58,     // y
                txt,                // txt
                0,                  // dx
                0,                  // dy
                DaxLib.SVG.Attr.Shapes(
                    color,          // fill
                    BLANK(),        // fillOpacity
                    BLANK(),        // fillRule
                    BLANK(),        // stroke
                    BLANK(),        // strokeWidth
                    BLANK(),        // strokeOpacity
                    BLANK()         // opacity
                ) &
                DaxLib.SVG.Attr.Txt(
                    "Segoe UI",     // fontFamily
                    12,             // fontSize
                    BLANK(),        // fontWeight
                    BLANK(),        // fontStyle
                    "middle",       // textAnchor
                    "middle",       // baseline
                    BLANK(),        // textDecoration
                    BLANK(),        // letterSpacing
                    BLANK()         // wordSpacing
                ),                  // attributes
                BLANK()             // transforms
            )

        VAR _CombinedElements = 
            _Pill & 
            _TextElement

        RETURN
            IF( NOT ISBLANK( txt ), _CombinedElements )
    ```