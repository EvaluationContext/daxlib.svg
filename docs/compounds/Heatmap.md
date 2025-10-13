---
comments: true
---

# Compound.Heatmap

Generates a KDE-based Heatmap compound SVG Visual using Kernel Density Estimation (KDE) for smooth color gradients

??? info "Kernel Density Estimation (KDE)"
    
    KDE is a statistical method that estimates the probability density function of your data by placing a "kernel" (typically a normal distribution) at each data point. The heatmap visualizes data density across the range, creating smooth gradients that reveal patterns and concentrations in your dataset.

    **Key Parameters:**

    - **Samples**: Controls the resolution of the density calculation (higher = smoother, but slower performance)

    - **Bandwidth**: Controls the smoothing level - smaller values create sharper peaks around data points, larger values create broader, smoother distributions

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><linearGradient id='kde-gradient' x1='0%' y1='0%' x2='100%' y2='0%'><stop offset='0%' stop-color='#F57AC3' /><stop offset='1.66666666666667%' stop-color='#EE1A98' /><stop offset='3.33333333333333%' stop-color='#EC008C' /><stop offset='5%' stop-color='#F362B8' /><stop offset='6.66666666666667%' stop-color='#F252B1' /><stop offset='8.33333333333333%' stop-color='#F35CB6' /><stop offset='10%' stop-color='#F8A3D6' /><stop offset='11.6666666666667%' stop-color='#F8A0D4' /><stop offset='13.3333333333333%' stop-color='#F8A6D7' /><stop offset='15%' stop-color='#F471BF' /><stop offset='16.6666666666667%' stop-color='#EE1997' /><stop offset='18.3333333333333%' stop-color='#F687C9' /><stop offset='20%' stop-color='#FEF6FB' /><stop offset='21.6666666666667%' stop-color='#FFFFFF' /><stop offset='23.3333333333333%' stop-color='#FFFFFF' /><stop offset='25%' stop-color='#FFFFFF' /><stop offset='26.6666666666667%' stop-color='#FFFFFF' /><stop offset='28.3333333333333%' stop-color='#FFFFFF' /><stop offset='30%' stop-color='#FFFFFF' /><stop offset='31.6666666666667%' stop-color='#FFFFFF' /><stop offset='33.3333333333333%' stop-color='#FFFFFF' /><stop offset='35%' stop-color='#FFFFFF' /><stop offset='36.6666666666667%' stop-color='#FFFFFF' /><stop offset='38.3333333333333%' stop-color='#FFFFFF' /><stop offset='40%' stop-color='#FFFFFF' /><stop offset='41.6666666666667%' stop-color='#FFFEFF' /><stop offset='43.3333333333333%' stop-color='#FDDFF1' /><stop offset='45%' stop-color='#F78ECC' /><stop offset='46.6666666666667%' stop-color='#FCD6ED' /><stop offset='48.3333333333333%' stop-color='#FBC6E5' /><stop offset='50%' stop-color='#FEEEF7' /><stop offset='51.6666666666667%' stop-color='#FFFFFF' /><stop offset='53.3333333333333%' stop-color='#FFFFFF' /><stop offset='55%' stop-color='#FFFCFE' /><stop offset='56.6666666666667%' stop-color='#FCD7ED' /><stop offset='58.3333333333333%' stop-color='#FCD6EC' /><stop offset='60%' stop-color='#FFF9FC' /><stop offset='61.6666666666667%' stop-color='#FCD6EC' /><stop offset='63.3333333333333%' stop-color='#FCD7ED' /><stop offset='65%' stop-color='#FFFCFE' /><stop offset='66.6666666666667%' stop-color='#FFFFFF' /><stop offset='68.3333333333333%' stop-color='#FFFFFF' /><stop offset='70%' stop-color='#FFFFFF' /><stop offset='71.6666666666667%' stop-color='#FFFFFF' /><stop offset='73.3333333333333%' stop-color='#FFFFFF' /><stop offset='75%' stop-color='#FFFFFF' /><stop offset='76.6666666666667%' stop-color='#FFFFFF' /><stop offset='78.3333333333333%' stop-color='#FFFFFF' /><stop offset='80%' stop-color='#FFFFFF' /><stop offset='81.6666666666667%' stop-color='#FFFFFF' /><stop offset='83.3333333333333%' stop-color='#FFFFFF' /><stop offset='85%' stop-color='#FFFFFF' /><stop offset='86.6666666666667%' stop-color='#FFFFFF' /><stop offset='88.3333333333333%' stop-color='#FFFFFF' /><stop offset='90%' stop-color='#FFFFFF' /><stop offset='91.6666666666667%' stop-color='#FFFFFF' /><stop offset='93.3333333333333%' stop-color='#FFFFFF' /><stop offset='95%' stop-color='#FFFFFF' /><stop offset='96.6666666666667%' stop-color='#FFFFFF' /><stop offset='98.3333333333333%' stop-color='#FEF0F8' /><stop offset='100%' stop-color='#FBC6E5' /></linearGradient></defs><rect x='0' y='0' width='100' height='20' rx='0' ry='0' fill='url(#kde-gradient)'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Heatmap( x, y, width, height, paddingX, paddingY, axisRef, measureRef, samples, bandwidth, color )
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
    | bandwidth | <span class="type-label number">NUMERIC</span> | :material-check: | Kernel bandwidth for smoothing (default auto-calculated) |
    | color | <span class="type-label string">STRING</span> | :material-check: | The Hex color for high density areas (e.g., "#01B8AA") |

    <span class="type-label string">**STRING**</span> An SVG heatmap with smooth color gradients representing data density using kernel density estimation

