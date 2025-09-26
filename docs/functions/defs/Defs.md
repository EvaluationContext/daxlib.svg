---
title: Defs
nav_order: 5
has_children: true
parent: Functions
---

# Defs

This section documents SVG definition (defs) functions, which allow you to define reusable SVG elements such as gradients, clip paths, and shapes. Defs should be wrapped in `DaxLib.SVG.Element.Defs` to ensure correct SVG structure. D

efine an element once, then reuse or override properties with [`DaxLib.SVG.Element.UseDef`]({{ site.baseurl }}/docs/functions/defs/DaxLib.SVG.Element.UseDef.md) to reduce SVG size and improve performance

{: .info}
> DaxLib.SVG.Def.* should be wrapped in `DaxLib.SVG.Element.Defs()`{:.dax} to add `<defs>...</defs>`{:.xml} tags.
> 
> ```dax
> DaxLib.SVG.Element.Defs(
> 	    DaxLib.SVG.Def.Circle(...) &
> 	    DaxLib.SVG.Def.Rect(...)
> )
> // Returns: <defs>...</defs>
> ```

{: .warning}
> Use `additionProperties` parameters to override properties on a def. Overwriting style may be problematic.

## Available Def Functions

The following functions are available: