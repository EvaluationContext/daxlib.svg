---
title: Element.Txt
nav_order: 3
parent: Elements
---

# DaxLib.SVG.Element.Txt

Creates a `<text>`{:.xml} SVG element

## Syntax

```dax
DaxLib.SVG.Element.Txt(
	x: STRING,
	y: STRING,
	txt: STRING,
	dx: STRING,
	dy: STRING,
	style: STRING,
	class: STRING,
	transform: STRING
)
```

## Parameters

| Name      | Type   | Required | Description                                                                 |
|:---:|:---:|:---:|:---:|
| x         | STRING | Yes 		| The x position of the text                                                  |
| y         | STRING | Yes 		| The y position of the text                                                  |
| txt       | STRING | Yes 		| The text content                                                            |
| dx        | STRING | No  		| x offset from position                                            		  |
| dy        | STRING | No  		| y offset from position                                            		  |
| style     | STRING | No  		| Style to apply, can use DaxLib.SVG.Style.* or manual CSS          		  |
| class     | STRING | No  		| CSS class to apply                                                		  |
| transform | STRING | No  		| Additional transforms (e.g. "scale(1.2) translate(10,10)")        		  |

## Returns

(*STRING*) `<text>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Txt(
	50,
	100,
	"Hello SVG!",
	5,
	10,
	"fill:black;stroke:none;",
	"my-text",
	"scale(1.2) translate(10,10)"
)
```

## Definition

```dax
function 'DaxLib.SVG.Element.Txt' =
	(
		x: STRING,
		y: STRING,
		txt: STRING,
		dx: STRING,
		dy: STRING,
		style: STRING,
		class: STRING,
		transform: STRING
	) =>

		VAR _DX = IF(NOT ISBLANK( dx ), " dx='" & dx & "'" )
		VAR _DY = IF(NOT ISBLANK( dy ), " dy='" & dy & "'" )
		VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

		RETURN
		
			"<text" &
			" x='" & x & "'" &
			" y='" & y & "'" &
			_DX &
			_DY &
			_OCE &
			">" & txt &
			"</text>"
```