## 7. Conclusiones

El manejo de datos faltantes es una etapa ineludible y crítica en el ciclo de vida de la ciencia de datos. La elección del método para tratar los valores ausentes no es una decisión trivial y puede tener un impacto profundo en la validez, precisión y fiabilidad de cualquier análisis o modelo predictivo.

### Comparación de Enfoques

| Método | Tipo | Ventajas | Desventajas | Cuándo Usarlo |
| :--- | :--- | :--- | :--- | :--- |
| **Eliminación (Listwise/Column)** | Eliminación | Simple y rápido. No introduce sesgo si los datos son MCAR. | Pérdida de información y poder estadístico. Puede introducir sesgos si no es MCAR. | Con datasets muy grandes y una proporción muy pequeña de datos faltantes (<5%) que se asumen MCAR. |
| **Imputación por Media/Mediana/Moda** | Imputación Simple | Fácil de implementar. Mantiene el tamaño de la muestra. | Distorsiona la distribución de la variable. Reduce la varianza. Debilita las correlaciones. | Como un análisis exploratorio rápido o una línea base. Cuando la cantidad de datos faltantes es mínima. |
| **Imputación por KNN** | Imputación Avanzada | Utiliza información de otras variables. Más preciso que la imputación simple. No asume un modelo. | Computacionalmente más costoso. Sensible a la elección de K y a la escala de las variables. | Cuando se desea una imputación más precisa que preserve las relaciones entre variables y se dispone de los recursos computacionales. |

Los **métodos simples**, como la eliminación de datos o la imputación por la media, son fáciles de implementar pero conllevan riesgos significativos. La eliminación de datos, aunque directa, puede resultar en una pérdida sustancial de información y poder estadístico, además de introducir sesgos si el mecanismo de ausencia no es completamente aleatorio (MCAR). Por su parte, la imputación simple, si bien preserva el tamaño de la muestra, lo hace a costa de distorsionar la distribución original de los datos, reducir artificialmente la varianza y atenuar las relaciones entre variables.

En contraste, los **métodos de imputación más avanzados**, como **K-Nearest Neighbors (KNN)**, ofrecen una solución más robusta. Al aprovechar la estructura multivariada de los datos, KNN puede proporcionar estimaciones para los valores faltantes que son mucho más plausibles y que preservan mejor las características del conjunto de datos original. Aunque computacionalmente más intensivos y sensibles a parámetros como el número de vecinos (K), estos métodos representan un estándar más alto de práctica en la ciencia de datos seria.

La elección final del método debe basarse en una comprensión profunda del conjunto de datos, el mecanismo de ausencia de datos y los objetivos del análisis. No existe una solución única para todos los casos, pero una regla general es preferir siempre los métodos de imputación sobre la eliminación, y los métodos avanzados sobre los simples, siempre que sea computacionalmente factible.
