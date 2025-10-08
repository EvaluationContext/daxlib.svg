---
title: Def.Paths
nav_order: 6
parent: Defs
---

# DaxLib.SVG.Def.Paths

Generates a reusable `<path>`{:.xml} definition

## Syntax

```dax
DaxLib.SVG.Def.Paths( defId, d, attributes, transforms )
```

| Name       | Type   | Required | Description                                                                |
|:---:|:---:|:---:|---|
| defId      | <span class="type-label string">STRING</span> | Yes      | The unique identifier for the path                                        |
| d          | <span class="type-label string">STRING</span> | Yes      | The path data string (e.g., "M10 10 L90 90")                             |
| attributes | <span class="type-label string">STRING</span> | No       | Direct SVG attributes to apply (e.g., "fill='none' stroke='blue'"), can generate with `DaxLib.SVG.Attr.*` or manually |
| transforms | <span class="type-label string">STRING</span> | No       | Transformation to apply (can be generated with `DaxLib.SVG.Transforms`)    |

## Returns

<span class="type-label string">**STRING**</span> `<path>`{:.xml} definition

## Example

```dax
DaxLib.SVG.Def.Paths(
    "myPath",
    "M10 10 L90 90",
    DaxLib.SVG.Attr.Shapes(
        "none",     // fill
        BLANK(),    // fillOpacity
        BLANK(),    // fillRule
        "black",    // stroke
        2,          // strokeWidth
        BLANK(),    // strokeOpacity
        BLANK()     // opacity
    ),
    BLANK()
)
// Returns: <path id='myPath' d='M10 10 L90 90' fill='none' stroke='black' stroke-width='2' />
```

## Definition

```dax
function 'DaxLib.SVG.Def.Paths' =
    (
        defId: STRING,
        d: STRING,
        attributes: STRING,
        transforms: STRING
    ) =>

        "<path id='" & defId & "'" &
        " d='" & d & "'" &
        IF( NOT ISBLANK( attributes ), " " & attributes & " " ) &
        IF( NOT ISBLANK( transforms ), " transform='" & transforms & "'" ) &
        "/>"
```