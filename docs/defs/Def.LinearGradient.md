# Def.LinearGradient

Create a linear gradient definition

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><linearGradient id='myGradient'><stop offset='20%' stop-color='#EC008C'/><stop offset='80%' stop-color='#533285'/></linearGradient></defs><rect x='2' y='2' width='80%' height='80%' fill='url("#myGradient")'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.LinearGradient( defId, stops, x1, y1, x2, y2 )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | defId | <span class="type-label string">STRING</span> | :material-check: |  | The unique identifier for the gradient |
    | stops | <span class="type-label string">STRING</span> | :material-check: |  | Concatenated list of one or more `DaxLib.SVG.Def.GradientStop` elements |
    | x1 | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Start X position |
    | y1 | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Start Y position |
    | x2 | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: End X position |
    | y2 | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: End Y position |

    <span class="type-label string">STRING</span> <linearGradient> definition

=== "Example"

    ```dax hl_lines="6-29"
    DaxLib.SVG.SVG(
        500,
        100,
        "0 0 100 20",
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.LinearGradient(
                "myGradient",   // defId
                DaxLib.SVG.Def.GradientStop(
                    "20%",      // offset
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        25
                    ),          // color
                    BLANK()     // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "80%",      // offset
                    DaxLib.SVG.Color.Theme(
                        "Power BI",
                        26
                    ),           // color
                    BLANK()     // opacity
                ),              // stops
                BLANK(),        // x1
                BLANK(),        // y1
                BLANK(),        // x2
                BLANK()         // y2
            )                   // defs
        ) &
        DaxLib.SVG.Element.Rect(
            2,                  // x
            2,                  // y
            "80%",              // width
            "80%",              // height
            BLANK(),            // rx
            BLANK(),            // ry
            DaxLib.SVG.Attr.Shapes(
                "url(""" & "#myGradient" & """)", // fill
                BLANK(),        // fillOpacity
                BLANK(),        // fillRule   
                BLANK(),        // stroke
                BLANK(),        // strokeWidth
                BLANK(),        // strokeOpacity
                BLANK()         // opacity
            ),                  // attributes
            BLANK()             // transforms
        ),
        BLANK()                 // sortValue               
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.LinearGradient' =
    		(
    			defId: STRING,
    			stops: STRING,
    			x1: STRING = BLANK(),
    			y1: STRING = BLANK(),
    			x2: STRING = BLANK(),
    			y2: STRING = BLANK()
    		) =>
    			
    			"<linearGradient" & 
    			" id='" & defId & "'" &
    			IF( NOT ISBLANK( x1 ), " x1='" & x1 & "'" ) &
    			IF( NOT ISBLANK( y1 ), " y1='" & y1 & "'" ) &
    			IF( NOT ISBLANK( x2 ), " x2='" & x2 & "'" ) &
    			IF( NOT ISBLANK( y2 ), " y2='" & y2 & "'" ) &
    			">" &
    			stops &
    			"</linearGradient>"
    ```