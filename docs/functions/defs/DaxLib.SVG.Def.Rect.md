---
title: Def.Rect
nav_order: 3
parent: Defs
---

# DaxLib.SVG.Def.Rect

Creates a reusable `<rect>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.Rect(defId, width, height, rx, ry, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|-----------|--------|----------|--------------------------------------------------------------------|
| defId     | STRING | Yes      | The unique identifier for the rectangle                            |
| width     | STRING | Yes      | The width of the rectangle (pixels or percentage)                  |
| height    | STRING | Yes      | The height of the rectangle (pixels or percentage)                 |
| rx        | STRING | No       | X radius for rounded corners                                       |
| ry        | STRING | No       | Y radius for rounded corners                                       |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<rect>`{:.xml}  definition

## Example

```dax
DaxLib.SVG.Def.Rect(
    "myRect",
    100,
    50,
    10,
    10,
    "fill:blue;stroke:black;",
    BLANK(),
    BLANK()
)
// Returns: <rect id='myRect' width='100' height='50' rx='10' ry='10' style='fill:blue;stroke:black;'/>
```

## Definition

```dax
function 'DaxLib.SVG.Def.Rect' =
    (
        defId: STRING,
        width: STRING,
        height: STRING,
        rx: STRING,
        ry: STRING,
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>
        VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )
        RETURN
            "<rect id='" & defId & "'" &
            " width='" & width & "'" &
            " height='" & height & "'" &
            IF(NOT ISBLANK(rx), " rx='" & rx & "'" ) &
            IF(NOT ISBLANK(ry), " ry='" & ry & "'" ) &
            _OCE &
            "/>"
```