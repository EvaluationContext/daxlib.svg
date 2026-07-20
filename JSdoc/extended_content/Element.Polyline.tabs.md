=== "Example"

	```dax
	DaxLib.SVG.Element.Polyline(
		"0,10 20,30 40,15",
		DaxLib.SVG.Attr.Shapes("none", BLANK(), BLANK(), "#0078D4", "2", BLANK(), BLANK()),
		"translate(5,5)"
	)
	// Returns: <polyline points='0,10 20,30 40,15' fill='none' stroke='#0078D4' stroke-width='2' transform='translate(5,5)' />
	```
