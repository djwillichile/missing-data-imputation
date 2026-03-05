# Guía sobre Datos Faltantes y Métodos de Imputación

**Handling Missing Data and Imputation Methods in Data Science**

![KNN vs Mean Comparison](../figures/knn_vs_mean_comparison.png)

Este repositorio contiene una guía técnica y educativa completa sobre el problema de los **datos faltantes** (*missing data*) y los métodos de imputación utilizados en ciencia de datos. El proyecto está diseñado para ser un recurso educativo reproducible, listo para ser publicado en GitHub y desplegado como un sitio de documentación técnica a través de GitHub Pages.

El objetivo es explicar de forma clara, rigurosa y reproducible los desafíos que presentan los valores ausentes y las estrategias para manejarlos, desde técnicas simples hasta métodos más avanzados como K-Nearest Neighbors (KNN).

## Contenido del Repositorio

-   `/docs`: Contiene los documentos en formato Markdown que componen la guía, incluyendo el documento unificado `missing_data_imputation_guide.md`.
-   `/site`: Contiene la versión web autoconclusiva (`index.html`) de la guía, con imágenes incrustadas y estilos para una fácil lectura.
-   `/code`: Contiene los scripts de Python (`.py`) utilizados para generar todas las figuras y ejemplos del proyecto.
-   `/data`: Contiene el dataset de ejemplo (`sample_dataset.csv`) generado por los scripts.
-   `/figures`: Contiene todas las figuras y diagramas generados (`.png`).

## Cómo Usar este Repositorio

### 1. Ver la Guía

Hay dos maneras de leer la guía:

1.  **Versión Web (Recomendado):** Abre el archivo `/site/index.html` en tu navegador web para una experiencia de lectura optimizada, con navegación lateral, renderizado de ecuaciones y resaltado de código.
2.  **Documento Markdown:** Lee el archivo `/docs/missing_data_imputation_guide.md` directamente en GitHub o en tu editor de Markdown preferido.

### 2. Reproducir los Resultados

Para regenerar todas las figuras y datos de este proyecto, sigue estos pasos:

#### a. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/missing-data-imputation-guide.git
cd missing-data-imputation-guide
```

#### b. Instalar Dependencias

Se recomienda crear un entorno virtual para instalar las dependencias del proyecto.

```bash
# Crear y activar un entorno virtual (opcional pero recomendado)
python3 -m venv venv
source venv/bin/activate

# Instalar las librerías requeridas
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```
numpy
pandas
matplotlib
scikit-learn
```

#### c. Ejecutar los Scripts

Los scripts en la carpeta `/code` generarán las figuras en `/figures` y el dataset de ejemplo en `/data`.

```bash
# Ejecutar el script para generar los histogramas de imputación por media
python3 code/generate_histograms.py

# Ejecutar el script para el ejemplo de imputación KNN
python3 code/knn_imputation_example.py
```

### 3. Desplegar en GitHub Pages

El archivo `/site/index.html` es autoconclusivo y está listo para ser desplegado con GitHub Pages.

1.  Asegúrate de que tu repositorio tenga una rama llamada `gh-pages` o configura GitHub Pages para que sirva desde la rama `main` en la carpeta `/site`.
2.  Ve a la configuración de tu repositorio en GitHub (`Settings` > `Pages`).
3.  En la sección "Build and deployment", selecciona "Deploy from a branch" y elige la rama y carpeta (`/site`) donde se encuentra tu `index.html`.
4.  Guarda los cambios. GitHub Pages te proporcionará una URL donde tu sitio estará visible (ej. `https://tu-usuario.github.io/missing-data-imputation-guide/`).

## Licencia

Este trabajo se distribuye bajo la licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Eres libre de compartir y adaptar este material para cualquier propósito, siempre que des el crédito apropiado.

---

*Este proyecto fue desarrollado como un recurso educativo en ciencia de datos por Guillermo - ICTA Ltda.*
