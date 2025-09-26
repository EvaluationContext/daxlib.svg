---
title: Element.Paths
nav_order: 3
parent: Elements
---

# DaxLib.SVG.Element.Paths

Creates a `<path>{`:.xml} element

## Syntax

```dax
DaxLib.SVG.Element.Paths(d, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| d         | STRING | Yes      | The path data string (e.g., "M10 10 L90 90")                       |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<path>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Paths(
	"M10 10 L90 90", 
	"stroke:black;", 
	BLANK(), 
	BLANK()
)
// Returns: <path d='M10 10 L90 90' style='stroke:black;' />
```

## Definition

```dax
function 'DaxLib.SVG.Element.Paths' =
    (
        d: STRING,
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>

        VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

        RETURN

            "<path d='" & d & "'" &
            _OCE & 
            " />"
```