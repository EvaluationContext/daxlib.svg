---
comments: true
---

# Def.Line

Generates a reusable `#!xml <line>` definition

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.Line( defId, x1, y1, x2, y2, attributes, transforms )
    ```

    | Name       | Type   | Required | Description                                                                |
    |:---:|:---:|:---:|---|
    | defId      | <span class="type-label string">STRING</span> | :material-check: | The unique identifier for the line                                        |
    | x1         | <span class="type-label string">STRING</span> | :material-check: | The x position of the start point                                         |
    | y1         | <span class="type-label string">STRING</span> | :material-check: | The y position of the start point                                         |
    | x2         | <span class="type-label string">STRING</span> | :material-check: | The x position of the end point                                           |
    | y2         | <span class="type-label string">STRING</span> | :material-check: | The y position of the end point                                           |
    | attributes | <span class="type-label string">STRING</span> | :material-close: | Direct SVG attributes to apply (e.g., "stroke-width='2' stroke='blue'"), can generate with `DaxLib.SVG.Attr.*` or manually |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`)    |

    <span class="type-label string">**STRING**</span> `#!xml <line>` definition

=== "Example"

    ```dax
    DaxLib.SVG.Def.Line(
        "myLine",
        "0",
        "0",
        "100",
        "100",
        DaxLib.SVG.Attr.Stroke(
            "black",    // stroke
            2,          // strokeWidth
            BLANK(),    // strokeOpacity
            BLANK(),    // strokeDasharray
            BLANK(),    // strokeDashoffset
            BLANK(),    // strokeLinecap
            BLANK(),    // strokeLinejoin
            BLANK(),    // strokeMiterlimit
            BLANK(),    // markerStart
            BLANK(),    // markerMid
            BLANK()     // markerEnd
        ),
        BLANK()
    )
    // Returns: <line id='myLine' x1='0' y1='0' x2='100' y2='100' stroke='black' stroke-width='2' />
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.Line' = 
        (
            defId: STRING,
            x1: STRING,
            y1: STRING,
            x2: STRING,
            y2: STRING,
            attributes: STRING,
            transforms: STRING
        ) =>

            "<line id='" & defId & "'" &
            " x1='" & x1 & "'" &
            " y1='" & y1 & "'" &
            " x2='" & x2 & "'" &
            " y2='" & y2 & "'" &
            IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
            IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) &
            "/>"
    ```