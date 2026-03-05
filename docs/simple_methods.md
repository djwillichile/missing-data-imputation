## 3. Métodos Simples para Tratar Datos Faltantes

Ante la presencia de datos faltantes, las primeras soluciones que suelen considerarse son las más directas: eliminar las observaciones o variables problemáticas. Aunque estos métodos son fáciles de implementar, deben usarse con precaución debido a sus potenciales desventajas.

### Eliminación de Filas (Listwise Deletion)

La **eliminación por lista** (o *listwise deletion*) es el método más común y consiste en descartar todas las filas (observaciones) que contengan al menos un valor faltante. Es el enfoque predeterminado en mucho software estadístico.

-   **Ventajas:**
    -   Es muy fácil de implementar.
    -   Si los datos son MCAR (Missing Completely At Random), los análisis sobre el conjunto de datos reducido no serán sesgados.
    -   Permite realizar un análisis completo con las mismas observaciones para todas las variables.

-   **Limitaciones:**
    -   **Pérdida de información:** Se descartan datos valiosos de otras columnas que sí estaban completos en la fila eliminada.
    -   **Reducción del tamaño de la muestra:** Puede reducir drásticamente el tamaño del dataset, especialmente si los datos faltantes están dispersos en muchas filas. Esto disminuye el poder estadístico de los análisis.
    -   **Sesgo:** Si los datos no son MCAR, este método puede introducir un sesgo significativo en los resultados, ya que la submuestra restante puede no ser representativa de la población original.

### Eliminación de Columnas

Este enfoque consiste en eliminar por completo una variable (columna) si contiene una gran cantidad de valores faltantes. La decisión se basa generalmente en un umbral predefinido (por ejemplo, eliminar columnas con más del 50% de datos faltantes).

-   **Ventajas:**
    -   Puede ser una solución pragmática cuando una variable es prácticamente irrecuperable debido a la escasez de datos.
    -   Evita tener que imputar una gran cantidad de valores, lo que podría introducir un ruido considerable.

-   **Limitaciones:**
    -   **Pérdida de información:** Se pierde por completo la información que esa variable podría haber aportado, incluso si era predictiva.
    -   **Decisión arbitraria:** La elección del umbral para eliminar una columna es a menudo subjetiva.

Ambos métodos de eliminación son soluciones drásticas que deben considerarse con cuidado. Generalmente, solo son recomendables cuando la cantidad de datos faltantes es muy pequeña y se tiene una fuerte evidencia de que son MCAR. En la mayoría de los casos, los métodos de **imputación** son una alternativa preferible.
