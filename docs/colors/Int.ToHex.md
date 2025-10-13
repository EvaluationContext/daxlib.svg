---
comments: true
---

# Color.Int.ToHex

Int to Hex conversion

=== "Syntax"

    ```dax
    DaxLib.SVG.Color.Int.ToHex( number, padTo )
    ```

    | Name   | Type  | Required | Description                                    |
    |:---:|:---:|:---:|---|
    | number | <span class="type-label int64">INT64</span> | :material-check: | The integer to convert                        |
    | padTo  | <span class="type-label int64">INT64</span> | :material-close: | Minimum number of characters in result |

    <span class="type-label string">STRING</span> Hexadecimal representation of the integer

=== "Example"

    ```dax
    DaxLib.SVG.Color.Int.ToHex(255, 2)
    // Returns: "FF"
    ```

=== "Definition"

    ```dax
    function 'DaxLib.SVG.Color.Int.ToHex' =
        (
            number: INT64,
            padTo: INT64
        ) =>
        
            VAR MinPadding = IF( number = 0, 1, CEILING( LOG( number + 1, 16 ), 1 ) )
            VAR ActualPadding = MAX( MinPadding, IF( ISBLANK( padTo ), MinPadding, padTo ) )
            VAR BitTable = GENERATESERIES( 1, ActualPadding )
            VAR Hex =
                CONCATENATEX(
                    BitTable,
                    VAR c = MOD( TRUNC( number / POWER( 16, [Value] - 1 ) ), 16 )
                    RETURN
                        SWITCH( c, 10, "A", 11, "B", 12, "C", 13, "D", 14, "E", 15, "F", c ),
                    "",
                    [Value],
                    DESC
                )
        
            RETURN Hex
    ```