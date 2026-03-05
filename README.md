# Guía sobre Datos Faltantes y Métodos de Imputación

**Handling Missing Data and Imputation Methods in Data Science**

![KNN vs Mean Comparison](figures/knn_vs_mean_comparison.png)

Este repositorio contiene una guía técnica y educativa completa sobre el problema de los **datos faltantes** (*missing data*) y los métodos de imputación utilizados en ciencia de datos. El proyecto está diseñado para ser un recurso educativo reproducible, publicado como sitio web técnico a través de GitHub Pages.

El objetivo es explicar de forma clara, rigurosa y reproducible los desafíos que presentan los valores ausentes y las estrategias para manejarlos, desde técnicas simples hasta métodos más avanzados como K-Nearest Neighbors (KNN).

**Versión web:** [https://djwillichile.github.io/missing-data-imputation/](https://djwillichile.github.io/missing-data-imputation/)

## Contenido del Repositorio

| Carpeta | Descripción |
|---------|-------------|
| `/docs` | Documentos en formato Markdown que componen la guía, incluyendo el documento unificado `missing_data_imputation_guide.md`. |
| `/site` | Versión web autocontenida (`index.html`) con imágenes incrustadas y estilos para lectura optimizada. |
| `/code` | Scripts de Python (`.py`) utilizados para generar todas las figuras y ejemplos del proyecto. |
| `/data` | Dataset de ejemplo (`sample_dataset.csv`) generado por los scripts. |
| `/figures` | Figuras y diagramas generados (`.png`). |
| `/notebooks` | Notebook Jupyter para reproducir las figuras. |

## Cómo Usar este Repositorio

### 1. Ver la Guía

Hay dos maneras de leer la guía:

1.  **Versión Web (Recomendado):** Visita [https://djwillichile.github.io/missing-data-imputation/](https://djwillichile.github.io/missing-data-imputation/) para una experiencia de lectura optimizada, con navegación lateral, renderizado de ecuaciones y resaltado de código.
2.  **Documento Markdown:** Lee el archivo `/docs/missing_data_imputation_guide.md` directamente en GitHub o en tu editor de Markdown preferido.

### 2. Reproducir los Resultados

Para regenerar todas las figuras y datos de este proyecto, sigue estos pasos:

#### a. Clonar el Repositorio

```bash
git clone https://github.com/djwillichile/missing-data-imputation.git
cd missing-data-imputation
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

#### c. Ejecutar los Scripts

Los scripts en la carpeta `/code` generarán las figuras en `/figures` y el dataset de ejemplo en `/data`.

```bash
# Ejecutar el script para generar los histogramas de imputación por media
python3 code/generate_histograms.py

# Ejecutar el script para el ejemplo de imputación KNN
python3 code/knn_imputation_example.py
```

## Licencia

Este trabajo se distribuye bajo la licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Eres libre de compartir y adaptar este material para cualquier propósito, siempre que des el crédito apropiado.

---

*Este proyecto fue desarrollado como un recurso educativo en ciencia de datos por Guillermo - ICTA Ltda.*
