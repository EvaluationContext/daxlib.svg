# Axes.Baseline

Maps the numeric baseline to plot coordinates honoring orientation

=== "Syntax"

    ```dax
    DaxLib.SVG.Axes.Baseline( orientation, yMin, yMax, plotX, plotY, plotWidth, plotHeight )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | orientation | <span class="type-label string">STRING</span> | :material-check: |  | "Horizontal" or "Vertical" |
    | yMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Y-axis minimum value |
    | yMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Y-axis maximum value |
    | plotX | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area X origin |
    | plotY | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area Y origin |
    | plotWidth | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area width |
    | plotHeight | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | Plot area height |

    <span class="type-label table">TABLE</span> Single-row table with `@BaseX` and `@BaseY`

=== "Example"

    ```dax
    DaxLib.SVG.Axes.Baseline(
        "Vertical",     // orientation
        0,              // yMin
        500,            // yMax
        40,             // plotX
        5,              // plotY
        460,            // plotWidth
        270             // plotHeight
    )
    // Returns single-row table: { @BaseX, @BaseY }
    // Maps the numeric baseline (yMin) to plot coordinates
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Axes.Baseline' =
    		(
    			orientation: STRING,
    			yMin: NUMERIC VAL,
    			yMax: NUMERIC VAL,
    			plotX: NUMERIC VAL,
    			plotY: NUMERIC VAL,
    			plotWidth: NUMERIC VAL,
    			plotHeight: NUMERIC VAL
    		) =>
    
    			VAR _BaseX = IF( yMax = yMin, plotX, DaxLib.SVG.Scale.Normalize( yMin, yMin, yMax, plotX, plotX + plotWidth ) )
    			VAR _BaseY = IF( yMax = yMin, plotY + plotHeight, DaxLib.SVG.Scale.Normalize( yMin, yMin, yMax, plotY + plotHeight, plotY ) )
    
    			RETURN
    				ROW(
    					"@BaseX", IF( orientation = "Horizontal", _BaseX, plotX ),
    					"@BaseY", IF( orientation = "Horizontal", plotY, _BaseY )
    				)
    ```