---
title: Element.Polygon
nav_order: 6
parent: Elements
---

# DaxLib.SVG.Element.Polygon

Creates a `<polygon>`{:.xml} (closed shape) element

## Syntax
```dax
DaxLib.SVG.Element.Polygon(
    points, 
    attributes, 
    transforms
)
```

| Name       | Type   | Required | Description                                                                                    |
|:----------:|:------:|:--------:|:-----------------------------------------------------------------------------------------------|
| points     | STRING | Yes      | Space-separated x,y coordinate pairs (e.g., "0,10 20,30 40,15")                              |
| attributes | STRING | No       | Direct SVG attributes to apply (e.g., "fill-rule='nonzero'"), can generate with DaxLib.SVG.Attr.* or manually |
| transforms | STRING | No       | Transformation to apply (can be generated with DaxLib.SVG.Transforms)                        |

## Returns

**STRING** `<polygon>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Polygon(
	"0,10 20,30 40,15",
	DaxLib.SVG.Attr.Shapes("#32CD32", "#800080", "1", BLANK(), BLANK(), BLANK(), BLANK()),
	"rotate(10)"
)
// Returns: <polygon points='0,10 20,30 40,15' fill='#32CD32' stroke='#800080' stroke-width='1' transform='rotate(10)' />
```

## Definition

```dax
function 'DaxLib.SVG.Element.Polygon' =
	(
		points: STRING,
		attributes: STRING,
		transforms: STRING
	) =>

		"<polygon" &
		" points='" & points & "'" &
		IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
		IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
		"/>"
```