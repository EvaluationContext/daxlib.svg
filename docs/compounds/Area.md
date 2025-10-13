---
comments: true
---

# Compound.Area

Generates an Area compound SVG Visual

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><polygon points='2.5,19.8 2.5,19.6992211720227 4.11016949152542,18.970056710775 10.5508474576271,19.3850283553875 15.3813559322034,18.3475992438563 16.9915254237288,16.5987901701323 23.4322033898305,18.5965822306238 25.0423728813559,19.0737996219282 29.8728813559322,10.9611039697543 31.4830508474576,17.206427221172 36.3135593220339,16.3142381852552 37.9237288135593,16.3764839319471 42.7542372881356,18.0393345935728 44.364406779661,10.90404536862 49.1949152542373,16.5513648393195 50.8050847457627,16.2208695652174 55.635593220339,18.5550850661626 57.2457627118644,7.5153572778828 62.0762711864407,19.5984423440454 63.6864406779661,8.48313043478261 70.1271186440678,17.8437051039698 71.7372881355932,18.1660491493384 76.5677966101695,19.2012551984877 78.1779661016949,16.8173913043478 84.6186440677966,0.199999999999999 89.4491525423729,19.0174820415879 91.0593220338983,17.4139130434783 95.8898305084746,19.2961058601134 97.5,10.255652173913 97.5,19.8' fill='#EC008C' fill-opacity='0.2' stroke='none' stroke-width='0'  /><polyline points='2.5,19.6992211720227 4.11016949152542,18.970056710775 10.5508474576271,19.3850283553875 15.3813559322034,18.3475992438563 16.9915254237288,16.5987901701323 23.4322033898305,18.5965822306238 25.0423728813559,19.0737996219282 29.8728813559322,10.9611039697543 31.4830508474576,17.206427221172 36.3135593220339,16.3142381852552 37.9237288135593,16.3764839319471 42.7542372881356,18.0393345935728 44.364406779661,10.90404536862 49.1949152542373,16.5513648393195 50.8050847457627,16.2208695652174 55.635593220339,18.5550850661626 57.2457627118644,7.5153572778828 62.0762711864407,19.5984423440454 63.6864406779661,8.48313043478261 70.1271186440678,17.8437051039698 71.7372881355932,18.1660491493384 76.5677966101695,19.2012551984877 78.1779661016949,16.8173913043478 84.6186440677966,0.199999999999999 89.4491525423729,19.0174820415879 91.0593220338983,17.4139130434783 95.8898305084746,19.2961058601134 97.5,10.255652173913' fill='none' stroke='#EC008C' stroke-width='1'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Area( x, y, width, height, paddingX, paddingY, axisRef, measureRef, fillColor, fillOpacity, strokeColor )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | x | <span class="type-label int64">INT64</span> | :material-check: | The x position of the compound |
    | y | <span class="type-label int64">INT64</span> | :material-check: | The y position of the compound |
    | width | <span class="type-label int64">INT64</span> | :material-check: | The width of the compound |
    | height | <span class="type-label int64">INT64</span> | :material-check: | The height of the compound |
    | paddingX | <span class="type-label number">DOUBLE</span> | :material-close: | The horizontal padding percentage (0.0-1.0, e.g., 0.1 = 10% padding) |
    | paddingY | <span class="type-label number">DOUBLE</span> | :material-close: | The vertical padding percentage (0.0-1.0, e.g., 0.1 = 10% padding) |
    | axisRef | <span class="type-label anyref">ANYREF</span> <span class="type-label expr">EXPR</span> | :material-check: | The column that the measure will be evaluated against |
    | measureRef | <span class="type-label numeric">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: | The measure to evaluate |
    | fillColor | <span class="type-label string">STRING</span> | :material-check: | The color of the area fill (e.g., "#01B8AA") |
    | fillOpacity | <span class="type-label number">NUMERIC</span> | :material-close: | The opacity of the fill (0-1), defaults to 0.3 |
    | strokeColor | <span class="type-label string">STRING</span> | :material-check: | The color of the stroke line |

    <span class="type-label string">**STRING**</span> An SVG area chart element that visualizes the measure across the specified axis with filled area

