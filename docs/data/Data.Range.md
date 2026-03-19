# Data.Range

Computes min/max/baseline values from shaped scalar range inputs

=== "Syntax"

    ```dax
    DaxLib.SVG.Data.Range( dataMin, dataMax, includeZero )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | dataMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | Minimum value from source data |
    | dataMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | Maximum value from source data |
    | includeZero | <span class="type-label boolean">BOOLEAN</span> | :material-close: | Use zero baseline when range is fully positive. Defaults to FALSE |

    <span class="type-label table">TABLE</span> Single-row table with `@Min`, `@Max`, and `@Baseline`

=== "Example"

    ```dax
    DaxLib.SVG.Data.Range( 3.2, 97.8, TRUE )
    // Returns single-row table:
    //   @Min = 3.2
    //   @Max = 97.8
    //   @Baseline = 0     (zero because includeZero = TRUE and min > 0)

    DaxLib.SVG.Data.Range( -10, 50, FALSE )
    // Returns single-row table:
    //   @Min = -10
    //   @Max = 50
    //   @Baseline = -10   (baseline equals min when includeZero = FALSE)
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Data.Range' =
    		(
    			dataMin: NUMERIC VAL,
    			dataMax: NUMERIC VAL,
    			includeZero: BOOLEAN
    		) =>
    
    			VAR _IncludeZero = IF( ISBLANK( includeZero ), FALSE(), includeZero )
    			VAR _Min = dataMin
    			VAR _Max = dataMax
    			VAR _Baseline = IF( _IncludeZero && _Min > 0, 0, _Min )
    
    			RETURN
    				ROW(
    					"@Min", _Min,
    					"@Max", _Max,
    					"@Baseline", _Baseline
    				)
    ```