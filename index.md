---
title: DaxLib.SVG
layout: home
nav_order: 1
description: "A comprehensive set of DAX User-Defined Functions (UDF) designed to enable easy creation of SVG visuals for Power BI"
permalink: /
---

# DaxLib.SVG
{: .fs-9 }

A comprehensive set of DAX User-Defined Functions (UDF) designed to enable easy creation of SVG visuals for Power BI.
{: .fs-6 .fw-300 }

[Download From DaxLib](https://daxlib.org/package/DaxLib.SVG/){: .btn .btn-primary .mr-2 }
[Download Example PBIP](https://github.com/EvaluationContext/daxlib.svg/tree/main/assets/PBIP){: .btn .btn-outline }
[0.1.2-beta]({{ site.baseurl }}/docs/version/){: .btn .btn-green }

---

![DaxLib.SVG in Action]({{ site.baseurl }}/assets/img/UDFInAction.png)

---

### SVG Wrapper

Functions for wrapping SVG content for use in Power BI visuals:

- Create SVG containers with proper namespaces
- Set viewBox and other container attributes
- Combine multiple SVG elements into a single visual

[View SVG Wrapper →]({{ site.baseurl }}/docs/functions/svg/SVG/){: .btn .btn-outline }

---

### Elements

Core SVG element generator functions:

- Create basic shapes (Circle, Rect, Line, etc.)
- Build text elements with styling
- Group elements for organization and reuse

[View Elements →]({{ site.baseurl }}/docs/functions/elements/Elements/){: .btn .btn-outline }

---

### Compounds

Composite SVG components:

- Prebuilt complex visual elements

[View Compounds →]({{ site.baseurl }}/docs/functions/compounds/Compounds/){: .btn .btn-outline }

---

### Defs

Reusable SVG definitions for gradients, shapes, and more:

- Create and reuse gradient definitions
- Define clip paths for complex masking
- Build reusable shape definitions

[View Defs →]({{ site.baseurl }}/docs/functions/defs/Defs/){: .btn .btn-outline }

---

### Attributes

Functions for creating SVG attribute strings:

- Style shapes with fill, stroke, and opacity
- Configure text with font and alignment options
- Apply comprehensive stroke settings

[View Attributes →]({{ site.baseurl }}/docs/functions/attributes/){: .btn .btn-outline }

---

### Transforms

Functions for creating SVG transform attribute values:

- Apply translations, rotations, and scaling

[View Transforms →]({{ site.baseurl }}/docs/functions/transforms/){: .btn .btn-outline }

---

### Colors

Color utility functions for dynamic theming and visualization:

- Access predefined color themes and palettes
- Themes for performance-based color coding
- Interpolate colors for gradients and heat maps

[View Colors →]({{ site.baseurl }}/docs/functions/colors/Colors/){: .btn .btn-outline }

---

### Scales

Functions for mapping and normalizing values for SVG graphics:

- Convert data values to visual dimensions

[View Scales →]({{ site.baseurl }}/docs/functions/scales/Scales/){: .btn .btn-outline }

---

{: .tip}
> **Getting Started**
> 
> 1. Download the library from [DaxLib](https://daxlib.org/package/DaxLib.SVG/)
> 2. Install using TMDL view
> 3. Start using the functions in your measures
> 
> For detailed examples, check out our [example PBIP file](https://github.com/EvaluationContext/daxlib.svg/tree/main/assets/PBIP).