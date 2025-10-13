---
comments: true
---

# Attr.Txt

Creates SVG attribute strings for text styling properties

=== "Syntax"

    ```dax
    DaxLib.SVG.Attr.Txt( fontFamily, fontSize, fontWeight, fontStyle, textAnchor, baseline, textDecoration, letterSpacing, wordSpacing )
    ```

    | Parameter         | Type      | Required  | Description                                                           | 
    |:---:|:---:|:---:|---|
    | fontFamily        | <span class="type-label string">STRING</span>    | :material-close:        | Font family for text (e.g., "Arial, sans-serif") |
    | fontSize          | <span class="type-label int64">INT64</span>     | :material-close:        | Font size in pixels |
    | fontWeight        | <span class="type-label string">STRING</span>    | :material-close:        | Font weight ("normal", "bold", "lighter", "100-900")                  |
    | fontStyle         | <span class="type-label string">STRING</span>    | :material-close:        | Font style ("normal", "italic", "oblique")                            |
    | textAnchor        | <span class="type-label string">STRING</span>    | :material-close:        | Text anchor position ("start", "middle", "end")                       |
    | baseline          | <span class="type-label string">STRING</span>    | :material-close:        | Dominant baseline alignment                                           |
    | textDecoration    | <span class="type-label string">STRING</span>    | :material-close:        | Text decoration ("none", "underline", "overline", "line-through")     |
    | letterSpacing     | <span class="type-label string">STRING</span>    | :material-close:        | Space between letters                                                 |
    | wordSpacing       | <span class="type-label string">STRING</span>    | :material-close:        | Space between words                                                   |

    <span class="type-label string">STRING</span> An attribute string that can be used directly in SVG text elements

=== "Example"

    ```dax
    DaxLib.SVG.Attr.Txt("Arial, sans-serif", 14, "bold", "normal", "middle", "middle", "none", "", "")
    // Returns "font-family='Arial, sans-serif' font-size='14' font-weight='bold' font-style='normal' text-anchor='middle' dominant-baseline='middle' text-decoration='none'"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Attr.Txt' = 
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

            IF( NOT ISBLANK( fontFamily ),     "font-family='" & fontFamily & "' ") &
            IF( NOT ISBLANK( fontSize ),       "font-size='" & fontSize & "' ") &
            IF( NOT ISBLANK( fontWeight ),     "font-weight='" & fontWeight & "' ") &
            IF( NOT ISBLANK( fontStyle ),      "font-style='" & fontStyle & "' ") &
            IF( NOT ISBLANK( textAnchor ),     "text-anchor='" & textAnchor & "' ") &
            IF( NOT ISBLANK( baseline ),       "dominant-baseline='" & baseline & "' ") &
            IF( NOT ISBLANK( textDecoration ), "text-decoration='" & textDecoration & "' ") &
            IF( NOT ISBLANK( letterSpacing ),  "letter-spacing='" & letterSpacing & "' ") &
            IF( NOT ISBLANK( wordSpacing ),    "word-spacing='" & wordSpacing & "' ")
    ```