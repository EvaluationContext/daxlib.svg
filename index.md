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

<!-- Placeholder for SVG library image -->
![DaxLib.SVG in Action](/assets/img/UDFInPowerBI.png)

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

- Create complex visual elements from simple parts
- Combine shapes and styles for consistent visuals
- Build reusable UI components

[View Compounds →]({{ site.baseurl }}/docs/functions/compounds/Compounds/){: .btn .btn-outline }

---

### Defs

Reusable SVG definitions for gradients, shapes, and more:

- Create and reuse gradient definitions
- Define clip paths for complex masking
- Build reusable shape definitions

[View Defs →]({{ site.baseurl }}/docs/functions/defs/Defs/){: .btn .btn-outline }

---

### Scales

Functions for mapping and normalizing values for SVG graphics:

- Convert data values to visual dimensions
- Create dynamic scaling for responsive visuals
- Generate paths and arcs based on data

[View Scales →]({{ site.baseurl }}/docs/functions/scales/Scales){: .btn .btn-outline }

---

### Styles

Functions to generate style strings for SVG elements:

- Create consistent styling across elements
- Generate text formatting for SVG text elements
- Apply line styles for paths and outlines

[View Styles →]({{ site.baseurl }}/docs/functions/styles/Styles/){: .btn .btn-outline }

---

### Visuals

Ready to use chart and visual components built from library elements:

- Pre-built visuals you can apply to your data

[View Visuals →]({{ site.baseurl }}/docs/functions/visuals/Visuals/){: .btn .btn-outline }

---

### Utils

Helper and utility functions for internal use:

- Format and process SVG element properties
- Handle optional elements and attributes
- Support internal library operations

[View Utils →]({{ site.baseurl }}/docs/functions/util/Util/){: .btn .btn-outline }

---

{: .tip}
> **Getting Started**
> 
> 1. Download the library from [DaxLib](https://daxlib.org/package/DaxLib.SVG/)
> 2. Install using TMDL view
> 3. Start using the functions in your measures
> 
> For detailed examples, check out our [example PBIP file](https://github.com/EvaluationContext/daxlib.svg/tree/main/assets/PBIP).