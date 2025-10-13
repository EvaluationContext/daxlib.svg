---
comments: true
---

# Transforms

Creates an SVG transform attribute value for applying multiple transformations to an element

=== "Syntax"

    ```dax
    DaxLib.SVG.Transforms(translate, rotate, scale, skewX, skewY)
    ```

    | Parameter | Type      | Required | Description | 
    |:---:|:---:|:---:|---|
    | translate | <span class="type-label string">STRING</span>    | :material-close: | Translation coordinates in the format "x,y" | 
    | rotate    | <span class="type-label string">STRING</span>    | :material-close: | Rotation angle in degrees, or "angle x y" for rotation around a point |
    | scale     | <span class="type-label string">STRING</span>    | :material-close: | Scale factor, or "x,y" for different scaling in each dimension | 
    | skewX     | <span class="type-label string">STRING</span>    | :material-close: | Horizontal skew angle in degrees | 
    | skewY     | <span class="type-label string">STRING</span>    | :material-close: | Vertical skew angle in degrees |

    <span class="type-label string">STRING</span> A transform attribute value that can be used with the transform attribute of SVG elements.

=== "Example"

    ```dax
    DaxLib.SVG.Transforms("10,20", "45", "1.5", "", "")
    // Returns: "translate(10,20) rotate(45) scale(1.5)"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Transforms' = 
        (
            translate: STRING,
            rotate: STRING,
            scale: STRING,
            skewX: STRING,
            skewY: STRING
        ) =>

            IF(NOT ISBLANK(translate),  "translate(" & translate & ") ") &
            IF(NOT ISBLANK(rotate),     "rotate(" & rotate & ") ") &
            IF(NOT ISBLANK(scale),      "scale(" & scale & ") ") &
            IF(NOT ISBLANK(skewX),      "skewX(" & skewX & ") ") &
            IF(NOT ISBLANK(skewY),      "skewY(" & skewY & ") ") 
    ```