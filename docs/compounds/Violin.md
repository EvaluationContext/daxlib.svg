---
comments: true
---

# Compound.Violin

Generates a Violin Plot compound SVG Visual showing distribution density using Kernel Density Estimation (KDE)

??? info "Kernel Density Estimation (KDE)"

    KDE creates a smooth estimate of your data's probability density by placing a "kernel" (normal distribution curve) at each data point and summing them together. The violin plot displays this density as a symmetrical shape - wider areas indicate higher probability/frequency of values.
    
    **Key Parameters:**

    - **Samples**: Controls the resolution of the density calculation (higher = smoother, but slower performance)

    - **Bandwidth**: Controls how much each data point influences nearby areas. Smaller bandwidth values create sharper, more detailed curves that closely follow individual data points. Larger bandwidth values create smoother, more generalized shapes that show overall trends

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><path d='M 2.5 10 L 2.5 4.89144110292255 S 3.29166666666667 1.20606972683534, 4.08333333333333 1.20606972683534 S 4.875 0.199999999999999, 5.66666666666667 0.199999999999999 S 6.45833333333333 3.9578916677529, 7.25 3.9578916677529 S 8.04166666666667 3.35479718748696, 8.83333333333333 3.35479718748696 S 9.625 3.75231256706734, 10.4166666666667 3.75231256706734 S 11.2083333333333 6.47864557826522, 12 6.47864557826522 S 12.7916666666667 6.35862127447642, 13.5833333333333 6.35862127447642 S 14.375 6.5672972843234, 15.1666666666667 6.5672972843234 S 15.9583333333333 4.54849310649522, 16.75 4.54849310649522 S 17.5416666666667 1.16650209772613, 18.3333333333333 1.16650209772613 S 19.125 5.3757903631394, 19.9166666666667 5.3757903631394 S 20.7083333333333 9.66905995631387, 21.5 9.66905995631387 S 22.2916666666667 9.99793178750071, 23.0833333333333 9.99793178750071 S 23.875 9.99999902642176, 24.6666666666667 9.99999902642176 S 25.4583333333333 9.99999999996766, 26.25 9.99999999996766 S 27.0416666666667 10, 27.8333333333333 10 S 28.625 10, 29.4166666666667 10 S 30.2083333333333 10, 31 10 S 31.7916666666667 10, 32.5833333333333 10 S 33.375 10, 34.1666666666667 10 S 34.9583333333333 10, 35.75 10 S 36.5416666666667 9.99999999999998, 37.3333333333333 9.99999999999998 S 38.125 9.99999999665713, 38.9166666666667 9.99999999665713 S 39.7083333333333 9.9999655783716, 40.5 9.9999655783716 S 41.2916666666667 9.97543586002223, 42.0833333333333 9.97543586002223 S 42.875 8.77307303854743, 43.6666666666667 8.77307303854743 S 44.4583333333333 5.67084750293614, 45.25 5.67084750293614 S 46.0416666666667 8.44264194967561, 46.8333333333333 8.44264194967561 S 47.625 7.80568388906012, 48.4166666666667 7.80568388906012 S 49.2083333333333 9.34128845336407, 50 9.34128845336407 S 50.7916666666667 9.98666021114291, 51.5833333333333 9.98666021114291 S 52.375 9.99955329547763, 53.1666666666667 9.99955329547763 S 53.9583333333333 9.90090821574378, 54.75 9.90090821574378 S 55.5416666666667 8.46781510503492, 56.3333333333333 8.46781510503492 S 57.125 8.41494231840535, 57.9166666666667 8.41494231840535 S 58.7083333333333 9.78199123696239, 59.5 9.78199123696239 S 60.2916666666667 8.42065653068517, 61.0833333333333 8.42065653068517 S 61.875 8.46200902219531, 62.6666666666667 8.46200902219531 S 63.4583333333333 9.89979384836692, 64.25 9.89979384836692 S 65.0416666666667 9.99956332427697, 65.8333333333333 9.99956332427697 S 66.625 9.99999987272364, 67.4166666666667 9.99999987272364 S 68.2083333333333 9.99999999999752, 69 9.99999999999752 S 69.7916666666667 10, 70.5833333333333 10 S 71.375 10, 72.1666666666667 10 S 72.9583333333333 10, 73.75 10 S 74.5416666666667 10, 75.3333333333333 10 S 76.125 10, 76.9166666666667 10 S 77.7083333333333 10, 78.5 10 S 79.2916666666667 10, 80.0833333333333 10 S 80.875 10, 81.6666666666667 10 S 82.4583333333333 10, 83.25 10 S 84.0416666666667 10, 84.8333333333333 10 S 85.625 10, 86.4166666666667 10 S 87.2083333333333 10, 88 10 S 88.7916666666667 9.99999999999999, 89.5833333333333 9.99999999999999 S 90.375 9.99999999912476, 91.1666666666667 9.99999999912476 S 91.9583333333333 9.99998868920325, 92.75 9.99998868920325 S 93.5416666666667 9.990223506012, 94.3333333333333 9.990223506012 S 95.125 9.43480657495187, 95.9166666666667 9.43480657495187 S 96.7083333333333 7.81457911631953, 97.5 7.81457911631953 S 98.2916666666667 9.43480657495187, 99.0833333333333 9.43480657495187 S 98.2916666666667 10.5651934250481, 99.0833333333333 10.5651934250481 S 96.7083333333333 12.1854208836805, 97.5 12.1854208836805 S 95.125 10.5651934250481, 95.9166666666667 10.5651934250481 S 93.5416666666667 10.009776493988, 94.3333333333333 10.009776493988 S 91.9583333333333 10.0000113107968, 92.75 10.0000113107968 S 90.375 10.0000000008752, 91.1666666666667 10.0000000008752 S 88.7916666666667 10, 89.5833333333333 10 S 87.2083333333333 10, 88 10 S 85.625 10, 86.4166666666667 10 S 84.0416666666667 10, 84.8333333333333 10 S 82.4583333333333 10, 83.25 10 S 80.875 10, 81.6666666666667 10 S 79.2916666666667 10, 80.0833333333333 10 S 77.7083333333333 10, 78.5 10 S 76.125 10, 76.9166666666667 10 S 74.5416666666667 10, 75.3333333333333 10 S 72.9583333333333 10, 73.75 10 S 71.375 10, 72.1666666666667 10 S 69.7916666666667 10, 70.5833333333333 10 S 68.2083333333333 10.0000000000025, 69 10.0000000000025 S 66.625 10.0000001272764, 67.4166666666667 10.0000001272764 S 65.0416666666667 10.000436675723, 65.8333333333333 10.000436675723 S 63.4583333333333 10.1002061516331, 64.25 10.1002061516331 S 61.875 11.5379909778047, 62.6666666666667 11.5379909778047 S 60.2916666666667 11.5793434693148, 61.0833333333333 11.5793434693148 S 58.7083333333333 10.2180087630376, 59.5 10.2180087630376 S 57.125 11.5850576815946, 57.9166666666667 11.5850576815946 S 55.5416666666667 11.5321848949651, 56.3333333333333 11.5321848949651 S 53.9583333333333 10.0990917842562, 54.75 10.0990917842562 S 52.375 10.0004467045224, 53.1666666666667 10.0004467045224 S 50.7916666666667 10.0133397888571, 51.5833333333333 10.0133397888571 S 49.2083333333333 10.6587115466359, 50 10.6587115466359 S 47.625 12.1943161109399, 48.4166666666667 12.1943161109399 S 46.0416666666667 11.5573580503244, 46.8333333333333 11.5573580503244 S 44.4583333333333 14.3291524970639, 45.25 14.3291524970639 S 42.875 11.2269269614526, 43.6666666666667 11.2269269614526 S 41.2916666666667 10.0245641399778, 42.0833333333333 10.0245641399778 S 39.7083333333333 10.0000344216284, 40.5 10.0000344216284 S 38.125 10.0000000033429, 38.9166666666667 10.0000000033429 S 36.5416666666667 10, 37.3333333333333 10 S 34.9583333333333 10, 35.75 10 S 33.375 10, 34.1666666666667 10 S 31.7916666666667 10, 32.5833333333333 10 S 30.2083333333333 10, 31 10 S 28.625 10, 29.4166666666667 10 S 27.0416666666667 10, 27.8333333333333 10 S 25.4583333333333 10.0000000000323, 26.25 10.0000000000323 S 23.875 10.0000009735782, 24.6666666666667 10.0000009735782 S 22.2916666666667 10.0020682124993, 23.0833333333333 10.0020682124993 S 20.7083333333333 10.3309400436861, 21.5 10.3309400436861 S 19.125 14.6242096368606, 19.9166666666667 14.6242096368606 S 17.5416666666667 18.8334979022739, 18.3333333333333 18.8334979022739 S 15.9583333333333 15.4515068935048, 16.75 15.4515068935048 S 14.375 13.4327027156766, 15.1666666666667 13.4327027156766 S 12.7916666666667 13.6413787255236, 13.5833333333333 13.6413787255236 S 11.2083333333333 13.5213544217348, 12 13.5213544217348 S 9.625 16.2476874329327, 10.4166666666667 16.2476874329327 S 8.04166666666667 16.645202812513, 8.83333333333333 16.645202812513 S 6.45833333333333 16.0421083322471, 7.25 16.0421083322471 S 4.875 19.8, 5.66666666666667 19.8 S 3.29166666666667 18.7939302731647, 4.08333333333333 18.7939302731647 S 1.25 15.1085588970775, 2.5 15.1085588970775 Z' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Violin( x, y, width, height, paddingX, paddingY, axisRef, measureRef, samples, bandwidth, color )
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
    | samples | <span class="type-label int64">INT64</span> | :material-check: | Number of density calculation points |
    | bandwidth | <span class="type-label number">NUMERIC</span> | :material-check: | Kernel bandwidth for smoothing |
    | color | <span class="type-label string">STRING</span> | :material-check: | Fill color for the violin shape |

    <span class="type-label string">**STRING**</span> An SVG violin plot showing the probability density of data using kernel density estimation

