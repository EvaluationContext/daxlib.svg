---
title: DaxLib.SVG.BulletChart.ActionDot
nav_order: 3
parent: Visuals
---

/// Example chart created using the DaxLib.SVG functions
	/// Generate SVG performance bar with target line and status indicator
	/// Returns SVG string for use in Table/Matrix visuals (set Image size: Height 25px, Width 100px)
	/// actual					EXPR			Actual measure to evaluate
	/// target					EXPR			Target measure to evaluate
	/// columnOne				ANYREF EXPR		Table scope for calculating axis max (e.g., 'Customers'[Key Account Name], multiple columns not yet supported)
	/// thresholdVeryBad		NUMERIC VAL		Performance thresholds (Percenage)
	/// thresholdBad			NUMERIC VAL		Performance thresholds (Percenage)
	/// thresholdGood			NUMERIC VAL		Performance thresholds (Percenage)
	/// thresholdVeryGood		NUMERIC VAL		Performance thresholds (Percenage)
	/// colourBadLow			STRING VAL		Status colours
	/// colourBadHigh			STRING VAL	 	Status colours
	/// colourGoodLow			STRING VAL		Status colours
	/// colourGoodHigh			STRING VAL		Status colours
	function 'DaxLib.SVG.BulletChart.ActionDot' =
			(
				actual: EXPR,
				target: EXPR,
				columnOne: ANYREF EXPR,
				thresholdVeryBad: NUMERIC VAL,
				thresholdBad: NUMERIC VAL,
				thresholdGood: NUMERIC VAL,
				thresholdVeryGood: NUMERIC VAL,
				colourBadLow: STRING VAL,
				colourBadHigh: STRING VAL,
				colourGoodLow: STRING VAL,
				colourGoodHigh: STRING VAL
			) =>
            
            // Chart dimensions
            VAR _BarMax = 100
            VAR _BarMin = 20

            // Fixed colour config
            VAR _ColourBackground = "#F5F5F5"
            VAR _ColourBaseline = "#797979"
            VAR _ColourTarget = "black"

            // Get current values
            VAR _Actual = actual
            VAR _Target = target

            // Calculate performance
            VAR _Performance = DIVIDE( _Actual - _Target, _Target )

            // Determine performance colour
            VAR _PerformanceColour =
                SWITCH(
                    true,
                    _Performance < thresholdVeryBad, 	colourBadLow,
                    _Performance < thresholdBad, 		colourBadHigh,
                    _Performance > thresholdVeryGood, 	colourGoodHigh,
                    _Performance > thresholdGood, 		colourGoodLow,
                    "#CFCFCF"  // Default grey
                )

            // Action dot fill color
            VAR _ActionDotFill =
                IF(
                    _Performance >= thresholdBad && _Performance <= thresholdGood,
                    "#FFFFFF00",  // Transparent
                    _PerformanceColour
                )

			// Scale
            VAR _AxisMax =
                MAX(
                    DaxLib.SVG.Calc.AxisMax( actual, columnOne, 1.1 ),
                    DaxLib.SVG.Calc.AxisMax( target, columnOne, 1.1 )
                )
            VAR _AxisRange = DaxLib.SVG.Calc.AxisRange( _AxisMax, 0 )
            VAR _ActualNormalized = DaxLib.SVG.Calc.Normalize( _Actual, 0, _AxisMax, _BarMin, _BarMax )
            VAR _TargetNormalized = DaxLib.SVG.Calc.Normalize( _Target, 0, _AxisMax, _BarMin, _BarMax )

            // Create SVG Elements
            VAR _ActionDot = 
                DaxLib.SVG.Element.Circle(
                    10,              		// cx
                    10,              		// cy
                    5,               		// r
                    DaxLib.SVG.Style.Common(
                        _ActionDotFill, 	// fill
                        BLANK(),       		// fillOpacity
                        BLANK(),       		// stroke
                        BLANK(),       		// strokeWidth
                        BLANK(),       		// strokeOpacity
                        BLANK()        		// opacity
                    ),				   		// style
                    BLANK(),           		// class
                    BLANK()            		// transform
                )

            VAR _BarBackground =
                DaxLib.SVG.Element.Rect(
                    _BarMin, 				// x
                    2,                  	// y
                    _BarMax, 				// width
                    16,                 	// height (80% of 20)
                    BLANK(),              	// rx
                    BLANK(),              	// ry
                    DaxLib.SVG.Style.Common(
                        _ColourBackground, 	// fill
                        BLANK(),           	// fillOpacity
                        BLANK(),           	// stroke
                        BLANK(),           	// strokeWidth
                        BLANK(),           	// strokeOpacity
                        BLANK()            	// opacity
                    ),						// style
                    BLANK(),               	// class
                    BLANK()                	// transform
                )

            VAR _ActualBar =
                DaxLib.SVG.Element.Rect(
                    _BarMin,						// x
                    5,                           	// y
                    _ActualNormalized, 				// width
                    10,                           	// height (50% of 20)
                    BLANK(),                        // rx
                    BLANK(),                        // ry
                    DaxLib.SVG.Style.Common(
                        "#CFCFCF",             		// fill
                        BLANK(),                   	// fillOpacity
                        BLANK(),                   	// stroke
                        BLANK(),                   	// strokeWidth
                        BLANK(),                   	// strokeOpacity
                        BLANK()                    	// opacity
                    ),
                    BLANK(),                        // class
                    BLANK()                         // transform
                )

            VAR _TargetLine =
                DaxLib.SVG.Element.Rect(
                    _TargetNormalized,				// x
                    2,                            	// y
                    2,                            	// width
                    16,                           	// height
                    BLANK(),                        // rx
                    BLANK(),                        // ry
                    DaxLib.SVG.Style.Common(
                        _ColourTarget,              // fill
                        BLANK(),                   	// fillOpacity
                        BLANK(),                   	// stroke
                        BLANK(),                   	// strokeWidth
                        BLANK(),                   	// strokeOpacity
                        BLANK()                    	// opacity
                    ),
                    BLANK(),                        // class
                    BLANK()                         // transform
                )

            VAR _BarBaseline =
                DaxLib.SVG.Element.Rect(
                    _BarMin,							// x
                    4,                           	// y
                    1,                           	// width
                    12,                          	// height
                    BLANK(),                       	// rx
                    BLANK(),                       	// ry
                    DaxLib.SVG.Style.Common(
                        _ColourBaseline,           	// fill
                        BLANK(),                   	// fillOpacity
                        BLANK(),                   	// stroke
                        BLANK(),                   	// strokeWidth
                        BLANK(),                   	// strokeOpacity
                        BLANK()                    	// opacity
                    ),
                    BLANK(),                       	// class
                    BLANK()                        	// transform
                )

            RETURN

                DaxLib.SVG.SVG(
                    100,           	// width
                    20,            	// height
                    BLANK(),        // viewbox
                    _ActionDot &
					_BarBackground &
					_ActualBar &
					_TargetLine &
					_BarBaseline,   // contents
                    _Actual         // sortValue
                )