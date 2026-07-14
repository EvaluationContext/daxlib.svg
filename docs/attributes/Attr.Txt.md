# Attr.Txt

Text-specific attributes

=== "Syntax"

    ```dax
    DaxLib.SVG.Attr.Txt( fontFamily, fontSize, fontWeight, fontStyle, textAnchor, baseline, textDecoration, letterSpacing, wordSpacing )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | fontFamily | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Font family for text. Omitted if not specified |
    | fontSize | <span class="type-label int64">INT64</span> | :material-close: | `#!dax BLANK()` | Font size for text. Omitted if not specified |
    | fontWeight | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Weight ("normal", "bold", "lighter", "100-900"). Omitted if not specified |
    | fontStyle | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Style ("normal", "italic", "oblique"). Omitted if not specified |
    | textAnchor | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Anchor ("start", "middle", "end"). Omitted if not specified |
    | baseline | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Dominant baseline. Omitted if not specified |
    | textDecoration | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Decoration ("none", "underline", "overline", "line-through"). Omitted if not specified |
    | letterSpacing | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Space between letters. Omitted if not specified |
    | wordSpacing | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Space between words. Omitted if not specified |

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
    			fontFamily: STRING = BLANK(),
    			fontSize: INT64 = BLANK(),
    			fontWeight: STRING = BLANK(),
    			fontStyle: STRING = BLANK(),
    			textAnchor: STRING = BLANK(),
    			baseline: STRING = BLANK(),
    			textDecoration: STRING = BLANK(),
    			letterSpacing: STRING = BLANK(),
    			wordSpacing: STRING = BLANK()
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