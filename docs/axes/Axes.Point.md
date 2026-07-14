# Axes.Point

Maps axis/value data to plot coordinates honoring orientation

=== "Syntax"

    ```dax
    DaxLib.SVG.Axes.Point( orientation, axisIndex, measureValue, xMin, xMax, yMin, yMax, plotX, plotY, plotWidth, plotHeight )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | orientation | <span class="type-label string">STRING</span> | :material-check: |  | "Horizontal" or "Vertical" |
    | axisIndex | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | The axis index value to map |
    | measureValue | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | The measure value to map |
    | xMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | X-axis minimum value |
    | xMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | X-axis maximum value |
    | yMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Y-axis minimum value |
    | yMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Y-axis maximum value |
    | plotX | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area X origin |
    | plotY | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area Y origin |
    | plotWidth | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area width |
    | plotHeight | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area height |

    <span class="type-label table">TABLE</span> Single-row table with `@X` and `@Y`

=== "Example"

    ```dax
    DaxLib.SVG.Axes.Point(
        "Vertical",     // orientation
        50,             // axisIndex
        250,            // measureValue
        0,              // xMin
        100,            // xMax
        0,              // yMin
        500,            // yMax
        40,             // plotX
        5,              // plotY
        460,            // plotWidth
        270             // plotHeight
    )
    // Returns single-row table: { @X, @Y }
    // Coordinates mapped to plot pixel space
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Axes.Point' =
    		(
    			orientation: STRING,
    			axisIndex: NUMERIC VAL,
    			measureValue: NUMERIC VAL,
    			xMin: NUMERIC VAL,
    			xMax: NUMERIC VAL,
    			yMin: NUMERIC VAL,
    			yMax: NUMERIC VAL,
    			plotX: NUMERIC VAL,
    			plotY: NUMERIC VAL,
    			plotWidth: NUMERIC VAL,
    			plotHeight: NUMERIC VAL
    		) =>
    
    			VAR _AxisX = IF( xMax = xMin, plotX, DaxLib.SVG.Scale.Normalize( axisIndex, xMin, xMax, plotX, plotX + plotWidth ) )
    			VAR _AxisY = IF( xMax = xMin, plotY + plotHeight, DaxLib.SVG.Scale.Normalize( axisIndex, xMin, xMax, plotY + plotHeight, plotY ) )
    
    			VAR _ValueX = IF( yMax = yMin, plotX, DaxLib.SVG.Scale.Normalize( measureValue, yMin, yMax, plotX, plotX + plotWidth ) )
    			VAR _ValueY = IF( yMax = yMin, plotY + plotHeight, DaxLib.SVG.Scale.Normalize( measureValue, yMin, yMax, plotY + plotHeight, plotY ) )
    
    			RETURN
    				ROW(
    					"@X", IF( orientation = "Horizontal", _ValueX, _AxisX ),
    					"@Y", IF( orientation = "Horizontal", _AxisY, _ValueY )
    				)
    ```