=== "Example"

    ```dax hl_lines="5-20"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Violin(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            0.05,               // paddingX
            0.02,               // paddingY
            Dates[Date],        // axisRef
            [Total Cost],       // measureVal
            MAX( Samples[Samples] ), // samples
            MAX( Bandwidth[Bandwidth] ), // bandwidth
            DaxLib.SVG.Colour.Theme(
                "Power BI",
                25
            )                   // color
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Violin' =
        (
            x: INT64,
            y: INT64,
            width: INT64,
            height: INT64,
            paddingX: DOUBLE,
            paddingY: DOUBLE,
            axisRef: ANYREF EXPR,
            measureRef: NUMERIC EXPR,
            samples: INT64,
            bandwidth: NUMERIC,
            color: STRING
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

            VAR _NumValues = 		COUNTROWS( _Data )
            VAR _Min = 				MINX( _Data, [@Value] )
            VAR _Max = 				MAXX( _Data, [@Value] )
            VAR _Range = 			_Max - _Min
            VAR _RangePerSample = 	_Range / samples

            // Calculate Kernel Density Estimation using Normal distribution
            VAR _KDE = 
                ADDCOLUMNS(
                    GENERATESERIES( 0, samples + 1, 1 ),
                    "@InputX", _Min + _RangePerSample * [Value],
                    "@KDE", 
                        ( 1 / _NumValues ) * 
                        SUMX(
                            _Data, 
                            NORM.DIST( 
                                _Min + _RangePerSample * [Value], 
                                [@Value], 
                                bandwidth, 
                                FALSE 
                            ) 
                        )
                )

            VAR _MaxKDE = 		MAXX( _KDE, [@KDE] )

            // Map KDE values to SVG coordinates using normalize function
            VAR _Points = 
                ADDCOLUMNS(
                    _KDE,
                    "@X", DaxLib.SVG.Scale.Normalize( [@InputX], _Min, _Max, _X, _X + _Width),
                    "@Y", DaxLib.SVG.Scale.Normalize( [@KDE], 0, _MaxKDE, _Y + _Height * 0.5, _Y )
                )

            // Create control points for smooth Bézier curves
            VAR _PointsWithPrev = 
                NATURALLEFTOUTERJOIN(
                    _Points,
                    SELECTCOLUMNS(
                        _Points,
                        "Value", [Value] + 1,
                        "@PrevX", [@X],
                        "@PrevY", [@Y]
                    )
                )

            VAR _WithControlPoints = 
                ADDCOLUMNS(
                    _PointsWithPrev,
                    "@CX", [@prevX] + ( ( [@x] - [@prevX] ) / 2 ),
                    "@CY", [@y]
                )

            // Create the violin shape as a single closed path
            // Start at the center-left, go up the top curve, then down the bottom curve, and close
            VAR _FirstPoint = MINX( _Points, [@X] )
            VAR _LastPoint = MAXX( _Points, [@X] )
            VAR _CenterY = _Y + (_Height * 0.5)

            // Top half curve (from left to right)
            VAR _TopCurve = 
                CONCATENATEX(
                    _WithControlPoints,
                    IF(
                        [Value] = 0,
                        "M " & [@X] & " " & _CenterY & " L " & [@X] & " " & [@Y],
                        "S " & [@CX] & " " & [@CY] & ", " & [@X] & " " & [@Y]
                    ),
                    " ",
                    [Value],
                    ASC
                )

            // Bottom half curve (from right to left, mirrored)
            VAR _BottomCurve = 
                CONCATENATEX(
                    _WithControlPoints,
                    VAR _MirroredY = _CenterY + (_CenterY - [@Y])
                    VAR _MirroredCY = _CenterY + (_CenterY - [@CY])
                    RETURN
                        "S " & [@CX] & " " & _MirroredCY & ", " & [@X] & " " & _MirroredY,
                    " ",
                    [Value],
                    DESC
                )

            // Create a single closed path for the violin shape
            VAR _ViolinPath = 
                _TopCurve & 
                " " & _BottomCurve & 
                " Z" // Close the path

            // Combined Elements
            VAR _CombinedElements = 
                DaxLib.SVG.Element.Paths(
                    _ViolinPath, // d
                    DaxLib.SVG.Attr.Shapes(
                        color,          // fill
                        0.5,          	// fillOpacity
                        BLANK(),        // fillRule
                        color,          // stroke
                        1,              // strokeWidth
                        BLANK(),        // strokeOpacity
                        BLANK()         // opacity
                    ),
                    BLANK()             // transforms
                )

            RETURN

                IF( NOT ISEMPTY( _Data ), _CombinedElements )
    ```