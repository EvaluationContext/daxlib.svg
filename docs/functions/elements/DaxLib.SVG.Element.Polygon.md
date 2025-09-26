---
title: Element.Polygon
nav_order: 3.5
parent: Elements
---

# DaxLib.SVG.Element.Polygon

Creates a `<polygon>`{:.xml} (closed shape) element

## Syntax
```dax
DaxLib.SVG.Element.Polygon(points, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                                 |
|:---:|:---:|:---:|:---:|
| points    | STRING | Yes      | Space-separated x,y coordinate pairs (e.g., "0,10 20,30 40,15")             |
| style     | STRING | No       | Style to apply, can use DaxLib.SVG.Style.* or manual CSS          	      |
| class     | STRING | No       | CSS class to apply                                                	      |
| transform | STRING | No       | Transformation to apply                                           	      |

## Returns

(*STRING*) `<polygon>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Polygon(
	"0,10 20,30 40,15",
	"fill:lime;stroke:purple;stroke-width:1",
	"my-polygon",
	"rotate(10)"
)
```

## Definition

```dax
function 'DaxLib.SVG.Element.Polygon' =
	(
		points: STRING,
		style: STRING,
		class: STRING,
		transform: STRING

	) =>

		VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

		RETURN
			"<polygon" &
			" points='" & points & "'" &
			_OCE &
			"/>"
```