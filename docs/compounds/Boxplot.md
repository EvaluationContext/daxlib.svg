---
comments: true
---

# Compound.Boxplot

Generates a Box Plot compound SVG Visual showing statistical distribution

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><line x1='2.5' y1='10' x2='5.99471764079957' y2='10' stroke='#EC008C' stroke-width='1'  /><line x1='19.105324162043' y1='10' x2='38.7712339439082' y2='10' stroke='#EC008C' stroke-width='1'  /><line x1='2.5' y1='4.12' x2='2.5' y2='15.88' stroke='#EC008C' stroke-width='1'  /><line x1='38.7712339439082' y1='4.12' x2='38.7712339439082' y2='15.88' stroke='#EC008C' stroke-width='1'  /><rect x='5.99471764079957' y='4.12' width='13.1106065212434' height='11.76' rx='2' ry='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1'  /><line x1='12.5870259177624' y1='4.12' x2='12.5870259177624' y2='15.88' stroke='#EC008C' stroke-width='2'  /><circle cx='48.5089686098655' cy='10' r='2' fill='#EC008C'  /><circle cx='61.8596564566391' cy='10' r='2' fill='#EC008C'  /><circle cx='45.3500038002584' cy='10' r='2' fill='#EC008C'  /><circle cx='45.072014897013' cy='10' r='2' fill='#EC008C'  /><circle cx='97.5' cy='10' r='2' fill='#EC008C'  /><circle cx='57.144675837957' cy='10' r='2' fill='#EC008C'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Boxplot( x, y, width, height, paddingX, paddingY, axisRef, measureRef, fillColor, strokeColor, showOutliers )
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
    | fillColor | <span class="type-label string">STRING</span> | :material-check: | Color for the box fill |
    | strokeColor | <span class="type-label string">STRING</span> | :material-check: | Color for lines, whiskers, and median |
    | showOutliers | <span class="type-label boolean">BOOLEAN</span> | :material-close: | Whether to show outlier points beyond whiskers |

    <span class="type-label string">**STRING**</span> An SVG box plot showing statistical distribution including quartiles, median, whiskers, and optionally outliers