=== "Example"

    ```dax hl_lines="5-20"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Heatmap(
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
            )                   // Colour
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Heatmap' =
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
                    GENERATESERIES( 0, samples, 1 ),
                    "@InputX", _Min + _RangePerSample * [Value],
                    "@KDE", 
                        ( 1 / _NumValues ) * 
                        SUMX(
                            _Data, 
                            NORM.DIST( 
                                _Min + _RangePerSample * [Value], 
                                [@Value], 
                                bandwidth, 
                                FALSE() 
                            ) 
                        )
                )

            VAR _MaxKDE = 		MAXX( _KDE, [@KDE] )

            // Create gradient stops from KDE points
            VAR _GradientStops = 
                CONCATENATEX(
                    _KDE,
                    VAR _Position = DaxLib.SVG.Scale.Normalize( [@InputX], _Min, _Max, 0, 100 )
                    VAR _Intensity = IF( _MaxKDE > 0, [@KDE] / _MaxKDE, 0 )
                    VAR _StopColor = 
                        DaxLib.SVG.Color.Hex.Interpolate(
                            "#FFFFFF",
                            color,
                            _Intensity
                        )
                    RETURN
                        "<stop offset='" & _Position & "%' stop-color='" & _StopColor & "' />",
                    "",
                    [Value],
                    ASC
                )

            // Create linear gradient definition
            VAR _GradientDef = 
                "<defs>" &
                    "<linearGradient id='kde-gradient' x1='0%' y1='0%' x2='100%' y2='0%'>" &
                        _GradientStops &
                    "</linearGradient>" &
                "</defs>"

            // Create rectangle with gradient fill
            VAR _HeatmapRect = 
                DaxLib.SVG.Element.Rect(
                    0,                          // x
                    0,                          // y
                    width,                      // width
                    height,                     // height
                    0,                          // rx
                    0,                          // ry
                    DaxLib.SVG.Attr.Shapes(
                        "url(#kde-gradient)", 	// fill
                        BLANK(),                // fillOpacity
                        BLANK(),                // fillRule
                        BLANK(),                // stroke
                        BLANK(),                // strokeWidth
                        BLANK(),                // strokeOpacity
                        BLANK()                 // opacity
                    ),
                    BLANK()                     // transforms
                )
            
            // Combined elements
            VAR _CombinedElements =
                _GradientDef & 
                _HeatmapRect
                    
            RETURN

                IF( NOT ISEMPTY( _Data ), _CombinedElements )
    ```