---
comments: true
---

# Element.Paths

Generates a `#!xml <path>` element

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><path d='M10 10 L30 5 C50 0 70 20 90 15 L100 0' fill='none' stroke='#EC008C' stroke-width='2'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.Paths( d, attributes, transforms )
    ```

    | Name       | Type   | Required | Description                                                        |
    |:---:|:---:|:---:|---|
    | d          | <span class="type-label string">STRING</span> | :material-check: | The path data string (e.g., "M10 10 L90 90")                     |
    | attributes | <span class="type-label string">STRING</span> | :material-close: | Direct SVG attributes to apply (e.g., "pathLength='100' fill-rule='evenodd'"), can generate with `DaxLib.SVG.Attr.* `or manually |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`) |

    <span class="type-label string">**STRING**</span> `#!xml <path>` element

=== "Example"

    ```dax hl_lines="5-20"
    DaxLib.SVG.SVG(
        500,                // width
        100,                // height
        "0 0 100 20",       // viewbox
        DaxLib.SVG.Element.Paths(
            "M10 10 L30 5 C50 0 70 20 90 15 L100 0", // d
            DaxLib.SVG.Attr.Shapes(
                "none",     // fill
                BLANK(),    // fillOpacity
                BLANK(),    // fillRule
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // stroke
                2,          // strokeWidth
                BLANK(),    // strokeOpacity
                BLANK()     // opacity
            ),              // attributes
            BLANK()         // transforms
        ),                  // contents
        BLANK()             // sortValue
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Element.Paths' =
        (
            d: STRING,
            attributes: STRING,
            transforms: STRING
        ) =>

            "<path d='" & d & "'" &
            IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
            IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
            "/>"
    ```