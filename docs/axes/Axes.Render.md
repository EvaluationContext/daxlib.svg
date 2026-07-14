# Axes.Render

Renders cartesian axis lines, ticks, and labels

=== "Syntax"

    ```dax
    DaxLib.SVG.Axes.Render( plotX, plotY, plotWidth, plotHeight, xAxisMin, xAxisMax, yAxisMin, yAxisMax, showAxis, axisFontSize, xAxisIsDate, yAxisIsDate, tickCountX, tickCountY )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | plotX | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area X origin |
    | plotY | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area Y origin |
    | plotWidth | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area width |
    | plotHeight | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area height |
    | xAxisMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | X-axis minimum value |
    | xAxisMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | X-axis maximum value |
    | yAxisMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Y-axis minimum value |
    | yAxisMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Y-axis maximum value |
    | showAxis | <span class="type-label boolean">BOOLEAN</span> | :material-close: | `#!dax FALSE()` | Optional: Whether axes are enabled. Defaults to FALSE |
    | axisFontSize | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 10` | Optional: Axis label font size. Defaults to 10 |
    | xAxisIsDate | <span class="type-label boolean">BOOLEAN</span> | :material-close: | `#!dax FALSE()` | Optional: Whether X-axis values represent dates. Defaults to FALSE |
    | yAxisIsDate | <span class="type-label boolean">BOOLEAN</span> | :material-close: | `#!dax FALSE()` | Optional: Whether Y-axis values represent dates. Defaults to FALSE |
    | tickCountX | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 5` | Optional: Number of X-axis ticks. Defaults to 5 |
    | tickCountY | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 4` | Optional: Number of Y-axis ticks. Defaults to 4 |

    <span class="type-label string">STRING</span> Axis SVG string or blank when axes are disabled

