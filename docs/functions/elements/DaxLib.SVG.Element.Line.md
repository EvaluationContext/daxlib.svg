---
title: Element.Line
nav_order: 4
parent: Elements
---

# DaxLib.SVG.Element.Line

Generates a `<line>`{:.xml} element

## Syntax
```dax
DaxLib.SVG.Element.Line( x1, y1, x2, y2, attributes, transforms )
```

| Name       | Type   | Required | Description                                                               |
|:---:|:---:|:---:|---|
| x1         | <span class="type-label string">STRING</span> | Yes      | Starting X position (left edge is 0)                                    |
| y1         | <span class="type-label string">STRING</span> | Yes      | Starting Y position (top edge is 0)                                     |
| x2         | <span class="type-label string">STRING</span> | Yes      | Ending X position (left edge is 0)                                      |
| y2         | <span class="type-label string">STRING</span> | Yes      | Ending Y position (top edge is 0)                                       |
| attributes | <span class="type-label string">STRING</span> | No       | Direct SVG attributes to apply (e.g., "stroke-dasharray='5,5' marker-end='url(#arrow)'"), can generate with DaxLib.SVG.Attr.* or manually |
| transforms | <span class="type-label string">STRING</span> | No       | Transformation to apply (can be generated with DaxLib.SVG.Transforms)   |

## Returns

<span class="type-label string">STRING</span> `<line>`{:.xml} element

## Example

```dax
DaxLib.SVG.SVG(
    500,                // width
    100,                // height
    "0 0 100 20",       // viewbox
    DaxLib.SVG.Element.Line(
        1,              // x1
        5,              // y1
        80,             // x2
        5,              // y2
        DaxLib.SVG.Attr.Shapes(
            BLANK(),    // fill
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

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><line x1='1' y1='5' x2='80' y2='5' stroke='#EC008C' stroke-width='2'  /></svg>

## Definition

```dax
function 'DaxLib.SVG.Element.Line' =
    (
        x1: STRING,
        y1: STRING,
        x2: STRING,
        y2: STRING,
        attributes: STRING,
        transforms: STRING
    ) =>  
        
        "<line" &
        " x1='" & x1 & "'" &
        " y1='" & y1 & "'" &
        " x2='" & x2 & "'" &
        " y2='" & y2 & "'" &
        IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
        IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
        "/>"
```