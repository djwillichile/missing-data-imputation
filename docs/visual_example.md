## 5. Ejemplo Visual del Problema de Imputar la Media

Una de las mejores maneras de entender los problemas de la imputación simple es a través de una visualización. A continuación, se ilustra cómo la imputación por la media puede distorsionar la distribución de una variable.

### Ejemplo Conceptual

Imaginemos que tenemos una variable que sigue una distribución normal, como podría ser la altura de una población. Si tomamos una muestra de esta población, esperamos que el histograma de las alturas se asemeje a una campana de Gauss. Ahora, supongamos que perdemos el 30% de estos datos de forma completamente aleatoria (MCAR).

Si simplemente imputamos la media de los datos restantes en los huecos, estamos introduciendo un valor constante repetidamente. Esto tendrá un efecto visible en la distribución: aparecerá un pico artificial en el valor de la media, y la forma general de la distribución se verá distorsionada. La varianza también se reducirá, ya que los nuevos puntos no aportan variabilidad.

### Código de Generación de Histogramas

A continuación se presenta el código en Python para generar tres histogramas que ilustran este problema. El código utiliza `numpy` para generar los datos, `pandas` para manejarlos y `matplotlib` para la visualización.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generar datos originales
np.random.seed(42)
original_data = np.random.normal(loc=170, scale=10, size=1000)

# 2. Introducir valores faltantes
data_with_missing = pd.Series(original_data).copy()
data_with_missing[data_with_missing.sample(frac=0.3, random_state=42).index] = np.nan

# 3. Imputar la media
mean_imputed_data = data_with_missing.fillna(data_with_missing.mean())

# 4. Crear los histogramas
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharex=True, sharey=True)

# Histograma 1: Datos originales
axes[0].hist(original_data, bins=30, color='skyblue', edgecolor='black')
axes[0].set_title('1. Distribución Original')
axes[0].set_xlabel('Valor')
axes[0].set_ylabel('Frecuencia')

# Histograma 2: Datos con valores eliminados
axes[1].hist(data_with_missing.dropna(), bins=30, color='salmon', edgecolor='black')
axes[1].set_title('2. Distribución con Valores Eliminados')
axes[1].set_xlabel('Valor')

# Histograma 3: Datos con imputación por media
axes[2].hist(mean_imputed_data, bins=30, color='lightgreen', edgecolor='black')
axes[2].axvline(data_with_missing.mean(), color='red', linestyle='--', linewidth=2, label=f'Media Imputada: {data_with_missing.mean():.2f}')
axes[2].set_title('3. Distribución con Imputación por Media')
axes[2].set_xlabel('Valor')
axes[2].legend()

plt.suptitle('Comparación de Distribuciones: Imputación por Media', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('/home/ubuntu/missing-data-imputation-guide/figures/imputation_comparison.png')
plt.show()
```

### Análisis de los Resultados

Al ejecutar el código anterior, se generará una figura con tres histogramas:

1.  **Distribución Original:** Muestra la forma de campana esperada de una distribución normal.
2.  **Distribución con Valores Eliminados:** La forma es similar a la original, pero la frecuencia en cada bin es menor debido a la reducción del tamaño de la muestra.
3.  **Distribución con Imputación por Media:** Aquí es donde el problema se hace evidente. Se observa un pico muy pronunciado en el valor de la media (marcado con una línea roja). Esta única barra contiene todos los valores imputados, distorsionando la forma de la distribución y reduciendo artificialmente la varianza.

Este ejemplo visual demuestra por qué la imputación por la media, a pesar de su simplicidad, debe ser utilizada con extrema precaución.

![Comparación de Histogramas](/home/ubuntu/missing-data-imputation-guide/figures/imputation_comparison.png)