=== "Example"

    ```dax
    DaxLib.SVG.Axes.Render(
        40,             // plotX
        5,              // plotY
        460,            // plotWidth
        270,            // plotHeight
        0,              // xAxisMin
        100,            // xAxisMax
        0,              // yAxisMin
        500,            // yAxisMax
        TRUE,           // showAxis
        10,             // axisFontSize
        FALSE,          // xAxisIsDate
        FALSE,          // yAxisIsDate
        5,              // tickCountX
        4               // tickCountY
    )
    // Returns SVG string with axis lines, ticks, and labels
    // Returns BLANK when showAxis = FALSE
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Axes.Render' =
    		(
    			plotX: NUMERIC VAL,
    			plotY: NUMERIC VAL,
    			plotWidth: NUMERIC VAL,
    			plotHeight: NUMERIC VAL,
    			xAxisMin: NUMERIC VAL,
    			xAxisMax: NUMERIC VAL,
    			yAxisMin: NUMERIC VAL,
    			yAxisMax: NUMERIC VAL,
    			showAxis: BOOLEAN = FALSE(),
    			axisFontSize: INT64 = 10,
    			xAxisIsDate: BOOLEAN = FALSE(),
    			yAxisIsDate: BOOLEAN = FALSE(),
    			tickCountX: INT64 = 5,
    			tickCountY: INT64 = 4
    		) =>
    
    			VAR _AxisFontFamily = "Segoe UI"
    			VAR _AxisColor = "#605E5C"
    			VAR _AxisLineStrokeWidth = 1
    			VAR _TickLength = 3
    			VAR _TickPadding = 4
    			VAR _XAxisSpan = ABS( xAxisMax - xAxisMin )
    			VAR _YAxisSpan = ABS( yAxisMax - yAxisMin )
    			VAR _XAxisDecimals = IF( _XAxisSpan >= 100, 0, IF( _XAxisSpan >= 10, 1, 2 ) )
    			VAR _YAxisDecimals = IF( _YAxisSpan >= 100, 0, IF( _YAxisSpan >= 10, 1, 2 ) )
    
    			VAR _XTickBase =
    				ADDCOLUMNS(
    					GENERATESERIES( 0, tickCountX - 1, 1 ),
    					"@TickValue",
    						IF(
    							tickCountX = 1,
    							xAxisMin,
    							xAxisMin + DIVIDE( [Value], tickCountX - 1, 0 ) * ( xAxisMax - xAxisMin )
    						),
    					"@TickIndex", [Value]
    				)
    
    			VAR _XTickTable =
    				ADDCOLUMNS(
    					_XTickBase,
    					"@Pos",
    						IF(
    							xAxisMax = xAxisMin,
    							plotX + plotWidth / 2,
    							DaxLib.SVG.Scale.Normalize( [@TickValue], xAxisMin, xAxisMax, plotX, plotX + plotWidth )
    						),
    					"@Label",
    						FORMAT(
    							IF(
    								xAxisIsDate,
    								[@TickValue],
    								ROUND( [@TickValue], _XAxisDecimals )
    							),
    							IF( xAxisIsDate, "dd-mmm-yy", "General Number" )
    						),
    					"@Anchor",
    						IF(
    							[@TickIndex] = 0, "start",
    							IF( [@TickIndex] = tickCountX - 1, "end", "middle" )
    						)
    				)
    
    			// Detect X-axis label overlap and filter to first/last when needed
    			VAR _XLabelWidthFactor = 0.56
    			VAR _MaxXLabelLen = MAXX( _XTickTable, LEN( [@Label] ) )
    			VAR _EstXLabelWidth = _MaxXLabelLen * axisFontSize * _XLabelWidthFactor
    			VAR _XLabelsOverlap = _EstXLabelWidth * tickCountX > plotWidth * 0.9
    
    			VAR _XTickRendered =
    				FILTER(
    					_XTickTable,
    					NOT _XLabelsOverlap || [@TickIndex] = 0 || [@TickIndex] = tickCountX - 1
    				)
    
    			VAR _YTickBase =
    				ADDCOLUMNS(
    					GENERATESERIES( 0, tickCountY - 1, 1 ),
    					"@TickValue",
    						IF(
    							tickCountY = 1,
    							yAxisMin,
    							yAxisMin + DIVIDE( [Value], tickCountY - 1, 0 ) * ( yAxisMax - yAxisMin )
    						)
    				)
    
    			VAR _YTickTable =
    				ADDCOLUMNS(
    					_YTickBase,
    					"@Pos",
    						IF(
    							yAxisMax = yAxisMin,
    							plotY + plotHeight / 2,
    							DaxLib.SVG.Scale.Normalize( [@TickValue], yAxisMin, yAxisMax, plotY + plotHeight, plotY )
    						),
    					"@Label",
    						FORMAT(
    							IF(
    								yAxisIsDate,
    								[@TickValue],
    								ROUND( [@TickValue], _YAxisDecimals )
    							),
    							IF( yAxisIsDate, "dd-mmm-yy", "General Number" )
    						)
    				)
    
    			// Detect Y-axis label overlap and filter to first/last when needed
    			VAR _EstYLabelHeight = axisFontSize * 1.5
    			VAR _YLabelsOverlap = _EstYLabelHeight * tickCountY > plotHeight * 0.9
    
    			VAR _YTickRendered =
    				FILTER(
    					_YTickTable,
    					NOT _YLabelsOverlap || [Value] = 0 || [Value] = tickCountY - 1
    				)
    
    			VAR _XAxisLine =
    				DaxLib.SVG.Element.Line(
    					plotX,
    					plotY + plotHeight,
    					plotX + plotWidth,
    					plotY + plotHeight,
    					DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _AxisColor, _AxisLineStrokeWidth )
    				)
    
    			VAR _YAxisLine =
    				DaxLib.SVG.Element.Line(
    					plotX,
    					plotY,
    					plotX,
    					plotY + plotHeight,
    					DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _AxisColor, _AxisLineStrokeWidth )
    				)
    
    			VAR _XTicks =
    				CONCATENATEX(
    					_XTickRendered,
    					DaxLib.SVG.Element.Line(
    						[@Pos],
    						plotY + plotHeight,
    						[@Pos],
    						plotY + plotHeight + _TickLength,
    						DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _AxisColor, 1 )
    					)
    					&
    					DaxLib.SVG.Element.Txt(
    						[@Pos],
    						plotY + plotHeight + _TickLength + _TickPadding,
    						[@Label],
    						BLANK(),
    						BLANK(),
    						DaxLib.SVG.Attr.Shapes( _AxisColor )
    						& DaxLib.SVG.Attr.Txt( _AxisFontFamily, axisFontSize, BLANK(), BLANK(), [@Anchor], "hanging" )
    					),
    					""
    				)
    
    			VAR _YTicks =
    				CONCATENATEX(
    					_YTickRendered,
    					DaxLib.SVG.Element.Line(
    						plotX - _TickLength,
    						[@Pos],
    						plotX,
    						[@Pos],
    						DaxLib.SVG.Attr.Shapes( BLANK(), BLANK(), BLANK(), _AxisColor, 1 )
    					)
    					&
    					DaxLib.SVG.Element.Txt(
    						plotX - _TickLength - _TickPadding,
    						[@Pos],
    						[@Label],
    						BLANK(),
    						BLANK(),
    						DaxLib.SVG.Attr.Shapes( _AxisColor )
    						& DaxLib.SVG.Attr.Txt( _AxisFontFamily, axisFontSize, BLANK(), BLANK(), "end", "middle" )
    					),
    					""
    				)
    
    			RETURN
    				IF( showAxis, _XAxisLine & _YAxisLine & _XTicks & _YTicks )
    ```