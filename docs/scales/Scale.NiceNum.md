# Scale.NiceNum

Returns a "nice" rounded number close to the given value. Used for choosing human-friendly tick intervals and axis bounds

=== "Syntax"

    ```dax
    DaxLib.SVG.Scale.NiceNum( rawValue, roundMode )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | rawValue | <span class="type-label number">NUMERIC</span> <span class="type-label val">VAL</span> | :material-check: |  | The raw value to round to a nice number |
    | roundMode | <span class="type-label boolean">BOOLEAN</span> | :material-close: | `#!dax TRUE()` | Optional: TRUE for rounding to nearest nice number (for intervals), FALSE for ceiling to next nice number (for range extents). Defaults to TRUE. |

    <span class="type-label number">NUMERIC</span> A human-friendly number (1, 2, 2.5, 5, or 10 scaled by the appropriate power of 10)

=== "Example"

    ```dax
    DaxLib.SVG.Scale.NiceNum( 17.3, TRUE )
    // Returns 20 (rounds to nearest nice number)

    DaxLib.SVG.Scale.NiceNum( 17.3, FALSE )
    // Returns 20 (ceiling to next nice number for range extents)

    DaxLib.SVG.Scale.NiceNum( 0.73, TRUE )
    // Returns 1
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Scale.NiceNum' =
    		(
    			rawValue: NUMERIC VAL,
    			roundMode: BOOLEAN = TRUE()
    		) =>
    
    			VAR _Value = ABS( rawValue )
    			VAR _RoundMode = IF( ISBLANK( roundMode ), TRUE(), roundMode )
    			VAR _Exponent = IF( _Value = 0, 0, INT( LOG10( _Value ) ) )
    			VAR _Fraction = IF( _Value = 0, 0, _Value / POWER( 10, _Exponent ) )
    			VAR _NiceFraction =
    				IF(
    					_Value = 0,
    					0,
    					IF(
    						_RoundMode,
    						IF( _Fraction < 1.5, 1, IF( _Fraction < 3, 2, IF( _Fraction < 7, 5, 10 ) ) ),
    						IF( _Fraction <= 1, 1, IF( _Fraction <= 2, 2, IF( _Fraction <= 5, 5, 10 ) ) )
    					)
    				)
    
    			RETURN
    				_NiceFraction * POWER( 10, _Exponent )
    ```