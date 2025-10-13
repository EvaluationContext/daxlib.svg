---
comments: true
---

# Color.Hex.ToInt

Hex to Int conversion

=== "Syntax"

    ```dax
    DaxLib.SVG.Color.Hex.ToInt(hex)
    ```

    | Name | Type   | Required | Description                                  |
    |:---:|:---:|:---:|---|
    | hex  | <span class="type-label string">STRING</span> | :material-check: | The hex value to convert i.e "1A"          |

    <span class="type-label number">NUMERIC</span> Integer representation of the hexadecimal value

=== "Example"

    ```dax
    DaxLib.SVG.Color.Hex.ToInt("FF")
    // Returns: 255
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Color.Hex.ToInt' =
        (
            hex: STRING
        ) =>
        
            VAR CleanHex = IF( LEFT( hex, 1 ) = "#", MID( hex, 2, LEN( hex ) - 1), hex )
            VAR Result =
                SUMX(
                    GENERATESERIES( 1, LEN( CleanHex ) ),
                    VAR Pos = [Value]
                    VAR c = MID( CleanHex, Pos, 1 )
                    VAR DigitValue = SWITCH( UPPER( c ), "A", 10, "B", 11, "C", 12, "D", 13, "E", 14, "F", 15, VALUE( c ) )
                    RETURN
                        DigitValue * POWER( 16, LEN( hex ) - Pos )
                )
        
            RETURN Result
    ```