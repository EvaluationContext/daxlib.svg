# Compound.Boxplot

Creates a Box Plot compound SVG Visual showing statistical distribution

<svg width='500' height='100' xmlns='http://www.w3.org/2000/svg'><line x1='12.5' y1='50' x2='63.7916258570029' y2='50' stroke='#E044A7' stroke-width='1'  /><line x1='217.62773424747' y1='50' x2='448.38189683317' y2='50' stroke='#E044A7' stroke-width='1'  /><line x1='12.5' y1='20.6' x2='12.5' y2='79.4' stroke='#E044A7' stroke-width='1'  /><line x1='448.38189683317' y1='20.6' x2='448.38189683317' y2='79.4' stroke='#E044A7' stroke-width='1'  /><rect x='63.7916258570029' y='20.6' width='153.836108390467' height='58.8' rx='2' ry='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1'  /><line x1='140.283219066275' y1='20.6' x2='140.283219066275' y2='79.4' stroke='#E044A7' stroke-width='2'  /><circle cx='456.484655566438' cy='50' r='2' fill='#E044A7'  /><circle cx='466.409565785178' cy='50' r='2' fill='#E044A7'  /><circle cx='487.5' cy='50' r='2' fill='#E044A7'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Boxplot( x, y, width, height, axisRef, measureRef, fillColor, strokeColor, showOutliers, orientation, paddingX, paddingY )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | x | <span class="type-label int64">INT64</span> | :material-check: |  | The x position of the compound |
    | y | <span class="type-label int64">INT64</span> | :material-check: |  | The y position of the compound |
    | width | <span class="type-label int64">INT64</span> | :material-check: |  | The width of the compound |
    | height | <span class="type-label int64">INT64</span> | :material-check: |  | The height of the compound |
    | axisRef | <span class="type-label anyref">ANYREF</span> <span class="type-label expr">EXPR</span> | :material-check: |  | The column that the measure will be evaluated against |
    | measureRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: |  | The measure to evaluate |
    | fillColor | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Color for the box fill. Defaults to "#01B8AA" |
    | strokeColor | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: Color for lines, whiskers, and median. Defaults to "#605E5C" |
    | showOutliers | <span class="type-label boolean">BOOLEAN</span> | :material-close: | `#!dax FALSE()` | Whether to show outlier points beyond whiskers. Defaults to FALSE |
    | orientation | <span class="type-label string">STRING</span> | :material-close: | `#!dax "Horizontal"` | Optional: "Horizontal" (default) or "Vertical" |
    | paddingX | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.05` | Optional: The horizontal padding percentage (0.0-1.0, e.g., 0.1 = 10% padding). Defaults to 0.05 |
    | paddingY | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.02` | Optional: The vertical padding percentage (0.0-1.0, e.g., 0.1 = 10% padding). Defaults to 0.02 |

    <span class="type-label string">STRING</span> SVG Box Plot

