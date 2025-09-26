---
title: Tutorial
nav_order: 3
---

# xxx

xxx

## SVG xxx

### Viewbox

```
viewBox="minX minY width height"
```

minX, minY: The top-left corner of the SVG’s internal coordinate system.
width, height: The width and height of the coordinate system.

The viewBox acts like a window through which you view your SVG content.
All drawing commands (like x, y, cx, cy, etc.) are relative to this coordinate system.
If the SVG’s width and height (the output size) differ from the viewBox size, the SVG will scale its contents to fit, preserving the aspect ratio by default.

#### Example

```xml
<svg width="200" height="100" viewBox="0 0 100 50">
  <!-- Content here uses 0-100 for x and 0-50 for y -->
</svg>
```

The SVG will be displayed at `200px` by `100px`, but all coordinates inside are mapped from a `100x50` grid.