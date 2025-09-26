---
title: Scale.ArcPath
nav_order: 7.2
parent: Scales
---

# DaxLib.SVG.Scale.ArcPath

Generates `<path>`{:.xml} data (d) for arc segments, useful for donut and gauge charts

## Syntax

```dax
DaxLib.SVG.Scale.ArcPath(cx, cy, radius, startAngle, endAngle, innerRadius)
```

## Parameters

| Name        | Type        | Description                                                       |
|:---:|:---:|:---:|
| cx          | SCALAR VAL  | Center X position in pixels                                       |
| cy          | SCALAR VAL  | Center Y position in pixels                                       |
| radius      | SCALAR VAL  | Outer radius in pixels                                            |
| startAngle  | SCALAR VAL  | Starting angle in degrees (0 = right, 90 = bottom)                |
| endAngle    | SCALAR VAL  | Ending angle in degrees                                           |
| innerRadius | SCALAR VAL  | Inner radius for donut effect (0 for pie slice)                   |

## Returns

(*STRING*) `<path>`{:.xml} data (d)

## Example

```dax
DaxLib.SVG.Scale.ArcPath(100, 100, 80, 0, 120, 60)
// Returns SVG path data for a donut arc segment
```

## Definition

```dax
function 'DaxLib.SVG.Scale.ArcPath' =
    (
        cx : SCALAR VAL,
        cy : SCALAR VAL,
        radius : SCALAR VAL,
        startAngle : SCALAR VAL,
        endAngle : SCALAR VAL,
        innerRadius : SCALAR VAL
    ) =>

        VAR _StartRad = startAngle * PI() / 180
        VAR _EndRad = endAngle * PI() / 180
        VAR _LargeArc = IF( endAngle - startAngle > 180, 1, 0 )
        VAR _X1 = cx + radius * COS (_StartRad )
        VAR _Y1 = cy + radius * SIN (_StartRad )
        VAR _X2 = cx + radius * COS (_EndRad )
        VAR _Y2 = cy + radius * SIN (_EndRad )
        VAR _InnerX1 = cx + innerRadius * COS( _StartRad )
        VAR _InnerY1 = cy + innerRadius * SIN( _StartRad )
        VAR _InnerX2 = cx + innerRadius * COS( _EndRad )
        VAR _InnerY2 = cy + innerRadius * SIN( _EndRad )

        RETURN

            IF(
                innerRadius > 0,
                "M " & _InnerX1 & " " & _InnerY1 &
                " L " & _X1 & " " & _Y1 &
                " A " & radius & " " & radius &
                " 0 " & _LargeArc & " 1 " &
                _X2 & " " & _Y2 &
                " L " & _InnerX2 & " " & _InnerY2 &
                " A " & innerRadius & " " & innerRadius &
                " 0 " & _LargeArc & " 0 " &
                _InnerX1 & " " & _InnerY1 & " Z",
                "M " & cx & " " & cy &
                " L " & _X1 & " " & _Y1 &
                " A " & radius & " " & radius &
                " 0 " & _LargeArc & " 1 " &
                _X2 & " " & _Y2 & " Z"
            )
```
