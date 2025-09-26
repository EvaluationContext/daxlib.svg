---
title: Util.OptionalCommentElements
nav_order: 8.1
parent: Utils
---

# DaxLib.SVG.Util.OptionalCommentElements

Generates optional common SVG element attributes for style, class, and transform

## Syntax

```dax
DaxLib.SVG.Util.OptionalCommentElements(style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | The CSS class to apply to the element                              |
| transform | STRING | No       | The transform to apply (e.g., "rotate(45)")                        |

## Returns

(*STRING*) attribute string

## Example

```dax
DaxLib.SVG.Util.OptionalCommentElements("fill:red;", "my-class", "rotate(45)")
// Returns: style='fill:red;' class='my-class' transform='rotate(45)'
```

## Definition

```dax
function 'DaxLib.SVG.Util.OptionalCommentElements' = 
    (
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>

        VAR _Style = 		IF( NOT ISBLANK( style ), IF( SEARCH( "style=", style, 1, 0 ) > 0, " " & style & " ", " style='" & style & "' " ) )
        VAR _Class = 		IF( NOT ISBLANK( class ), IF( SEARCH( "class=", class, 1, 0 ) > 0, " " & class & " ", " class='" & class & "' " ) )
        VAR _Transform = 	IF( NOT ISBLANK( transform ), IF( SEARCH( "transform=", transform, 1, 0 ) > 0, " " & transform & " ", " transform='" & transform & "' " ) )

        RETURN

            _Style &
            _Class &
            _Transform
```