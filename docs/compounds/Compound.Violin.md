# Compound.Violin

Creates a Violin Plot compound SVG Visual showing distribution density using Kernel Density Estimation (KDE)

??? info "Kernel Density Estimation (KDE)"

    KDE creates a smooth estimate of your data's probability density by placing a "kernel" (normal distribution curve) at each data point and summing them together. The violin plot displays this density as a symmetrical shape - wider areas indicate higher probability/frequency of values.
    
    **Key Parameters:**

    - **Samples**: Controls the resolution of the density calculation (higher = smoother, but slower performance)

    - **Bandwidth**: Controls how much each data point influences nearby areas. Smaller bandwidth values create sharper, more detailed curves that closely follow individual data points. Larger bandwidth values create smoother, more generalized shapes that show overall trends

<svg width='250' height='100' xmlns='http://www.w3.org/2000/svg'><path d='M 6.25 50 S 8.22916666666667 13.5988448333337, 10.2083333333333 13.5988448333337 S 12.1875 7.13443689107196, 14.1666666666667 7.13443689107196 S 16.1458333333333 13.4254332267382, 18.125 13.4254332267382 S 20.1041666666667 9.32401511123012, 22.0833333333333 9.32401511123012 S 24.0625 40.7631790543889, 26.0416666666667 40.7631790543889 S 28.0208333333333 20.808738344417, 30 20.808738344417 S 31.9791666666667 35.3197415731218, 33.9583333333333 35.3197415731218 S 35.9375 1, 37.9166666666667 1 S 39.8958333333333 40.2291537903052, 41.875 40.2291537903052 S 43.8541666666667 39.1249980994134, 45.8333333333333 39.1249980994134 S 47.8125 49.9880663333201, 49.7916666666667 49.9880663333201 S 51.7708333333333 27.9205430208122, 53.75 27.9205430208122 S 55.7291666666667 38.6214045946875, 57.7083333333333 38.6214045946875 S 59.6875 40.6552772348799, 61.6666666666667 40.6552772348799 S 63.6458333333333 41.5836867360033, 65.625 41.5836867360033 S 67.6041666666667 39.9569930359308, 69.5833333333333 39.9569930359308 S 71.5625 49.9997232393212, 73.5416666666667 49.9997232393212 S 75.5208333333333 49.7338007298534, 77.5 49.7338007298534 S 79.4791666666667 45.4769442199976, 81.4583333333333 45.4769442199976 S 83.4375 46.7699443349842, 85.4166666666666 46.7699443349842 S 87.3958333333333 47.551931593251, 89.375 47.551931593251 S 91.3541666666667 49.999999895352, 93.3333333333333 49.999999895352 S 95.3125 49.9988046964593, 97.2916666666667 49.9988046964593 S 99.2708333333333 30.7142246902948, 101.25 30.7142246902948 S 103.229166666667 43.1948022761676, 105.208333333333 43.1948022761676 S 107.1875 49.0772310898017, 109.166666666667 49.0772310898017 S 111.145833333333 49.0697174260728, 113.125 49.0697174260728 S 115.104166666667 31.1880706790335, 117.083333333333 31.1880706790335 S 119.0625 38.6050415483723, 121.041666666667 38.6050415483723 S 123.020833333333 38.9178134118706, 125 38.9178134118706 S 126.979166666667 49.9935251344659, 128.958333333333 49.9935251344659 S 130.9375 49.9999999999998, 132.916666666667 49.9999999999998 S 134.895833333333 50, 136.875 50 S 138.854166666667 50, 140.833333333333 50 S 142.8125 50, 144.791666666667 50 S 146.770833333333 50, 148.75 50 S 150.729166666667 50, 152.708333333333 50 S 154.6875 50, 156.666666666667 50 S 158.645833333333 49.9999999999999, 160.625 49.9999999999999 S 162.604166666667 49.9946182609977, 164.583333333333 49.9946182609977 S 166.5625 38.8101357064449, 168.541666666667 38.8101357064449 S 170.520833333333 49.998830853595, 172.5 49.998830853595 S 174.479166666667 50, 176.458333333333 50 S 178.4375 50, 180.416666666667 50 S 182.395833333333 49.9999999990841, 184.375 49.9999999990841 S 186.354166666667 49.7171963684577, 188.333333333333 49.7171963684577 S 190.3125 45.6122252528023, 192.291666666667 45.6122252528023 S 194.270833333333 49.9999965790592, 196.25 49.9999965790592 S 198.229166666667 50, 200.208333333333 50 S 202.1875 50, 204.166666666667 50 S 206.145833333333 50, 208.125 50 S 210.104166666667 50, 212.083333333333 50 S 214.0625 50, 216.041666666667 50 S 218.020833333333 50, 220 50 S 221.979166666667 50, 223.958333333333 50 S 225.9375 50, 227.916666666667 50 S 229.895833333333 50, 231.875 50 S 233.854166666667 50, 235.833333333333 50 S 237.8125 49.9974477393213, 239.791666666667 49.9974477393213 S 241.770833333333 38.6144481902767, 243.75 38.6144481902767 S 245.729166666667 49.9974477393213, 247.708333333333 49.9974477393213 L 247.708333333333 50.0025522606787 S 245.729166666667 61.3855518097233, 243.75 61.3855518097233 S 241.770833333333 50.0025522606787, 239.791666666667 50.0025522606787 S 237.8125 50, 235.833333333333 50 S 233.854166666667 50, 231.875 50 S 229.895833333333 50, 227.916666666667 50 S 225.9375 50, 223.958333333333 50 S 221.979166666667 50, 220 50 S 218.020833333333 50, 216.041666666667 50 S 214.0625 50, 212.083333333333 50 S 210.104166666667 50, 208.125 50 S 206.145833333333 50, 204.166666666667 50 S 202.1875 50, 200.208333333333 50 S 198.229166666667 50.0000034209408, 196.25 50.0000034209408 S 194.270833333333 54.3877747471977, 192.291666666667 54.3877747471977 S 190.3125 50.2828036315423, 188.333333333333 50.2828036315423 S 186.354166666667 50.0000000009159, 184.375 50.0000000009159 S 182.395833333333 50, 180.416666666667 50 S 178.4375 50, 176.458333333333 50 S 174.479166666667 50.001169146405, 172.5 50.001169146405 S 170.520833333333 61.1898642935551, 168.541666666667 61.1898642935551 S 166.5625 50.0053817390023, 164.583333333333 50.0053817390023 S 162.604166666667 50.0000000000001, 160.625 50.0000000000001 S 158.645833333333 50, 156.666666666667 50 S 154.6875 50, 152.708333333333 50 S 150.729166666667 50, 148.75 50 S 146.770833333333 50, 144.791666666667 50 S 142.8125 50, 140.833333333333 50 S 138.854166666667 50, 136.875 50 S 134.895833333333 50.0000000000002, 132.916666666667 50.0000000000002 S 130.9375 50.0064748655341, 128.958333333333 50.0064748655341 S 126.979166666667 61.0821865881294, 125 61.0821865881294 S 123.020833333333 61.3949584516277, 121.041666666667 61.3949584516277 S 119.0625 68.8119293209665, 117.083333333333 68.8119293209665 S 115.104166666667 50.9302825739272, 113.125 50.9302825739272 S 111.145833333333 50.9227689101983, 109.166666666667 50.9227689101983 S 107.1875 56.8051977238324, 105.208333333333 56.8051977238324 S 103.229166666667 69.2857753097052, 101.25 69.2857753097052 S 99.2708333333333 50.0011953035407, 97.2916666666667 50.0011953035407 S 95.3125 50.000000104648, 93.3333333333333 50.000000104648 S 91.3541666666667 52.448068406749, 89.375 52.448068406749 S 87.3958333333333 53.2300556650158, 85.4166666666666 53.2300556650158 S 83.4375 54.5230557800024, 81.4583333333333 54.5230557800024 S 79.4791666666667 50.2661992701466, 77.5 50.2661992701466 S 75.5208333333333 50.0002767606788, 73.5416666666667 50.0002767606788 S 71.5625 60.0430069640692, 69.5833333333333 60.0430069640692 S 67.6041666666667 58.4163132639967, 65.625 58.4163132639967 S 63.6458333333333 59.3447227651201, 61.6666666666667 59.3447227651201 S 59.6875 61.3785954053125, 57.7083333333333 61.3785954053125 S 55.7291666666667 72.0794569791878, 53.75 72.0794569791878 S 51.7708333333333 50.0119336666799, 49.7916666666667 50.0119336666799 S 47.8125 60.8750019005866, 45.8333333333333 60.8750019005866 S 43.8541666666667 59.7708462096948, 41.875 59.7708462096948 S 39.8958333333333 99, 37.9166666666667 99 S 35.9375 64.6802584268782, 33.9583333333333 64.6802584268782 S 31.9791666666667 79.191261655583, 30 79.191261655583 S 28.0208333333333 59.2368209456111, 26.0416666666667 59.2368209456111 S 24.0625 90.6759848887699, 22.0833333333333 90.6759848887699 S 20.1041666666667 86.5745667732618, 18.125 86.5745667732618 S 16.1458333333333 92.865563108928, 14.1666666666667 92.865563108928 S 12.1875 86.4011551666663, 10.2083333333333 86.4011551666663 S 8.22916666666667 50, 6.25 50 Z' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Violin( x, y, width, height, axisRef, measureRef, samples, bandwidth, color, orientation, paddingX, paddingY )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | x | <span class="type-label int64">INT64</span> | :material-check: |  | The x position of the compound |
    | y | <span class="type-label int64">INT64</span> | :material-check: |  | The y position of the compound |
    | width | <span class="type-label int64">INT64</span> | :material-check: |  | The width of the compound |
    | height | <span class="type-label int64">INT64</span> | :material-check: |  | The height of the compound |
    | axisRef | <span class="type-label anyref">ANYREF</span> <span class="type-label expr">EXPR</span> | :material-check: |  | The column that the measure will be evaluated against |
    | measureRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: |  | The measure to evaluate |
    | samples | <span class="type-label int64">INT64</span> | :material-check: |  | Number of density calculation points |
    | bandwidth | <span class="type-label number">NUMERIC</span> | :material-check: |  | Kernel bandwidth for smoothing |
    | color | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Fill color for the violin shape. Defaults to "#01B8AA" |
    | orientation | <span class="type-label string">STRING</span> | :material-close: | `#!dax "Horizontal"` | Optional: "Horizontal" (default) or "Vertical" |
    | paddingX | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.05` | Optional: The horizontal padding percentage (0.0-1.0, e.g., 0.1 = 10% padding). Defaults to 0.05 |
    | paddingY | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.02` | Optional: The vertical padding percentage (0.0-1.0, e.g., 0.1 = 10% padding). Defaults to 0.02 |

    <span class="type-label string">STRING</span> SVG Violin Plot

