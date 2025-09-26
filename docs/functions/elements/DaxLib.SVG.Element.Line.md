---
title: Element.Line
nav_order: 3.3
parent: Elements
---

# DaxLib.SVG.Element.Line

Generates a `<line>`{:.xml} element

## Syntax
```dax
DaxLib.SVG.Element.Line(x1, y1, x2, y2, style, class, transform)
```

## Parameters
| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| x1        | STRING | Yes      | Starting X position (left edge is 0)                               |
| y1        | STRING | Yes      | Starting Y position (top edge is 0)                                |
| x2        | STRING | Yes      | Ending X position (left edge is 0)                                 |
| y2        | STRING | Yes      | Ending Y position (top edge is 0)                                  |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<line>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Line(
	0, 
	0, 
	100, 
	100, 
	"stroke:black;", 
	BLANK(), 
	BLANK()
)
// Returns: <line x1='0' y1='0' x2='100' y2='100' style='stroke:black;' />
```

## Definition

```dax
function 'DaxLib.SVG.Element.Line' =
    (
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
		
            "<line" &
            " x1='" & x1 & "'" &
            " y1='" & y1 & "'" &
            " x2='" & x2 & "'" &
            " y2='" & y2 & "'" &
            _OCE & 
            " />"
```