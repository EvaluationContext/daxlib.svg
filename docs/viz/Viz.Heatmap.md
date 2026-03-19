# Viz.Heatmap

Renders a heatmap as an SVG data URI showing data density using kernel density estimation

??? info "Kernel Density Estimation (KDE)"
    
    KDE is a statistical method that estimates the probability density function of your data by placing a "kernel" (typically a normal distribution) at each data point. The heatmap visualizes data density across the range, creating smooth gradients that reveal patterns and concentrations in your dataset.

    **Key Parameters:**

    - **Samples**: Controls the resolution of the density calculation (higher = smoother, but slower performance)

    - **Bandwidth**: Controls the smoothing level - smaller values create sharper peaks around data points, larger values create broader, smoother distributions

<svg width='500' height='100' xmlns='http://www.w3.org/2000/svg'><defs><linearGradient id='kde-gradient' x1='0%' y1='0%' x2='100%' y2='0%'><stop offset='0%' stop-color='#EC8ECA' /><stop offset='1.66666666666667%' stop-color='#E874BE' /><stop offset='3.33333333333333%' stop-color='#E45BB2' /><stop offset='5%' stop-color='#E873BD' /><stop offset='6.66666666666667%' stop-color='#E564B6' /><stop offset='8.33333333333333%' stop-color='#F9DCEE' /><stop offset='10%' stop-color='#ED90CB' /><stop offset='11.6666666666667%' stop-color='#F6C7E5' /><stop offset='13.3333333333333%' stop-color='#E044A7' /><stop offset='15%' stop-color='#F9DAED' /><stop offset='16.6666666666667%' stop-color='#F8D5EB' /><stop offset='18.3333333333333%' stop-color='#FFFFFF' /><stop offset='20%' stop-color='#F1ABD7' /><stop offset='21.6666666666667%' stop-color='#F8D4EB' /><stop offset='23.3333333333333%' stop-color='#F9DBEE' /><stop offset='25%' stop-color='#FADFF0' /><stop offset='26.6666666666667%' stop-color='#F9D9ED' /><stop offset='28.3333333333333%' stop-color='#FFFFFF' /><stop offset='30%' stop-color='#FFFEFF' /><stop offset='31.6666666666667%' stop-color='#FCEEF7' /><stop offset='33.3333333333333%' stop-color='#FDF3F9' /><stop offset='35%' stop-color='#FDF6FB' /><stop offset='36.6666666666667%' stop-color='#FFFFFF' /><stop offset='38.3333333333333%' stop-color='#FFFFFF' /><stop offset='40%' stop-color='#F3B5DC' /><stop offset='41.6666666666667%' stop-color='#FBE5F3' /><stop offset='43.3333333333333%' stop-color='#FEFBFD' /><stop offset='45%' stop-color='#FEFBFD' /><stop offset='46.6666666666667%' stop-color='#F3B7DD' /><stop offset='48.3333333333333%' stop-color='#F8D4EB' /><stop offset='50%' stop-color='#F8D5EB' /><stop offset='51.6666666666667%' stop-color='#FFFFFF' /><stop offset='53.3333333333333%' stop-color='#FFFFFF' /><stop offset='55%' stop-color='#FFFFFF' /><stop offset='56.6666666666667%' stop-color='#FFFFFF' /><stop offset='58.3333333333333%' stop-color='#FFFFFF' /><stop offset='60%' stop-color='#FFFFFF' /><stop offset='61.6666666666667%' stop-color='#FFFFFF' /><stop offset='63.3333333333333%' stop-color='#FFFFFF' /><stop offset='65%' stop-color='#FFFFFF' /><stop offset='66.6666666666667%' stop-color='#FFFFFF' /><stop offset='68.3333333333333%' stop-color='#F8D4EB' /><stop offset='70%' stop-color='#FFFFFF' /><stop offset='71.6666666666667%' stop-color='#FFFFFF' /><stop offset='73.3333333333333%' stop-color='#FFFFFF' /><stop offset='75%' stop-color='#FFFFFF' /><stop offset='76.6666666666667%' stop-color='#FFFEFE' /><stop offset='78.3333333333333%' stop-color='#FCEEF7' /><stop offset='80%' stop-color='#FFFFFF' /><stop offset='81.6666666666667%' stop-color='#FFFFFF' /><stop offset='83.3333333333333%' stop-color='#FFFFFF' /><stop offset='85%' stop-color='#FFFFFF' /><stop offset='86.6666666666667%' stop-color='#FFFFFF' /><stop offset='88.3333333333333%' stop-color='#FFFFFF' /><stop offset='90%' stop-color='#FFFFFF' /><stop offset='91.6666666666667%' stop-color='#FFFFFF' /><stop offset='93.3333333333333%' stop-color='#FFFFFF' /><stop offset='95%' stop-color='#FFFFFF' /><stop offset='96.6666666666667%' stop-color='#FFFFFF' /><stop offset='98.3333333333333%' stop-color='#FFFFFF' /><stop offset='100%' stop-color='#F8D4EB' /></linearGradient></defs><rect x='12.5' y='2' width='475' height='196' rx='0' ry='0' fill='url(#kde-gradient)'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Viz.Heatmap( axisRef, measureRef, color, width, height )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | axisRef | <span class="type-label anyref">ANYREF</span> <span class="type-label expr">EXPR</span> | :material-check: | Axis reference column |
    | measureRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: | Measure expression |
    | color | <span class="type-label string">STRING</span> | :material-close: | Optional color for high density areas. Defaults to Power BI theme color |
    | width | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG width. Defaults to 120 |
    | height | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG height. Defaults to 48 |

    <span class="type-label string">STRING</span> SVG Heatmap

=== "Example"

    ```dax
    DaxLib.SVG.Viz.Heatmap(
        Products[Product],  // axisRefColumn
        [Total Cost],       // measureRefExpr
        BLANK(),            // color (uses default theme)
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded heatmap
    // Set as a measure with DataCategory = "ImageUrl"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Viz.Heatmap' =
    		(
    			axisRef: ANYREF EXPR,
    			measureRef: NUMERIC EXPR,
    			color: STRING,
    			width: INT64,
    			height: INT64
    		) =>
    
    			VAR _W = IF( ISBLANK( width ), 120, width )
    			VAR _H = IF( ISBLANK( height ), 48, height )
    			VAR _Color = IF( NOT ISBLANK( color ), color, DaxLib.SVG.Color.Theme( "Power BI", 1 ) )
    			VAR _Marks =
    				DaxLib.SVG.Compound.Heatmap(
    					0, 0, _W, _H, 0, 0,
    					axisRef, measureRef, 50, 1, _Color
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Marks ), DaxLib.SVG.SVG( "100%", "100%", "0 0 " & _W & " " & _H, _Marks, BLANK() ) )
    ```