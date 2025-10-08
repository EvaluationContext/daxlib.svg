---
title: Element.Group
nav_order: 1
parent: Elements
---

# DaxLib.SVG.Element.Group

Generates a `<g>`{:.xml} element. Transformations applied to the `<g>`{:.xml} element are performed on its child elements, and its attributes are inherited by its children. It can also group multiple elements to be referenced later with the `<use>`{:.xml} element.

## Syntax

```dax
DaxLib.SVG.Element.Group(
    contents, 
    transform, 
    opacity
)
```

| Name      | Type       | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| contents  | SCALAR VAL | Yes      | Content to group (recommend including all content in a single variable) |
| transform | SCALAR VAL | No       | Transform (e.g., "translate(50,50) rotate(45)")                    |
| opacity   | SCALAR VAL | No       | Opacity for entire group (0-1, optional)                           |

## Returns

**STRING** `<g>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.Group(
	"<circle ... />", 
	"translate(10,10)", 
	0.8
	)
// Returns: <g transform='translate(10,10)' opacity='0.8'><circle ... /></g>
```

## Definition

```dax
function 'DaxLib.SVG.Element.Group' =
    (
        contents : SCALAR VAL,
        transform : SCALAR VAL,
        opacity : SCALAR VAL
    ) =>

        "<g" &
        " transform='" & transform & "'" &
        " opacity='" & opacity & "'" &
        ">" & contents & "</g>"
```