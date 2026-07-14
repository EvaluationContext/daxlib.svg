# Axes.Layout

Calculates axis-aware plot area bounds

=== "Syntax"

    ```dax
    DaxLib.SVG.Axes.Layout( x, y, width, height, maxTickLabelWidth, showAxis, axisFontSize )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | x | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Content x |
    | y | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Content y |
    | width | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Content width |
    | height | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Content height |
    | maxTickLabelWidth | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Estimated max y-label width |
    | showAxis | <span class="type-label boolean">BOOLEAN</span> | :material-close: | `#!dax FALSE()` | Optional: Whether axes are enabled. Defaults to FALSE |
    | axisFontSize | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 10` | Optional: Axis font size. Defaults to 10 |

    <span class="type-label table">TABLE</span> Single-row table with `@PlotX`, `@PlotY`, `@PlotWidth`, `@PlotHeight`

=== "Example"

    ```dax
    DaxLib.SVG.Axes.Layout(
        0,              // x
        0,              // y
        500,            // width
        300,            // height
        35,             // maxTickLabelWidth
        TRUE,           // showAxis
        10              // axisFontSize
    )
    // Returns single-row table:
    //   @PlotX     – left edge of plot area (after Y-axis reservation)
    //   @PlotY     – top edge of plot area (after top padding)
    //   @PlotWidth – available plot width
    //   @PlotHeight – available plot height
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Axes.Layout' =
    		(
    			x: NUMERIC VAL,
    			y: NUMERIC VAL,
    			width: NUMERIC VAL,
    			height: NUMERIC VAL,
    			maxTickLabelWidth: NUMERIC VAL,
    			showAxis: BOOLEAN = FALSE(),
    			axisFontSize: INT64 = 10
    		) =>
    
    			VAR _TickLength = 3
    			VAR _TickPadding = 4
    			VAR _AxisLinePadding = 2
    
    			VAR _ReservedXAxisHeight = IF( showAxis, axisFontSize + _TickLength + _TickPadding + _AxisLinePadding, 0 )
    			VAR _ReservedYAxisWidth = IF( showAxis, maxTickLabelWidth + _TickLength + _TickPadding + _AxisLinePadding, 0 )
    			VAR _ReservedTopPadding = IF( showAxis, axisFontSize / 2, 0 )
    
    			RETURN
    				ROW(
    					"@PlotX", x + _ReservedYAxisWidth,
    					"@PlotY", y + _ReservedTopPadding,
    					"@PlotWidth", MAX( 0, width - _ReservedYAxisWidth ),
    					"@PlotHeight", MAX( 0, height - _ReservedXAxisHeight - _ReservedTopPadding )
    				)
    ```