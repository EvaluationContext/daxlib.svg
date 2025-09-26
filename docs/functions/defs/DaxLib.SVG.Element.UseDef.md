---
title: Element.UseDef
nav_order: 3
parent: Defs
---

# DaxLib.SVG.Element.UseDef

Applies a previously defined `DaxLib.SVG.Def.*` shape element (rect, circle, line etc.), via `<use>`{:.xml}, with the ability to overwrite properties

## Syntax

```dax
DaxLib.SVG.Element.UseDef(defId, x, y, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| defId     | STRING | Yes      | The identifier of the defined element to use                       |
| x         | STRING | No       | X position where the element should be placed                      |
| y         | STRING | No       | Y position where the element should be placed                      |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<use>`{:.xml} element

## Example

```dax
DaxLib.SVG.Element.UseDef(
    "myCircle",
    100,
    100,
    "fill:green;",
    BLANK(),
    BLANK()
)
// Returns: <use href='#myCircle' x='100' y='100' style='fill:green;'/>
```

## Definition

```dax
function 'DaxLib.SVG.Element.UseDef' =
    (
        defId: STRING,
        x: STRING,
        y: STRING,
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>
        VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )
        RETURN
            "<use" &
            " href='#" & defId & "'" &
            IF( NOT ISBLANK( x ), " x='" & x & "'" ) &
            IF( NOT ISBLANK( y ), " y='" & y & "'" ) &
            _OCE &
            "/>"
```