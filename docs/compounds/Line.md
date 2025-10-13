---
comments: true
---

# Compound.Line

Generates a Line compound SVG Visual

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><polyline points='2.5,19.5012778827977 4.11016949152542,18.7869943289225 10.5508474576271,19.1934971644612 15.3813559322034,18.1772400756144 16.9915254237288,16.4641209829868 23.4322033898305,18.4211417769376 25.0423728813559,18.8886200378072 29.8728813559322,10.9414896030246 31.4830508474576,17.0593572778828 36.3135593220339,16.1853761814745 37.9237288135593,16.2463516068053 42.7542372881356,17.8752665406427 44.364406779661,10.885595463138 49.1949152542373,16.417663516068 50.8050847457627,16.0939130434783 55.635593220339,18.3804914933837 57.2457627118644,7.56606427221172 62.0762711864407,19.4025557655955 63.6864406779661,8.51408695652174 70.1271186440678,17.683629489603 71.7372881355932,17.9993950850662 76.5677966101695,19.0134744801512 78.1779661016949,16.6782608695652 84.6186440677966,0.399999999999999 89.4491525423729,18.8334517958412 91.0593220338983,17.2626086956522 95.8898305084746,19.1063894139887 97.5,10.2504347826087' fill='none' stroke='#EC008C' stroke-width='1'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Line( x, y, width, height, paddingX, paddingY, axisRef, measureRef, lineColor )
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
    | lineColor | <span class="type-label string">STRING</span> | :material-check: | The Hex color of the line (e.g., "#01B8AA") |

    <span class="type-label string">**STRING**</span> An SVG line chart element that visualizes the measure across the specified axis.

=== "Example"

    ```dax hl_lines="5-18"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Line(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            0.05,               // paddingX
            0.04,               // paddingY
            Dates[Date],        // xAxis
            [Total Cost],       // measureVal
            DaxLib.SVG.Colour.Theme(
                "Power BI",
                25
            )                   // lineColour
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Line' =
        (
            x: INT64,
            y: INT64,
            width: INT64,
            height: INT64,
            paddingX: DOUBLE,
            paddingY: DOUBLE,
            axisRef: ANYREF EXPR,
            measureRef: NUMERIC EXPR,
            lineColor: STRING
        ) =>

            // Apply padding to dimensions
            VAR _X =            x + (width * (IF(ISBLANK(paddingX), 0, paddingX) / 2))
            VAR _Y =            y + (height * (IF(ISBLANK(paddingY), 0, paddingY) / 2))
            VAR _Width =        width * (1 - IF(ISBLANK(paddingX), 0, paddingX))
            VAR _Height =       height * (1 - IF(ISBLANK(paddingY), 0, paddingY))

            // Check if Axis is numeric
            VAR axisSample =    MAX( axisRef )
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

            // Define axis scales		
            VAR _XMin = 	MINX( _Data, [@AxisIndex] )
            VAR _XMax = 	MAXX( _Data, [@AxisIndex] )
            VAR _RawYMin = 	MINX( _Data, [@Value] )
            VAR _YMin = 	IF( _RawYMin > 0, 0, _RawYMin )
            VAR _YMax = 	MAXX( _Data, [@Value] )

            //Points
            VAR _Points = 
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

            // Line Element
            VAR _LineElement =
                DaxLib.SVG.Element.Polyline(
                    _Points,		// points
                    DaxLib.SVG.Attr.Shapes(
                        "none",		// fill
                        BLANK(),	// fillOpacity
                        BLANK(),	// fillRule
                        IF( NOT ISBLANK( lineColor ), lineColor, "#01B8AA" ), // stroke
                        1,			// stroke
                        BLANK(),	// strokeOpacity
                        BLANK()		// opacity
                    ),
                    BLANK()			// transforms
                )

            // Single Point Element
            VAR _SinglePointElement =
                DaxLib.SVG.Element.Circle(
                    DaxLib.SVG.Scale.Normalize( MAXX( _Data, [@AxisIndex] ), _XMin, _XMax, _X, _X + _Width ), // cx
                    DaxLib.SVG.Scale.Normalize( MAXX( _Data, [@Value] ), _YMin, _YMax, _Y + _Height, _Y ), // cy
                    2,           	// r
                    DaxLib.SVG.Attr.Shapes(
                        lineColor, 	// fill
                        BLANK(),    // fillOpacity
                        BLANK(),    // fillRule
                        BLANK(),    // stroke
                        BLANK(),    // strokeWidth
                        BLANK(),    // strokeOpacity
                        BLANK()     // opacity
                    ),
                    BLANK()         // transforms
                )

            // Combined elements
            VAR _CombinedElement = 
                IF(
                    COUNTROWS( _Data ) = 1,
                    _SinglePointElement,
                    _LineElement
                )

            RETURN
                
                IF( NOT ISEMPTY( _Data ), _CombinedElement )
    ```