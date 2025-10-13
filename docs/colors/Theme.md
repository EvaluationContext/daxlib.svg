---
comments: true
---

# Color.Theme

Select theme color, wrapping around to the start if variant exceeds available options

=== "Syntax"

    ```dax
    DaxLib.SVG.Color.Theme(themeName, variant)
    ```

    | Name      | Type   | Required | Description                                                     |
    |:---:|:---:|:---:|---|
    | themeName | <span class="type-label string">STRING</span> | :material-check: | Theme name                       |
    | variant   | <span class="type-label int64">INT64</span>  | :material-check: | Variant index (1-N, wraps around if exceeds available variants) |

    <span class="type-label string">**STRING**</span> Hex color code

=== "Available Themes"

    | Variant | Power BI | Modern Corporate | Ocean Breeze | Sunset Vibes | Forest Green | Purple Rain | Monochrome | Vibrant Tech | Earth Tones | Pastel Dreams | Midnight Blue |
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    | 1 | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #118DFF;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #2E3440;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #0077BE;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FF6B35;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #355E3B;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #301934;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #1C1C1C;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FF0080;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #8B4513;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFB3BA;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #191970;"></span> |
    | 2 | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #12239E;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #3B4252;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #00A8CC;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F7931E;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #228B22;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #663399;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #333333;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #00FFFF;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #A0522D;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFDFBA;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #000080;"></span> |
    | 3 | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #E66C37;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #434C5E;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #40E0D0;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFD23F;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #32CD32;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #9966CC;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #666666;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFFF00;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #CD853F;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFFFBA;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #0000CD;"></span> |
    | 4 | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #6B007B;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #4C566A;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #87CEEB;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #EE4B2B;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #90EE90;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #BA55D3;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #999999;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FF8000;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #DEB887;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #BAFFC9;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #4169E1;"></span> |
    | 5 | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #E044A7;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #5E81AC;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #B0E0E6;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #C04000;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #98FB98;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #DDA0DD;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #CCCCCC;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #8000FF;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F4A460;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #BAE1FF;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #6495ED;"></span> |
    | 6 | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #744EC2;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #81A1C1;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #E0F6FF;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFCBA4;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F0FFF0;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #E6E6FA;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F5F5F5;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #00FF80;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFF8DC;"></span> | | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #B0C4DE;"></span> |
    | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
    | 41 | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #0B511F;"></span> | | | | | | | | | | |

