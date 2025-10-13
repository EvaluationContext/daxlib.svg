---
comments: true
---
# Element.Rect

Generates a `#!xml <rect>` element

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><rect x='50%' y='0%' width='40%' height='8' fill='#EC008C' fill-opacity='0.3' stroke='#EC008C' stroke-width='2' stroke-opacity='0.9'   transform='translate(-15) rotate(5) skewX(-20) '/></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.Rect( x, y, width, height, rx, ry, attributes, transforms )
    ```

    | Name       | Type   | Required | Description                                                               |
    |:---:|:---:|:---:|---|
    | x          | <span class="type-label string">STRING</span> | :material-check: | The x position                                                           |
    | y          | <span class="type-label string">STRING</span> | :material-check: | The y position                                                           |
    | width      | <span class="type-label string">STRING</span> | :material-check: | The width (pixels or percentage)                                         |
    | height     | <span class="type-label string">STRING</span> | :material-check: | The height (pixels or percentage)                                        |
    | rx         | <span class="type-label string">STRING</span> | :material-close: | x radius for rounded corners                                   |
    | ry         | <span class="type-label string">STRING</span> | :material-close: | y radius for rounded corners                                   |
    | attributes | <span class="type-label string">STRING</span> | :material-close: | Direct SVG attributes to apply (e.g., "fill='red' stroke-width='2'"), can generate with `DaxLib.SVG.Attr.*` or manually |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`)   |

    <span class="type-label string">STRING</span> `#!xml <rect>` element

=== "Example"

    ```dax hl_lines="5-34"
    DaxLib.SVG.SVG( 
        500,                // width
        100,                // height
        "0 0 100 20",       // viewbox
        DaxLib.SVG.Element.Rect(
            "50%",          // x
            "0%",           // y
            "40%",          // width
            8,              // height
            blank(),        // rx
            blank(),        // ry
            DaxLib.SVG.Attr.Shapes(
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // fill
                0.3,        // fillOpacity
                BLANK(),    // fillRule
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // stroke
                2,          // strokeWidth
                0.9,        // strokeOpacity
                BLANK()     // opacity
            ),              // attributes
            DaxLib.SVG.Transforms(
                -15,        // translate
                5,          // rotate
                BLANK(),    // scale
                -20,        // skewX
                BLANK()     // skewY
            )               // transforms
        ),                  // contents
        BLANK()             // sortValue
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Element.Rect' =
        (
            x: STRING,
            y: STRING,
            width: STRING,
            height: STRING,
            rx: STRING,
            ry: STRING,
            attributes: STRING,
            transforms: STRING
        ) =>

            "<rect" &
            " x='" & x & "'" &
            " y='" & y & "'" &
            " width='" & width & "'" &
            " height='" & height & "'" &
            IF( NOT ISBLANK( rx ), " rx='" & rx & "'" ) &
            IF( NOT ISBLANK( ry ), " ry='" & ry & "'" ) &
            IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
            IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
            "/>"
    ```