# Scale.NiceRange

Computes a "nice" axis range with rounded min, max, and tick interval Returns values suitable for human-friendly axis labelling

=== "Syntax"

    ```dax
    DaxLib.SVG.Scale.NiceRange( dataMin, dataMax, maxTicks, includeZero )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | dataMin | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | Minimum value from source data |
    | dataMax | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: | Maximum value from source data |
    | maxTicks | <span class="type-label int64">INT64</span> | :material-close: | Optional: Desired maximum number of ticks. Defaults to 5 |
    | includeZero | <span class="type-label boolean">BOOLEAN</span> | :material-close: | Optional: Whether to include zero in the range when data is fully positive. Defaults to FALSE. |

    <span class="type-label table">TABLE</span> Single-row table with `@NiceMin`, `@NiceMax`, `@NiceInterval`, `@NiceTickCount`

=== "Example"

    ```dax
    DaxLib.SVG.Scale.NiceRange( 3.2, 97.8, 5, TRUE )
    // Returns single-row table:
    //   @NiceMin = 0
    //   @NiceMax = 100
    //   @NiceInterval = 25
    //   @NiceTickCount = 5
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Scale.NiceRange' =
    		(
    			dataMin: NUMERIC VAL,
    			dataMax: NUMERIC VAL,
    			maxTicks: INT64,
    			includeZero: BOOLEAN
    		) =>
    
    			VAR _MaxTicks = IF( ISBLANK( maxTicks ) || maxTicks < 2, 5, maxTicks )
    			VAR _IncludeZero = IF( ISBLANK( includeZero ), FALSE(), includeZero )
    			VAR _DataMin = IF( _IncludeZero && dataMin > 0, 0, dataMin )
    			VAR _DataMax = dataMax
    			VAR _Range = _DataMax - _DataMin
    			VAR _NiceInterval =
    				IF(
    					_Range = 0,
    					IF( _DataMax = 0, 1, DaxLib.SVG.Scale.NiceNum( ABS( _DataMax ) * 0.2, TRUE() ) ),
    					DaxLib.SVG.Scale.NiceNum( _Range / ( _MaxTicks - 1 ), TRUE() )
    				)
    			VAR _NiceMin = INT( _DataMin / _NiceInterval ) * _NiceInterval
    			VAR _NiceMax = -INT( -_DataMax / _NiceInterval ) * _NiceInterval
    			VAR _NiceTickCount = INT( ( _NiceMax - _NiceMin ) / _NiceInterval ) + 1
    
    			RETURN
    				ROW(
    					"@NiceMin", _NiceMin,
    					"@NiceMax", _NiceMax,
    					"@NiceInterval", _NiceInterval,
    					"@NiceTickCount", _NiceTickCount
    				)
    ```