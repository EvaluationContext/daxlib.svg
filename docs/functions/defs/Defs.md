---
title: Defs
nav_order: 5
has_children: true
parent: Functions
---

# Defs

This section documents SVG definition (defs) functions, which allow you to define reusable SVG elements such as gradients, clip paths, and shapes. Defs should be wrapped in `DaxLib.SVG.Element.Defs` to ensure correct SVG structure.

Define an element once, then reuse with [`DaxLib.SVG.Element.UseDef`]({{ site.baseurl }}/docs/functions/defs/DaxLib.SVG.Element.UseDef.md) to reduce SVG size and improve performance.

{: .tip}
> DaxLib.SVG.Def.* should be wrapped in `DaxLib.SVG.Element.Defs()`{:.dax} to add `<defs>...</defs>`{:.xml} tags.
> 
> ```dax
> DaxLib.SVG.Element.Defs(
> 	    DaxLib.SVG.Def.Circle(...) &
> 	    DaxLibtip.Def.Rect(...)
> )
> // Returns: <defs>...</defs>
> ```