=== "Example"

    ```dax hl_lines="5-23"
        DaxLib.SVG.SVG(
            500,
            100,
            BLANK(),
            DaxLib.SVG.Compound.Area(
                0,              // x
                0,              // y
                500,            // width
                100,            // height
                0.05,           // paddingX
                0.02,           // paddingY
                Dates[Date],    // xAxis
                [Total Cost],   // measureVal
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                ),              // fillColour
                0.2,            // fillOpacity
                DaxLib.SVG.Colour.Theme(
                    "Power BI",
                    25
                )               // strokeColour
            ),
            BLANK()
        )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Area' =
        (
            x: INT64,
            y: INT64,
            width: INT64,
            height: INT64,
            paddingX: DOUBLE,
            paddingY: DOUBLE,
            axisRef: ANYREF EXPR,
            measureRef: NUMERIC EXPR,
            fillColor: STRING,
            fillOpacity: NUMERIC,
            strokeColor: STRING
        ) =>

            // Apply padding to dimensions
            VAR _X = 			x + (width * (IF(ISBLANK(paddingX), 0, paddingX) / 2))
            VAR _Y = 			y + (height * (IF(ISBLANK(paddingY), 0, paddingY) / 2))
            VAR _Width = 		width * (1 - IF(ISBLANK(paddingX), 0, paddingX))
            VAR _Height = 		height * (1 - IF(ISBLANK(paddingY), 0, paddingY))
        
            // Check if Axis is numeric
            VAR axisSample = 	MAX( axisRef )
            VAR axisIsNumeric = ISNUMERIC( axisSample ) || ISDATETIME( axisSample )
            
            // For totals
            VAR _Data = 
                ADDCOLUMNS(
                    FILTER(
                        VALUES( axisRef ),
                        NOT ISBLANK( measureRef )
                    ),
                    "@AxisIndex", 	
                        IF(
                            axisIsNumeric,
                            axisRef,
                            RANK( DENSE, CALCULATETABLE( VALUES( axisRef ), ALLSELECTED() ) )
                        ),
                    "@Value", measureRef
                )
            
            VAR _XMin = 	MINX( _Data, [@AxisIndex] )
            VAR _XMax = 	MAXX( _Data, [@AxisIndex] )
            VAR _RawYMin = 	MINX( _Data, [@Value] )
            VAR _YMin = 	IF( _RawYMin > 0, 0, _RawYMin )
            VAR _YMax = 	MAXX( _Data, [@Value] )

            // Calculate baseline Y position (for zero line or bottom)
            VAR _BaselineY = DaxLib.SVG.Scale.Normalize( _YMin, _YMin, _YMax, _Y + _Height, _Y )

            // Get first and last X positions
            VAR _FirstX = 
                MINX(
                    FILTER( _Data, NOT ISBLANK( [@Value] ) ),
                    DaxLib.SVG.Scale.Normalize( [@AxisIndex], _XMin, _XMax, _X, _X + _Width )
                )
            
            VAR _LastX = 
                MAXX(
                    FILTER( _Data, NOT ISBLANK( [@Value] ) ),
                    DaxLib.SVG.Scale.Normalize( [@AxisIndex], _XMin, _XMax, _X, _X + _Width )
                )

            // Generate points for the area polygon
            // Start at baseline (bottom left), go up the data line, then back down to baseline
            VAR _PolygonPoints = 
                // Start at first X position at baseline
                _FirstX & "," & _BaselineY
                // Add all the data points (the top line)
                & " " & 
                CONCATENATEX(
                    _Data,
                    IF( 
                        NOT ISBLANK( [@Value] ), 
                        COMBINEVALUES( 
                            ",", 
                            DaxLib.SVG.Scale.Normalize( [@AxisIndex], _XMin, _XMax, _X, _X + _Width ), 
                            DaxLib.SVG.Scale.Normalize( [@Value], _YMin, _YMax, _Y + _Height, _Y )
                        )
                    ),
                    " ",
                    [@AxisIndex],
                    ASC
                )
                // End at last X position at baseline
                & " " & _LastX & "," & _BaselineY

            // Generate points for just the top line (for optional stroke)
            VAR _TopPoints = 
                CONCATENATEX(
                    _Data,
                    IF( 
                        NOT ISBLANK( [@Value] ), 
                        COMBINEVALUES( 
                            ",", 
                            DaxLib.SVG.Scale.Normalize( [@AxisIndex], _XMin, _XMax, _X, _X + _Width ), 
                            DaxLib.SVG.Scale.Normalize( [@Value], _YMin, _YMax, _Y + _Height, _Y )
                        )
                    ),
                    " ",
                    [@AxisIndex],
                    ASC
                )

            // Area Element (using polygon for filled area)
            VAR _AreaElement =
                DaxLib.SVG.Element.Polygon(
                    _PolygonPoints,		// points
                    DaxLib.SVG.Attr.Shapes(
                        fillColor, 		// fill
                        IF( NOT ISBLANK( fillOpacity ), fillOpacity, 0.3 ), // fillOpacity
                        BLANK(),      	// fillRule
                        "none",         // stroke
                        0,              // strokeWidth
                        BLANK(),        // strokeOpacity
                        BLANK()         // opacity
                    ),
                    BLANK()				// transforms
                )

            // stroke line on top of the area
            VAR _StrokeElement = 
                DaxLib.SVG.Element.Polyline(
                    _TopPoints,			// points
                    DaxLib.SVG.Attr.Shapes(
                        "none",			// fill
                        BLANK(),		// fillOpacity
                        BLANK(),		// fillRule
                        strokeColor,	// stroke
                        1,				// strokeWidth
                        BLANK(),		// strokeOpacity
                        BLANK()			// opacity
                    ),
                    BLANK()				// transforms
                )
            
            // Circle if only one point
            VAR _SinglePointElement =
                DaxLib.SVG.Element.Circle(
                        DaxLib.SVG.Scale.Normalize( MAXX( _Data, [@AxisIndex] ), _XMin, _XMax, _X, _X + _Width ), // cx
                        DaxLib.SVG.Scale.Normalize( MAXX( _Data, [@Value] ), _YMin, _YMax, _Y + _Height, _Y ), // cy
                        2,               	// r
                        DaxLib.SVG.Attr.Shapes(
                            fillColor,     // fill
                            BLANK(),        // fillOpacity
                            BLANK(),        // fillRule
                            BLANK(),        // stroke
                            BLANK(),        // strokeWidth
                            BLANK(),        // strokeOpacity
                            BLANK()         // opacity
                        ),
                        BLANK()             // transforms
                    )

            // Combine elements
            VAR _CombinedElements = 
                IF(
                    COUNTROWS( _Data ) = 1,
                    _SinglePointElement,
                    _AreaElement &
                    _StrokeElement
                )

            RETURN
            
                IF( NOT ISEMPTY( _Data ), _CombinedElements )
    ```