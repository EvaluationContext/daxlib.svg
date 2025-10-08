---
title: Attr.Stroke
parent: Attributes
grand_parent: Functions
nav_order: 4
---

# DaxLib.SVG.Attr.Stroke

Creates SVG attribute strings for comprehensive stroke styling properties

## Syntax

```dax
DaxLib.SVG.Attr.Stroke(stroke, strokeWidth, strokeOpacity, strokeDasharray, strokeDashoffset, strokeLinecap, strokeLinejoin, strokeMiterlimit, markerStart, markerMid, markerEnd)
```

| Parameter         | Type      | Required   | Description                                          | 
| :---: | :---: | :---: | :---: |
| stroke            | STRING    |  No        | Stroke color (e.g., "#FF0000", "red")              |
| strokeWidth       | INT64     |  No        | Stroke width                                         |
| strokeOpacity     | DOUBLE    |  No        | Stroke opacity (0-1)                                 |
| strokeDasharray   | STRING    |  No        | Stroke dasharray pattern (e.g., "5,5" for dashed)    |
| strokeDashoffset  | STRING    |  No        | Stroke dashoffset                                    |
| strokeLinecap     | STRING    |  No        | Stroke linecap ("butt", "round", "square")           |
| strokeLinejoin    | STRING    |  No        | Stroke linejoin ("miter", "round", "bevel")          |
| strokeMiterlimit  | STRING    |  No        | Miter limit for stroke joins                         |
| markerStart       | STRING    |  No        | Marker for start of line (e.g., 'url(#arrowStart)')  |
| markerMid         | STRING    |  No        | Marker for middle points of line                     |
| markerEnd         | STRING    |  No        | Marker for end of line (e.g., 'url(#arrowEnd)')      |

## Returns

**STRING** An attribute string that can be used directly in SVG elements

## Example

```dax
DaxLib.SVG.Attr.Stroke("#0000FF", 2, 1, "5,5", "0", "round", "round", "", "", "", "url(#arrow)")
// Returns "stroke='#0000FF' stroke-width='2' stroke-opacity='1' stroke-dasharray='5,5' stroke-dashoffset='0' stroke-linecap='round' stroke-linejoin='round' marker-end='url(#arrow)'"
```

## Definition

```dax
function 'DaxLib.SVG.Attr.Stroke' = 
    (
        stroke: STRING,
        strokeWidth: INT64,
        strokeOpacity: DOUBLE,
        strokeDasharray: STRING,
        strokeDashoffset: STRING,
        strokeLinecap: STRING,
        strokeLinejoin: STRING,
        strokeMiterlimit: STRING,
        markerStart: STRING,
        markerMid: STRING,
        markerEnd: STRING
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