---
title: svg
nav_order: 2.1
has_children: true
parent: SVG
---

# DaxLib.SVG.SVG

Wraps content in an SVG container for Power BI visualization

{: .tip}
> Any measures use these UDFs must have `DataCategory = "ImageUrl"`{:.txt}

## Syntax

```dax
DaxLib.SVG.SVG(
	width,
	height,
	viewbox,
	contents,
	sortValue
)
```

| Name      | Type   | Required | Description                                                                 |
|-----------|--------|----------|-----------------------------------------------------------------------------|
| width     | STRING | No       | Width (pixels or percentage)                                                |
| height    | STRING | No       | Height (pixels or percentage)                                               |
| viewbox   | STRING | No       | viewBox (e.g., "0 0 100 100")                                               |
| contents  | STRING | Yes      | SVG elements to include (e.g., from DaxLib.SVG.Element functions)           |
| sortValue | EXPR   | No       | Sort value for ordering in tables                                           |

## Returns

**STRING** SVG string

## Example

```dax
DaxLib.SVG.SVG(
	"100",
	"100",
	"viewBox='0 0 100 100' ",
	DaxLib.SVG.Element.Circle("50", "50", "40", "fill:blue;", BLANK(), BLANK()),
	1
)
```

## Definition

```dax
function 'DaxLib.SVG.SVG' =
	(
		width : STRING,
		height : STRING,
		viewbox : STRING,
		contents : STRING,
		sortValue : EXPR
	) =>

		VAR _Canvas = 	IF( NOT ISBLANK( width ) && NOT ISBLANK( height ), "width='" & width & "' height='" & height & "' " )
		VAR _SortDesc = IF( NOT ISBLANK( sortValue ), "<desc>" & FORMAT( sortValue, "000000000000" ) & "</desc>" )

		RETURN 
		
			"data:image/svg+xml;utf8," &
			"<svg " &
			_Canvas &
			viewbox &
			"xmlns='http://www.w3.org/2000/svg'>" &
			_SortDesc &
			contents &
			"</svg>"
```