=== "Example"

    ```dax hl_lines="5-18"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Boxplot(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            Dates[Date],        // axisRef
            [Total Cost],       // measureRef
            "#EC008C",          // fillColor
            "#605E5C",          // strokeColor
            TRUE,               // showOutliers
            "Horizontal",       // orientation
            0.05,               // paddingX
            0.02                // paddingY
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
    			axisRef: ANYREF EXPR,
    			measureRef: NUMERIC EXPR,
    			fillColor: STRING = BLANK(),
    			strokeColor: STRING = BLANK(),
    			showOutliers: BOOLEAN = FALSE(),
    			orientation: STRING = "Horizontal",
                paddingX: DOUBLE = 0.05,
    			paddingY: DOUBLE = 0.02
    		) =>
    
    			// Apply padding to dimensions
    			VAR _X = 			x + (width * (IF(ISBLANK(paddingX), 0, paddingX) / 2))
    			VAR _Y = 			y + (height * (IF(ISBLANK(paddingY), 0, paddingY) / 2))
    			VAR _Width = 		width * (1 - IF(ISBLANK(paddingX), 0, paddingX))
    			VAR _Height = 		height * (1 - IF(ISBLANK(paddingY), 0, paddingY))
    
    			VAR _FillColor = IF( NOT ISBLANK( fillColor ), fillColor, "#01B8AA" )
    			VAR _StrokeColor = IF( NOT ISBLANK( strokeColor ), strokeColor, "#605E5C" )
    
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
    
    			VAR _Orientation = IF( orientation = "Vertical", "Vertical", "Horizontal" )
    
    			// Primary axis (data-mapped) and cross axis
    			VAR _PrimLow = IF( _Orientation = "Horizontal", _X, _Y + _Height )
    			VAR _PrimHigh = IF( _Orientation = "Horizontal", _X + _Width, _Y )
    			VAR _CrossStart = IF( _Orientation = "Horizontal", _Y, _X )
    			VAR _CrossLen = IF( _Orientation = "Horizontal", _Height, _Width )
    
    			// Scale statistical values to primary axis coordinates
    			VAR _Q1P = DaxLib.SVG.Scale.Normalize( _Q1, _XMin, _XMax, _PrimLow, _PrimHigh )
    			VAR _MedianP = DaxLib.SVG.Scale.Normalize( _Median, _XMin, _XMax, _PrimLow, _PrimHigh )
    			VAR _Q3P = DaxLib.SVG.Scale.Normalize( _Q3, _XMin, _XMax, _PrimLow, _PrimHigh )
    			VAR _LowerWhiskerP = DaxLib.SVG.Scale.Normalize( _LowerWhisker, _XMin, _XMax, _PrimLow, _PrimHigh )
    			VAR _UpperWhiskerP = DaxLib.SVG.Scale.Normalize( _UpperWhisker, _XMin, _XMax, _PrimLow, _PrimHigh )
    
    			// Cross-axis dimensions
    			VAR _BoxCross = _CrossStart + _CrossLen * 0.2
    			VAR _BoxCrossLen = _CrossLen * 0.6
    			VAR _CenterCross = _CrossStart + _CrossLen * 0.5
    
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
    							IF( _Orientation = "Horizontal", DaxLib.SVG.Scale.Normalize( [@Value], _XMin, _XMax, _PrimLow, _PrimHigh ), _CenterCross ),
    							IF( _Orientation = "Horizontal", _CenterCross, DaxLib.SVG.Scale.Normalize( [@Value], _XMin, _XMax, _PrimLow, _PrimHigh ) ),
    							2,
    							DaxLib.SVG.Attr.Shapes( _StrokeColor )
    						),
    						""
    					)
    				)
    			
    			// Lower whisker line (along primary axis)
    			VAR _LowerWhiskerLine = 
    				DaxLib.SVG.Element.Line(
    					IF( _Orientation = "Horizontal", _LowerWhiskerP, _CenterCross ),
    					IF( _Orientation = "Horizontal", _CenterCross, _LowerWhiskerP ),
    					IF( _Orientation = "Horizontal", _Q1P, _CenterCross ),
    					IF( _Orientation = "Horizontal", _CenterCross, _Q1P ),
    					DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _StrokeColor, 1 )
    				)
    
    			// Upper whisker line (along primary axis)
    			VAR _UpperWhiskerLine = 
    				DaxLib.SVG.Element.Line(
    					IF( _Orientation = "Horizontal", _Q3P, _CenterCross ),
    					IF( _Orientation = "Horizontal", _CenterCross, _Q3P ),
    					IF( _Orientation = "Horizontal", _UpperWhiskerP, _CenterCross ),
    					IF( _Orientation = "Horizontal", _CenterCross, _UpperWhiskerP ),
    					DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _StrokeColor, 1 )
    				)
    
    			// Lower whisker cap (across cross axis)
    			VAR _LowerCap = 
    				DaxLib.SVG.Element.Line(
    					IF( _Orientation = "Horizontal", _LowerWhiskerP, _BoxCross ),
    					IF( _Orientation = "Horizontal", _BoxCross, _LowerWhiskerP ),
    					IF( _Orientation = "Horizontal", _LowerWhiskerP, _BoxCross + _BoxCrossLen ),
    					IF( _Orientation = "Horizontal", _BoxCross + _BoxCrossLen, _LowerWhiskerP ),
    					DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _StrokeColor, 1 )
    				)
    
    			// Upper whisker cap (across cross axis)
    			VAR _UpperCap = 
    				DaxLib.SVG.Element.Line(
    					IF( _Orientation = "Horizontal", _UpperWhiskerP, _BoxCross ),
    					IF( _Orientation = "Horizontal", _BoxCross, _UpperWhiskerP ),
    					IF( _Orientation = "Horizontal", _UpperWhiskerP, _BoxCross + _BoxCrossLen ),
    					IF( _Orientation = "Horizontal", _BoxCross + _BoxCrossLen, _UpperWhiskerP ),
    					DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _StrokeColor, 1 )
    				)
    
    			// Main box (Q1 to Q3)
    			VAR _Box = 
    				DaxLib.SVG.Element.Rect(
    					IF( _Orientation = "Horizontal", MIN( _Q1P, _Q3P ), _BoxCross ),
    					IF( _Orientation = "Horizontal", _BoxCross, MIN( _Q1P, _Q3P ) ),
    					IF( _Orientation = "Horizontal", ABS( _Q3P - _Q1P ), _BoxCrossLen ),
    					IF( _Orientation = "Horizontal", _BoxCrossLen, ABS( _Q3P - _Q1P ) ),
    					2, 2,
    					DaxLib.SVG.Attr.Shapes( _FillColor, 0.5, BLANK(), _StrokeColor, 1 )
    				)
    
    			// Median line (across cross axis)
    			VAR _MedianLine = 
    				DaxLib.SVG.Element.Line(
    					IF( _Orientation = "Horizontal", _MedianP, _BoxCross ),
    					IF( _Orientation = "Horizontal", _BoxCross, _MedianP ),
    					IF( _Orientation = "Horizontal", _MedianP, _BoxCross + _BoxCrossLen ),
    					IF( _Orientation = "Horizontal", _BoxCross + _BoxCrossLen, _MedianP ),
    					DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _StrokeColor, 2 )
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