---
icon: material/replay
---

# Defs

This section documents SVG definition (defs) functions, which allow you to define reusable SVG elements such as `#!xml <linearGradient>`, `#!xml <clipPath>`, and shapes. Shapes can be reused by invoking them with [`#!dax DaxLib.SVG.Element.UseDef()`](../elements/UseDef.md), providing the matching id. The use of Defs to define Shapes which are invoked multiple times can reduce overall SVG string length and improve performance in Power BI.

??? tip "Defining Defs"

    `DaxLib.SVG.Def.*` should be wrapped in [`#!dax DaxLib.SVG.Element.Defs()`](../elements/Defs.md) to add `<defs>...</defs>` tags.

    ```dax
    DaxLib.SVG.Element.Defs(
    	    DaxLib.SVG.Def.Circle(...) &
    	    DaxLib.SVG.Def.Rect(...)
    )
    // Returns: <defs>...</defs>
    ```

=== "ClipPath"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><clipPath id='clip-circle'><circle cx='50%' cy='80%' r='8'/></clipPath></defs><rect x='0%' y='0%' width='100%' height='80%' fill='#EC008C' clip-path='url(#clip-circle)' /></svg>

=== "LinearGradient"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><linearGradient id='myGradient'><stop offset='20%' stop-color='#EC008C'/><stop offset='80%' stop-color='#533285'/></linearGradient></defs><rect x='2' y='2' width='80%' height='80%' fill='url("#myGradient")'  /></svg>

=== "RadialGradient"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><radialGradient id='myGradient'><stop offset='10%' stop-color='#EC008C'/><stop offset='80%' stop-color='#533285' stop-opacity='0.5'/><stop offset='95%' stop-color='#99700A'/></radialGradient></defs><circle cx='50%' cy='50%' r='15' fill='url("#myGradient")'  /></svg>