# Compound.Pill

Create a pill SVG compound (rounded rectangle with auto-sized text centered inside)

<svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><rect x='1' y='1' width='93.1' height='18.032' rx='10' ry='10' fill='#EC008C' fill-opacity='0.2' stroke='#EC008C' stroke-width='1'  /><text x='47.5' y='11.368' dx='0' dy='0' fill='#EC008C' font-family='Segoe UI' font-size='12' text-anchor='middle' dominant-baseline='middle'  >DaxLib</text></svg>

=== "Syntax"

    ```dax
    DaxLib.SVG.Compound.Pill( x, y, width, height, txt, color, paddingX, paddingY )
    ```

    | Parameter | Type | Required | Default | Description |
    |:---:|:---:|:---:|:---:|---|
    | x | <span class="type-label int64">INT64</span> | :material-check: |  | The x position of compound |
    | y | <span class="type-label int64">INT64</span> | :material-check: |  | The y position of compound |
    | width | <span class="type-label int64">INT64</span> | :material-check: |  | The width of the compound |
    | height | <span class="type-label int64">INT64</span> | :material-check: |  | The height of the compound |
    | txt | <span class="type-label string">STRING</span> | :material-check: |  | The text to display |
    | color | <span class="type-label string">STRING</span> | :material-close: | `#!dax BLANK()` | Optional: The hex color of the pill, e.g., "#01B8AA80". Defaults to "#01B8AA" |
    | paddingX | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.05` | Optional: The horizontal padding percentage (0.0-1.0, e.g., 0.1 = 10% padding). Defaults to 0.05 |
    | paddingY | <span class="type-label number">DECIMAL</span> | :material-close: | `#!dax 0.02` | Optional: The vertical padding percentage (0.0-1.0, e.g., 0.1 = 10% padding). Defaults to 0.02 |

    <span class="type-label string">STRING</span> SVG Pill

=== "Example"

    ```dax hl_lines="5-14"
    DaxLib.SVG.SVG(
        500,
        100,
        BLANK(),
        DaxLib.SVG.Compound.Pill(
            0,                  // x
            0,                  // y
            500,                // width
            100,                // height
            MAX( Products[Brand] ), // txt
            "#EC008C",          // color
            0.05,               // paddingX
            0.02                // paddingY
        ),
        BLANK()
    )
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Compound.Pill' =
    		(
    			x: INT64,
    			y: INT64,
    			width: INT64,
    			height: INT64,
    			txt: STRING,
    			color: STRING = BLANK(),
    			paddingX: DOUBLE = 0.05,
    			paddingY: DOUBLE = 0.02
    		) =>
    
    		// Apply padding to dimensions
    		VAR _X = 			x + (width * (IF(ISBLANK(paddingX), 0, paddingX) / 2))
    		VAR _Y = 			y + (height * (IF(ISBLANK(paddingY), 0, paddingY) / 2))
    		VAR _Width = 		width * (1 - IF(ISBLANK(paddingX), 0, paddingX))
    		VAR _Height = 		height * (1 - IF(ISBLANK(paddingY), 0, paddingY))
    
    		VAR _Color = IF( NOT ISBLANK( color ), color, "#01B8AA" )
    
    		VAR _Pill = 
    			DaxLib.SVG.Element.Rect(
    				_X,
    				_Y,
    				_Width * 0.98,
    				_Height * 0.92,
    				10,
    				10,
    				DaxLib.SVG.Attr.Shapes(
    					_Color,
    					0.2,
    					BLANK(),
    					_Color,
    					1
    				)
    			)
    
    		// Auto-size font to fit text within pill
    		VAR _AvailableWidth = _Width * 0.90
    		VAR _CharWidthRatio = 0.55
    		VAR _TextWidthAtOne = LEN( txt ) * _CharWidthRatio
    		VAR _MaxFontFromWidth = IF( _TextWidthAtOne > 0, _AvailableWidth / _TextWidthAtOne, 12 )
    		VAR _MaxFontFromHeight = _Height * 0.75
    		VAR _FontSize = MAX( 4, MIN( 12, MIN( _MaxFontFromWidth, _MaxFontFromHeight ) ) )
    
    		VAR _TextElement = 
    			DaxLib.SVG.Element.Txt(
    				_X + (_Width * 0.50),
    				_Y + (_Height * 0.58),
    				txt,
    				0,
    				0,
    				DaxLib.SVG.Attr.Shapes( _Color ) &
    				DaxLib.SVG.Attr.Txt(
    					"Segoe UI",
    					_FontSize,
    					BLANK(),
    					BLANK(),
    					"middle",
    					"middle"
    				)
    			)
    
    		VAR _CombinedElements = 
    			_Pill & 
    			_TextElement
    
    		RETURN
    		
    			IF( NOT ISBLANK( txt ), _CombinedElements )
    ```