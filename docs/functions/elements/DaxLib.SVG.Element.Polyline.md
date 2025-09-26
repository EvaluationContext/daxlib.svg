---
title: Element.Polyline
nav_order: 3
parent: Elements
---

# DaxLib.SVG.Element.Polyline

Creates a `<polyline>`{:.xml} (connected points) element

## Syntax
```dax
DaxLib.SVG.Element.Polyline(
	points: STRING,
	style: STRING,
	class: STRING,
	transform: STRING
)
```

## Parameters

| Name      | Type   | Required | Description                                                                 |
|:---:|:---:|:---:|:---:|
| points    | STRING | Yes 		| Space-separated x,y coordinate pairs (e.g., "0,10 20,30 40,15")             |
| style     | STRING | No  		| Style to apply, can use DaxLib.SVG.Style.* or manual CSS          		  |
| class     | STRING | No  		| CSS class to apply                                                		  |
| transform | STRING | No  		| Transformation to apply                                           		  |

## Returns

(*STRING*) `<polyline>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Polyline(
	"0,10 20,30 40,15",
	"fill:none;stroke:blue;stroke-width:2",
	"my-polyline",
	"translate(5,5)"
)
```

## Definition

```dax
function 'DaxLib.SVG.Element.Polyline' =
	(
		points: STRING,
		style: STRING,
		class: STRING,
		transform: STRING
	) =>

		VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

		RETURN
		
			"<polyline" &
			" points='" & points & "'" &
			_OCE &
			"/>"
```