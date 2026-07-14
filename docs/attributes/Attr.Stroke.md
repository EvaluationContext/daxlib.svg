# Attr.Stroke

Comprehensive stroke attributes function

=== "Syntax"

    ```dax
    DaxLib.SVG.Attr.Stroke( stroke, strokeWidth, strokeOpacity, strokeDasharray, strokeDashoffset, strokeLinecap, strokeLinejoin, strokeMiterlimit, markerStart, markerMid, markerEnd )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | stroke | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Stroke color (e.g., "#FF0000", "red"). Omitted if not specified |
    | strokeWidth | <span class="type-label int64">INT64</span> | :material-close: | `#!dax BLANK()` | Stroke width. Omitted if not specified |
    | strokeOpacity | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax BLANK()` | Stroke opacity (0-1). Omitted if not specified |
    | strokeDasharray | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Stroke dasharray pattern (e.g., "5,5" for dashed). Omitted if not specified |
    | strokeDashoffset | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Stroke dashoffset. Omitted if not specified |
    | strokeLinecap | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Stroke linecap ("butt", "round", "square"). Omitted if not specified |
    | strokeLinejoin | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Stroke linejoin ("miter", "round", "bevel"). Omitted if not specified |
    | strokeMiterlimit | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Miter limit for stroke joins. Omitted if not specified |
    | markerStart | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Marker for start of line (e.g., 'url(#arrowStart)'). Omitted if not specified |
    | markerMid | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Marker for middle points of line. Omitted if not specified |
    | markerEnd | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Marker for end of line (e.g., 'url(#arrowEnd)'). Omitted if not specified |

    <span class="type-label string">STRING</span> An attribute string that can be used directly in SVG elements

=== "Example"

    ```dax
    DaxLib.SVG.Attr.Stroke("#0000FF", 2, 1, "5,5", "0", "round", "round", "", "", "", "url(#arrow)")
    // Returns "stroke='#0000FF' stroke-width='2' stroke-opacity='1' stroke-dasharray='5,5' stroke-dashoffset='0' stroke-linecap='round' stroke-linejoin='round' marker-end='url(#arrow)'"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Attr.Stroke' =
    		(
    			stroke: STRING = BLANK(),
    			strokeWidth: INT64 = BLANK(),
    			strokeOpacity: DOUBLE = BLANK(),
    			strokeDasharray: STRING = BLANK(),
    			strokeDashoffset: STRING = BLANK(),
    			strokeLinecap: STRING = BLANK(),
    			strokeLinejoin: STRING = BLANK(),
    			strokeMiterlimit: STRING = BLANK(),
    			markerStart: STRING = BLANK(),
    			markerMid: STRING = BLANK(),
    			markerEnd: STRING = BLANK()
    		) =>
    			VAR _Stroke =           IF(NOT ISBLANK(stroke),           "stroke='" & stroke & "' ")
    			VAR _StrokeWidth =      IF(NOT ISBLANK(strokeWidth),      "stroke-width='" & strokeWidth & "' ")
    			VAR _StrokeOpacity =    IF(NOT ISBLANK(strokeOpacity),    "stroke-opacity='" & strokeOpacity & "' ")
    			VAR _StrokeDasharray =  IF(NOT ISBLANK(strokeDasharray),  "stroke-dasharray='" & strokeDasharray & "' ")
    			VAR _StrokeDashoffset = IF(NOT ISBLANK(strokeDashoffset), "stroke-dashoffset='" & strokeDashoffset & "' ")
    			VAR _StrokeLinecap =    IF(NOT ISBLANK(strokeLinecap),    "stroke-linecap='" & strokeLinecap & "' ")
    			VAR _StrokeLinejoin =   IF(NOT ISBLANK(strokeLinejoin),   "stroke-linejoin='" & strokeLinejoin & "' ")
    			VAR _StrokeMiterlimit = IF(NOT ISBLANK(strokeMiterlimit), "stroke-miterlimit='" & strokeMiterlimit & "' ")
    			VAR _MarkerStart =      IF(NOT ISBLANK(markerStart),      "marker-start='" & markerStart & "' ")
    			VAR _MarkerMid =        IF(NOT ISBLANK(markerMid),        "marker-mid='" & markerMid & "' ")
    			VAR _MarkerEnd =        IF(NOT ISBLANK(markerEnd),        "marker-end='" & markerEnd & "' ")
    			
    			RETURN
    				_Stroke &
    				_StrokeWidth &
    				_StrokeOpacity &
    				_StrokeDasharray &
    				_StrokeDashoffset &
    				_StrokeLinecap &
    				_StrokeLinejoin &
    				_StrokeMiterlimit &
    				_MarkerStart &
    				_MarkerMid &
    				_MarkerEnd
    ```