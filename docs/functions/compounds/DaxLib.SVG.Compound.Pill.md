---
title: Compound.Pill
nav_order: 4.1
parent: Compounds
---

# DaxLib.SVG.Compound.Pill

Creates a pill compound element (rounded rectangle with centered text)

## Syntax

```dax
DaxLib.SVG.Compound.Pill(
    width: STRING,
    height: STRING,
    txt: STRING,
    pillColour: STRING,
    txtColour: STRING
)
```

## Parameters

| Name        | Type   | Required | Description                                         |
|:---:|:---:|:---:|:---:|
| width       | Yes    |STRING    | The width of the SVG canvas                         |
| height      | Yes    |STRING    | The height of the SVG canvas                        |
| txt         | Yes    |STRING    | The text to display                                 |
| pillColour  | Yes    |STRING    | The hex color of the fill (e.g., "#01B8AA80")     |
| txtColour   | Yes    |STRING    | The hex color of the text (e.g., "#FFFFFF")       |

## Returns

(*STRING*) pill compound element (rounded rectangle with centered text)

## Example

```dax
DaxLib.SVG.Compound.Pill(
    "120",
    "40",
    "Hello World",
    "#01B8AA80",
    "#FFFFFF"
)
```

## Definition

```dax
function 'DaxLib.SVG.Compound.Pill' =
    (
		width: STRING,
		height: STRING,
		txt: STRING,
		pillColour: STRING,
		txtColour: STRING
	) =>

	VAR Pill = 
		DaxLib.SVG.Element.Rect(
			1,                 	// X
			1,                 	// Y
			width,      		// Width
			height,     		// Height
			10,               	// RX
			10,               	// RY
			DaxLib.SVG.Style.Common(
				pillColour,
				BLANK(),
				txtColour,
				1,
				BLANK(),
				BLANK()
			),         			// Style
			BLANK(),           	// Class
			BLANK()           	// Transform
		)

	VAR TextElement = 
		DaxLib.SVG.Element.Txt(
			width * 0.50,      	// X
			height * 0.58,     	// Y
			txt,              	// Text content
			0,                	// DX
			0,                	// DY
			DaxLib.SVG.Style.Common(
				txtColour,
				BLANK(),
				BLANK(),
				BLANK(),
				BLANK(),
				BLANK()
			) &
			DaxLib.SVG.Style.Txt(
				"Segoe UI",
				12,
				BLANK(),
				BLANK(),
				"middle",
				"middle",
				BLANK(),
				BLANK(),
				BLANK()
			),         			// Style
			BLANK(),			// Class
			BLANK()				// Transform
		)

	RETURN
	
		Pill & 
		TextElement
```