=== "Example"

    ```dax
    DaxLib.SVG.Color.Theme("Power BI", 1)
    // Returns: "#118DFF"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Color.Theme' =
        (
            themeName: STRING,
            variant: INT64
        ) =>
        
            VAR Themes =
                DATATABLE(
                "ThemeName", STRING,
                "Variant", INTEGER,
                "Color", STRING,
                {
                    // Power BI Default
                    {"Power BI", 1, "#118DFF"},
                    {"Power BI", 2, "#12239E"},
                    {"Power BI", 3, "#E66C37"},
                    {"Power BI", 4, "#6B007B"},
                    {"Power BI", 5, "#E044A7"},
                    {"Power BI", 6, "#744EC2"},
                    {"Power BI", 7, "#D9B300"},
                    {"Power BI", 8, "#D64550"},
                    {"Power BI", 9, "#197278"},
                    {"Power BI", 10, "#1AAB40"},
                    {"Power BI", 11, "#15C6F4"},
                    {"Power BI", 12, "#4092FF"},
                    {"Power BI", 13, "#FFA058"},
                    {"Power BI", 14, "#BE5DC9"},
                    {"Power BI", 15, "#F472D0"},
                    {"Power BI", 16, "#B5A1FF"},
                    {"Power BI", 17, "#C4A200"},
                    {"Power BI", 18, "#FF8080"},
                    {"Power BI", 19, "#00DBBC"},
                    {"Power BI", 20, "#5BD667"},
                    {"Power BI", 21, "#0091D5"},
                    {"Power BI", 22, "#4668C5"},
                    {"Power BI", 23, "#FF6300"},
                    {"Power BI", 24, "#99008A"},
                    {"Power BI", 25, "#EC008C"},
                    {"Power BI", 26, "#533285"},
                    {"Power BI", 27, "#99700A"},
                    {"Power BI", 28, "#FF4141"},
                    {"Power BI", 29, "#1F9A85"},
                    {"Power BI", 30, "#25891C"},
                    {"Power BI", 31, "#0057A2"},
                    {"Power BI", 32, "#002050"},
                    {"Power BI", 33, "#C94F0F"},
                    {"Power BI", 34, "#450F54"},
                    {"Power BI", 35, "#B60064"},
                    {"Power BI", 36, "#34124F"},
                    {"Power BI", 37, "#6A5A29"},
                    {"Power BI", 38, "#1AAB40"},
                    {"Power BI", 39, "#BA141A"},
                    {"Power BI", 40, "#0C3D37"},
                    {"Power BI", 41, "#0B511F"},
        
                    // Modern Corporate - Professional blues and grays
                    {"Modern Corporate", 1, "#2E3440"},
                    {"Modern Corporate", 2, "#3B4252"},
                    {"Modern Corporate", 3, "#434C5E"},
                    {"Modern Corporate", 4, "#4C566A"},
                    {"Modern Corporate", 5, "#5E81AC"},
                    {"Modern Corporate", 6, "#81A1C1"},
        
                    // Ocean Breeze - Cool blues and teals
                    {"Ocean Breeze", 1, "#0077BE"},
                    {"Ocean Breeze", 2, "#00A8CC"},
                    {"Ocean Breeze", 3, "#40E0D0"},
                    {"Ocean Breeze", 4, "#87CEEB"},
                    {"Ocean Breeze", 5, "#B0E0E6"},
                    {"Ocean Breeze", 6, "#E0F6FF"},
        
                    // Sunset Vibes - Warm oranges and reds
                    {"Sunset Vibes", 1, "#FF6B35"},
                    {"Sunset Vibes", 2, "#F7931E"},
                    {"Sunset Vibes", 3, "#FFD23F"},
                    {"Sunset Vibes", 4, "#EE4B2B"},
                    {"Sunset Vibes", 5, "#C04000"},
                    {"Sunset Vibes", 6, "#FFCBA4"},
        
                    // Forest Green - Natural greens
                    {"Forest Green", 1, "#355E3B"},
                    {"Forest Green", 2, "#228B22"},
                    {"Forest Green", 3, "#32CD32"},
                    {"Forest Green", 4, "#90EE90"},
                    {"Forest Green", 5, "#98FB98"},
                    {"Forest Green", 6, "#F0FFF0"},
        
                    // Purple Rain - Rich purples
                    {"Purple Rain", 1, "#301934"},
                    {"Purple Rain", 2, "#663399"},
                    {"Purple Rain", 3, "#9966CC"},
                    {"Purple Rain", 4, "#BA55D3"},
                    {"Purple Rain", 5, "#DDA0DD"},
                    {"Purple Rain", 6, "#E6E6FA"},
        
                    // Monochrome - Sophisticated grays
                    {"Monochrome", 1, "#1C1C1C"},
                    {"Monochrome", 2, "#333333"},
                    {"Monochrome", 3, "#666666"},
                    {"Monochrome", 4, "#999999"},
                    {"Monochrome", 5, "#CCCCCC"},
                    {"Monochrome", 6, "#F5F5F5"},
        
                    // Vibrant Tech - Bold and energetic
                    {"Vibrant Tech", 1, "#FF0080"},
                    {"Vibrant Tech", 2, "#00FFFF"},
                    {"Vibrant Tech", 3, "#FFFF00"},
                    {"Vibrant Tech", 4, "#FF8000"},
                    {"Vibrant Tech", 5, "#8000FF"},
                    {"Vibrant Tech", 6, "#00FF80"},
        
                    // Earth Tones - Natural browns and beiges
                    {"Earth Tones", 1, "#8B4513"},
                    {"Earth Tones", 2, "#A0522D"},
                    {"Earth Tones", 3, "#CD853F"},
                    {"Earth Tones", 4, "#DEB887"},
                    {"Earth Tones", 5, "#F4A460"},
                    {"Earth Tones", 6, "#FFF8DC"},
        
                    // Pastel Dreams - Soft and gentle
                    {"Pastel Dreams", 1, "#FFB3BA"},
                    {"Pastel Dreams", 2, "#FFDFBA"},
                    {"Pastel Dreams", 3, "#FFFFBA"},
                    {"Pastel Dreams", 4, "#BAFFC9"},
                    {"Pastel Dreams", 5, "#BAE1FF"},
                    // {"Pastel Dreams", 6, "#E1BAFF"},
        
                    // Midnight Blue - Deep blues and navy
                    {"Midnight Blue", 1, "#191970"},
                    {"Midnight Blue", 2, "#000080"},
                    {"Midnight Blue", 3, "#0000CD"},
                    {"Midnight Blue", 4, "#4169E1"},
                    {"Midnight Blue", 5, "#6495ED"},
                    {"Midnight Blue", 6, "#B0C4DE"}
                }
            )
        
            VAR ThemeColors = FILTER(Themes, [ThemeName] = themeName)
            VAR MaxVariant = MAXX(ThemeColors, [Variant])
            VAR AdjustedVariant = IF(
                MaxVariant > 0,
                MOD( variant - 1, MaxVariant ) + 1,
                variant
            )
            VAR SelectedColor =
                MAXX(
                    FILTER( ThemeColors, [Variant] = AdjustedVariant),
                    [Color]
                )

            RETURN SelectedColor
    ```