=== "Example"

    ```dax hl_lines="5-23"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Boxplot(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            0.05,               // paddingX
            0.02,               // paddingY
            Dates[Date],        // axisRef
            [Total Cost],       // measureVal
            DaxLib.SVG.Colour.Theme(
                "Power BI",
                25
            ),                  // fillColour
            DaxLib.SVG.Colour.Theme(
                "Power BI",
                25
            ),                  // strokeColour
            TRUE                // showOutliers
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Boxplot' =
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
            strokeColor: STRING,
            showOutliers: BOOLEAN
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

            VAR _XMin = 			MINX( _Data, [@Value] )
            VAR _XMax = 			MAXX( _Data, [@Value] )

            VAR _Count = 			COUNTROWS( _Data )
            VAR _Min = 				MINX( _Data, [@Value] )
            VAR _Max = 				MAXX( _Data, [@Value] )

            // Calculate quartiles using standard definitions
            VAR _Q1 = 				PERCENTILEX.INC( _Data, [@Value], 0.25 )
            VAR _Median = 			PERCENTILEX.INC( _Data, [@Value], 0.5 )
            VAR _Q3 = 				PERCENTILEX.INC( _Data, [@Value], 0.75 )

            // Calculate IQR and whisker boundaries (1.5 * IQR rule)
            VAR _IQR = 				_Q3 - _Q1
            VAR _LowerWhisker =		MAX( _Min, _Q1 - 1.5 * _IQR )
            VAR _UpperWhisker = 	MIN( _Max, _Q3 + 1.5 * _IQR )

            // Scale statistical values to SVG coordinates
            VAR _Q1X = 				DaxLib.SVG.Scale.Normalize( _Q1, _XMin, _XMax, _X, _X + _Width )
            VAR _MedianX = 			DaxLib.SVG.Scale.Normalize( _Median, _XMin, _XMax, _X, _X + _Width )
            VAR _Q3X = 				DaxLib.SVG.Scale.Normalize( _Q3, _XMin, _XMax, _X, _X + _Width )
            VAR _LowerWhiskerX = 	DaxLib.SVG.Scale.Normalize( _LowerWhisker, _XMin, _XMax, _X, _X + _Width )
            VAR _UpperWhiskerX = 	DaxLib.SVG.Scale.Normalize( _UpperWhisker, _XMin, _XMax, _X, _X + _Width )

            // Box dimensions - centered vertically with padding
            VAR _BoxHeight = 		_Height * 0.6
            VAR _BoxY = 			_Y + _Height * 0.2
            VAR _CenterY = 			_Y + _Height * 0.5

            // Create outlier points beyond whiskers if enabled
            VAR _Outliers = 
                IF(
                    showOutliers,
                    CONCATENATEX(
                        FILTER(
                            _Data,
                            [@Value] < _LowerWhisker || [@Value] > _UpperWhisker
                        ),
                        DaxLib.SVG.Element.Circle(
                            DaxLib.SVG.Scale.Normalize( [@Value], _XMin, _XMax, _X, _X + _Width ), // cx
                            _CenterY,          	// cy
                            2,                  // radius
                            DaxLib.SVG.Attr.Shapes(
                                strokeColor,    // fill
                                BLANK(),        // fillOpacity
                                BLANK(),        // fillRule
                                BLANK(),        // stroke
                                BLANK(),        // strokeWidth
                                BLANK(),        // strokeOpacity
                                BLANK()         // opacity
                            ),
                            BLANK()             // transforms
                        ),
                        ""
                    )
                )
            
            // Lower whisker line from whisker to Q1 (horizontal)
            VAR _LowerWhiskerLine = 
                DaxLib.SVG.Element.Line(
                    _LowerWhiskerX,         // x1
                    _CenterY,              	// y1
                    _Q1X,                   // x2
                    _CenterY,              	// y2
                    DaxLib.SVG.Attr.Shapes(
                        BLANK(),            // fill
                        BLANK(),            // fillOpacity
                        BLANK(),            // fillRule
                        strokeColor,        // stroke
                        1,                  // strokeWidth
                        BLANK(),            // strokeOpacity
                        BLANK()             // opacity
                    ),
                    BLANK()                 // transforms
                )

            // Upper whisker line from Q3 to whisker (horizontal)
            VAR _UpperWhiskerLine = 
                DaxLib.SVG.Element.Line(
                    _Q3X,                   // x1
                    _CenterY,             	// y1
                    _UpperWhiskerX,         // x2
                    _CenterY,             	// y2
                    DaxLib.SVG.Attr.Shapes(
                        BLANK(),            // fill
                        BLANK(),            // fillOpacity
                        BLANK(),            // fillRule
                        strokeColor,        // stroke
                        1,                  // strokeWidth
                        BLANK(),            // strokeOpacity
                        BLANK()             // opacity
                    ),
                    BLANK()                 // transforms
                )

            // Lower whisker cap (vertical line)
            VAR _LowerCap = 
                DaxLib.SVG.Element.Line(
                    _LowerWhiskerX,         // x1
                    _BoxY,                  // y1
                    _LowerWhiskerX,         // x2
                    _BoxY + _BoxHeight,     // y2
                    DaxLib.SVG.Attr.Shapes(
                        BLANK(),            // fill
                        BLANK(),            // fillOpacity
                        BLANK(),            // fillRule
                        strokeColor,        // stroke
                        1,                  // strokeWidth
                        BLANK(),            // strokeOpacity
                        BLANK()             // opacity
                    ),
                    BLANK()                 // transforms
                )

            // Upper whisker cap (vertical line)
            VAR _UpperCap = 
                DaxLib.SVG.Element.Line(
                    _UpperWhiskerX,         // x1
                    _BoxY,                  // y1
                    _UpperWhiskerX,         // x2
                    _BoxY + _BoxHeight,     // y2
                    DaxLib.SVG.Attr.Shapes(
                        BLANK(),            // fill
                        BLANK(),            // fillOpacity
                        BLANK(),            // fillRule
                        strokeColor,        // stroke
                        1,                  // strokeWidth
                        BLANK(),            // strokeOpacity
                        BLANK()             // opacity
                    ),
                    BLANK()                 // transforms
                )

            // Main box (Q1 to Q3) - horizontal
            VAR _Box = 
                DaxLib.SVG.Element.Rect(
                    _Q1X,                   // x (left of box)
                    _BoxY,                  // y
                    _Q3X - _Q1X,            // width (Q3 - Q1)
                    _BoxHeight,             // height
                    2,                      // rx
                    2,                      // ry
                    DaxLib.SVG.Attr.Shapes(
                        fillColor,          // fill
                        0.5,                // fillOpacity
                        BLANK(),            // fillRule
                        strokeColor,        // stroke
                        1,                  // strokeWidth
                        BLANK(),            // strokeOpacity
                        BLANK()             // opacity
                    ),
                    BLANK()                 // transforms
                )

            // Median line (vertical)
            VAR _MedianLine = 
                DaxLib.SVG.Element.Line(
                    _MedianX,               // x1
                    _BoxY,                  // y1
                    _MedianX,               // x2
                    _BoxY + _BoxHeight,     // y2
                    DaxLib.SVG.Attr.Shapes(
                        BLANK(),            // fill
                        BLANK(),            // fillOpacity
                        BLANK(),            // fillRule
                        strokeColor,        // stroke
                        2,                  // strokeWidth (thicker for median)
                        BLANK(),            // strokeOpacity
                        BLANK()             // opacity
                    ),
                    BLANK()                 // transforms
                )

            // Combined elements
            VAR _CombinedElements = 
                _LowerWhiskerLine &
                _UpperWhiskerLine &
                _LowerCap &
                _UpperCap &
                _Box &
                _MedianLine &
                _Outliers

            RETURN

                IF( NOT ISEMPTY( _Data ), _CombinedElements )
    ```