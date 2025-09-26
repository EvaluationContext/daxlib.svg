---
title: svg
nav_order: 3
has_children: true
parent: SVG
---

	/// Wraps content in SVG container for Power BI visualization
	/// Warning: Any measures that use this function must have the "DataCategory" property = "ImageUrl"
	/// Note: Enter BLANK() to skip any optional parameter
	/// width		STRING		Optional: width (pixels or percentage)
	/// height		STRING		Optional: height (pixels or percentage)
	/// viewbox		STRING		Optional: viewBox (e.g., "0 0 100 100")
	/// contents	STRING		To include one or more SVG elements (e.g., from DaxLib.SVG.Element functions)
	/// sortValue	EXPR		Optional: sort value for ordering in tables
	function 'DaxLib.SVG.SVG' =
			(
				width : STRING,
				height : STRING, 
				viewbox : STRING,
				contents : STRING,
				sortValue : EXPR
			) =>

				VAR _Canvas = 		IF( NOT ISBLANK( width ) && NOT ISBLANK( height ), "width='" & width & "' height='" & height & "' " )
				VAR _SortDesc = 	IF( NOT ISBLANK( sortValue ), "<desc>" & FORMAT( sortValue, "000000000000" ) & "</desc>" )

				VAR _result =
					"data:image/svg+xml;utf8," &
					"<svg " & 
					_Canvas &
					viewbox &
					"xmlns='http://www.w3.org/2000/svg'>" &
					_SortDesc &
					contents &
					"</svg>"

				RETURN _result