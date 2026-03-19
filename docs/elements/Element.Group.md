# Element.Group

Generates SVG group element Transformations applied to the <g> element are performed on its child elements, and its attributes are inherited by its children. It can also group multiple elements to be referenced later with the <use> element

=== "Syntax"

    ```dax
    DaxLib.SVG.Element.Group( contents, opacity, transforms )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | contents | <span class="type-label string">STRING</span> | :material-check: | Content to group (recommend including all content in a single _SvgGroup variable defined upstream) |
    | opacity | <span class="type-label string">STRING</span> | :material-close: | Optional: Opacity for entire group (0-1, optional) |
    | transforms | <span class="type-label string">STRING</span> | :material-close: | Optional: Transform (e.g., "translate(50,50) rotate(45)") (can be generated with `DaxLib.SVG.Transforms`) |

    <span class="type-label string">STRING</span> <g> element

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
    			contents : STRING,
    			opacity : STRING,
    			transforms : STRING
    		) =>
    
    			"<g" &
    			IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) &
    			IF( NOT ISBLANK( opacity ), " opacity='" & opacity & "'" ) &
    			">" & contents & "</g>"
    ```