---
title: Element.Circle
nav_order: 3.1
parent: Elements
---

# DaxLib.SVG.Element.Circle

Generates a `<circle>`{:.xml} element

## Syntax

```dax
DaxLib.SVG.Element.Circle(cx, cy, r, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| cx        | STRING | Yes      | The x position of the center                                       |
| cy        | STRING | Yes      | The y position of the center                                       |
| r         | STRING | Yes      | The radius                                                         |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) SVG `<circle>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Circle(
	50, 
	50, 
	40, 
	"fill:red;", 
	BLANK(), 
	BLANK()
)
// Returns: <circle cx='50' cy='50' r='40' style='fill:red;' />
```

## Definition

```dax
function 'DaxLib.SVG.Element.Circle' = 
    (
        cx: STRING,
        cy: STRING,
        r: STRING,
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>

        VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

        RETURN
            "<circle" &
            " cx='" & cx & "'" &
            " cy='" & cy & "'" &
            " r='" & r & "'" &
            _OCE & 
            " />"
```