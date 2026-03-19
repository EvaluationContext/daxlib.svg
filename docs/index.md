---
title: Home
---

# DaxLib.SVG

Easily embed performant SVG charts directly in Power BI tables, matrices and cards.

[Download From DaxLib :material-download:](https://daxlib.org/package/daxlib.svg/){ .md-button .md-button--primary }
[Download Example PBIP :material-download:](https://github.com/EvaluationContext/daxlib.svg/tree/main/PowerBI){ .md-button }

<div class="carousel-section">
<h2>Explore the Library</h2>
<p class="section-sub">Browse namespaces &mdash; from low-level SVG primitives to complete chart visualizations.</p>
  <div class="carousel-wrapper" id="ns-carousel">
    <button class="carousel-btn carousel-btn--prev" aria-label="Previous" onclick="carouselPrev('ns-carousel')">&#9664;</button>
    <div class="carousel-viewport">
    <div class="carousel-track">
      <a class="ns-card" href="svg/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M5.13 10.71h3.74L6.22 8.06c-1.01 0-1.83-.82-1.83-1.84a1.83 1.83 0 0 1 1.83-1.83c1.02 0 1.84.82 1.84 1.83l2.65 2.65V5.13a1.84 1.84 0 0 1 0-2.59 1.81 1.81 0 0 1 2.58 0c.71.71.71 1.87 0 2.59v3.74l2.66-2.65a1.83 1.83 0 0 1 3.66 0c0 1.02-.82 1.84-1.83 1.84l-2.65 2.65h3.74a1.84 1.84 0 0 1 2.59 0c.72.71.72 1.87 0 2.58-.71.71-1.87.71-2.59 0h-3.74l2.65 2.66c1.01 0 1.83.81 1.83 1.83a1.83 1.83 0 0 1-1.83 1.83c-1.02 0-1.83-.82-1.83-1.83l-2.66-2.65v3.74c.71.72.71 1.88 0 2.59-.71.72-1.87.72-2.58 0a1.84 1.84 0 0 1 0-2.59v-3.74l-2.65 2.65c0 1.01-.82 1.83-1.84 1.83a1.83 1.83 0 0 1 0-3.66l2.65-2.66H5.13c-.72.71-1.88.71-2.59 0a1.81 1.81 0 0 1 0-2.58 1.84 1.84 0 0 1 2.59 0"/></svg></span>
          <span class="ns-card-title">SVG</span>
        </div>
        <div class="ns-card-desc">Wraps SVG content in a valid container for use in Power BI visuals</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-core">Core</span>
        </div>
      </a>
      <a class="ns-card" href="scales/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="m10.59 12 4-4H11V6h7v7h-2V9.41l-4 4V16h8V4H8v8zM22 2v16H12v4H2V12h4V2zM10 14H4v6h6z"/></svg></span>
          <span class="ns-card-title">Scales</span>
        </div>
        <div class="ns-card-desc">Normalize and map data values to SVG coordinates, colors, and other visual properties</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-data">Data</span>
        </div>
      </a>
      <a class="ns-card" href="data/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C7.58 3 4 4.79 4 7v10c0 2.21 3.59 4 8 4s8-1.79 8-4V7c0-2.21-3.58-4-8-4m6 14c0 .5-2.13 2-6 2s-6-1.5-6-2v-2.23c1.61.78 3.72 1.23 6 1.23s4.39-.45 6-1.23zm0-4.55c-1.3.95-3.58 1.55-6 1.55s-4.7-.6-6-1.55V9.64c1.47.83 3.61 1.36 6 1.36s4.53-.53 6-1.36zM12 9C8.13 9 6 7.5 6 7s2.13-2 6-2 6 1.5 6 2-2.13 2-6 2"/></svg></span>
          <span class="ns-card-title">Data</span>
        </div>
        <div class="ns-card-desc">Prepare and structure data for visualization — axis evaluation, measure materialization, ranges</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-data">Data</span>
        </div>
      </a>
      <a class="ns-card" href="axes/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="m12 2 4 4h-3v7.85l6.53 3.76L21 15.03l1.5 5.47-5.5 1.46 1.53-2.61L12 15.58l-6.53 3.77L7 21.96 1.5 20.5 3 15.03l1.47 2.58L11 13.85V6H8z"/></svg></span>
          <span class="ns-card-title">Axes</span>
        </div>
        <div class="ns-card-desc">Axis layout, rendering, and positioning — tick calculation, label sizing, axis line rendering</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-render">Render</span>
        </div>
      </a>
      <a class="ns-card" href="attributes/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19 11.5s-2 2.17-2 3.5a2 2 0 0 0 2 2 2 2 0 0 0 2-2c0-1.33-2-3.5-2-3.5M5.21 10 10 5.21 14.79 10m1.77-1.06L7.62 0 6.21 1.41l2.38 2.38-5.15 5.15c-.59.56-.59 1.53 0 2.12l5.5 5.5c.29.29.68.44 1.06.44s.77-.15 1.06-.44l5.5-5.5c.59-.59.59-1.56 0-2.12"/></svg></span>
          <span class="ns-card-title">Attributes</span>
        </div>
        <div class="ns-card-desc">Generate attribute strings for fill, stroke, opacity, and text formatting</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-style">Style</span>
        </div>
      </a>
      <a class="ns-card" href="transforms/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M7.34 6.41.86 12.9l6.49 6.48 6.49-6.48zM3.69 12.9l3.66-3.66L11 12.9l-3.66 3.66zm15.67-6.26A8.95 8.95 0 0 0 13 4V.76L8.76 5 13 9.24V6c1.79 0 3.58.68 4.95 2.05a7.007 7.007 0 0 1 0 9.9 6.97 6.97 0 0 1-7.79 1.44l-1.49 1.49C10 21.62 11.5 22 13 22c2.3 0 4.61-.88 6.36-2.64a8.98 8.98 0 0 0 0-12.72"/></svg></span>
          <span class="ns-card-title">Transforms</span>
        </div>
        <div class="ns-card-desc">Create SVG transform attribute values for rotating, scaling, and translating elements</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-render">Render</span>
        </div>
      </a>
      <a class="ns-card" href="elements/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M11 13.5v8H3v-8zm-2 2H5v4h4zM12 2l5.5 9h-11zm0 3.86L10.08 9h3.84zM17.5 13c2.5 0 4.5 2 4.5 4.5S20 22 17.5 22 13 20 13 17.5s2-4.5 4.5-4.5m0 2a2.5 2.5 0 0 0-2.5 2.5 2.5 2.5 0 0 0 2.5 2.5 2.5 2.5 0 0 0 2.5-2.5 2.5 2.5 0 0 0-2.5-2.5"/></svg></span>
          <span class="ns-card-title">Elements</span>
        </div>
        <div class="ns-card-desc">Core SVG primitives — circle, rect, line, polygon, polyline, text, and group elements</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-core">Core</span>
        </div>
      </a>
      <a class="ns-card" href="defs/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 5V1L7 6l5 5V7a6 6 0 0 1 6 6 6 6 0 0 1-6 6 6 6 0 0 1-6-6H4a8 8 0 0 0 8 8 8 8 0 0 0 8-8 8 8 0 0 0-8-8"/></svg></span>
          <span class="ns-card-title">Defs</span>
        </div>
        <div class="ns-card-desc">Reusable SVG definitions — gradients, clip paths, and shapes invoked via UseDef</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-core">Core</span>
        </div>
      </a>
      <a class="ns-card" href="compounds/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M2.5 2.75a.75.75 0 0 0-1.5 0v18.5c0 .414.336.75.75.75H20a.75.75 0 0 0 0-1.5H2.5z"/><path d="M22.28 7.78a.75.75 0 0 0-1.06-1.06l-5.72 5.72-3.72-3.72a.75.75 0 0 0-1.06 0l-6 6a.75.75 0 1 0 1.06 1.06l5.47-5.47 3.72 3.72a.75.75 0 0 0 1.06 0z"/></svg></span>
          <span class="ns-card-title">Compounds</span>
        </div>
        <div class="ns-card-desc">Higher-level components combining multiple elements into complete chart visualizations</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-viz">Viz</span>
        </div>
      </a>
      <a class="ns-card" href="viz/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M9 17H7v-7h2zm4 0h-2V7h2zm4 0h-2v-4h2zm2 2H5V5h14v14.1M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2"/></svg></span>
          <span class="ns-card-title">Viz</span>
        </div>
        <div class="ns-card-desc">Quick-use visualizations with sensible defaults — produce complete SVG data URIs for Power BI</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-viz">Viz</span>
        </div>
      </a>
      <a class="ns-card" href="colors/">
        <div class="ns-card-header">
          <span class="ns-card-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="m2.5 19.6 1.3.6v-9L1.4 17c-.4 1.1.1 2.2 1.1 2.6M15.2 4.8l5 12-7.3 3-5-11.9v-.1zm.1-2c-.3 0-.5 0-.8.1L7.1 6c-.7.3-1.2 1-1.2 1.8 0 .2 0 .5.1.8l5 11.9c.3.8 1 1.2 1.8 1.2.3 0 .5 0 .8-.1l7.4-3.1c1-.4 1.5-1.6 1.1-2.6L17.1 4c-.3-.8-1.1-1.2-1.8-1.2m-4.8 7.1c-.6 0-1-.4-1-1s.4-1 1-1 1 .5 1 1-.4 1-1 1m-4.6 9.9c0 1.1.9 2 2 2h1.4l-3.4-8.3z"/></svg></span>
          <span class="ns-card-title">Colors</span>
        </div>
        <div class="ns-card-desc">Theming and color interpolation for dynamic, accessible SVG visualizations</div>
        <div class="ns-card-meta">
          <span class="ns-card-badge ns-badge-style">Style</span>
        </div>
      </a>
    </div>
    </div>
    <button class="carousel-btn carousel-btn--next" aria-label="Next" onclick="carouselNext('ns-carousel')">&#9654;</button>
    <div class="carousel-dots" id="ns-carousel-dots"></div>
  </div>
</div>

<div class="carousel-section">
  <!-- <h2>Examples</h2> -->
  <p class="section-sub">Each chart type ships with a quick-use <strong>Viz</strong> function and a composable <strong>Compound</strong> function.</p>
  <div class="carousel-wrapper" id="viz-carousel">
    <button class="carousel-btn carousel-btn--prev" aria-label="Previous" onclick="carouselPrev('viz-carousel')">&#9664;</button>
    <div class="carousel-viewport">
    <div class="carousel-track"><div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 100 20' width='100' height='20' xmlns='http://www.w3.org/2000/svg'><rect x='2.70212765957447' y='18.201664' width='1.61702127659574' height='1.398336' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='4.72340425531915' y='19.03552' width='1.61702127659574' height='0.56448' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='6.74468085106383' y='19.483072' width='1.61702127659574' height='0.116928000000001' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='8.76595744680851' y='18.068416' width='1.61702127659574' height='1.531584' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='10.7872340425532' y='10.81216' width='1.61702127659574' height='8.78784' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='12.8085106382979' y='19.22368' width='1.61702127659574' height='0.37632' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='14.8297872340426' y='11.567584' width='1.61702127659574' height='8.032416' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='16.8510638297872' y='19.34128' width='1.61702127659574' height='0.25872' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='18.8723404255319' y='10.6912' width='1.61702127659574' height='8.9088' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='20.8936170212766' y='17.505856' width='1.61702127659574' height='2.094144' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='22.9148936170213' y='18.472192' width='1.61702127659574' height='1.127808' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='24.936170212766' y='19.324192' width='1.61702127659574' height='0.275808000000001' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='26.9574468085106' y='11.99296' width='1.61702127659574' height='7.60704' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='28.9787234042553' y='17.06656' width='1.61702127659574' height='2.53344' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='31' y='17.237056' width='1.61702127659574' height='2.362944' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='33.0212765957447' y='15.107968' width='1.61702127659574' height='4.492032' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='35.0425531914894' y='19.01632' width='1.61702127659574' height='0.583680000000001' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='37.063829787234' y='14.781184' width='1.61702127659574' height='4.818816' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='39.0851063829787' y='17.73232' width='1.61702127659574' height='1.86768' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='41.1063829787234' y='14.56576' width='1.61702127659574' height='5.03424' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='43.1276595744681' y='17.707552' width='1.61702127659574' height='1.892448' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='45.1489361702128' y='16.844608' width='1.61702127659574' height='2.755392' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='47.1702127659574' y='17.3152' width='1.61702127659574' height='2.2848' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='49.1914893617021' y='4.872448' width='1.61702127659574' height='14.727552' rx='0' ry='0' fill='#2E8B57' stroke-width='1'  /> <rect x='51.2127659574468' y='18.859456' width='1.61702127659574' height='0.740544' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='53.2340425531915' y='18.130048' width='1.61702127659574' height='1.469952' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='55.2553191489362' y='15.474592' width='1.61702127659574' height='4.125408' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='57.2765957446809' y='13.6864' width='1.61702127659574' height='5.9136' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='59.2978723404255' y='19.048768' width='1.61702127659574' height='0.551231999999999' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='61.3191489361702' y='13.121536' width='1.61702127659574' height='6.478464' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='63.3404255319149' y='16.97248' width='1.61702127659574' height='2.62752' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='65.3617021276596' y='16.438912' width='1.61702127659574' height='3.161088' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='67.3829787234043' y='17.082496' width='1.61702127659574' height='2.517504' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='69.4042553191489' y='17.62432' width='1.61702127659574' height='1.97568' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='71.4255319148936' y='10.889344' width='1.61702127659574' height='8.710656' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='73.4468085106383' y='19.190752' width='1.61702127659574' height='0.409248000000002' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='75.468085106383' y='19.564096' width='1.61702127659574' height='3.59039999999986E-02' rx='0' ry='0' fill='#D04848' stroke-width='1'  /> <rect x='77.4893617021277' y='18.67312' width='1.61702127659574' height='0.926880000000001' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='79.5106382978723' y='11.578432' width='1.61702127659574' height='8.021568' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='81.531914893617' y='18.720256' width='1.61702127659574' height='0.879743999999999' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='83.5531914893617' y='18.883072' width='1.61702127659574' height='0.716927999999999' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='85.5744680851064' y='18.2752' width='1.61702127659574' height='1.3248' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='87.5957446808511' y='18.2944' width='1.61702127659574' height='1.3056' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='89.6170212765958' y='17.014336' width='1.61702127659574' height='2.585664' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='91.6382978723404' y='18.27616' width='1.61702127659574' height='1.32384' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='93.6595744680851' y='19.55776' width='1.61702127659574' height='4.22399999999996E-02' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /> <rect x='95.6808510638298' y='18.45808' width='1.61702127659574' height='1.14192' rx='0' ry='0' fill='#E044A7' stroke-width='1'  /></svg>
  </div>
  <div class="gallery-label">Bars</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Bars</span>
    <div class="gallery-links">
      <a href="viz/Viz.Bars/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Bars/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 100 20' width='100' height='20' xmlns='http://www.w3.org/2000/svg'><polyline points='2.5,17.68906 4.05737704918033,18.4708 5.61475409836066,18.89038 7.17213114754098,17.56414 8.72950819672131,10.7614 10.2868852459016,18.6472 11.844262295082,11.46961 13.4016393442623,18.75745 14.9590163934426,10.648 16.5163934426229,17.03674 18.0737704918033,17.94268 19.6311475409836,18.74143 21.1885245901639,11.8684 22.7459016393443,16.6249 24.3032786885246,16.78474 25.8606557377049,14.78872 27.4180327868852,18.4528 28.9754098360656,14.48236 30.5327868852459,17.24905 32.0901639344262,14.2804 33.6475409836066,17.22583 35.2049180327869,16.41682 36.7622950819672,16.858 38.3196721311475,5.19292 39.8770491803279,18.30574 41.4344262295082,17.62192 42.9918032786885,15.13243 44.5491803278689,13.456 46.1065573770492,18.48322 47.6639344262295,12.92644 49.2213114754098,16.5367 50.7786885245902,16.03648 52.3360655737705,16.63984 53.8934426229508,17.1478 55.4508196721311,10.83376 57.0081967213115,18.61633 58.5655737704918,18.96634 60.1229508196721,18.13105 61.6803278688525,11.47978 63.2377049180328,18.17524 64.7950819672131,18.32788 66.3524590163934,17.758 67.9098360655738,17.776 69.4672131147541,16.57594 71.0245901639344,17.7589 72.5819672131148,18.9604 74.1393442622951,17.92945 75.6967213114754,16.49044 77.2540983606557,15.41656 78.8114754098361,16.39936 80.3688524590164,18.35551 81.9262295081967,6.8779 83.483606557377,1.25632 85.0409836065574,11.82304 86.5983606557377,18.10666 88.155737704918,18.1306 89.7131147540984,10.0945 91.2704918032787,10.40104 92.827868852459,18.56242 94.3852459016393,12.9142 95.9426229508197,15.4486 97.5,16.52194' fill='none' stroke='#E044A7' stroke-width='1'  /><circle cx='58.5655737704918' cy='18.96634' r='2' fill='white' fill-opacity='0.7'  /><circle cx='58.5655737704918' cy='18.96634' r='1.5' fill='#D04848'  /><circle cx='83.483606557377' cy='1.25632' r='2' fill='white' fill-opacity='0.7'  /><circle cx='83.483606557377' cy='1.25632' r='1.5' fill='#2E8B57'  /></svg>
  </div>
  <div class="gallery-label">Line</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Line</span>
    <div class="gallery-links">
      <a href="viz/Viz.Line/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Line/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 100 20' width='100' height='20' xmlns='http://www.w3.org/2000/svg'><polygon points='2.5,19.8 2.5,18.372532 4.05737704918033,19.22376 5.61475409836066,19.680636 7.17213114754098,18.236508 8.72950819672131,10.82908 10.2868852459016,19.41584 11.844262295082,11.600242 13.4016393442623,19.53589 14.9590163934426,10.7056 16.5163934426229,17.662228 18.0737704918033,18.648696 19.6311475409836,19.518446 21.1885245901639,12.03448 22.7459016393443,17.21378 24.3032786885246,17.387828 25.8606557377049,15.214384 27.4180327868852,19.20416 28.9754098360656,14.880792 30.5327868852459,17.89341 32.0901639344262,14.66088 33.6475409836066,17.868126 35.2049180327869,16.987204 36.7622950819672,17.4676 38.3196721311475,4.765624 39.8770491803279,19.044028 41.4344262295082,18.299424 42.9918032786885,15.588646 44.5491803278689,13.7632 46.1065573770492,19.237284 47.6639344262295,13.186568 49.2213114754098,17.11774 50.7786885245902,16.573056 52.3360655737705,17.230048 53.8934426229508,17.78316 55.4508196721311,10.907872 57.0081967213115,19.382226 58.5655737704918,19.763348 60.1229508196721,18.85381 61.6803278688525,11.611316 63.2377049180328,18.901928 64.7950819672131,19.068136 66.3524590163934,18.4476 67.9098360655738,18.4672 69.4672131147541,17.160468 71.0245901639344,18.44858 72.5819672131148,19.75688 74.1393442622951,18.63429 75.6967213114754,17.067368 77.2540983606557,15.898032 78.8114754098361,16.968192 80.3688524590164,19.098222 81.9262295081967,6.60038 83.483606557377,0.479104 85.0409836065574,11.985088 86.5983606557377,18.827252 88.155737704918,18.85332 89.7131147540984,10.1029 91.2704918032787,10.436688 92.827868852459,19.323524 94.3852459016393,13.17324 95.9426229508197,15.93292 97.5,17.101668 97.5,19.8' fill='#E044A7' fill-opacity='0.2' stroke='none' stroke-width='0'  /><polyline points='2.5,18.372532 4.05737704918033,19.22376 5.61475409836066,19.680636 7.17213114754098,18.236508 8.72950819672131,10.82908 10.2868852459016,19.41584 11.844262295082,11.600242 13.4016393442623,19.53589 14.9590163934426,10.7056 16.5163934426229,17.662228 18.0737704918033,18.648696 19.6311475409836,19.518446 21.1885245901639,12.03448 22.7459016393443,17.21378 24.3032786885246,17.387828 25.8606557377049,15.214384 27.4180327868852,19.20416 28.9754098360656,14.880792 30.5327868852459,17.89341 32.0901639344262,14.66088 33.6475409836066,17.868126 35.2049180327869,16.987204 36.7622950819672,17.4676 38.3196721311475,4.765624 39.8770491803279,19.044028 41.4344262295082,18.299424 42.9918032786885,15.588646 44.5491803278689,13.7632 46.1065573770492,19.237284 47.6639344262295,13.186568 49.2213114754098,17.11774 50.7786885245902,16.573056 52.3360655737705,17.230048 53.8934426229508,17.78316 55.4508196721311,10.907872 57.0081967213115,19.382226 58.5655737704918,19.763348 60.1229508196721,18.85381 61.6803278688525,11.611316 63.2377049180328,18.901928 64.7950819672131,19.068136 66.3524590163934,18.4476 67.9098360655738,18.4672 69.4672131147541,17.160468 71.0245901639344,18.44858 72.5819672131148,19.75688 74.1393442622951,18.63429 75.6967213114754,17.067368 77.2540983606557,15.898032 78.8114754098361,16.968192 80.3688524590164,19.098222 81.9262295081967,6.60038 83.483606557377,0.479104 85.0409836065574,11.985088 86.5983606557377,18.827252 88.155737704918,18.85332 89.7131147540984,10.1029 91.2704918032787,10.436688 92.827868852459,19.323524 94.3852459016393,13.17324 95.9426229508197,15.93292 97.5,17.101668' fill='none' stroke='#E044A7' stroke-width='1'  /><circle cx='58.5655737704918' cy='19.763348' r='2' fill='white' fill-opacity='0.7'  /><circle cx='58.5655737704918' cy='19.763348' r='1.5' fill='#D04848'  /><circle cx='83.483606557377' cy='0.479104' r='2' fill='white' fill-opacity='0.7'  /><circle cx='83.483606557377' cy='0.479104' r='1.5' fill='#2E8B57'  /></svg>
  </div>
  <div class="gallery-label">Area</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Area</span>
    <div class="gallery-links">
      <a href="viz/Viz.Area/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Area/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 120 20' xmlns='http://www.w3.org/2000/svg'><rect x='0' y='0' width='120' height='20' rx='3' ry='3' fill='#E1DFDD'/><rect x='0' y='0' width='84' height='20' rx='3' ry='3' fill='#EC008C' fill-opacity='0.95'/></svg>
  </div>
  <div class="gallery-label">ProgressBar</div>
  <div class="gallery-overlay">
    <span class="gallery-name">ProgressBar</span>
    <div class="gallery-links">
      <a href="viz/Viz.ProgressBar/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.ProgressBar/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 120 24' xmlns='http://www.w3.org/2000/svg'><rect x='1' y='1' width='110' height='22' rx='11' ry='11' fill='#EC008C' fill-opacity='0.2' stroke='#EC008C' stroke-width='1'/><text x='56' y='13' fill='#EC008C' font-family='Segoe UI' font-size='12' text-anchor='middle' dominant-baseline='middle'>DaxLib</text></svg>
  </div>
  <div class="gallery-label">Pill</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Pill</span>
    <div class="gallery-links">
      <a href="viz/Viz.Pill/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Pill/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 120 24' xmlns='http://www.w3.org/2000/svg'><line x1='5' y1='12' x2='25' y2='12' stroke='#EC008C' stroke-width='1'/><line x1='70' y1='12' x2='90' y2='12' stroke='#EC008C' stroke-width='1'/><line x1='5' y1='5' x2='5' y2='19' stroke='#EC008C' stroke-width='1'/><line x1='90' y1='5' x2='90' y2='19' stroke='#EC008C' stroke-width='1'/><rect x='25' y='5' width='45' height='14' rx='2' ry='2' fill='#EC008C' fill-opacity='0.5' stroke='#EC008C' stroke-width='1'/><line x1='45' y1='5' x2='45' y2='19' stroke='#EC008C' stroke-width='2'/><circle cx='100' cy='12' r='2' fill='#EC008C'/><circle cx='110' cy='12' r='2' fill='#EC008C'/></svg>
  </div>
  <div class="gallery-label">Boxplot</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Boxplot</span>
    <div class="gallery-links">
      <a href="viz/Viz.Boxplot/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Boxplot/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 120 20' width='100' height='20' xmlns='http://www.w3.org/2000/svg'><circle cx='9.51879767894822' cy='6.63958' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='5.33334685927609' cy='10.12348' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='3.08690756370719' cy='11.9061' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='10.1876217334848' cy='7.71758' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='46.6096210030839' cy='10.02156' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='4.38889790618406' cy='13.51428' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='42.8178512011037' cy='14.31151' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='3.79861731050154' cy='8.09243' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='47.2167667586431' cy='8.95336' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='13.0113313585457' cy='5.82226' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='8.16091137802305' cy='11.33868' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='3.88438869501704' cy='8.35213' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='40.6827219607207' cy='11.36416' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='15.2163305469891' cy='12.60386' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='14.3605441486772' cy='8.22326' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='25.0472731699399' cy='9.78636' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='5.42971920142834' cy='12.91648' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='26.6875304333712' cy='6.81696' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='11.8746195828599' cy='6.02463' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='27.7688281123194' cy='13.54956' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='11.9989399042363' cy='14.14393' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='16.3303948222691' cy='6.66506' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='13.9683087161175' cy='6.95416' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='76.4233687713034' cy='14.75496' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='6.21708123681221' cy='11.92178' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='9.87826651517611' cy='8.53588' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='23.2070432965428' cy='13.71861' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='32.1826813828924' cy='6.90516' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='5.26684994319104' cy='11.32398' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='35.0179556890115' cy='11.57976' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='15.6885550235351' cy='5.92026' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='18.3667424119461' cy='10.47236' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='15.1363415030028' cy='7.97336' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='12.4167140074663' cy='8.26736' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='46.2222041876319' cy='13.95136' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='4.55417647297517' cy='7.50443' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='2.6802162798247' cy='10.6027' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='7.15237481739977' cy='5.44643' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='42.7634008277877' cy='9.39926' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='6.915780717416' cy='10.42728' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='6.09854325596494' cy='9.77068' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='9.14969160850511' cy='11.88748' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='9.05331926635287' cy='5.40968' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='15.4784633176432' cy='7.25306' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='9.1448729913975' cy='13.79358' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='2.71201915273495' cy='9.0298' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='8.23174504950495' cy='12.70823' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='15.9362319428664' cy='12.57936' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='21.6858058756695' cy='10.77616' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='16.4238759941568' cy='14.88236' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='5.95061171076124' cy='13.63433' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='67.4019538224314' cy='14.14246' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='97.5' cy='8.83576' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='40.9255802629443' cy='5.90556' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='7.28295934101607' cy='12.18638' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='7.15478412595358' cy='8.27128' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='50.1802162798247' cy='8.55646' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='48.5389952929719' cy='12.82436' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='4.84281163772115' cy='6.32598' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='35.0834888816751' cy='7.81656' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='21.5142631066385' cy='8.10076' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /> <circle cx='15.7675803441' cy='12.66266' r='2' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1' stroke-opacity='0.9'  /></svg>
  </div>
  <div class="gallery-label">Jitter</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Jitter</span>
    <div class="gallery-links">
      <a href="viz/Viz.Jitter/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Jitter/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 120 20' xmlns='http://www.w3.org/2000/svg'><defs><linearGradient id='home-kde'><stop offset='0%' stop-color='#FFFFFF'/><stop offset='15%' stop-color='#F57AC3'/><stop offset='30%' stop-color='#EC008C'/><stop offset='50%' stop-color='#FFFFFF'/><stop offset='70%' stop-color='#F57AC3'/><stop offset='85%' stop-color='#FFFFFF'/><stop offset='100%' stop-color='#FBC6E5'/></linearGradient></defs><rect x='0' y='0' width='120' height='20' fill='url(#home-kde)'/></svg>
  </div>
  <div class="gallery-label">Heatmap</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Heatmap</span>
    <div class="gallery-links">
      <a href="viz/Viz.Heatmap/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Heatmap/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
<div class="gallery-tile">
  <div class="gallery-preview">
    <svg viewbox='0 0 120 20' width='100' height='20' xmlns='http://www.w3.org/2000/svg'><path d='M 2.5 10 S 3.29166666666667 2.71976896666673, 4.08333333333333 2.71976896666673 S 4.875 1.42688737821439, 5.66666666666667 1.42688737821439 S 6.45833333333333 2.68508664534765, 7.25 2.68508664534765 S 8.04166666666667 1.86480302224602, 8.83333333333333 1.86480302224602 S 9.625 8.15263581087779, 10.4166666666667 8.15263581087779 S 11.2083333333333 4.16174766888341, 12 4.16174766888341 S 12.7916666666667 7.06394831462437, 13.5833333333333 7.06394831462437 S 14.375 0.199999999999999, 15.1666666666667 0.199999999999999 S 15.9583333333333 8.04583075806104, 16.75 8.04583075806104 S 17.5416666666667 7.82499961988267, 18.3333333333333 7.82499961988267 S 19.125 9.99761326666401, 19.9166666666667 9.99761326666401 S 20.7083333333333 5.58410860416244, 21.5 5.58410860416244 S 22.2916666666667 7.72428091893751, 23.0833333333333 7.72428091893751 S 23.875 8.13105544697597, 24.6666666666667 8.13105544697597 S 25.4583333333333 8.31673734720066, 26.25 8.31673734720066 S 27.0416666666667 7.99139860718616, 27.8333333333333 7.99139860718616 S 28.625 9.99994464786424, 29.4166666666667 9.99994464786424 S 30.2083333333333 9.94676014597069, 31 9.94676014597069 S 31.7916666666667 9.09538884399952, 32.5833333333333 9.09538884399952 S 33.375 9.35398886699684, 34.1666666666667 9.35398886699684 S 34.9583333333333 9.51038631865021, 35.75 9.51038631865021 S 36.5416666666667 9.99999997907039, 37.3333333333333 9.99999997907039 S 38.125 9.99976093929185, 38.9166666666667 9.99976093929185 S 39.7083333333333 6.14284493805895, 40.5 6.14284493805895 S 41.2916666666667 8.63896045523351, 42.0833333333333 8.63896045523351 S 42.875 9.81544621796034, 43.6666666666667 9.81544621796034 S 44.4583333333333 9.81394348521456, 45.25 9.81394348521456 S 46.0416666666667 6.2376141358067, 46.8333333333333 6.2376141358067 S 47.625 7.72100830967447, 48.4166666666667 7.72100830967447 S 49.2083333333333 7.78356268237412, 50 7.78356268237412 S 50.7916666666667 9.99870502689318, 51.5833333333333 9.99870502689318 S 52.375 9.99999999999996, 53.1666666666667 9.99999999999996 S 53.9583333333333 10, 54.75 10 S 55.5416666666667 10, 56.3333333333333 10 S 57.125 10, 57.9166666666667 10 S 58.7083333333333 10, 59.5 10 S 60.2916666666667 10, 61.0833333333333 10 S 61.875 10, 62.6666666666667 10 S 63.4583333333333 9.99999999999997, 64.25 9.99999999999997 S 65.0416666666667 9.99892365219954, 65.8333333333333 9.99892365219954 S 66.625 7.76202714128898, 67.4166666666667 7.76202714128898 S 68.2083333333333 9.99976617071899, 69 9.99976617071899 S 69.7916666666667 10, 70.5833333333333 10 S 71.375 10, 72.1666666666667 10 S 72.9583333333333 9.99999999981681, 73.75 9.99999999981681 S 74.5416666666667 9.94343927369155, 75.3333333333333 9.94343927369155 S 76.125 9.12244505056045, 76.9166666666667 9.12244505056045 S 77.7083333333333 9.99999931581184, 78.5 9.99999931581184 S 79.2916666666667 10, 80.0833333333333 10 S 80.875 10, 81.6666666666667 10 S 82.4583333333333 10, 83.25 10 S 84.0416666666667 10, 84.8333333333333 10 S 85.625 10, 86.4166666666667 10 S 87.2083333333333 10, 88 10 S 88.7916666666667 10, 89.5833333333333 10 S 90.375 10, 91.1666666666667 10 S 91.9583333333333 10, 92.75 10 S 93.5416666666667 9.99999999999999, 94.3333333333333 9.99999999999999 S 95.125 9.99948954786426, 95.9166666666667 9.99948954786426 S 96.7083333333333 7.72288963805534, 97.5 7.72288963805534 S 98.2916666666667 9.99948954786426, 99.0833333333333 9.99948954786426 L 99.0833333333333 10.0005104521357 S 98.2916666666667 12.2771103619447, 97.5 12.2771103619447 S 96.7083333333333 10.0005104521357, 95.9166666666667 10.0005104521357 S 95.125 10, 94.3333333333333 10 S 93.5416666666667 10, 92.75 10 S 91.9583333333333 10, 91.1666666666667 10 S 90.375 10, 89.5833333333333 10 S 88.7916666666667 10, 88 10 S 87.2083333333333 10, 86.4166666666667 10 S 85.625 10, 84.8333333333333 10 S 84.0416666666667 10, 83.25 10 S 82.4583333333333 10, 81.6666666666667 10 S 80.875 10, 80.0833333333333 10 S 79.2916666666667 10.0000006841882, 78.5 10.0000006841882 S 77.7083333333333 10.8775549494395, 76.9166666666667 10.8775549494395 S 76.125 10.0565607263085, 75.3333333333333 10.0565607263085 S 74.5416666666667 10.0000000001832, 73.75 10.0000000001832 S 72.9583333333333 10, 72.1666666666667 10 S 71.375 10, 70.5833333333333 10 S 69.7916666666667 10.000233829281, 69 10.000233829281 S 68.2083333333333 12.237972858711, 67.4166666666667 12.237972858711 S 66.625 10.0010763478005, 65.8333333333333 10.0010763478005 S 65.0416666666667 10, 64.25 10 S 63.4583333333333 10, 62.6666666666667 10 S 61.875 10, 61.0833333333333 10 S 60.2916666666667 10, 59.5 10 S 58.7083333333333 10, 57.9166666666667 10 S 57.125 10, 56.3333333333333 10 S 55.5416666666667 10, 54.75 10 S 53.9583333333333 10, 53.1666666666667 10 S 52.375 10.0012949731068, 51.5833333333333 10.0012949731068 S 50.7916666666667 12.2164373176259, 50 12.2164373176259 S 49.2083333333333 12.2789916903255, 48.4166666666667 12.2789916903255 S 47.625 13.7623858641933, 46.8333333333333 13.7623858641933 S 46.0416666666667 10.1860565147854, 45.25 10.1860565147854 S 44.4583333333333 10.1845537820397, 43.6666666666667 10.1845537820397 S 42.875 11.3610395447665, 42.0833333333333 11.3610395447665 S 41.2916666666667 13.857155061941, 40.5 13.857155061941 S 39.7083333333333 10.0002390607081, 38.9166666666667 10.0002390607081 S 38.125 10.0000000209296, 37.3333333333333 10.0000000209296 S 36.5416666666667 10.4896136813498, 35.75 10.4896136813498 S 34.9583333333333 10.6460111330032, 34.1666666666667 10.6460111330032 S 33.375 10.9046111560005, 32.5833333333333 10.9046111560005 S 31.7916666666667 10.0532398540293, 31 10.0532398540293 S 30.2083333333333 10.0000553521358, 29.4166666666667 10.0000553521358 S 28.625 12.0086013928138, 27.8333333333333 12.0086013928138 S 27.0416666666667 11.6832626527993, 26.25 11.6832626527993 S 25.4583333333333 11.868944553024, 24.6666666666667 11.868944553024 S 23.875 12.2757190810625, 23.0833333333333 12.2757190810625 S 22.2916666666667 14.4158913958376, 21.5 14.4158913958376 S 20.7083333333333 10.002386733336, 19.9166666666667 10.002386733336 S 19.125 12.1750003801173, 18.3333333333333 12.1750003801173 S 17.5416666666667 11.954169241939, 16.75 11.954169241939 S 15.9583333333333 19.8, 15.1666666666667 19.8 S 14.375 12.9360516853756, 13.5833333333333 12.9360516853756 S 12.7916666666667 15.8382523311166, 12 15.8382523311166 S 11.2083333333333 11.8473641891222, 10.4166666666667 11.8473641891222 S 9.625 18.135196977754, 8.83333333333333 18.135196977754 S 8.04166666666667 17.3149133546523, 7.25 17.3149133546523 S 6.45833333333333 18.5731126217856, 5.66666666666667 18.5731126217856 S 4.875 17.2802310333333, 4.08333333333333 17.2802310333333 S 3.29166666666667 10, 2.5 10 Z' fill='#E044A7' fill-opacity='0.5' stroke='#E044A7' stroke-width='1'  /></svg>
  </div>
  <div class="gallery-label">Violin</div>
  <div class="gallery-overlay">
    <span class="gallery-name">Violin</span>
    <div class="gallery-links">
      <a href="viz/Viz.Violin/" class="gallery-viz">Viz &rarr;</a>
      <a href="compounds/Compound.Violin/" class="gallery-compound">Compound &rarr;</a>
    </div>
  </div>
</div>
    </div>
    </div>
    <button class="carousel-btn carousel-btn--next" aria-label="Next" onclick="carouselNext('viz-carousel')">&#9654;</button>
    <div class="carousel-dots" id="viz-carousel-dots"></div>
  </div>
</div>

<script>
(function () {
  /* ── Carousel engine ── */
  const state = {};

  function getPerPage() {
    if (window.innerWidth <= 540) return 1;
    if (window.innerWidth <= 960) return 2;
    return 3;
  }

  function init(id) {
    const wrapper = document.getElementById(id);
    if (!wrapper) return;
    const track = wrapper.querySelector('.carousel-track');
    const items = Array.from(track.children).filter(
      (el) => el.classList.contains('ns-card') || el.classList.contains('gallery-tile')
    );
    const dotsContainer = document.getElementById(id + '-dots');
    const perPage = getPerPage();
    const totalPages = Math.ceil(items.length / perPage);

    /* Clear previous interval before overwriting state */
    if (state[id] && state[id].interval) clearInterval(state[id].interval);

    state[id] = { track, items, dotsContainer, page: 0, totalPages, perPage,
                  hovered: state[id] ? state[id].hovered : false, interval: null };

    /* Size items to fit viewport exactly */
    const viewport = track.parentElement;
    const viewportWidth = viewport.getBoundingClientRect().width;
    const gap = 16; /* 1rem */
    const itemWidth = (viewportWidth - (perPage - 1) * gap) / perPage;
    items.forEach(function (item) { item.style.width = itemWidth + 'px'; item.style.flex = '0 0 ' + itemWidth + 'px'; });

    /* Reset to first page */
    track.style.transform = 'translateX(0)';

    /* build dots */
    if (dotsContainer) {
      dotsContainer.innerHTML = '';
      for (let i = 0; i < totalPages; i++) {
        const dot = document.createElement('button');
        dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', 'Page ' + (i + 1));
        dot.addEventListener('click', () => goTo(id, i));
        dotsContainer.appendChild(dot);
      }
    }

    /* pause on hover — only bind once */
    if (!wrapper.dataset.carouselBound) {
      wrapper.addEventListener('mouseenter', () => { state[id].hovered = true; });
      wrapper.addEventListener('mouseleave', () => { state[id].hovered = false; });
      wrapper.dataset.carouselBound = '1';
    }

    updateButtons(id);
    startAuto(id);
  }

  function goTo(id, page) {
    const s = state[id];
    if (!s) return;
    s.page = Math.max(0, Math.min(page, s.totalPages - 1));

    /* Scroll by one viewport-width + gap per page */
    const viewport = s.track.parentElement;
    const viewportWidth = viewport.getBoundingClientRect().width;
    const gap = 16; /* 1rem */
    const offset = s.page * (viewportWidth + gap);
    s.track.style.transform = 'translateX(-' + offset + 'px)';

    updateButtons(id);
    updateDots(id);
  }

  function updateButtons(id) {
    const s = state[id];
    const wrapper = document.getElementById(id);
    const prev = wrapper.querySelector('.carousel-btn--prev');
    const next = wrapper.querySelector('.carousel-btn--next');
    if (prev) prev.disabled = s.page === 0;
    if (next) next.disabled = s.page >= s.totalPages - 1;
  }

  function updateDots(id) {
    const s = state[id];
    if (!s.dotsContainer) return;
    const dots = s.dotsContainer.querySelectorAll('.carousel-dot');
    dots.forEach((d, i) => d.classList.toggle('active', i === s.page));
  }

  function startAuto(id) {
    const s = state[id];
    if (s.interval) clearInterval(s.interval);
    s.interval = setInterval(() => {
      if (s.hovered) return;
      const next = (s.page + 1) % s.totalPages;
      goTo(id, next);
    }, 8000);
  }

  /* public nav functions */
  window.carouselPrev = function (id) {
    const s = state[id];
    if (s) goTo(id, s.page - 1);
  };
  window.carouselNext = function (id) {
    const s = state[id];
    if (s) goTo(id, s.page + 1);
  };

  /* init on load + reinit on resize */
  function initAll() {
    init('ns-carousel');
    init('viz-carousel');
  }

  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(initAll, 200);
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
</script>
