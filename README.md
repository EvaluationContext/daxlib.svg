
# DaxLib.SVG

DaxLib.SVG is a DAX User-Defined Functions (UDF) library designed to make creating SVG visuals in Power BI easier.

[![Download From DaxLib](https://img.shields.io/badge/Download%20from%20DaxLib-009688?style=for-the-badge&logo=cloudsmith&logoColor=white)](https://daxlib.org/package/daxlib.svg/)
[![Download Example PBIP](https://img.shields.io/badge/Download%20Example%20PBIP-607D8B?style=for-the-badge&logo=microsoftpowerbi&logoColor=white)](https://github.com/EvaluationContext/daxlib.svg/tree/main/PowerBI)

## Getting Started

1. Download the library from [DaxLib](https://daxlib.org/package/DaxLib.SVG/)
2. Install using TMDL view
3. Start using the functions in your measures
   
For detailed examples, check out our [example PBIP file](https://github.com/EvaluationContext/daxlib.svg/tree/main/assets/PBIP).

---

## Function Categories

| Category | Description |
|---|---|
| **[SVG Wrapper](docs/svg/index.md)** | Wraps one or more `Elements`, `Defs`, `Compounds`, applying required metadata and `<SVG>` tags |
| **[Elements](docs/elements/index.md)** | SVG primitives (i.e. `<Rect>`, `<Circle>`, `<line>`) |
| **[Compounds](docs/compounds/index.md)** | Complex components (i.e. boxplot, violin) made from `Elements` |
| **[Defs](docs/defs/index.md)** | Define reusable SVG elements (i.e. `<linearGradient>`, `<clipPath>`, and shapes) |
| **[Attributes](docs/attributes/index.md)** | Create Attributes (i.e. fill, stroke, opacity) string that can be applied to `Elements` and `Defs` |
| **[Transforms](docs/transforms/index.md)** | Create Transform strings |
| **[Scales](docs/scales/index.md)** | Mapping values between scales |
| **[Colors](docs/colors/index.md)** | Themes and functions for colour manipulation |

---

Full documentation is available at our [GitHub Pages site](https://evaluationcontext.github.io/daxlib.svg/).

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)