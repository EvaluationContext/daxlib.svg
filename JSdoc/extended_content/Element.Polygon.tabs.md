=== "Example"

	```dax
	DaxLib.SVG.Element.Polygon(
		"0,10 20,30 40,15",
		DaxLib.SVG.Attr.Shapes("#32CD32", "#800080", "1", BLANK(), BLANK(), BLANK(), BLANK()),
		"rotate(10)"
	)
	// Returns: <polygon points='0,10 20,30 40,15' fill='#32CD32' stroke='#800080' stroke-width='1' transform='rotate(10)' />
	```
