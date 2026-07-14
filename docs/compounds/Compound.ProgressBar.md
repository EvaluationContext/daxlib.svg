# Compound.ProgressBar

Creates a ProgressBar compound SVG visual

<svg width='500' height='50' xmlns='http://www.w3.org/2000/svg'><rect x='12.5' y='0.5' width='475' height='49' rx='3' ry='3' fill='#E1DFDD' fill-opacity='1' stroke='#E1DFDD' stroke-width='1'  /><rect x='12.5' y='0.5' width='380' height='49' rx='3' ry='3' fill='#E044A7' fill-opacity='0.95' stroke='#E044A7' stroke-width='1'  /></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.ProgressBar( x, y, width, height, valueRef, trackRef, fillColor, trackColor, orientation, paddingX, paddingY )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | x | <span class="type-label int64">INT64</span> | :material-check: |  | The x position of the compound |
    | y | <span class="type-label int64">INT64</span> | :material-check: |  | The y position of the compound |
    | width | <span class="type-label int64">INT64</span> | :material-check: |  | The width of the compound |
    | height | <span class="type-label int64">INT64</span> | :material-check: |  | The height of the compound |
    | valueRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-check: |  | Value expression (the bar measure) |
    | trackRef | <span class="type-label number">NUMERIC</span> <span class="type-label expr">EXPR</span> | :material-close: | `#!dax BLANK()` | Optional: Track measure (maximum value, can vary per context). Defaults to MAX(1, ABS(valueRef)) |
    | fillColor | <span class="type-label string">STRING</span> | :material-close: | `#!dax "#0F6CBD"` | Optional: Progress color. Defaults to "#0F6CBD" |
    | trackColor | <span class="type-label string">STRING</span> | :material-close: | `#!dax "#E1DFDD"` | Optional: Track color. Defaults to "#E1DFDD" |
    | orientation | <span class="type-label string">STRING</span> | :material-close: | `#!dax "Horizontal"` | "Horizontal" or "Vertical". Defaults to "Horizontal" |
    | paddingX | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.05` | Optional: Horizontal padding percentage (0.0-1.0). Defaults to 0.05 |
    | paddingY | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.02` | Optional: Vertical padding percentage (0.0-1.0). Defaults to 0.02 |

    <span class="type-label string">STRING</span> SVG Progress Bar

=== "Example"

    ```dax hl_lines="5-17"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.ProgressBar(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            [Completed],        // valueRef
            [Target],           // trackRef
            "#EC008C",          // fillColor
            "#E1DFDD",          // trackColor
            "Horizontal",       // orientation
            0.02,               // paddingX
            0.05                // paddingY
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.ProgressBar' =
    		(
    			x: INT64,
    			y: INT64,
    			width: INT64,
    			height: INT64,
    			valueRef: NUMERIC EXPR,
    			trackRef: NUMERIC EXPR = BLANK(),
    			fillColor: STRING = "#0F6CBD",
    			trackColor: STRING = "#E1DFDD",
    			orientation: STRING = "Horizontal",
    			paddingX: DOUBLE = 0.05,
    			paddingY: DOUBLE = 0.02
    		) =>
    
    			VAR _X = x + (width * (IF(ISBLANK(paddingX), 0, paddingX) / 2))
    			VAR _Y = y + (height * (IF(ISBLANK(paddingY), 0, paddingY) / 2))
    			VAR _Width = width * (1 - IF(ISBLANK(paddingX), 0, paddingX))
    			VAR _Height = height * (1 - IF(ISBLANK(paddingY), 0, paddingY))
    
    			VAR _Orientation = IF( orientation = "Vertical", "Vertical", "Horizontal" )
    			VAR _FillColor = IF( NOT ISBLANK( fillColor ), fillColor, "#0F6CBD" )
    			VAR _TrackColor = IF( NOT ISBLANK( trackColor ), trackColor, "#E1DFDD" )
    
    			VAR _Value = valueRef
    			VAR _Max = IF( ISBLANK( trackRef ), MAX( 1, ABS( _Value ) ), MAX( 1, ABS( trackRef ) ) )
    			VAR _Pct = MIN( 1, MAX( 0, DIVIDE( _Value, _Max, 0 ) ) )
    
    			VAR _Track =
    				DaxLib.SVG.Element.Rect(
    					_X,
    					_Y,
    					_Width,
    					_Height,
    					3,
    					3,
    					DaxLib.SVG.Attr.Shapes( _TrackColor, 1, BLANK(), _TrackColor, 1 )
    				)
    
    			VAR _FillW = IF( _Orientation = "Horizontal", _Width * _Pct, _Width )
    			VAR _FillH = IF( _Orientation = "Horizontal", _Height, _Height * _Pct )
    			VAR _FillX = _X
    			VAR _FillY = IF( _Orientation = "Horizontal", _Y, _Y + ( _Height - _FillH ) )
    
    			VAR _Fill =
    				DaxLib.SVG.Element.Rect(
    					_FillX,
    					_FillY,
    					_FillW,
    					_FillH,
    					3,
    					3,
    					DaxLib.SVG.Attr.Shapes( _FillColor, 0.95, BLANK(), _FillColor, 1 )
    				)
    
    			RETURN
    				IF( NOT ISBLANK( _Value ) && _Width > 0 && _Height > 0, _Track & _Fill )
    ```