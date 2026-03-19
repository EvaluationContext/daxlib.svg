---
icon: material/replay
---

# Defs

This section documents SVG definition (defs) functions, which allow you to define reusable SVG elements such as `#!xml <linearGradient>`, `#!xml <clipPath>`, and shapes. Shapes can be reused by invoking them with [`#!dax DaxLib.SVG.Element.UseDef()`](../elements/Element.UseDef.md), providing the matching id. The use of Defs to define Shapes which are invoked multiple times can reduce overall SVG string length and improve performance in Power BI.

??? tip "Defining Defs"

    `DaxLib.SVG.Def.*` should be wrapped in [`#!dax DaxLib.SVG.Element.Defs()`](../elements/Element.Defs.md) to add `<defs>...</defs>` tags.

    ```dax
    DaxLib.SVG.Element.Defs(
    	    DaxLib.SVG.Def.Circle(...) &
    	    DaxLib.SVG.Def.Rect(...)
    )
    // Returns: <defs>...</defs>
    ```