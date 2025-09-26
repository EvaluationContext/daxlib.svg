---
title: Def.LinearGradient
nav_order: 5.5
parent: Defs
---

# DaxLib.SVG.Def.LinearGradient

Creates a reusable `<linearGradient>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.LinearGradient(defId, stops, x1, y1, x2, y2)
```

## Parameters

| Name   | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|:---:|:---:|
| defId  | STRING | Yes      | The unique identifier for the gradient                             |
| stops  | STRING | Yes      | Concatenated list of one or more DaxLib.SVG.Def.GradientStop elements |
| x1     | STRING | No       | Start X position                                                   |
| y1     | STRING | No       | Start Y position                                                   |
| x2     | STRING | No       | End X position                                                     |
| y2     | STRING | No       | End Y position                                                     |

## Returns

(*STRING*) `<linearGradient>`{:.xml} definition

## Example

```dax
DaxLib.SVG.Def.LinearGradient(
    "myGradient",
    DaxLib.SVG.Def.GradientStop(
		"0%", 
		"red", 
		1
	) & 
	DaxLib.SVG.Def.GradientStop(
		"100%", 
		"blue", 
		1
	),
    "0%", 
	"0%", 
	"100%", 
	"0%"
)
// Returns: <linearGradient id='myGradient' x1='0%' y1='0%' x2='100%' y2='0%'>...</linearGradient>
```

## Definition

```dax
function 'DaxLib.SVG.Def.LinearGradient' =
    (
        defId: STRING,
        stops: STRING,
        x1: STRING,
        y1: STRING,
        x2: STRING,
        y2: STRING
    ) =>

        "<linearGradient" &
        " id='" & defId & "'" &
        IF( NOT ISBLANK( x1 ), " x1='" & x1 & "'" ) &
        IF( NOT ISBLANK( y1 ), " y1='" & y1 & "'" ) &
        IF( NOT ISBLANK( x2 ), " x2='" & x2 & "'" ) &
        IF( NOT ISBLANK( y2 ), " y2='" & y2 & "'" ) &
        ">" &
        stops &
        "</linearGradient>"
```