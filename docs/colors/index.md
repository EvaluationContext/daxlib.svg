---
icon: material/palette-swatch-outline
---

# Colors

This library offers functions for working with colors in SVG visualizations. These functions provide capabilities for theming, and interpolation to create dynamic and accessible visualizations

*These are subset of functions from [EvaluationContext.Colour](https://daxlib.org/package/EvaluationContext.Colour)*

!!! tip

    Color functions can be used with attribute functions like `#!dax DaxLib.SVG.Attr.Shapes()` to create dynamic coloring based on data values.

    ```dax
    DaxLib.SVG.Attr.Shapes(
        DaxLib.SVG.Color.Theme("Power BI", 1),  // Dynamic theme color
        BLANK(), 
        BLANK(), 
        BLANK(), 
        BLANK(), 
        BLANK(), 
        BLANK()
    )
    ```