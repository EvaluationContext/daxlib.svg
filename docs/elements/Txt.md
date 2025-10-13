---
comments: true
---

# Element.Txt

Generates a `#!xml <text>` SVG element

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><text x='10' y='10' dx='0' dy='0' font-family='Arial' font-size='12'  >DaxLib</text></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.Txt( x, y, txt, dx, dy, attributes, transforms )
    ```

    | Name       | Type   | Required | Description                                                         |
    |:---:|:---:|:---:|---|
    | x          | <span class="type-label string">STRING</span> | :material-check: | The x position of the text                                         |
    | y          | <span class="type-label string">STRING</span> | :material-check: | The y position of the text                                         |
    | txt        | <span class="type-label string">STRING</span> | :material-check: | The text content                                                   |
    | dx         | <span class="type-label string">STRING</span> | :material-close: | x offset from position                                   |
    | dy         | <span class="type-label string">STRING</span> | :material-close: | y offset from position                                   |
    | attributes | <span class="type-label string">STRING</span> | :material-close: | Direct SVG attributes to apply (e.g., "text-anchor='middle' dominant-baseline='middle'"), can generate with `DaxLib.SVG.Attr.*` or manually |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Additional transforms (e.g. "scale(1.2) translate(10,10)") (can be generated with `DaxLib.SVG.Transforms`) |

    <span class="type-label string">STRING</span> `#!xml <text>` element

=== "Example"

    ```dax hl_lines="5-23"
    DaxLib.SVG.SVG( 
        500,                // width
        100,                // height
        "0 0 100 20",       // viewbox
        DaxLib.SVG.Element.Txt(
            10,             // x
            10, 	        // y
            "DaxLib",       // txt
            0,              // dx
            0,              // dy
            DaxLib.SVG.Attr.Txt(
                "Arial",    // fontFamily
                12,         // fontSize
                BLANK(),    // fontWeight
                BLANK(),    // fontStyle
                BLANK(),    // textAnchor
                BLANK(),    // baseline
                BLANK(),    // textDecoration
                BLANK(),    // letterSpacing
                BLANK()     // wordSpacing
            ),              // attributes
            BLANK()         // transforms
        ),                  // contents
        BLANK()             // sortValue
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Element.Txt' =
        (
            x: STRING,
            y: STRING,
            txt: STRING,
            dx: STRING,
            dy: STRING,
            attributes: STRING,
            transforms: STRING
        ) =>

            "<text" &
            " x='" & x & "'" &
            " y='" & y & "'" &
            IF(NOT ISBLANK( dx ), " dx='" & dx & "'" ) & 
            IF(NOT ISBLANK( dy ), " dy='" & dy & "'" ) &
            IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
            IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) &
            ">" & txt & 
            "</text>"
    ```