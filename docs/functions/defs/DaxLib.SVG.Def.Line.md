---
title: Def.Line
nav_order: 5.4
parent: Defs
---

# DaxLib.SVG.Def.Line

Creates a reusable `<line>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.Line(defId, x1, y1, x2, y2, style, class, transform)
```

## Parameters
| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| defId     | STRING | Yes      | The unique identifier for the line                                 |
| x1        | STRING | Yes      | X position of the start point                                      |
| y1        | STRING | Yes      | Y position of the start point                                      |
| x2        | STRING | Yes      | X position of the end point                                        |
| y2        | STRING | Yes      | Y position of the end point                                        |
| style     | STRING | No       | The style to apply (e.g., "stroke:black;stroke-width:2;")          |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<line>`{:.xml} definition

## Example

```dax
DaxLib.SVG.Def.Line(
	"myLine",
	0,
	0,
	100,
	100,
	"stroke:black;stroke-width:2;",
	BLANK(),
	BLANK()
)
// Returns: <line id='myLine' x1='0' y1='0' x2='100' y2='100' style='stroke:black;stroke-width:2;'/>
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
		style: STRING,
		class: STRING,
		transform: STRING
	) =>

		VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )
		RETURN
			"<line id='" & defId & "'" &
			" x1='" & x1 & "'" &
			" y1='" & y1 & "'" &
			" x2='" & x2 & "'" &
			" y2='" & y2 & "'" &
			_OCE &
			"/>"
```