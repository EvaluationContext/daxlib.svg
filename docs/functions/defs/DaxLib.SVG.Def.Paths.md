---
title: Def.Paths
nav_order: 3
parent: Defs
---

# DaxLib.SVG.Def.Paths

Creates a reusable `<path>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.Paths(defId, d, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| defId     | STRING | Yes      | The unique identifier for the path                                 |
| d         | STRING | Yes      | The path data string (e.g., "M10 10 L90 90")                       |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               | 
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<path>`{:.xml} definition

## Example

```dax
DaxLib.SVG.Def.Paths(
    "myPath",
    "M10 10 L90 90",
    "stroke:black;fill:none;",
    BLANK(),
    BLANK()
)
// Returns: <path id='myPath' d='M10 10 L90 90' style='stroke:black;fill:none;'/>
```

## Definition

```dax
function 'DaxLib.SVG.Def.Paths' =
    (
        defId: STRING,
        d: STRING,
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>
        VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

        RETURN

            "<path id='" & defId & "'" &
            " d='" & d & "'" &
            _OCE &
            "/>"
```