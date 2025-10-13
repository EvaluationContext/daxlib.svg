---
comments: true
---
# Element.Group

Generates a `#!xml <g>` element. Transformations applied to the `#!xml <g>` element are performed on its child elements, and its attributes are inherited by its children. It can also group multiple elements to be referenced later with the `#!xml <use>` element.

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.Group( contents, transform, opacity )
    ```

    | Name      | Type       | Required | Description                                                        |
    |:---:|:---:|:---:|---|
    | contents  | <span class="type-label string">STRING</span> | :material-check: | Content to group |
    | transform | <span class="type-label string">STRING</span> | :material-close: | Transform (e.g., "translate(50,50) rotate(45)")                    |
    | opacity   | <span class="type-label string">STRING</span> | :material-close: | Opacity for entire group (0-1)                           |

    <span class="type-label string">STRING</span> `#!xml <g>` element

=== "Example"

    ```dax
    DaxLib.SVG.Element.Group(
        "<circle ... />", 
        "translate(10,10)", 
        0.8
        )
    // Returns: <g transform='translate(10,10)' opacity='0.8'><circle ... /></g>
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Element.Group' =
        (
            contents : SCALAR VAL,
            transform : SCALAR VAL,
            opacity : SCALAR VAL
        ) =>

            "<g" &
            " transform='" & transform & "'" &
            " opacity='" & opacity & "'" &
            ">" & contents & "</g>"
    ```