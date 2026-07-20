# Viz.Line

Renders a line chart as an SVG data URI showing measure values across an axis

=== "With Axis"

    <svg width='500' height='200' xmlns='http://www.w3.org/2000/svg'><polyline points='48.38,161.42003 55.5786885245902,168.3254 62.7773770491803,172.03169 69.9760655737705,160.31657 77.1747540983607,100.2257 84.3734426229508,169.8836 91.572131147541,106.481555 98.7708196721312,170.857475 105.969508196721,99.224 113.168196721311,155.65787 120.366885245902,163.66034 127.565573770492,170.715965 134.764262295082,110.0042 141.962950819672,152.01995 149.161639344262,153.43187 156.360327868852,135.80036 163.559016393443,168.1664 170.757704918033,133.09418 177.956393442623,157.533275 185.155081967213,131.3102 192.353770491803,157.328165 199.552459016393,150.18191 206.751147540984,154.079 213.949836065574,51.03746 221.148524590164,166.86737 228.347213114754,160.82696 235.545901639344,138.836465 242.744590163934,124.028 249.943278688525,168.43511 257.141967213115,119.35022 264.340655737705,151.24085 271.539344262295,146.82224 278.738032786885,152.15192 285.936721311475,156.6389 293.135409836066,100.86488 300.334098360656,169.610915 307.532786885246,172.70267 314.731475409836,165.324275 321.930163934426,106.57139 329.128852459016,165.71462 336.327540983607,167.06294 343.526229508197,162.029 350.724918032787,162.188 357.923606557377,151.58747 365.122295081967,162.03695 372.320983606557,172.6502 379.519672131148,163.543475 386.718360655738,150.83222 393.917049180328,141.34628 401.115737704918,150.02768 408.314426229508,167.307005 415.513114754098,65.92145 422.711803278688,16.26416 429.910491803279,109.60352 437.109180327869,165.10883 444.307868852459,165.3203 451.506557377049,94.33475 458.705245901639,97.04252 465.90393442623,169.13471 473.10262295082,119.2421 480.30131147541,141.6293 487.5,151.11047' fill='none' stroke='#E044A7' stroke-width='1'  /><line x1='48.38' y1='173' x2='487.5' y2='173' stroke='#605E5C' stroke-width='1'  /><line x1='48.38' y1='14' x2='48.38' y2='173' stroke='#605E5C' stroke-width='1'  /><line x1='48.38' y1='173' x2='48.38' y2='176' stroke='#605E5C' stroke-width='1'  /><text x='48.38' y='180' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='start' dominant-baseline='hanging'  >01-Aug-25</text><line x1='158.16' y1='173' x2='158.16' y2='176' stroke='#605E5C' stroke-width='1'  /><text x='158.16' y='180' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='middle' dominant-baseline='hanging'  >16-Aug-25</text><line x1='267.94' y1='173' x2='267.94' y2='176' stroke='#605E5C' stroke-width='1'  /><text x='267.94' y='180' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='middle' dominant-baseline='hanging'  >31-Aug-25</text><line x1='377.72' y1='173' x2='377.72' y2='176' stroke='#605E5C' stroke-width='1'  /><text x='377.72' y='180' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='middle' dominant-baseline='hanging'  >15-Sep-25</text><line x1='487.5' y1='173' x2='487.5' y2='176' stroke='#605E5C' stroke-width='1'  /><text x='487.5' y='180' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='end' dominant-baseline='hanging'  >01-Oct-25</text><line x1='45.38' y1='173' x2='48.38' y2='173' stroke='#605E5C' stroke-width='1'  /><text x='41.38' y='173' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='end' dominant-baseline='middle'  >0</text><line x1='45.38' y1='141.2' x2='48.38' y2='141.2' stroke='#605E5C' stroke-width='1'  /><text x='41.38' y='141.2' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='end' dominant-baseline='middle'  >20000</text><line x1='45.38' y1='109.4' x2='48.38' y2='109.4' stroke='#605E5C' stroke-width='1'  /><text x='41.38' y='109.4' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='end' dominant-baseline='middle'  >40000</text><line x1='45.38' y1='77.6' x2='48.38' y2='77.6' stroke='#605E5C' stroke-width='1'  /><text x='41.38' y='77.6' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='end' dominant-baseline='middle'  >60000</text><line x1='45.38' y1='45.8' x2='48.38' y2='45.8' stroke='#605E5C' stroke-width='1'  /><text x='41.38' y='45.8' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='end' dominant-baseline='middle'  >80000</text><line x1='45.38' y1='14' x2='48.38' y2='14' stroke='#605E5C' stroke-width='1'  /><text x='41.38' y='14' fill='#605E5C' font-family='Segoe UI' font-size='8' text-anchor='end' dominant-baseline='middle'  >100000</text></svg>

