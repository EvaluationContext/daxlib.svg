---
comments: true
---

# Compound.Jitter

Generates a Jitter Plot compound SVG Visual showing values as points with x-position based on value and y-position jittered around center

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><circle cx='2.98846880907372' cy='6.5112' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='6.5226843100189' cy='5.51748' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='4.51134215500945' cy='7.3638' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='9.53969754253308' cy='5.44888' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='18.0160680529301' cy='14.45508' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='8.33289224952741' cy='12.86748' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='6.01984877126654' cy='5.63508' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='45.3415879017013' cy='8.70836' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='15.0708884688091' cy='11.18188' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='19.3952741020794' cy='9.94708' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='19.093572778828' cy='12.31868' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='11.0338374291115' cy='12.71068' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='45.6181474480151' cy='5.62871' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='18.2459357277883' cy='7.51668' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='19.8478260869565' cy='14.07778' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='8.53402646502835' cy='7.75188' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='62.0429111531191' cy='9.20326' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='3.47693761814745' cy='6.815' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='57.3521739130435' cy='6.95416' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='11.9820415879017' cy='5.60568' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='10.4196597353497' cy='8.32763' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='5.40207939508507' cy='12.95568' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='16.9565217391304' cy='11.66943' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='97.5' cy='8.11546' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='6.29281663516068' cy='8.50648' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='14.0652173913043' cy='8.27128' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='4.94234404536862' cy='7.50688' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='48.7608695652174' cy='8.74756' r='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1' stroke-opacity='0.9'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Jitter( x, y, width, height, paddingX, paddingY, axisRef, measureRef, pointColor, jitterAmount )
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
    | pointColor | <span class="type-label string">STRING</span> | :material-check: | The Hex color of the points (e.g., "#01B8AA") |
    | jitterAmount | <span class="type-label number">DOUBLE</span> | :material-close: | The amount of y-axis jitter as a percentage of height (0.0-1.0, defaults to 0.3) |

    <span class="type-label string">**STRING**</span> An SVG jitter plot showing data points with horizontal positioning based on values and vertical jittering for visibility

=== "Example"

    ```dax hl_lines="5-19"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Jitter(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            0.05,               // paddingX
            0.02,               // paddingY
            Dates[Date],        // xAxis
            [Total Cost],       // measureRef
            DaxLib.SVG.Colour.Theme(
                "Power BI",
                25
            )                   // pointColour
            0.5                 // jitterAmount
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Jitter' = 
        (
            x: INT64,
            y: INT64,
            width: INT64,
            height: INT64,
            paddingX: DOUBLE,
            paddingY: DOUBLE,
            axisRef: ANYREF EXPR,
            measureRef: NUMERIC EXPR,
            pointColor: STRING,
            jitterAmount: DOUBLE
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
                    
            VAR _RawXMin = 	MINX( _Data, [@Value] )
            VAR _XMin = 	IF( _RawXMin > 0, 0, _RawXMin )
            VAR _XMax = 	MAXX( _Data, [@Value] )
        
            // Points
            VAR _CenterY = 		_Y + _Height * 0.5
            VAR _JitterRange = 	_Height * IF( ISBLANK( jitterAmount ), 0.3, jitterAmount )
            VAR _CircleElements = 
                CONCATENATEX(
                    _Data,
                    IF( 
                        NOT ISBLANK( [@Value] ),
                        VAR _Seed = 		ABS( [@Value] * 12345 ) + ABS( [@AxisIndex] * 67890 ) + ABS( LEN( FORMAT( [@Value], "0.000000" ) ) * 9876 )
                        VAR _PseudoRandom = MOD( _Seed, 10000 ) / 10000
                        VAR _JitterY = 		_CenterY + ( _PseudoRandom - 0.5 ) * _JitterRange
                        VAR _ClampedY = 	MAX( _Y, MIN( _Y + _Height, _JitterY ) )
                        RETURN
                            DaxLib.SVG.Element.Circle(
                                DaxLib.SVG.Scale.Normalize( [@Value], _XMin, _XMax, _X, _X + _Width ), // cx
                                _ClampedY,          // cy
                                2,         			// r
                                DaxLib.SVG.Attr.Shapes(
                                    pointColor,   	// fill
                                    0.5,            // fillOpacity
                                    BLANK(),        // fillRule
                                    pointColor,   	// stroke
                                    1,              // strokeWidth
                                    0.9,            // strokeOpacity
                                    BLANK()         // opacity
                                ),
                                BLANK()             // transforms
                            )
                    ),
                    " ",
                    [@AxisIndex],
                    ASC
                )

            RETURN
                
                IF( NOT ISEMPTY( _Data ), _CircleElements )
    ```