# Viz.Boxplot

Renders a box plot as an SVG data URI showing statistical distribution

<svg width='500' height='100' xmlns='http://www.w3.org/2000/svg'><line x1='12.5' y1='50' x2='63.7916258570029' y2='50' stroke='#E044A7' stroke-width='1'  /><line x1='217.62773424747' y1='50' x2='448.38189683317' y2='50' stroke='#E044A7' stroke-width='1'  /><line x1='12.5' y1='20.6' x2='12.5' y2='79.4' stroke='#E044A7' stroke-width='1'  /><line x1='448.38189683317' y1='20.6' x2='448.38189683317' y2='79.4' stroke='#E044A7' stroke-width='1'  /><rect x='63.7916258570029' y='20.6' width='153.836108390467' height='58.8' rx='2' ry='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1'  /><line x1='140.283219066275' y1='20.6' x2='140.283219066275' y2='79.4' stroke='#E044A7' stroke-width='2'  /><circle cx='456.484655566438' cy='50' r='2' fill='#E044A7'  /><circle cx='466.409565785178' cy='50' r='2' fill='#E044A7'  /><circle cx='487.5' cy='50' r='2' fill='#E044A7'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Viz.Boxplot( axisRef, measureRef, color, showOutliers, width, height )
    ```

    | Parameter | Type | Required | Description |
    |:---:|:---:|:---:|---|
    | axisRef | <span class="type-label anyref">ANYREF</span> <span class="type-label expr">EXPR</span> | :material-check: | Axis reference column |
    | measureRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: | Measure expression |
    | color | <span class="type-label string">STRING</span> | :material-close: | Optional box fill color. Defaults to Power BI theme color |
    | showOutliers | <span class="type-label boolean">BOOLEAN</span> | :material-close: | Optional: show outlier points. Defaults to FALSE |
    | width | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG width. Defaults to 120 |
    | height | <span class="type-label int64">INT64</span> | :material-close: | Optional: SVG height. Defaults to 48 |

    <span class="type-label string">STRING</span> SVG Box Plot

=== "Example"

    ```dax
    DaxLib.SVG.Viz.Boxplot(
        Products[Product],  // axisRefColumn
        [Total Cost],       // measureRefExpr
        BLANK(),            // color (uses default theme)
        TRUE,               // showOutliers
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded box plot
    // Set as a measure with DataCategory = "ImageUrl"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Viz.Boxplot' =
    		(
    			axisRef: ANYREF EXPR,
    			measureRef: NUMERIC EXPR,
    			color: STRING,
    			showOutliers: BOOLEAN,
    			width: INT64,
    			height: INT64
    		) =>
    
    			VAR _W = IF( ISBLANK( width ), 120, width )
    			VAR _H = IF( ISBLANK( height ), 48, height )
    			VAR _Color = IF( NOT ISBLANK( color ), color, DaxLib.SVG.Color.Theme( "Power BI", 1 ) )
    			VAR _Marks =
    				DaxLib.SVG.Compound.Boxplot(
    					0, 0, _W, _H, 0, 0,
    					axisRef, measureRef, _Color, "#605E5C", showOutliers, BLANK()
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Marks ), DaxLib.SVG.SVG( "100%", "100%", "0 0 " & _W & " " & _H, _Marks, BLANK() ) )
    ```