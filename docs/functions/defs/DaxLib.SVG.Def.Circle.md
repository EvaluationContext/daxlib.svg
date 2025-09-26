---
title: Def.Circle
nav_order: 5.1
parent: Defs
---

# DaxLib.SVG.Def.Circle

Creates a reusable `<circle>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.Circle(defId, cx, cy, r, style, class, transform)
```

## Parameters

| Name      | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|
| defId     | STRING | Yes      | The unique identifier for the circle                               |
| cx        | STRING | Yes      | X center coordinate                                                |
| cy        | STRING | Yes      | Y center coordinate                                                |
| r         | STRING | Yes      | Radius                                                             |
| style     | STRING | No       | The style to apply (e.g., "fill:black;stroke:blue;")               |
| class     | STRING | No       | CSS class to apply                                                 |
| transform | STRING | No       | Transformation to apply                                            |

## Returns

(*STRING*) `<circle>`{:.xml} definition

## Example

```dax
DaxLib.SVG.Def.Circle(
	"myCircle", 
	50, 
	50, 
	40, 
	"fill:red;", 
	BLANK(), 
	BLANK()
	)
// Returns: <circle id='myCircle' cx='50' cy='50' r='40' style='fill:red;' />
```

## Definition

```dax
function 'DaxLib.SVG.Def.Circle' = 
    (
        defId: STRING,
        cx: STRING,
        cy: STRING,  
        r: STRING,
        style: STRING,
        class: STRING,
        transform: STRING
    ) =>

        VAR _OCE = DaxLib.SVG.Util.OptionalCommentElements( style, class, transform )

        RETURN

            "<circle id='" & defId & "'" &
            " cx='" & cx & "'" &
            " cy='" & cy & "'" &
            " r='" & r & "'" &
            _OCE &
            "/>"
```