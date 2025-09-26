---
title: Element.Ellipse
nav_order: 3.4
parent: Elements
---

# DaxLib.SVG.Element.Ellipse

Generates an `<ellipse>`{:.xml} element

## Syntax

```dax
DaxLib.SVG.Element.Ellipse(cx, cy, rx, ry, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| cx        | STRING | Yes      | The x position of the center                                       |
| cy        | STRING | Yes      | The y position of the center                                       |
| rx        | STRING | Yes      | The x radius                                                       |
| ry        | STRING | Yes      | The y radius                                                       |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<ellipse>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Ellipse(
	50, 
	50, 
	40, 
	20, 
	"fill:blue;", 
	BLANK(), 
	BLANK()
)
// Returns: <ellipse cx='50' cy='50' rx='40' ry='20' style='fill:blue;' />
```

## Definition

```dax
function 'DaxLib.SVG.Element.Ellipse' = 
    (
        cx: STRING,
        cy: STRING,
        rx: STRING,
        ry: STRING,
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>

        VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

        RETURN
		
            "<ellipse" &
            " cx='" & cx & "'" &
            " cy='" & cy & "'" &
            " rx='" & rx & "'" &
            " ry='" & ry & "'" &
            _OCE & 
            " />"
```