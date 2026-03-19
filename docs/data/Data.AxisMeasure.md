# Data.AxisMeasure

Builds a shared axis/value data table for compound visuals

=== "Syntax"

    ```dax
    DaxLib.SVG.Data.AxisMeasure( axisRef, measureRef, axisMode )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | axisRef | <span class="type-label anyref">ANYREF</span> <span class="type-label expr">EXPR</span> | :material-check: | Axis reference column evaluated in current filter context |
    | measureRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: | Measure expression evaluated per axis value |
    | axisMode | <span class="type-label string">STRING</span> | :material-check: | "Auto", "Numeric", or "Categorical" |

    <span class="type-label table">TABLE</span> Standardized table with `@AxisValue`, `@AxisIndex`, and `@Value`

=== "Example"

    ```dax
    DaxLib.SVG.Data.AxisMeasure(
        Dates[Date],        // axisRefColumn
        [Total Cost],       // measureRefExpr
        "Auto"              // axisMode
    )
    // Returns table with columns:
    //   @AxisValue – the raw axis value
    //   @AxisIndex – numeric index (or value itself for numeric axes)
    //   @Value     – the evaluated measure
    // Sorted by @AxisIndex ascending
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Data.AxisMeasure' =
    		(
    			axisRef: ANYREF EXPR,
    			measureRef: NUMERIC EXPR,
    			axisMode: STRING
    		) =>
    
    			VAR _AxisMode =
    				IF(
    					axisMode = "Numeric" || axisMode = "Categorical",
    					axisMode,
    					"Auto"
    				)
    
    			VAR _AxisSample = MAX( axisRef )
    			VAR _AxisIsNumeric = ISNUMBER( _AxisSample ) || ISDATETIME( _AxisSample )
    			VAR _UseNumericAxis =
    				IF(
    					_AxisMode = "Numeric",
    					TRUE(),
    					IF( _AxisMode = "Categorical", FALSE(), _AxisIsNumeric )
    				)
    
    			VAR _WithValues =
    				ADDCOLUMNS(
    					VALUES( axisRef ),
    					"@AxisValue", axisRef,
    					"@Value", measureRef
    				)
    
    			VAR _Indexed =
    				ADDCOLUMNS(
    					_WithValues,
    					"@AxisIndex",
    						IF(
    							_UseNumericAxis,
    							[@AxisValue],
    							RANK( DENSE, CALCULATETABLE( VALUES( axisRef ), ALLSELECTED() ) )
    						)
    				)
    
    			RETURN
    				TOPN(
    					COUNTROWS( _Indexed ),
    					_Indexed,
    					[@AxisIndex], ASC,
    					[@AxisValue], ASC
    				)
    ```