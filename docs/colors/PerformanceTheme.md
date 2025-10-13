---
comments: true
---

# Color.PerformanceTheme

Returns a color for the specified performance level and theme

=== "Syntax"

    ```dax
    DaxLib.SVG.Color.PerformanceTheme( themeName, variant )
    ```

    | Name      | Type   | Required | Description    |
    |:---:|:---:|:---:|---|
    | themeName | <span class="type-label string">STRING</span> | :material-check: | Theme name        |
    | variant   | <span class="type-label string">STRING</span> | :material-check: | Performance level |

    <span class="type-label string">**STRING**</span> Hex color code representing the performance level

=== "Available Themes"

    | Performance Level | Stoplight | Colorblind | Corporate | Pastel | Grayscale |
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | **veryBad** | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #D04848;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #8F2D56;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #8B0000;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F8BBD9;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #1A1A1A;"></span> |
    | **bad** | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F07857;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #C44536;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #4169E1;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #E6A0C4;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #404040;"></span> |
    | **neutral** | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFBF49;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #FFA500;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #6495ED;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F0E68C;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #808080;"></span> |
    | **good** | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #4CAF50;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #228B22;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #87CEEB;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #98FB98;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #CCCCCC;"></span> |
    | **veryGood** | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #2E8B57;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #006400;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #B0E0E6;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #90EE90;"></span> | <span class="d-inline-block p-2 mr-1 v-align-middle" style="background-color: #F5F5F5;"></span> |

=== "Example"

    ```dax
    DaxLib.SVG.Color.PerformanceTheme("Stoplight", "good")
    // Returns: "#4CAF50"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Color.PerformanceTheme' =
        (
            themeName: STRING,
            variant: STRING
        ) =>
            
            VAR Themes =
                DATATABLE(
                "ThemeName", STRING,
                "Variant", STRING,
                "Color", STRING,
                {
                    // Stoplight - Classic red/yellow/green
                    {"Stoplight", "veryBad",  "#D04848"}, // Red
                    {"Stoplight", "bad",      "#F07857"}, // Orange-red
                    {"Stoplight", "neutral",  "#FFBF49"}, // Amber
                    {"Stoplight", "good",     "#4CAF50"}, // Green
                    {"Stoplight", "veryGood", "#2E8B57"}, // Sea green
                    
                    // Colorblind-friendly
                    {"Colorblind", "veryBad",  "#8F2D56"}, // Wine red
                    {"Colorblind", "bad",      "#D95980"}, // Light raspberry
                    {"Colorblind", "neutral",  "#FFC857"}, // Yellow
                    {"Colorblind", "good",     "#41B3A3"}, // Teal
                    {"Colorblind", "veryGood", "#1D4E89"}, // Navy blue
                    
                    // Corporate - Blue theme for business use
                    {"Corporate", "veryBad",  "#BC2F4A"}, // Red accent
                    {"Corporate", "bad",      "#E36F6F"}, // Light red
                    {"Corporate", "neutral",  "#BDBDBD"}, // Gray
                    {"Corporate", "good",     "#6BB5D8"}, // Light blue
                    {"Corporate", "veryGood", "#114D85"}, // Dark blue
                    
                    // Pastel - Soft colors for gentler visualization
                    {"Pastel", "veryBad",  "#F8AFA6"}, // Soft red
                    {"Pastel", "bad",      "#FAD48E"}, // Soft orange
                    {"Pastel", "neutral",  "#F5F5F5"}, // Light gray
                    {"Pastel", "good",     "#A6DCEF"}, // Soft blue
                    {"Pastel", "veryGood", "#A6E4D0"}, // Soft green
                    
                    // Grayscale - For black and white or muted presentations
                    {"Grayscale", "veryBad",  "#4D4D4D"}, // Dark gray
                    {"Grayscale", "bad",      "#7D7D7D"}, // Gray
                    {"Grayscale", "neutral",  "#ADADAD"}, // Medium gray
                    {"Grayscale", "good",     "#D3D3D3"}, // Light gray
                    {"Grayscale", "veryGood", "#F9F9F9"}  // Near white
                }
            )

            VAR _variant = 		IF( ISBLANK( variant ), "neutral", variant )
            VAR _themeName = 	IF( ISBLANK( themeName ), "Stoplight", themeName )
            
            VAR SelectedColor =
                MAXX(
                    FILTER( Themes, [Variant] = _variant && [ThemeName] = _themeName),
                    [Color]
                )
    ```