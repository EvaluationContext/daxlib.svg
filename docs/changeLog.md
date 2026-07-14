## 2.0.0 (Latest)

:material-alert-outline: Some incompatible API changes: optional parameters have been reordered to trail required parameters in `#!dax DaxLib.SVG.Compound.*` and `#!dax DaxLib.SVG.Axes.Layout()`

:octicons-sparkles-fill-16: Optional parameters with default values in all UDFs, leveraging the new [DAX UDF optional parameter syntax](https://www.sqlbi.com/articles/optional-parameters-in-dax-user-defined-functions/)

:octicons-sparkles-fill-16: `#!dax DaxLib.SVG.Compound.Bars()` aligned with the native Power BI bar chart

:material-bug-outline: Resolves [EvaluationContext/daxlib.svg#4](https://github.com/EvaluationContext/daxlib.svg/issues/4)

## 1.0.1

:octicons-sparkles-fill-16: Source library split into individual per-function TMDL files for improved maintainability

:octicons-sparkles-fill-16: Update JSDoc annotations 

:material-bug-outline: Update/fix some `DaxLib.SVG.Compound` UDFs

## 1.0.0

:material-alert-outline: Some incompatible API changes to compounds

:octicons-sparkles-fill-16: `#!dax DaxLib.SVG.Compound.Bar()` renamed to `#!dax DaxLib.SVG.Compound.Bars()`

:octicons-sparkles-fill-16: Added `showAxis` and `axisFontSize` parameters to `#!dax DaxLib.SVG.Compound.Bars()`, `#!dax DaxLib.SVG.Compound.Line()`, `#!dax DaxLib.SVG.Compound.Area()`

:octicons-sparkles-fill-16: Added `orientation` parameter to `#!dax DaxLib.SVG.Compound.ProgressBar()`

:octicons-sparkles-fill-16: New `#!dax DaxLib.SVG.Compound.ProgressBar()` compound

:octicons-sparkles-fill-16: New **Scale** functions: `#!dax DaxLib.SVG.Scale.NiceNum()`, `#!dax DaxLib.SVG.Scale.NiceRange()`

:octicons-sparkles-fill-16: New **Data** namespace: `#!dax DaxLib.SVG.Data.AxisMeasure()`, `#!dax DaxLib.SVG.Data.Range()`

:octicons-sparkles-fill-16: New **Axes** namespace: `#!dax DaxLib.SVG.Axes.Layout()`, `#!dax DaxLib.SVG.Axes.Render()`, `#!dax DaxLib.SVG.Axes.Point()`, `#!dax DaxLib.SVG.Axes.Baseline()`, `#!dax DaxLib.SVG.Axes.MaxTickLabelWidth()`

:octicons-sparkles-fill-16: New **Viz** namespace with simplified chart wrappers: `#!dax DaxLib.SVG.Viz.Bars()`, `#!dax DaxLib.SVG.Viz.Line()`, `#!dax DaxLib.SVG.Viz.Area()`, `#!dax DaxLib.SVG.Viz.ProgressBar()`, `#!dax DaxLib.SVG.Viz.Pill()`, `#!dax DaxLib.SVG.Viz.Boxplot()`, `#!dax DaxLib.SVG.Viz.Jitter()`, `#!dax DaxLib.SVG.Viz.Heatmap()`, `#!dax DaxLib.SVG.Viz.Violin()`

## 0.2.3-beta

:octicons-sparkles-fill-16: `#!dax DaxLib.SVG.Compound.*` performance improvements

## 0.2.2-beta

:material-bug-outline: `#!dax DaxLib.SVG.Compound.Pill()` correctly accepts x and y parameters

:material-bug-outline: `#!dax DaxLib.SVG.Compound.Heatmap()` correctly accepts x and y parameters

:material-bug-outline: `#!dax DaxLib.SVG.Compound.Bar()` correctly accepts y parameters

:material-bug-outline: `#!dax DaxLib.SVG.Compound.Violin()` resolved spike from last point

## 0.2.1-beta

:octicons-sparkles-fill-16: [Tom Shanley](https://www.linkedin.com/in/tshanley/) contributed `#!dax DaxLib.SVG.Compound.Bar()`

:octicons-sparkles-fill-16: Annotation placeholders

## 0.2.0-beta 

:octicons-sparkles-fill-16: Restructured library will the idea of Elements and Compounds

:octicons-rocket-24: Documentation site launch

##  0.1.1-beta

:material-bug-outline: Fixed incorrect function references in `#!dax DaxLib.SVG.Example.BulletChart.ActionDot()`

##  0.1.0-beta

:octicons-rocket-24: Initial release of the DaxLib.SVG library with Docs Site