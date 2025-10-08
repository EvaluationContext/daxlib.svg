---
title: SVG
nav_order: 2
has_children: true
parent: Functions
---

# SVG

The `DaxLib.SVG.SVG` function wraps your SVG content in a valid SVG container for use in Power BI visuals. All element and compound functions should be wrapped in this function to ensure correct metadata and rendering.

{: .tip}
> Any measures use these UDFs must have `DataCategory = "ImageUrl"`{:.txt}