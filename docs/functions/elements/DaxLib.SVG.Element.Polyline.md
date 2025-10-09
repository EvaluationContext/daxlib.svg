---
title: Element.Polyline
nav_order: 7
parent: Elements
---

# DaxLib.SVG.Element.Polyline

Generates a `<polyline>`{:.xml} (connected points) element

## Syntax
```dax
DaxLib.SVG.Element.Polyline( points, attributes, transforms )
```

| Name       | Type   | Required | Description                                                                                         |
|:---:|:---:|:---:|---|
| points     | <span class="type-label string">STRING</span> | Yes      | Space-separated x,y coordinate pairs (e.g., "0,10 20,30 40,15")                                   |
| attributes | <span class="type-label string">STRING</span> | No       | Direct SVG attributes to apply (e.g., "marker-start='url(#dot)'"), can generate with `DaxLib.SVG.Attr.*` or manually |
| transforms | <span class="type-label string">STRING</span> | No       | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`)                             |

## Returns

<span class="type-label string">STRING</span> `<polyline>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Polyline(
	"0,10 20,30 40,15",
	DaxLib.SVG.Attr.Lines("none", "#0078D4", "2", BLANK(), BLANK(), BLANK(), BLANK()),
	"translate(5,5)"
)
// Returns: <polyline points='0,10 20,30 40,15' fill='none' stroke='#0078D4' stroke-width='2' transform='translate(5,5)' />
```

## Definition

```dax
function 'DaxLib.SVG.Element.Polyline' =
	(
		points: STRING,
		attributes: STRING,
		transforms: STRING
	) =>

		"<polyline" &
		" points='" & points & "'" &
		IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
		IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) & 
		"/>"
```