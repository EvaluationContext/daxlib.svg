---
title: Functions
nav_order: 2
has_children: true
---

# Functions

The DaxLib.SVG library provides a comprehensive set of functions for creating SVG visuals in Power BI.

---

## SVG Wrapper

`DaxLib.SVG.SVG`

[View Hex Manipulation Functions →]({{ site.baseurl }}/docs/functions/hex-manipulation/){: .btn .btn-outline }

--- 

## Visuals

`DaxLib.SVG.BulletChart.ActionDot`
`DaxLib.SVG.Bar`

---

## Elements

`DaxLib.SVG.Element.Defs`
`DaxLib.SVG.Element.Group`

`DaxLib.SVG.Element.Circle`
`DaxLib.SVG.Element.Rect`
`DaxLib.SVG.Element.Line`
`DaxLib.SVG.Element.Paths`
`DaxLib.SVG.Element.Ellipse`
`DaxLib.SVG.Element.Polygon`
`DaxLib.SVG.Element.Polyline`
`DaxLib.SVG.Element.Txt`

---

## Compounds

`DaxLib.SVG.Compound.Pill`

---

## Defs

Defs can be used to define style? or elements that can be reused.  

{: .info}
Def should should be wrapped with `DaxLib.SVG.Element.Defs` to add `<def>...</def>{:.xml} tags

{: .tip}
You can define a element once, then overwrite properties when creating a instance of it. Reducing the string size of the SVG, reducing the Power BI cache size, helping improve performance, and risk of risking String size limits.

{: .warning}
`additionProperties` parameters should be used if overwriting properties on a def, overwriting style will be problematic

`DaxLib.SVG.Def.GradientStop`
`DaxLib.SVG.Def.LinearGradient`
`DaxLib.SVG.Def.RadialGradient`
`DaxLib.SVG.Def.ClipPath`

`DaxLib.SVG.Def.Circle`
`DaxLib.SVG.Def.Rect`
`DaxLib.SVG.Def.Line`
`DaxLib.SVG.Def.Paths`

`DaxLib.SVG.Element.UseDef`


---

## Styles

Wrapper functions to define style strings to be consumed by `DaxLib.SVG.Element.*` and `DaxLib.SVG.Def.*` functions

`DaxLib.SVG.Style.Common`
`DaxLib.SVG.Style.Txt`
`DaxLib.SVG.Style.Line`

---

## Scaler

A range of functions for defining and mapping between scales.

`DaxLib.SVG.Scale.AngleFromPercent`
`DaxLib.SVG.Scale.ArcPath`
`DaxLib.SVG.Scale.AxisMax`
`DaxLib.SVG.Scale.AxisMin`
`DaxLib.SVG.Scale.AxisRange`
`DaxLib.SVG.Scale.ColourByThreshold`
`DaxLib.SVG.Scale.Normalize`
`DaxLib.SVG.Scale.ToPercent`

---

## Util

`DaxLib.SVG.Util.OptionalCommentElements`