---
title: Element.Rect
nav_order: 3.2
parent: Elements
---

# DaxLib.SVG.Element.Rect

Creates a `<rect>`{:.xml} element

## Syntax

```dax
DaxLib.SVG.Element.Rect(
	x: STRING,
	y: STRING,
	width: STRING,
	height: STRING,
	style: STRING,
	class: STRING,
	transform: STRING
)
```

## Parameters

| Name      | Type   | Required | Description                                                                 |
|:---:|:---:|:---:|:---:|
| x         | STRING | Yes      | X position (left edge is 0)                                                 |
| y         | STRING | Yes      | Y position (top edge is 0)                                                  |
| width     | STRING | Yes      | Width of the rectangle                                                      |
| height    | STRING | Yes      | Height of the rectangle                                                     |
| style     | STRING | No       | Style to apply, can use DaxLib.SVG.Style.* or manual CSS          		  |
| class     | STRING | No       | CSS class to apply                                                		  |
| transform | STRING | No       | Transformation to apply                                           		  |

## Returns

(*STRING*) `<rect>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Rect(
	10,
	20,
	100,
	50,
	"fill:yellow;stroke:black;stroke-width:2",
	"my-rect",
	"rotate(5)"
)
```

## Definition

```dax
function 'DaxLib.SVG.Element.Rect' =
	(
		x: STRING,
		y: STRING,
		width: STRING,
		height: STRING,
		style: STRING,
		class: STRING,
		transform: STRING
	) =>

		VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

		RETURN
			"<rect" &
			" x='" & x & "'" &
			" y='" & y & "'" &
			" width='" & width & "'" &
			" height='" & height & "'" &
			_OCE &
			"/>"
```