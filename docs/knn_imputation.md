## 6. Imputación mediante K-Nearest Neighbors (KNN)

Frente a las limitaciones de los métodos de imputación simples, surgen técnicas más sofisticadas que consideran las relaciones entre las variables para estimar los valores faltantes. Uno de los métodos más populares y efectivos es la **imputación mediante K-Vecinos más Cercanos (KNN)**.

Este método fue popularizado para la imputación de datos en el contexto de la genómica por Troyanskaya et al. (2001) y se basa en el principio de que "los pájaros del mismo plumaje vuelan juntos". En el contexto de los datos, esto significa que un valor faltante puede ser estimado utilizando los valores de las observaciones más similares a la observación que contiene el dato faltante.

### Concepto de Vecinos más Próximos

El algoritmo KNN funciona de la siguiente manera:

1.  Para una observación con un valor faltante en una variable, el algoritmo identifica las **K** observaciones más similares (los "vecinos más cercanos") en el conjunto de datos. La similitud se mide utilizando solo las variables que no tienen valores faltantes.

2.  La "similitud" se calcula mediante una métrica de distancia. La más común es la **distancia euclidiana**.

3.  Una vez identificados los K vecinos, el valor faltante se imputa utilizando los valores de esos vecinos. Para una variable numérica, esto se hace generalmente calculando la **media ponderada** de los valores de los vecinos (donde la ponderación puede ser inversamente proporcional a la distancia). Para una variable categórica, se utiliza la **moda** (el valor más frecuente) de los vecinos.

### Cálculo de la Distancia Euclidiana

La distancia euclidiana es la distancia "en línea recta" entre dos puntos en un espacio multidimensional. Para dos observaciones, $p$ y $q$, en un espacio de $m$ dimensiones (variables), la distancia euclidiana $d(p, q)$ se calcula como:

$$
d(p, q) = \sqrt{\sum_{i=1}^{m} (p_i - q_i)^2}
$$

Donde $p_i$ y $q_i$ son los valores de la $i$-ésima variable para las observaciones $p$ y $q$, respectivamente. Es crucial que las variables estén en la misma escala antes de calcular la distancia, por lo que generalmente se aplica una estandarización (por ejemplo, Z-score) como paso de preprocesamiento.

### Ventajas y Limitaciones del Método KNN

#### Ventajas

-   **Considera las relaciones entre variables:** A diferencia de la imputación simple, KNN utiliza la información de otras variables para realizar la imputación, lo que puede resultar in estimaciones mucho más precisas.
-   **Puede manejar datos faltantes en múltiples variables:** El algoritmo puede adaptarse para imputar valores en diferentes columnas.
-   **No requiere la creación de un modelo predictivo:** Es un método no paramétrico, lo que significa que no asume una distribución particular para los datos.

#### Limitaciones

-   **Costo computacional:** Encontrar los K vecinos más cercanos puede ser computacionalmente costoso en datasets muy grandes, ya que requiere calcular la distancia desde la observación con el valor faltante a todas las demás.
-   **Sensibilidad a la elección de K:** El rendimiento del algoritmo depende de la elección del número de vecinos, K. Un valor pequeño de K puede ser sensible al ruido, mientras que un valor grande puede incluir vecinos que no son muy similares.
-   **La "maldición de la dimensionalidad":** En espacios de muy alta dimensionalidad, el concepto de distancia puede volverse menos significativo, lo que puede afectar el rendimiento de KNN.
-   **Requiere preprocesamiento:** Es sensible a la escala de las variables, por lo que es necesario estandarizar los datos antes de aplicar el algoritmo.

### Ejemplo de Código con `scikit-learn`

La librería `scikit-learn` en Python proporciona una implementación fácil de usar del imputador KNN.

```python
import numpy as np
from sklearn.impute import KNNImputer

# Datos de ejemplo con valores faltantes
X = [[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7]]

# Crear el imputador KNN con K=2
imputer = KNNImputer(n_neighbors=2)

# Aplicar la imputación
X_imputed = imputer.fit_transform(X)

print("Datos originales:")
print(X)
print("\nDatos imputados:")
print(X_imputed)
```

Este código muestra cómo `KNNImputer` puede rellenar los valores `np.nan` basándose en los valores de los 2 vecinos más cercanos.
