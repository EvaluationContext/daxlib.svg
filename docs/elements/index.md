---
icon: material/shape-outline
---

# Elements

This section documents the core SVG element functions available in DaxLib.SVG. These functions generate SVG primitives such as `#!xml <circle>`, `#!xml <rect>`, `#!xml <line>`, `#!xml <polygon>`, `#!xml <polyline>`, `#!xml <text>`, and `#!xml <<g>`. Use these to build up complex SVG graphics in Power BI.

=== "Circle"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><circle cx='50' cy='10' r='10%' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1'  /></svg>

=== "line"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><line x1='1' y1='5' x2='80' y2='5' stroke='#EC008C' stroke-width='2'  /></svg>

=== "Paths"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><path d='M10 10 L30 5 C50 0 70 20 90 15 L100 0' fill='none' stroke='#EC008C' stroke-width='2'  /></svg>

=== "Rect"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><rect x='50%' y='0%' width='40%' height='8' fill='#EC008C' fill-opacity='0.3' stroke='#EC008C' stroke-width='2' stroke-opacity='0.9'   transform='translate(-15) rotate(5) skewX(-20) '/></svg>

=== "Txt"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><text x='10' y='10' dx='0' dy='0' font-family='Arial' font-size='12'  >DaxLib</text></svg>

=== "UseDef"

    <svg width='500' height='100' viewbox= '0 0 100 20' xmlns='http://www.w3.org/2000/svg'><defs><circle id='Circle1' cx='0' cy='0' r='8' fill='#EC008C' fill-opacity='0.8' stroke='black' stroke-width='1' stroke-opacity='0.8'  /><circle id='Circle2' cx='0' cy='0' r='8' fill='#533285' fill-opacity='0.8' stroke='black' stroke-width='1' stroke-opacity='0.8'  /><path id='myPath' d='M10 10 L30 5 L90 15 L100 0' fill='none' fill-opacity='0.8' stroke='#EC008C'  /></defs><use href='#Circle1' x='20' y='10' transform='rotate(30) '/><use href='#Circle2' x='50' y='10'/><use href='#Circle1' x='80' y='10'/><use href='#myPath' y='5'/><use href='#myPath' y='10' transform='rotate(-10) '/></svg>