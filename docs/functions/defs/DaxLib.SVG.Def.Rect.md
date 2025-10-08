---
title: Def.Rect
nav_order: 3
parent: Defs
---

# DaxLib.SVG.Def.Rect

Creates a reusable `<rect>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.Rect(
    defId, 
    width, 
    height, 
    rx, 
    ry, 
    attributes, 
    transforms
)
```

| Name       | Type   | Required | Description                                                                |
|:----------:|:------:|:--------:|:--------------------------------------------------------------------------|
| defId      | STRING | Yes      | The unique identifier for the rectangle                                   |
| width      | STRING | Yes      | The width of the rectangle (pixels or percentage)                         |
| height     | STRING | Yes      | The height of the rectangle (pixels or percentage)                        |
| rx         | STRING | No       | X radius for rounded corners                                              |
| ry         | STRING | No       | Y radius for rounded corners                                              |
| attributes | STRING | No       | Direct SVG attributes to apply (e.g., "fill='none' stroke='blue'"), can generate with DaxLib.SVG.Attr.* or manually |
| transforms | STRING | No       | Transformation to apply (can be generated with DaxLib.SVG.Transforms)    |

## Returns

**STRING** `<rect>`{:.xml} definition

## Example

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

## Definition

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