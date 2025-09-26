---
title: Def.RadialGradient
nav_order: 3
parent: Defs
---

# DaxLib.SVG.Def.RadialGradient

Creates a reusable `<radialGradient>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.RadialGradient(defId, stops, cx, cy, r, fx, fy, fr)
```

## Parameters

| Name   | Type   | Required | Description                                                        |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| defId  | STRING | Yes      | The unique identifier for the gradient                             |
| stops  | STRING | Yes      | Concatenated list of one or more DaxLib.SVG.Def.GradientStop elements |
| cx     | STRING | No       | Center X position                                                  |
| cy     | STRING | No       | Center Y position                                                  |
| r      | STRING | No       | Radius                                                             |
| fx     | STRING | No       | Focus X position                                                   |
| fy     | STRING | No       | Focus Y position                                                   |
| fr     | STRING | No       | Focus radius                                                       |

## Returns

(*STRING*) `<radialGradient>`{:.xml} definition

## Example

```dax
DaxLib.SVG.Def.RadialGradient(
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
    "50%", 
	"50%", 
	"50%", 
	"50%", 
	"50%", 
	"10%"
)
// Returns: <radialGradient id='myGradient' cx='50%' cy='50%' r='50%' fx='50%' fy='50%' fr='10%'>...</radialGradient>
```

## Definition

```dax
function 'DaxLib.SVG.Def.RadialGradient' =
    (
        defId: STRING,
        stops: STRING,
        cx: STRING,
        cy: STRING,
        r: STRING,
        fx: STRING,
        fy: STRING,
        fr: STRING
    ) =>

        "<radialGradient" &
        " id='" & defId & "'" &
        IF( NOT ISBLANK( cx ), " cx='" & cx & "'" ) &
        IF( NOT ISBLANK( cy ), " cy='" & cy & "'" ) &
        IF( NOT ISBLANK( r ),  " r='" & r & "'" ) &
        IF( NOT ISBLANK( fx ), " fx='" & fx & "'" ) &
        IF( NOT ISBLANK( fy ), " fy='" & fy & "'" ) &
        IF( NOT ISBLANK( fr ), " fr='" & fr & "'" ) &
        ">" &
        stops &
        "</radialGradient>"
```