=== "Example"

    ```dax hl_lines="5-18"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Violin(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            MAX( Samples[Samples] ), // samples
            MAX( Bandwidth[Bandwidth] ), // bandwidth
            "#EC008C",          // color
            "Horizontal",       // orientation
            0.05,               // paddingX
            0.02                // paddingY
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
    			axisRef: ANYREF EXPR,
    			measureRef: NUMERIC EXPR,
    			samples: INT64,
    			bandwidth: NUMERIC,
    			color: STRING = BLANK(),
    			orientation: STRING = "Horizontal",
    			paddingX: DOUBLE = 0.05,
    			paddingY: DOUBLE = 0.02
    		) =>
    		
    			// Apply padding to dimensions
    			VAR _X = 			x + (width * (IF(ISBLANK(paddingX), 0, paddingX) / 2))
    			VAR _Y = 			y + (height * (IF(ISBLANK(paddingY), 0, paddingY) / 2))
    			VAR _Width = 		width * (1 - IF(ISBLANK(paddingX), 0, paddingX))
    			VAR _Height = 		height * (1 - IF(ISBLANK(paddingY), 0, paddingY))
    
    			VAR _Color = IF( NOT ISBLANK( color ), color, "#01B8AA" )
    
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
    
    			VAR _Orientation = IF( orientation = "Vertical", "Vertical", "Horizontal" )
    
    			// Map KDE values to SVG coordinates using normalize function
    			VAR _Points = 
    				ADDCOLUMNS(
    					_KDE,
    					"@X", IF( _Orientation = "Horizontal",
    						DaxLib.SVG.Scale.Normalize( [@InputX], _Min, _Max, _X, _X + _Width ),
    						DaxLib.SVG.Scale.Normalize( [@KDE], 0, _MaxKDE, _X + _Width * 0.5, _X + _Width )
    					),
    					"@Y", IF( _Orientation = "Horizontal",
    						DaxLib.SVG.Scale.Normalize( [@KDE], 0, _MaxKDE, _Y + _Height * 0.5, _Y ),
    						DaxLib.SVG.Scale.Normalize( [@InputX], _Min, _Max, _Y + _Height, _Y )
    					)
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
    		VAR _CenterX = _X + (_Width * 0.5)
    
    		// Top/Right half curve
    		VAR _TopCurve = 
    			CONCATENATEX(
    				_WithControlPoints,
    				IF(
    					[Value] = 0,
    					IF( _Orientation = "Horizontal", "M " & [@X] & " " & _CenterY, "M " & _CenterX & " " & [@Y] ),
    					"S " & [@CX] & " " & [@CY] & ", " & [@X] & " " & [@Y]
    				),
    				" ",
    				[Value],
    				ASC
    			)
    
    		// Bottom/Left half curve (mirrored) – uses S Bézier for smooth mirror with control points
    		VAR _PointsWithNext = 
    			NATURALLEFTOUTERJOIN(
    				_Points,
    				SELECTCOLUMNS(
    					_Points,
    					"Value", [Value] - 1,
    					"@NextX", [@X],
    					"@NextY", [@Y]
    				)
    			)
    
    		VAR _BottomCurve = 
    			CONCATENATEX(
    				_PointsWithNext,
    				VAR _MirroredX = IF( _Orientation = "Horizontal", [@X], _CenterX + (_CenterX - [@X]) )
    				VAR _MirroredY = IF( _Orientation = "Horizontal", _CenterY + (_CenterY - [@Y]), [@Y] )
    				VAR _MCX = IF( _Orientation = "Horizontal",
    					[@NextX] + ( [@X] - [@NextX] ) / 2,
    					_CenterX + ( _CenterX - ( [@NextX] + ( [@X] - [@NextX] ) / 2 ) )
    				)
    				VAR _MCY = IF( _Orientation = "Horizontal",
    					_CenterY + ( _CenterY - [@Y] ),
    					[@NextY] + ( [@Y] - [@NextY] ) / 2
    				)
    				RETURN
    					IF(
    						ISBLANK( [@NextX] ),
    						"L " & _MirroredX & " " & _MirroredY,
    						IF(
    							[Value] = 0,
    							IF( _Orientation = "Horizontal",
    								"S " & _MCX & " " & _CenterY & ", " & [@X] & " " & _CenterY,
    								"S " & _CenterX & " " & _MCY & ", " & _CenterX & " " & [@Y]
    							),
    							"S " & _MCX & " " & _MCY & ", " & _MirroredX & " " & _MirroredY
    						)
    					),
    				" ",
    				[Value],
    				DESC
    			)			// Create a single closed path for the violin shape
    			VAR _ViolinPath = 
    				_TopCurve & 
    				" " & _BottomCurve & 
    				" Z" // Close the path
    
    			// Combined Elements
    			VAR _CombinedElements = 
    				DaxLib.SVG.Element.Paths(
    					_ViolinPath,
    					DaxLib.SVG.Attr.Shapes(
    						_Color,
    						0.5,
    						BLANK(),
    						_Color,
    						1
    					)
    				)
    
    			RETURN
    
    				IF( NOT ISEMPTY( _Data ), _CombinedElements )
    ```