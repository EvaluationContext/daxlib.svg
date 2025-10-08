---
title: Def.Line
nav_order: 5
parent: Defs
---

# DaxLib.SVG.Def.Line

Creates a reusable `<line>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.Line(
	defId, 
	x1, 
	y1, 
	x2, 
	y2, 
	attributes, 
	transforms
)
```

| Name       | Type   | Required | Description                                                                |
|:----------:|:------:|:--------:|:--------------------------------------------------------------------------|
| defId      | STRING | Yes      | The unique identifier for the line                                        |
| x1         | STRING | Yes      | The x position of the start point                                         |
| y1         | STRING | Yes      | The y position of the start point                                         |
| x2         | STRING | Yes      | The x position of the end point                                           |
| y2         | STRING | Yes      | The y position of the end point                                           |
| attributes | STRING | No       | Direct SVG attributes to apply (e.g., "stroke-width='2' stroke='blue'"), can generate with DaxLib.SVG.Attr.* or manually |
| transforms | STRING | No       | Transformation to apply (can be generated with DaxLib.SVG.Transforms)    |

## Returns

**STRING** `<line>`{:.xml} definition

## Example

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

## Definition

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