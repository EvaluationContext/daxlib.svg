---
title: Element.Circle
nav_order: 2
parent: Elements
---

# DaxLib.SVG.Element.Circle

Generates a `<circle>`{:.xml} element

## Syntax

```dax
DaxLib.SVG.Element.Circle( cx, cy, r, attributes, transforms )
```

| Name       | Type   | Required | Description                                                               |
|:---:|:---:|:---:|---|
| cx         | <span class="type-label string">STRING</span> | Yes      | The x position of the center                                             |
| cy         | <span class="type-label string">STRING</span> | Yes      | The y position of the center                                             |
| r          | <span class="type-label string">STRING</span> | Yes      | The radius                                                               |
| attributes | <span class="type-label string">STRING</span> | No       | Direct SVG attributes to apply (e.g., "fill='red' stroke-width='2'"), can generate with `DaxLib.SVG.Attr.*` or manually |
| transforms | <span class="type-label string">STRING</span> | No       | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`)   |

## Returns

<span class="type-label string">STRING</span> `<circle>`{:.xml} element

## Example

```dax
DaxLib.SVG.SVG(
    500,                // width
    100,                // height
    "0 0 100 20",       // viewbox
    DaxLib.SVG.Element.Circle(
        50,             // cx
        10,             // cy
        "10%",          // r
        DaxLib.SVG.Attr.Shapes(
            DaxLib.SVG.Colour.Theme(
            "Power BI",
            25
        ),              // fill
        0.5,            // fillOpacity
        BLANK(),        // fillRule   
        DaxLib.SVG.Colour.Theme(
            "Power BI",
            25
        ),              // stroke
        1,              // strokeWidth
        BLANK(),        // strokeOpacity
        BLANK()         // opacity
        ),              // attributes
        BLANK()         // transforms
    ),                  // contents
    BLANK()             // sortValue
)
```

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><circle cx='50' cy='10' r='10%' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1'  /></svg>

## Definition

```dax
function 'DaxLib.SVG.Element.Circle' = 
    (
        cx: STRING,
        cy: STRING,
        r: STRING,
        attributes: STRING,
        transforms: STRING
    ) =>

        "<circle" &
        " cx='" & cx & "'" &
        " cy='" & cy & "'" &
        " r='" & r & "'" &
        IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
        IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
        "/>"
```