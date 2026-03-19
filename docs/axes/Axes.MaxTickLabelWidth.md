# Axes.MaxTickLabelWidth

Estimates the maximum Y-axis tick label width for layout reservation

=== "Syntax"

    ```dax
    DaxLib.SVG.Axes.MaxTickLabelWidth( axisMin, axisMax, tickCount, axisFontSize, labelWidthFactor, axisIsDate )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | axisMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | Axis minimum value |
    | axisMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | Axis maximum value |
    | tickCount | <span class="type-label int64">INT64</span> | :material-close: | Optional: Number of ticks to estimate. Defaults to 1 |
    | axisFontSize | <span class="type-label int64">INT64</span> | :material-close: | Optional: Axis font size. Defaults to 10 |
    | labelWidthFactor | <span class="type-label number">DECIMAL</span> | :material-close: | Optional: Font width factor. Defaults to 0.56 (Segoe UI) |
    | axisIsDate | <span class="type-label boolean">BOOLEAN</span> | :material-close: | Optional: Whether the axis values represent dates. Defaults to FALSE |

    <span class="type-label number">NUMERIC</span> Estimated max label width in pixels

=== "Example"

    ```dax
    DaxLib.SVG.Axes.MaxTickLabelWidth(
        0,              // axisMin
        1000,           // axisMax
        5,              // tickCount
        10,             // axisFontSize
        0.56,           // labelWidthFactor (Segoe UI default)
        FALSE           // axisIsDate
    )
    // Returns estimated max label width in pixels
    // Used to reserve space for Y-axis labels in Axes.Layout
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Axes.MaxTickLabelWidth' =
    		(
    			axisMin: NUMERIC VAL,
    			axisMax: NUMERIC VAL,
    			tickCount: INT64,
    			axisFontSize: INT64,
    			labelWidthFactor: DOUBLE,
    			axisIsDate: BOOLEAN
    		) =>
    
    			VAR _TickCount = IF( ISBLANK( tickCount ) || tickCount < 1, 1, tickCount )
    			VAR _AxisFontSize = IF( ISBLANK( axisFontSize ), 10, axisFontSize )
    			VAR _LabelWidthFactor = IF( ISBLANK( labelWidthFactor ), 0.56, labelWidthFactor )
    			VAR _AxisIsDate = IF( ISBLANK( axisIsDate ), FALSE(), axisIsDate )
    			VAR _NumericSpan = ABS( axisMax - axisMin )
    			VAR _NumericDecimals = IF( _NumericSpan >= 100, 0, IF( _NumericSpan >= 10, 1, 2 ) )
    
    			VAR _TickBase =
    				ADDCOLUMNS(
    					GENERATESERIES( 0, _TickCount - 1, 1 ),
    					"@TickValue",
    						IF(
    							_TickCount = 1,
    							axisMin,
    							axisMin + DIVIDE( [Value], _TickCount - 1, 0 ) * ( axisMax - axisMin )
    						)
    				)
    
    			VAR _LabelTable =
    				ADDCOLUMNS(
    					_TickBase,
    					"@Label",
    						FORMAT(
    							IF(
    								_AxisIsDate,
    								[@TickValue],
    								ROUND( [@TickValue], _NumericDecimals )
    							),
    							IF( _AxisIsDate, "dd-mmm-yy", "General Number" )
    						)
    				)
    
    			VAR _MeasuredLabelTable =
    				ADDCOLUMNS(
    					_LabelTable,
    					"@EstimatedWidth", LEN( [@Label] ) * _AxisFontSize * _LabelWidthFactor
    				)
    
    			RETURN
    				MAXX( _MeasuredLabelTable, [@EstimatedWidth] )
    ```