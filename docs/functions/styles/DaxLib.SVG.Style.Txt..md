---
title: Style.Txt
nav_order: 6.3
parent: Styles
---

# DaxLib.SVG.Style.Txt

Text-specific style properties for SVG text elements

## Syntax

```dax
DaxLib.SVG.Style.Txt(fontFamily, fontSize, fontWeight, fontStyle, textAnchor, baseline, textDecoration, letterSpacing, wordSpacing)
```

## Parameters

| Name           | Type   | Required | Description                                         |
|:---:|:---:|:---:|:---:|
| fontFamily     | STRING | No       | Font family for text                                |
| fontSize       | INT64  | No       | Font size for text                                  |
| fontWeight     | STRING | No       | Weight ("normal", "bold", "lighter", "100-900")     |
| fontStyle      | STRING | No       | Style ("normal", "italic", "oblique")               |
| textAnchor     | STRING | No       | Anchor ("start", "middle", "end")                   |
| baseline       | STRING | No       | Dominant baseline                                   |
| textDecoration | STRING | No       | Decoration ("none", "underline", "overline", "line-through") |
| letterSpacing  | STRING | No       | Space between letters                               |
| wordSpacing    | STRING | No       | Space between words                                 |

## Returns

(*STRING*) style string

## Example

```dax
DaxLib.SVG.Style.Txt(
	"Arial", 
	14, 
	"bold", 
	"normal", 
	"middle", 
	"central",
	 "underline", 
	 "0.1em", 
	 "0.2em"
)
// Returns: font-family:Arial;font-size:14;font-weight:bold;font-style:normal;text-anchor:middle;dominant-baseline:central;text-decoration:underline;letter-spacing:0.1em;word-spacing:0.2em;
```

## Definition
```dax
function 'DaxLib.SVG.Style.Txt' = 
    (
        fontFamily: STRING,
        fontSize: INT64,
        fontWeight: STRING,
        fontStyle: STRING,
        textAnchor: STRING,
        baseline: STRING,
        textDecoration: STRING,
        letterSpacing: STRING,
        wordSpacing: STRING
    ) =>

        VAR _FontFamily =     IF( NOT ISBLANK( fontFamily ),     "font-family:" & fontFamily & ";" )
        VAR _FontSize =       IF( NOT ISBLANK( fontSize ),       "font-size:" & fontSize & ";" )
        VAR _FontWeight =     IF( NOT ISBLANK( fontWeight ),     "font-weight:" & fontWeight & ";" )
        VAR _FontStyle =      IF( NOT ISBLANK( fontStyle ),      "font-style:" & fontStyle & ";" )
        VAR _TextAnchor =     IF( NOT ISBLANK( textAnchor ),     "text-anchor:" & textAnchor & ";" )
        VAR _Baseline =       IF( NOT ISBLANK( baseline ),       "dominant-baseline:" & baseline & ";" )
        VAR _TextDecoration = IF( NOT ISBLANK( textDecoration ), "text-decoration:" & textDecoration & ";" )
        VAR _LetterSpacing =  IF( NOT ISBLANK( letterSpacing ),  "letter-spacing:" & letterSpacing & ";" )
        VAR _WordSpacing =    IF( NOT ISBLANK( wordSpacing ),    "word-spacing:" & wordSpacing & ";" )

        RETURN
		
            _FontFamily &
            _FontSize &
            _FontWeight &
            _FontStyle &
            _TextAnchor &
            _Baseline &
            _TextDecoration &
            _LetterSpacing &
            _WordSpacing
```