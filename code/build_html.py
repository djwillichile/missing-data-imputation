#!/usr/bin/env python3
"""
build_html.py
Genera el archivo HTML completo con imagenes incrustadas en base64.
"""
import base64, os

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(PROJ, "figures")
OUT = os.path.join(PROJ, "site", "index.html")

def img_b64(name):
    path = os.path.join(FIG, name)
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

imgs = {
    "imputation_comparison": img_b64("imputation_comparison.png"),
    "variance_comparison": img_b64("variance_comparison.png"),
    "imputation_flow": img_b64("imputation_flow.png"),
    "knn_vs_mean": img_b64("knn_vs_mean_comparison.png"),
    "knn_scatter": img_b64("knn_scatter_comparison.png"),
}

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Datos Faltantes y M&#233;todos de Imputaci&#243;n en Ciencia de Datos</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Merriweather:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}]}});"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/github.min.css">
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
<style>
:root{{--bg:#fff;--bg2:#f8f9fa;--bgc:#f1f3f5;--tx:#212529;--mu:#6c757d;--pr:#2563eb;--pl:#dbeafe;--bd:#dee2e6;--bl:#e9ecef;--fb:'Inter',sans-serif;--fh:'Merriweather',serif;--fc:'JetBrains Mono',monospace;--mw:860px;--sw:280px}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth;font-size:16px}}
body{{font-family:var(--fb);color:var(--tx);background:var(--bg);line-height:1.75}}
.pg{{display:flex;min-height:100vh}}
/* Sidebar */
.sb{{position:fixed;top:0;left:0;width:var(--sw);height:100vh;overflow-y:auto;background:var(--bg2);border-right:1px solid var(--bd);padding:2rem 1.25rem;z-index:200;transition:transform .3s ease}}
.sb-t{{font-family:var(--fh);font-size:1rem;font-weight:700;color:var(--pr);margin-bottom:.5rem;line-height:1.4}}
.sb-s{{font-size:.75rem;color:var(--mu);margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:1px solid var(--bl)}}
.sb nav a{{display:block;padding:.4rem .75rem;margin-bottom:.15rem;font-size:.85rem;color:var(--mu);text-decoration:none;border-radius:6px;transition:all .2s;line-height:1.5}}
.sb nav a:hover,.sb nav a.active{{color:var(--pr);background:var(--pl)}}
.sb nav a.active{{font-weight:600}}
.ns{{font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--mu);margin-top:1rem;margin-bottom:.25rem;padding-left:.75rem}}
/* Hamburger button */
.hb{{display:none;position:fixed;top:1rem;left:1rem;z-index:300;background:var(--pr);color:#fff;border:none;border-radius:8px;width:44px;height:44px;cursor:pointer;font-size:1.5rem;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.2);line-height:1}}
/* Overlay */
.ov{{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.4);z-index:150}}
/* Main content */
.mn{{margin-left:var(--sw);flex:1;padding:3rem 2.5rem}}
.wr{{max-width:var(--mw);margin:0 auto}}
.dh{{margin-bottom:3rem;padding-bottom:2rem;border-bottom:2px solid var(--bd)}}
.dh h1{{font-family:var(--fh);font-size:2.25rem;font-weight:700;line-height:1.3;margin-bottom:.75rem}}
.dh .st{{font-size:1.1rem;color:var(--mu);font-style:italic;margin-bottom:1rem}}
.dm{{display:flex;gap:1.5rem;font-size:.85rem;color:var(--mu);flex-wrap:wrap}}
h2{{font-family:var(--fh);font-size:1.65rem;font-weight:700;margin-top:3.5rem;margin-bottom:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--bl)}}
h3{{font-family:var(--fh);font-size:1.25rem;font-weight:700;margin-top:2rem;margin-bottom:.75rem}}
p{{margin-bottom:1.25rem}}
strong{{font-weight:600}}
a{{color:var(--pr);text-decoration:none}}
a:hover{{text-decoration:underline}}
/* Tables responsive wrapper */
.tw{{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.5rem 0}}
table{{width:100%;border-collapse:collapse;font-size:.9rem;min-width:500px}}
thead{{background:var(--bg2)}}
th{{font-weight:600;text-align:left;padding:.75rem 1rem;border-bottom:2px solid var(--bd);white-space:nowrap}}
td{{padding:.65rem 1rem;border-bottom:1px solid var(--bl);vertical-align:top}}
tr:hover td{{background:var(--bg2)}}
/* Code blocks */
pre{{background:var(--bgc);border:1px solid var(--bl);border-radius:8px;padding:1.25rem 1.5rem;overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.5rem 0;font-size:.85rem;line-height:1.6}}
pre code{{font-family:var(--fc);background:none;padding:0;border:none;white-space:pre}}
code{{font-family:var(--fc);font-size:.88em;background:var(--bgc);padding:.15em .4em;border-radius:4px;border:1px solid var(--bl);word-break:break-word}}
/* Figures */
.fig{{margin:2rem 0;text-align:center}}
.fig img{{max-width:100%;height:auto;border-radius:8px;border:1px solid var(--bl);box-shadow:0 2px 8px rgba(0,0,0,.06)}}
.fig figcaption{{margin-top:.75rem;font-size:.85rem;color:var(--mu);font-style:italic;max-width:90%;margin-left:auto;margin-right:auto;line-height:1.5}}
ol,ul{{margin:1rem 0;padding-left:1.75rem}}
li{{margin-bottom:.5rem}}
/* KaTeX */
.katex-display{{margin:1.5rem 0;overflow-x:auto;-webkit-overflow-scrolling:touch;padding:.5rem 0}}
/* References */
.rl{{list-style:none;padding-left:0}}
.rl li{{padding:.75rem 0;border-bottom:1px solid var(--bl);font-size:.92rem}}
.rl li:last-child{{border-bottom:none}}
.rn{{display:inline-block;width:1.75rem;font-weight:700;color:var(--pr)}}
/* Footer */
.df{{margin-top:4rem;padding-top:2rem;border-top:1px solid var(--bd);font-size:.85rem;color:var(--mu);text-align:center}}
/* Back to top */
.btt{{position:fixed;bottom:2rem;right:2rem;width:44px;height:44px;background:var(--pr);color:#fff;border:none;border-radius:50%;cursor:pointer;font-size:1.2rem;display:none;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.15);z-index:50}}
.btt.v{{display:flex}}
/* ===== RESPONSIVE: Tablet ===== */
@media(max-width:1024px){{
  .mn{{padding:2.5rem 2rem}}
}}
/* ===== RESPONSIVE: Mobile ===== */
@media(max-width:768px){{
  .sb{{transform:translateX(-100%)}}
  .sb.open{{transform:translateX(0)}}
  .hb{{display:flex}}
  .ov.open{{display:block}}
  .mn{{margin-left:0;padding:4.5rem 1rem 2rem 1rem}}
  .dh h1{{font-size:1.5rem}}
  .dh .st{{font-size:.95rem}}
  h2{{font-size:1.3rem;margin-top:2.5rem}}
  h3{{font-size:1.1rem;margin-top:1.5rem}}
  p{{margin-bottom:1rem;font-size:.95rem}}
  pre{{padding:.75rem 1rem;font-size:.78rem;border-radius:6px}}
  .fig img{{border-radius:6px}}
  .fig figcaption{{font-size:.8rem;max-width:100%}}
  .dm{{flex-direction:column;gap:.5rem}}
  table{{font-size:.82rem;min-width:400px}}
  th,td{{padding:.5rem .65rem}}
}}
/* ===== RESPONSIVE: Small Mobile ===== */
@media(max-width:480px){{
  .mn{{padding:4rem .75rem 1.5rem .75rem}}
  .dh h1{{font-size:1.3rem}}
  h2{{font-size:1.15rem}}
  h3{{font-size:1rem}}
  pre{{padding:.6rem .75rem;font-size:.72rem}}
  table{{min-width:320px}}
}}
</style>
</head>
<body>
<!-- Hamburger button for mobile -->
<button class="hb" id="hb" aria-label="Abrir men&#250; de navegaci&#243;n" onclick="toggleMenu()">&#9776;</button>
<!-- Overlay for mobile sidebar -->
<div class="ov" id="ov" onclick="toggleMenu()"></div>
<aside class="sb" id="sb">
<div class="sb-t">Datos Faltantes y M&#233;todos de Imputaci&#243;n</div>
<div class="sb-s">Gu&#237;a T&#233;cnica &middot; Ciencia de Datos</div>
<nav>
<div class="ns">Fundamentos</div>
<a href="#s1">1. Introducci&#243;n</a>
<a href="#s2">2. Problema de los Valores NA</a>
<div class="ns">M&#233;todos Simples</div>
<a href="#s3">3. Eliminaci&#243;n de Datos</a>
<a href="#s4">4. Imputaci&#243;n Simple</a>
<a href="#s5">5. Ejemplo Visual</a>
<div class="ns">M&#233;todos Avanzados</div>
<a href="#s6">6. Flujo de Decisi&#243;n</a>
<a href="#s7">7. Imputaci&#243;n KNN</a>
<div class="ns">Cierre</div>
<a href="#s8">8. Conclusiones</a>
<a href="#s9">9. Referencias</a>
</nav>
</aside>
<div class="pg">
<main class="mn"><div class="wr">

<header class="dh">
<h1>Datos Faltantes y M&#233;todos de Imputaci&#243;n en Ciencia de Datos</h1>
<p class="st">Handling Missing Data and Imputation Methods in Data Science</p>
<div class="dm">
<span><strong>Autor:</strong> Guillermo &middot; ICTA Ltda.</span>
<span><strong>Fecha:</strong> Marzo 2026</span>
<span><strong>Licencia:</strong> CC BY 4.0</span>
</div>
</header>

<!-- S1 -->
<section id="s1">
<h2>1. Introducci&#243;n al Problema de los Datos Faltantes</h2>
<p>Los <strong>datos faltantes</strong> (o <em>missing data</em>) constituyen una de las problem&#225;ticas m&#225;s frecuentes y desafiantes en el an&#225;lisis de datos y la ciencia de datos aplicada. Se definen como la ausencia de valores para una o m&#225;s variables en una o m&#225;s observaciones de un conjunto de datos. Su presencia puede originarse por m&#250;ltiples causas: errores en la recolecci&#243;n de datos, fallas en sensores de medici&#243;n, omisiones en encuestas, problemas de integraci&#243;n de bases de datos o incluso la negativa deliberada de los participantes a proporcionar cierta informaci&#243;n <sup>[1]</sup>.</p>
<p>Independientemente de su origen, los datos faltantes representan un desaf&#237;o significativo para el modelado estad&#237;stico y el aprendizaje autom&#225;tico. Si no se manejan adecuadamente, pueden conducir a conclusiones sesgadas, modelos predictivos con menor rendimiento y una reducci&#243;n general en la validez de los resultados.</p>
<h3>1.1 Categor&#237;as de Datos Faltantes</h3>
<p>Little y Rubin (2002) <sup>[1]</sup> propusieron una taxonom&#237;a que se ha convertido en el est&#225;ndar de referencia:</p>
<div class="tw"><table>
<thead><tr><th>Categor&#237;a</th><th>Nombre Completo</th><th>Descripci&#243;n</th><th>Ejemplo</th></tr></thead>
<tbody>
<tr><td><strong>MCAR</strong></td><td>Missing Completely At Random</td><td>La probabilidad de que un dato falte es la misma para todas las observaciones y no depende de ning&#250;n valor.</td><td>Un sensor falla aleatoriamente por un problema el&#233;ctrico.</td></tr>
<tr><td><strong>MAR</strong></td><td>Missing At Random</td><td>La probabilidad de ausencia depende de los valores observados de otras variables, pero no del valor faltante.</td><td>Los hombres son menos propensos a responder una pregunta sobre salud.</td></tr>
<tr><td><strong>MNAR</strong></td><td>Missing Not At Random</td><td>La probabilidad de ausencia depende del propio valor que falta.</td><td>Personas con ingresos altos son m&#225;s reacias a revelar sus ingresos.</td></tr>
</tbody>
</table></div>
<p>La distinci&#243;n entre estas categor&#237;as es crucial porque determina qu&#233; m&#233;todos de tratamiento son apropiados. Los datos MCAR son los m&#225;s sencillos de manejar. Los datos MAR pueden tratarse con m&#233;todos de imputaci&#243;n que consideren las relaciones entre variables. Los datos MNAR son los m&#225;s problem&#225;ticos, ya que requieren modelos expl&#237;citos del mecanismo de ausencia <sup>[3]</sup>.</p>
</section>

<!-- S2 -->
<section id="s2">
<h2>2. El Problema de los Valores NA en el An&#225;lisis de Datos</h2>
<p>La presencia de valores <code>NA</code> (Not Available) o nulos en un conjunto de datos no es un mero inconveniente t&#233;cnico; es un problema que puede invalidar an&#225;lisis estad&#237;sticos completos y comprometer la fiabilidad de modelos de machine learning.</p>
<h3>2.1 Errores en Operaciones Matem&#225;ticas</h3>
<p>La mayor&#237;a de las operaciones estad&#237;sticas fundamentales &mdash;como el c&#225;lculo de la media, la varianza, la correlaci&#243;n o la regresi&#243;n&mdash; no est&#225;n definidas para valores indefinidos. En Python, librer&#237;as como <code>NumPy</code> y <code>pandas</code> representan estos valores como <code>NaN</code>, lo que permite que los c&#225;lculos contin&#250;en sin errores de ejecuci&#243;n, pero el resultado final sigue siendo un valor indefinido.</p>
<h3>2.2 P&#233;rdida de Informaci&#243;n y Reducci&#243;n del Poder Estad&#237;stico</h3>
<p>Al eliminar filas con valores faltantes (<em>listwise deletion</em>), se reduce el tama&#241;o de la muestra, lo que disminuye el <strong>poder estad&#237;stico</strong> de las pruebas. Esto significa que se reduce la capacidad de detectar efectos reales en los datos <sup>[3]</sup>.</p>
<h3>2.3 Introducci&#243;n de Sesgos</h3>
<p>Si los datos no son MCAR, eliminarlos puede distorsionar la distribuci&#243;n de las variables y las relaciones entre ellas. Por ejemplo, si en un estudio sobre salarios las personas con ingresos m&#225;s altos son m&#225;s reacias a responder, eliminar estas observaciones har&#225; que el salario promedio calculado sea artificialmente m&#225;s bajo <sup>[1]</sup>.</p>
<h3>2.4 Impacto en Algoritmos de Machine Learning</h3>
<p>La mayor&#237;a de los algoritmos de machine learning &mdash;regresi&#243;n lineal, regresi&#243;n log&#237;stica, SVM, redes neuronales&mdash; no pueden funcionar con datos faltantes. Las implementaciones est&#225;ndar de <code>scikit-learn</code> arrojar&#225;n un error al intentar entrenar un modelo con <code>NaN</code> <sup>[2]</sup>.</p>
</section>

<!-- S3 -->
<section id="s3">
<h2>3. M&#233;todos Simples para Tratar Datos Faltantes</h2>
<p>Ante la presencia de datos faltantes, las primeras soluciones que suelen considerarse son las m&#225;s directas: eliminar las observaciones o variables problem&#225;ticas.</p>
<h3>3.1 Eliminaci&#243;n de Filas (Listwise Deletion)</h3>
<p>La <strong>eliminaci&#243;n por lista</strong> consiste en descartar todas las filas que contengan al menos un valor faltante. Es v&#225;lido &#250;nicamente cuando los datos son MCAR y la proporci&#243;n de datos faltantes es muy peque&#241;a.</p>
<h3>3.2 Eliminaci&#243;n de Columnas</h3>
<p>Consiste en eliminar por completo una variable si contiene una proporci&#243;n muy alta de valores faltantes (por ejemplo, m&#225;s del 50%).</p>
<h3>3.3 Problemas Asociados a la Eliminaci&#243;n</h3>
<div class="tw"><table>
<thead><tr><th>Problema</th><th>Descripci&#243;n</th><th>Consecuencia</th></tr></thead>
<tbody>
<tr><td><strong>P&#233;rdida de informaci&#243;n</strong></td><td>Se descartan datos v&#225;lidos de otras columnas en la fila eliminada.</td><td>Reducci&#243;n de la riqueza informativa del dataset.</td></tr>
<tr><td><strong>Reducci&#243;n del tama&#241;o de muestra</strong></td><td>El dataset resultante es m&#225;s peque&#241;o.</td><td>Menor poder estad&#237;stico para detectar efectos reales.</td></tr>
<tr><td><strong>Sesgos estad&#237;sticos</strong></td><td>Si los datos no son MCAR, la muestra restante no es representativa.</td><td>Estimaciones distorsionadas de par&#225;metros y relaciones.</td></tr>
</tbody>
</table></div>
</section>

<!-- S4 -->
<section id="s4">
<h2>4. M&#233;todos Simples de Imputaci&#243;n</h2>
<p>En lugar de eliminar datos, la <strong>imputaci&#243;n</strong> consiste en rellenar los valores faltantes con valores estimados.</p>
<h3>4.1 Imputaci&#243;n por la Media</h3>
<p>Reemplaza todos los valores faltantes por la <strong>media aritm&#233;tica</strong> de los valores observados:</p>
<p>$$\\bar{{x}} = \\frac{{1}}{{n}} \\sum_{{i=1}}^{{n}} x_i$$</p>
<h3>4.2 Imputaci&#243;n por la Mediana</h3>
<p>Reemplaza los valores faltantes por la <strong>mediana</strong>. Es preferible a la media cuando la distribuci&#243;n es asim&#233;trica o contiene valores at&#237;picos.</p>
<h3>4.3 Imputaci&#243;n por la Moda</h3>
<p>Reemplaza los valores faltantes por la <strong>moda</strong> (valor m&#225;s frecuente). Es el m&#233;todo de elecci&#243;n para variables categ&#243;ricas.</p>
<h3>4.4 Problemas de la Imputaci&#243;n Simple</h3>
<div class="tw"><table>
<thead><tr><th>Problema</th><th>Descripci&#243;n</th><th>Impacto</th></tr></thead>
<tbody>
<tr><td><strong>Distorsi&#243;n de la distribuci&#243;n</strong></td><td>Se introduce un pico artificial en el valor central.</td><td>La forma de la distribuci&#243;n original se altera significativamente.</td></tr>
<tr><td><strong>Reducci&#243;n de la varianza</strong></td><td>Los valores imputados no aportan variabilidad.</td><td>La varianza se subestima, produciendo intervalos de confianza estrechos.</td></tr>
<tr><td><strong>Sobre-representaci&#243;n</strong></td><td>Un &#250;nico valor se repite muchas veces.</td><td>Se distorsionan las frecuencias y se debilitan las correlaciones.</td></tr>
</tbody>
</table></div>
</section>

<!-- S5 -->
<section id="s5">
<h2>5. Ejemplo Visual del Problema de Imputar la Media</h2>
<p>Consideremos una variable que sigue una distribuci&#243;n normal ($\\mu = 170$ cm, $\\sigma = 10$ cm). Si tomamos $n = 1000$ observaciones y perdemos el 30% de forma MCAR, al imputar la media introducimos un valor constante ($\\bar{{x}} = 170.38$) en 300 posiciones. Esto genera un <strong>pico artificial</strong> y reduce la varianza de 95.79 a 66.98 (una reducci&#243;n del 30%).</p>
<h3>5.1 C&#243;digo Reproducible en Python</h3>
<pre><code class="language-python">import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
original_data = np.random.normal(loc=170, scale=10, size=1000)

data_series = pd.Series(original_data.copy())
missing_idx = data_series.sample(frac=0.30, random_state=42).index
data_with_missing = data_series.copy()
data_with_missing.iloc[missing_idx] = np.nan

data_deleted = data_with_missing.dropna()
imputed_mean = data_with_missing.mean()
data_mean_imputed = data_with_missing.fillna(imputed_mean)

fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), sharex=True, sharey=True)
axes[0].hist(original_data, bins=30, color='#4C72B0', edgecolor='white')
axes[0].set_title('1. Distribucion Original (n=1000)')
axes[1].hist(data_deleted, bins=30, color='#DD8452', edgecolor='white')
axes[1].set_title(f'2. Eliminacion (n={{len(data_deleted)}})')
axes[2].hist(data_mean_imputed, bins=30, color='#55A868', edgecolor='white')
axes[2].axvline(imputed_mean, color='red', linestyle='--', linewidth=2)
axes[2].set_title('3. Imputacion por Media (n=1000)')
plt.tight_layout()
plt.savefig('figures/imputation_comparison.png', dpi=150, bbox_inches='tight')
plt.show()</code></pre>

<h3>5.2 Resultado Visual</h3>
<figure class="fig">
<img src="data:image/png;base64,{imgs["imputation_comparison"]}" alt="Comparacion de distribuciones">
<figcaption>Figura 1. Comparaci&#243;n de tres distribuciones: (1) datos originales, (2) datos tras eliminaci&#243;n de filas, y (3) datos tras imputaci&#243;n por la media. N&#243;tese el pico pronunciado en el valor de la media en el tercer histograma.</figcaption>
</figure>

<h3>5.3 Comparaci&#243;n de Varianza</h3>
<figure class="fig">
<img src="data:image/png;base64,{imgs["variance_comparison"]}" alt="Comparacion de varianza">
<figcaption>Figura 2. Comparaci&#243;n de la varianza entre los tres escenarios. La imputaci&#243;n por media reduce la varianza de 95.79 a 66.98.</figcaption>
</figure>

<h3>5.4 Estad&#237;sticas Comparativas</h3>
<div class="tw"><table>
<thead><tr><th>M&#233;trica</th><th style="text-align:right">Original</th><th style="text-align:right">Eliminaci&#243;n</th><th style="text-align:right">Imputaci&#243;n por Media</th></tr></thead>
<tbody>
<tr><td><strong>N</strong></td><td style="text-align:right">1000</td><td style="text-align:right">700</td><td style="text-align:right">1000</td></tr>
<tr><td><strong>Media</strong></td><td style="text-align:right">170.19</td><td style="text-align:right">170.38</td><td style="text-align:right">170.38</td></tr>
<tr><td><strong>Desv. Est&#225;ndar</strong></td><td style="text-align:right">9.79</td><td style="text-align:right">9.78</td><td style="text-align:right">8.18</td></tr>
<tr><td><strong>Varianza</strong></td><td style="text-align:right">95.79</td><td style="text-align:right">95.72</td><td style="text-align:right">66.98</td></tr>
</tbody>
</table></div>
</section>

<!-- S6 -->
<section id="s6">
<h2>6. Flujo de Decisi&#243;n para el Tratamiento de Datos Faltantes</h2>
<p>El siguiente diagrama presenta un flujo de decisi&#243;n conceptual para seleccionar la estrategia m&#225;s adecuada de tratamiento de datos faltantes:</p>
<figure class="fig">
<img src="data:image/png;base64,{imgs["imputation_flow"]}" alt="Diagrama de flujo de imputacion" style="max-width:700px">
<figcaption>Figura 3. Flujo de decisi&#243;n para el tratamiento de datos faltantes. El proceso eval&#250;a la proporci&#243;n de datos faltantes, selecciona el m&#233;todo de imputaci&#243;n y valida el impacto en la distribuci&#243;n.</figcaption>
</figure>
</section>

<!-- S7 -->
<section id="s7">
<h2>7. Imputaci&#243;n mediante K-Nearest Neighbors (KNN)</h2>
<p>Frente a las limitaciones de los m&#233;todos simples, surgen t&#233;cnicas m&#225;s sofisticadas que consideran las <strong>relaciones entre las variables</strong>. Uno de los m&#233;todos m&#225;s populares es la <strong>imputaci&#243;n mediante K-Vecinos m&#225;s Cercanos (KNN)</strong>, popularizado por Troyanskaya et al. (2001) <sup>[4]</sup>.</p>

<h3>7.1 Concepto de Vecinos m&#225;s Pr&#243;ximos</h3>
<p>El algoritmo KNN se basa en un principio intuitivo: una observaci&#243;n con un valor faltante puede ser estimada utilizando la informaci&#243;n de las observaciones m&#225;s <strong>similares</strong>. El procedimiento opera as&#237;:</p>
<ol>
<li>Para una observaci&#243;n $p$ con un valor faltante en la variable $j$, se identifican las $K$ observaciones m&#225;s similares usando las variables completas.</li>
<li>La similitud se cuantifica mediante una <strong>m&#233;trica de distancia</strong> (t&#237;picamente euclidiana).</li>
<li>El valor faltante se estima calculando la <strong>media ponderada</strong> de los valores de los $K$ vecinos.</li>
</ol>

<h3>7.2 Distancia Euclidiana</h3>
<p>Para dos observaciones $p$ y $q$ en un espacio de $m$ dimensiones:</p>
<p>$$d(p, q) = \\sqrt{{\\sum_{{i=1}}^{{m}} (p_i - q_i)^2}}$$</p>
<p>Es fundamental que las variables est&#233;n <strong>estandarizadas</strong> antes de calcular la distancia.</p>

<h3>7.3 Construcci&#243;n del Vector de Distancias</h3>
<p>Para una observaci&#243;n $p$ con un valor faltante, se calcula la distancia a todas las dem&#225;s observaciones con valores v&#225;lidos, generando un vector:</p>
<p>$$\\mathbf{{D}}_p = [d(p, q_1), d(p, q_2), \\ldots, d(p, q_{{n'}})]$$</p>
<p>Se ordena de menor a mayor y se seleccionan los $K$ valores m&#225;s peque&#241;os.</p>

<h3>7.4 Predicci&#243;n del Valor Faltante</h3>
<p>Media simple de los $K$ vecinos:</p>
<p>$$\\hat{{x}}_{{p,j}} = \\frac{{1}}{{K}} \\sum_{{k=1}}^{{K}} x_{{q_k, j}}$$</p>
<p>Versi&#243;n ponderada por distancia:</p>
<p>$$\\hat{{x}}_{{p,j}} = \\frac{{\\sum_{{k=1}}^{{K}} w_k \\cdot x_{{q_k, j}}}}{{\\sum_{{k=1}}^{{K}} w_k}}, \\quad \\text{{donde }} w_k = \\frac{{1}}{{d(p, q_k)}}$$</p>

<h3>7.5 Ejemplo de C&#243;digo con scikit-learn</h3>
<pre><code class="language-python">import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

np.random.seed(42)
n = 200
temperature = np.random.normal(loc=22, scale=5, size=n)
humidity = 60 + 0.8 * temperature + np.random.normal(0, 3, size=n)
precipitation = 10 + 0.5 * humidity - 0.3 * temperature + np.random.normal(0, 2, size=n)

df = pd.DataFrame({{
    'temperatura': temperature,
    'humedad': humidity,
    'precipitacion': precipitation
}})

for col in df.columns:
    missing_idx = df.sample(frac=0.15, random_state=42).index
    df.loc[missing_idx, col] = np.nan

imputer = KNNImputer(n_neighbors=5, weights='uniform')
df_imputed = pd.DataFrame(
    imputer.fit_transform(df),
    columns=df.columns
)
print(df_imputed.describe())</code></pre>

<h3>7.6 Comparaci&#243;n Visual: KNN vs. Imputaci&#243;n por Media</h3>
<figure class="fig">
<img src="data:image/png;base64,{imgs["knn_vs_mean"]}" alt="Comparacion KNN vs Media">
<figcaption>Figura 4. Comparaci&#243;n de distribuciones para tres variables ambientales: datos originales (azul), imputaci&#243;n por media (naranja) e imputaci&#243;n KNN (verde).</figcaption>
</figure>
<figure class="fig">
<img src="data:image/png;base64,{imgs["knn_scatter"]}" alt="Scatter KNN vs Original">
<figcaption>Figura 5. Diagrama de dispersi&#243;n comparando las relaciones bivariadas entre variables originales y variables imputadas con KNN.</figcaption>
</figure>

<h3>7.7 Ventajas y Limitaciones del M&#233;todo KNN</h3>
<div class="tw"><table>
<thead><tr><th>Aspecto</th><th>Ventajas</th><th>Limitaciones</th></tr></thead>
<tbody>
<tr><td><strong>Relaciones entre variables</strong></td><td>Utiliza informaci&#243;n multivariada para la imputaci&#243;n.</td><td>Requiere relaciones significativas entre variables.</td></tr>
<tr><td><strong>Supuestos</strong></td><td>No asume una distribuci&#243;n particular (no param&#233;trico).</td><td>Sensible a la elecci&#243;n de $K$ y a la escala.</td></tr>
<tr><td><strong>Precisi&#243;n</strong></td><td>Generalmente m&#225;s preciso que la imputaci&#243;n simple.</td><td>Puede ser impreciso en alta dimensionalidad.</td></tr>
<tr><td><strong>Computaci&#243;n</strong></td><td>Implementaci&#243;n directa con scikit-learn.</td><td>Computacionalmente costoso en datasets grandes.</td></tr>
</tbody>
</table></div>
</section>

<!-- S8 -->
<section id="s8">
<h2>8. Conclusiones</h2>
<p>El manejo de datos faltantes es una etapa ineludible y cr&#237;tica en cualquier proyecto de ciencia de datos. La elecci&#243;n del m&#233;todo puede tener un impacto profundo en la validez, precisi&#243;n y fiabilidad de los resultados.</p>
<p>Los <strong>m&#233;todos simples</strong> (eliminaci&#243;n o imputaci&#243;n por la media) son f&#225;ciles de implementar pero conllevan riesgos: p&#233;rdida de informaci&#243;n, sesgos, distorsi&#243;n de la distribuci&#243;n y reducci&#243;n artificial de la varianza.</p>
<p>Los <strong>m&#233;todos avanzados</strong> como <strong>KNN</strong> ofrecen una soluci&#243;n m&#225;s robusta al aprovechar la estructura multivariada de los datos, proporcionando estimaciones m&#225;s plausibles que preservan mejor las caracter&#237;sticas del conjunto de datos original.</p>
<div class="tw"><table>
<thead><tr><th>M&#233;todo</th><th>Tipo</th><th style="text-align:center">Preserva Distribuci&#243;n</th><th style="text-align:center">Preserva Varianza</th><th style="text-align:center">Considera Relaciones</th><th style="text-align:center">Costo Computacional</th></tr></thead>
<tbody>
<tr><td>Eliminaci&#243;n</td><td>Eliminaci&#243;n</td><td style="text-align:center">Parcialmente</td><td style="text-align:center">S&#237;</td><td style="text-align:center">No</td><td style="text-align:center">Bajo</td></tr>
<tr><td>Media/Mediana/Moda</td><td>Imputaci&#243;n Simple</td><td style="text-align:center">No</td><td style="text-align:center">No</td><td style="text-align:center">No</td><td style="text-align:center">Bajo</td></tr>
<tr><td>KNN</td><td>Imputaci&#243;n Avanzada</td><td style="text-align:center">S&#237;</td><td style="text-align:center">Parcialmente</td><td style="text-align:center">S&#237;</td><td style="text-align:center">Alto</td></tr>
</tbody>
</table></div>
<p>La elecci&#243;n final debe basarse en una comprensi&#243;n profunda del conjunto de datos, el mecanismo de ausencia y los objetivos del an&#225;lisis. No existe una soluci&#243;n universal, pero una regla general es preferir los m&#233;todos de imputaci&#243;n sobre la eliminaci&#243;n, y los m&#233;todos avanzados sobre los simples.</p>
</section>

<!-- S9 -->
<section id="s9">
<h2>9. Referencias</h2>
<ol class="rl">
<li><span class="rn">[1]</span> Little, R. J. A., &amp; Rubin, D. B. (2002). <em>Statistical Analysis with Missing Data</em> (2nd ed.). John Wiley &amp; Sons. <a href="https://doi.org/10.1002/9781119013563" target="_blank">doi:10.1002/9781119013563</a></li>
<li><span class="rn">[2]</span> Hastie, T., Tibshirani, R., &amp; Friedman, J. (2009). <em>The Elements of Statistical Learning</em> (2nd ed.). Springer. <a href="https://hastie.su.domains/ElemStatLearn/" target="_blank">hastie.su.domains/ElemStatLearn</a></li>
<li><span class="rn">[3]</span> Allison, P. D. (2001). <em>Missing Data</em>. Sage Publications. <a href="https://doi.org/10.4135/9781412985079" target="_blank">doi:10.4135/9781412985079</a></li>
<li><span class="rn">[4]</span> Troyanskaya, O., et al. (2001). Missing value estimation methods for DNA microarrays. <em>Bioinformatics</em>, 17(6), 520-525. <a href="https://doi.org/10.1093/bioinformatics/17.6.520" target="_blank">doi:10.1093/bioinformatics/17.6.520</a></li>
</ol>
</section>

<footer class="df">
<p>Guillermo &middot; ICTA Ltda. &middot; Marzo 2026</p>
<p>Este material se distribuye bajo licencia <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">CC BY 4.0</a></p>
</footer>

</div></main>
</div>

<button class="btt" id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&uarr;</button>
<script>
// Back to top button
window.addEventListener('scroll',()=>{{document.getElementById('btt').classList.toggle('v',window.scrollY>400)}});
// Active section tracking
const ss=document.querySelectorAll('section[id]'),nl=document.querySelectorAll('.sb nav a');
window.addEventListener('scroll',()=>{{let c='';ss.forEach(s=>{{if(window.scrollY>=s.offsetTop-100)c=s.getAttribute('id')}});nl.forEach(l=>{{l.classList.remove('active');if(l.getAttribute('href')==='#'+c)l.classList.add('active')}});}});
// Mobile menu toggle
function toggleMenu(){{
  const sb=document.getElementById('sb');
  const ov=document.getElementById('ov');
  sb.classList.toggle('open');
  ov.classList.toggle('open');
}}
// Close sidebar when clicking a nav link on mobile
document.querySelectorAll('.sb nav a').forEach(a=>{{
  a.addEventListener('click',()=>{{
    if(window.innerWidth<=768){{
      const sb=document.getElementById('sb');
      const ov=document.getElementById('ov');
      sb.classList.remove('open');
      ov.classList.remove('open');
    }}
  }});
}});
</script>
</body>
</html>'''

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"HTML generado: {OUT}")
print(f"Tamano: {os.path.getsize(OUT)/1024:.0f} KB")
