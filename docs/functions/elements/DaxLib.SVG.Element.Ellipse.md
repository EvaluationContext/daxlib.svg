---
title: Element.Ellipse
nav_order: 5
parent: Elements
---

# DaxLib.SVG.Element.Ellipse

Generates an `<ellipse>`{:.xml} element

## Syntax

```dax
DaxLib.SVG.Element.Ellipse( cx, cy, rx, ry, attributes, transforms )
```

| Name       | Type   | Required | Description                                                                |
|:---:|:---:|:---:|---|
| cx         | <span class="type-label string">STRING</span> | Yes      | The x position of the center                                               |
| cy         | <span class="type-label string">STRING</span> | Yes      | The y position of the center                                               |
| rx         | <span class="type-label string">STRING</span> | Yes      | The x radius                                                               |
| ry         | <span class="type-label string">STRING</span> | Yes      | The y radius                                                               |
| attributes | <span class="type-label string">STRING</span> | No       | Direct SVG attributes to apply, can generate with DaxLib.SVG.Attr.* or manually |
| transforms | <span class="type-label string">STRING</span> | No       | Transformation to apply (can be generated with DaxLib.SVG.Transforms)     |

## Returns

<span class="type-label string">STRING</span> `<ellipse>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Ellipse(
	"50", 
	"50", 
	"40", 
	"20", 
	DaxLib.SVG.Attr.Shapes("#0078D4", BLANK(), BLANK(), BLANK(), BLANK(), BLANK(), BLANK()), 
	BLANK()
)
// Returns: <ellipse cx='50' cy='50' rx='40' ry='20' fill='#0078D4' />

// Using manual attributes
DaxLib.SVG.Element.Ellipse(
	"50", 
	"50", 
	"40", 
	"20", 
	"fill='blue' stroke='red' stroke-width='2'", 
	"rotate(45)"
)
// Returns: <ellipse cx='50' cy='50' rx='40' ry='20' fill='blue' stroke='red' stroke-width='2' transform='rotate(45)' />
```

## Definition

```dax
function 'DaxLib.SVG.Element.Ellipse' = 
    (
        cx: STRING,
        cy: STRING,
        rx: STRING,
        ry: STRING,
        attributes: STRING,
        transforms: STRING
    ) =>

        "<ellipse" &
        " cx='" & cx & "'" &
        " cy='" & cy & "'" &
        " rx='" & rx & "'" &
        " ry='" & ry & "'" &
        IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
        IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
        "/>"
```