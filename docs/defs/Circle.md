---
comments: true
---

# Def.Circle

Generates a reusable `#!xml <circle>` definition

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.Circle( defId, cx, cy, r, attributes, transforms )
    ```

    | Name       | Type   | Required | Description                                                                |
    |:---:|:---:|:---:|---|
    | defId      | <span class="type-label string">STRING</span> | :material-check: | The unique identifier for the circle                                      |
    | cx         | <span class="type-label string">STRING</span> | :material-check: | X center coordinate                                                       |
    | cy         | <span class="type-label string">STRING</span> | :material-check: | Y center coordinate                                                       |
    | r          | <span class="type-label string">STRING</span> | :material-check: | Radius                                                                    |
    | attributes | <span class="type-label string">STRING</span> | :material-close: | Direct SVG attributes to apply (e.g., "fill='none' stroke='blue'"), can generate with `DaxLib.SVG.Attr.*` or manually |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`)    |

    <span class="type-label string">**STRING**</span> `#!xml <circle>` definition

=== "Example"

    ```dax
    DaxLib.SVG.Def.Circle(
        "myCircle", 
        "50", 
        "50", 
        "40", 
        DaxLib.SVG.Attr.Shapes(
            "red",      // fill
            BLANK(),    // fillOpacity
            BLANK(),    // fillRule
            "blue",     // stroke
            2,          // strokeWidth
            BLANK(),    // strokeOpacity
            BLANK()     // opacity
        ), 
        BLANK()
    )
    // Returns: <circle id='myCircle' cx='50' cy='50' r='40' fill='red' stroke='blue' stroke-width='2' />
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.Circle' = 
        (
            defId: STRING,
            cx: STRING,
            cy: STRING,  
            r: STRING,
            attributes: STRING,
            transforms: STRING
        ) =>

            "<circle id='" & defId & "'" &
            " cx='" & cx & "'" &
            " cy='" & cy & "'" &
            " r='" & r & "'" &
            IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
            IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) &
            "/>"
    ```