=== "Without Axis"

    <svg width='500' height='200' xmlns='http://www.w3.org/2000/svg'><polyline points='12.5,176.8906 20.2868852459016,184.708 28.0737704918033,188.9038 35.8606557377049,175.6414 43.6475409836066,107.614 51.4344262295082,186.472 59.2213114754098,114.6961 67.0081967213115,187.5745 74.7950819672131,106.48 82.5819672131148,170.3674 90.3688524590164,179.4268 98.155737704918,187.4143 105.94262295082,118.684 113.729508196721,166.249 121.516393442623,167.8474 129.303278688525,147.8872 137.090163934426,184.528 144.877049180328,144.8236 152.66393442623,172.4905 160.450819672131,142.804 168.237704918033,172.2583 176.024590163934,164.1682 183.811475409836,168.58 191.598360655738,51.9292 199.385245901639,183.0574 207.172131147541,176.2192 214.959016393443,151.3243 222.745901639344,134.56 230.532786885246,184.8322 238.319672131148,129.2644 246.106557377049,165.367 253.893442622951,160.3648 261.680327868852,166.3984 269.467213114754,171.478 277.254098360656,108.3376 285.040983606557,186.1633 292.827868852459,189.6634 300.614754098361,181.3105 308.401639344262,114.7978 316.188524590164,181.7524 323.975409836066,183.2788 331.762295081967,177.58 339.549180327869,177.76 347.33606557377,165.7594 355.122950819672,177.589 362.909836065574,189.604 370.696721311475,179.2945 378.483606557377,164.9044 386.270491803279,154.1656 394.05737704918,163.9936 401.844262295082,183.5551 409.631147540984,68.779 417.418032786885,12.5632 425.204918032787,118.2304 432.991803278689,181.0666 440.77868852459,181.306 448.565573770492,100.945 456.352459016393,104.0104 464.139344262295,185.6242 471.926229508197,129.142 479.713114754098,154.486 487.5,165.2194' fill='none' stroke='#E044A7' stroke-width='1'  /></svg>

<div style="margin: 0; padding: 0;"></div>

=== "Syntax"

    ```dax
    DaxLib.SVG.Viz.Line( axisRef, measureRef, color, showAxis, width, height )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | axisRef | <span class="type-label anyref">ANYREF</span> <span class="type-label expr">EXPR</span> | :material-check: |  | Axis reference column |
    | measureRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: |  | Measure expression |
    | color | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional series color. Defaults to Power BI theme color |
    | showAxis | <span class="type-label boolean">BOOLEAN</span> | :material-close: | `#!dax FALSE()` | Optional axis toggle. Defaults to FALSE |
    | width | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 120` | Optional: SVG width. Defaults to 120 |
    | height | <span class="type-label int64">INT64</span> | :material-close: | `#!dax 48` | Optional: SVG height. Defaults to 48 |

    <span class="type-label string">STRING</span> SVG Line Chart

=== "Example"

    ```dax
    DaxLib.SVG.Viz.Line(
        Dates[Date],        // axisRef
        [Total Cost],       // measureRef
        ,                   // color
        TRUE,               // showAxis
        200,                // width
        60                  // height
    )
    // Returns an SVG data URI with an embedded line chart
    // Set as a measure with DataCategory = "ImageUrl"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Viz.Line' =
    		(
    			axisRef: ANYREF EXPR,
    			measureRef: NUMERIC EXPR,
    			color: STRING = BLANK(),
    			showAxis: BOOLEAN = FALSE(),
    			width: INT64 = 120,
    			height: INT64 = 48
    		) =>
    
    			VAR _Marks =
    				DaxLib.SVG.Compound.Line(
    					0, 0, width, height,
    					axisRef, measureRef, color, , , showAxis, 8
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Marks ), DaxLib.SVG.SVG( "100%", "100%", _Marks, "0 0 " & width & " " & height ) )
    ```