---
title: Def.RadialGradient
nav_order: 9
parent: Defs
---

# DaxLib.SVG.Def.RadialGradient

Generates a reusable `<radialGradient>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.RadialGradient( defId, stops, cx, cy, r, fx, fy, fr )
```

| Name   | Type   | Required | Description                                                        |
|:---:|:---:|:---:|---|
| defId  | <span class="type-label string">STRING</span> | Yes      | The unique identifier for the gradient                             |
| stops  | <span class="type-label string">STRING</span> | Yes      | Concatenated list of one or more `DaxLib.SVG.Def.GradientStop` elements |
| cx     | <span class="type-label string">STRING</span> | No       | Center X position                                                  |
| cy     | <span class="type-label string">STRING</span> | No       | Center Y position                                                  |
| r      | <span class="type-label string">STRING</span> | No       | Radius                                                             |
| fx     | <span class="type-label string">STRING</span> | No       | Focus X position                                                   |
| fy     | <span class="type-label string">STRING</span> | No       | Focus Y position                                                   |
| fr     | <span class="type-label string">STRING</span> | No       | Focus radius                                                       |

## Returns

<span class="type-label string">**STRING**</span> `<radialGradient>`{:.xml} definition

## Example

```dax
DaxLib.SVG.SVG(
    500,                    // width
    100,                    // height
    "0 0 100 20",           // viewbox
    DaxLib.SVG.Element.Defs(
        DaxLib.SVG.Def.RadialGradient(
            "myGradient",   // id
            DaxLib.SVG.Def.GradientStop( 
                "10%",      // offset
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),          // colour
                BLANK()     // opacity
            ) &
            DaxLib.SVG.Def.GradientStop( 
                "80%",      // offset
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    26
                ),          // colour
                0.5         // opacity
            ) &
            DaxLib.SVG.Def.GradientStop( 
                "95%",      // offset
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    27
                ),          // colour
                BLANK()     // opacity
            ),              // stops
            BLANK(),        // cx
            BLANK(),        // cy
            BLANK(),        // r
            BLANK(),        // fx
            BLANK(),        // fy
            BLANK()         // fr
        )
    ) &
    DaxLib.SVG.Element.Circle(
        "50%",              // cx
        "50%",              // cy
        15,                 // r
        DaxLib.SVG.Attr.Shapes(
            "url(""" & "#myGradient" & """)", // fill
            BLANK(),        // fillOpacity
            BLANK(),        // fillRule   
            BLANK(),        // stroke
            BLANK(),        // strokeWidth
            BLANK(),        // strokeOpacity
            BLANK()         // opacity
        ),                  // attributes
        BLANK()             // transforms
    ),                      // contents
    BLANK()                 // sortODer
)
```

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><radialGradient id='myGradient'><stop offset='10%' stop-color='#EC008C'/><stop offset='80%' stop-color='#533285' stop-opacity='0.5'/><stop offset='95%' stop-color='#99700A'/></radialGradient></defs><circle cx='50%' cy='50%' r='15' fill='url("#myGradient")'  /></svg>

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