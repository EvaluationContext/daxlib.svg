---
title: DaxLib.SVG.Transforms
parent: Transforms
grand_parent: Functions
nav_order: 1
---

# DaxLib.SVG.Transforms

Creates an SVG transform attribute value for applying multiple transformations to an element

## Syntax

```dax
DaxLib.SVG.Transforms(translate, rotate, scale, skewX, skewY)
```

## Parameters

| Parameter | Type      | Required | Description | 
| :---: | :---: | :---: | :---: |
| translate | STRING    | No       | Translation coordinates in the format "x,y" | 
| rotate    | STRING    | No       | Rotation angle in degrees, or "angle x y" for rotation around a point |
| scale     | STRING    | No       | Scale factor, or "x,y" for different scaling in each dimension | 
| skewX     | STRING    | No       | Horizontal skew angle in degrees | 
| skewY     | STRING    | No       | Vertical skew angle in degrees |

## Returns

(*STRING*) A transform attribute value that can be used with the transform attribute of SVG elements.

## Example

```dax
DaxLib.SVG.Transforms("10,20", "45", "1.5", "", "")
// Returns: "translate(10,20) rotate(45) scale(1.5)"
```

## Definition

```dax
function 'DaxLib.SVG.Transforms' = 
    (
        translate: STRING,
        rotate: STRING,
        scale: STRING,
        skewX: STRING,
        skewY: STRING
    ) =>

        IF(NOT ISBLANK(translate),  "translate(" & translate & ") ") &
        IF(NOT ISBLANK(rotate),     "rotate(" & rotate & ") ") &
        IF(NOT ISBLANK(scale),      "scale(" & scale & ") ") &
        IF(NOT ISBLANK(skewX),      "skewX(" & skewX & ") ") &
        IF(NOT ISBLANK(skewY),      "skewY(" & skewY & ") ") 
```