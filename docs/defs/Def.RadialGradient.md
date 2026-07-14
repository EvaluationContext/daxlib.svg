# Def.RadialGradient

Create a radial gradient definition

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><radialGradient id='myGradient'><stop offset='10%' stop-color='#EC008C'/><stop offset='80%' stop-color='#533285' stop-opacity='0.5'/><stop offset='95%' stop-color='#99700A'/></radialGradient></defs><circle cx='50%' cy='50%' r='15' fill='url("#myGradient")'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Def.RadialGradient( defId, stops, cx, cy, r, fx, fy, fr )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | defId | <span class="type-label string">STRING</span> | :material-check: |  | The unique identifier for the gradient |
    | stops | <span class="type-label string">STRING</span> | :material-check: |  | Concatenated list of one or more `DaxLib.SVG.Def.GradientStop` elements |
    | cx | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Center X position |
    | cy | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Center Y position |
    | r | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Radius |
    | fx | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Focus X position |
    | fy | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Focus Y position |
    | fr | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Focus radius |

    <span class="type-label string">STRING</span> <radialGradient> definition

=== "Example"

    ```dax hl_lines="6-38"
    DaxLib.SVG.SVG(
        500,                    // width
        100,                    // height
        "0 0 100 20",           // viewbox
        DaxLib.SVG.Element.Defs(
            DaxLib.SVG.Def.RadialGradient(
                "myGradient",   // id
                DaxLib.SVG.Def.GradientStop( 
                    "10%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        25
                    ),          // colour
                    BLANK()     // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "80%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        26
                    ),          // colour
                    0.5         // opacity
                ) &
                DaxLib.SVG.Def.GradientStop( 
                    "95%",      // offset
                    DaxLib.SVG.Colour.Theme(
                        "Power BI",
                        27
                    ),          // colour
                    BLANK()     // opacity
                ),              // stops
                BLANK(),        // cx
                BLANK(),        // cy
                BLANK(),        // r
                BLANK(),        // fx
                BLANK(),        // fy
                BLANK()         // fr
            )
        ) &
        DaxLib.SVG.Element.Circle(
            "50%",              // cx
            "50%",              // cy
            15,                 // r
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
        ),                      // contents
        BLANK()                 // sortODer
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Def.RadialGradient' =
    		(
    			defId: STRING,
    			stops: STRING,
    			cx: STRING = BLANK(),
    			cy: STRING = BLANK(),
    			r: STRING = BLANK(),
    			fx: STRING = BLANK(),
    			fy: STRING = BLANK(),
    			fr: STRING = BLANK()
    		) =>
    
    			"<radialGradient" & 
    			" id='" & defId & "'" &
    			IF( NOT ISBLANK( cx ), " cx='" & cx & "'" ) &
    			IF( NOT ISBLANK( cy ), " cy='" & cy & "'" ) &
    			IF( NOT ISBLANK( r ),  " r='" & r & "'" ) &
    			IF( NOT ISBLANK( fx ), " fx='" & fx & "'" ) &
    			IF( NOT ISBLANK( fy ), " fy='" & fy & "'" ) &
    			IF( NOT ISBLANK( fr ), " fr='" & fr & "'" ) &
    			">" &
    			stops &
    			"</radialGradient>"
    ```