---
comments: true
---

# Element.Defs

Generates a `#!xml <defs>` element from one or more `DaxLib.SVG.Def.*` elements

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.Defs( defs )
    ```

    | Name | Type   | Required | Description                                                    |
    |:---:|:---:|:---:|---|
    | defs | <span class="type-label string">STRING</span> | :material-check: | Concatenated list of def elements to include in a defs block   |

    <span class="type-label string">**STRING**</span> `#!xml <defs>` element

=== "Example"

    ```dax
    DaxLib.SVG.Element.Defs(
        DaxLib.SVG.Def.Circle(...) &
        DaxLib.SVG.Def.Rect(...)
    )
    // Returns: <defs>...</defs>
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Element.Defs' = 
        (
            defs: STRING
        ) =>

            "<defs>" &
            defs &
            "</defs>"
    ```