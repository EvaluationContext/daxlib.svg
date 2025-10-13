---
comments: true
---

# Def.Rect

Generates a reusable `#!xml <rect>` definition

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.Rect( defId, width, height, rx, ry, attributes, transforms )
    ```

    | Name       | Type   | Required | Description                                                                |
    |:---:|:---:|:---:|---|
    | defId      | <span class="type-label string">STRING</span> | :material-check: | The unique identifier for the rectangle                                   |
    | width      | <span class="type-label string">STRING</span> | :material-check: | The width of the rectangle (pixels or percentage)                         |
    | height     | <span class="type-label string">STRING</span> | :material-check: | The height of the rectangle (pixels or percentage)                        |
    | rx         | <span class="type-label string">STRING</span> | :material-close: | X radius for rounded corners                                              |
    | ry         | <span class="type-label string">STRING</span> | :material-close: | Y radius for rounded corners                                              |
    | attributes | <span class="type-label string">STRING</span> | :material-close: | Direct SVG attributes to apply (e.g., "fill='none' stroke='blue'"), can generate with `DaxLib.SVG.Attr.*` or manually |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`)    |

    <span class="type-label string">**STRING**</span> `#!xml <rect>` definition

=== "Example"

    ```dax
    DaxLib.SVG.Def.Rect(
        "myRect",
        "100",
        "50",
        "10",
        "10",
        DaxLib.SVG.Attr.Shapes(
            "blue",     // fill
            BLANK(),    // fillOpacity
            BLANK(),    // fillRule
            "black",    // stroke
            2,          // strokeWidth
            BLANK(),    // strokeOpacity
            BLANK()     // opacity
        ),
        BLANK()
    )
    // Returns: <rect id='myRect' width='100' height='50' rx='10' ry='10' fill='blue' stroke='black' stroke-width='2' />
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.Rect' = 
        (
            defId: STRING,
            width: STRING,
            height: STRING,
            rx: STRING,
            ry: STRING,
            attributes: STRING,
            transforms: STRING
        ) =>

            "<rect id='" & defId & "'" &
            " width='" & width & "'" &
            " height='" & height & "'" &
            IF(NOT ISBLANK( rx ), " rx='" & rx & "'" ) & 
            IF(NOT ISBLANK( ry ), " ry='" & ry & "'" ) &
            IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
            IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) &
            "/>"
    ```