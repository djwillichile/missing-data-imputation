## 4. Métodos Simples de Imputación

En lugar de eliminar datos, la **imputación** consiste en rellenar los valores faltantes con valores estimados. Los métodos más simples se basan en estadísticas descriptivas del conjunto de datos.

### Imputación por la Media

Este método reemplaza todos los valores faltantes de una variable por la **media** de los valores observados de esa misma variable. La media ($\bar{x}$) se calcula como:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

donde $x_i$ son los valores observados y $n$ es el número de observaciones no faltantes.

-   **Cuándo usarlo:** Es adecuado para variables numéricas que tienen una distribución aproximadamente simétrica (por ejemplo, normal).

### Imputación por la Mediana

Este método reemplaza los valores faltantes por la **mediana** de los valores observados. La mediana es el valor que se encuentra en el centro de la distribución de los datos ordenados.

-   **Cuándo usarlo:** Es preferible a la media cuando la variable numérica tiene una distribución asimétrica o contiene valores atípicos (*outliers*), ya que la mediana es una medida de tendencia central más robusta.

### Imputación por la Moda

Este método reemplaza los valores faltantes por la **moda**, que es el valor más frecuente en el conjunto de datos.

-   **Cuándo usarlo:** Es el método de elección para variables categóricas.

### Problemas de la Imputación Simple

A pesar de su simplicidad, estos métodos tienen serias desventajas que pueden comprometer la validez de los análisis posteriores:

1.  **Distorsión de la distribución:** Al imputar un valor constante (media, mediana o moda) en múltiples lugares, se introduce un pico artificial en la distribución de la variable. Esto puede distorsionar la forma de la distribución, como se verá en el ejemplo visual.

2.  **Reducción de la varianza:** La imputación simple no tiene en cuenta la variabilidad natural de los datos. Al rellenar los faltantes con un valor central, la varianza de la variable imputada se reduce artificialmente. Esto puede llevar a que las pruebas estadísticas subestimen la incertidumbre y produzcan intervalos de confianza demasiado estrechos.

3.  **Debilitamiento de las relaciones entre variables:** La imputación simple no considera las relaciones entre las variables. Al imputar la media en una variable, se debilita su correlación con otras variables, ya que los valores imputados no siguen la tendencia que podrían haber tenido en función de los otros predictores.

Debido a estos problemas, la imputación simple debe usarse con cautela, generalmente como un primer enfoque rápido o cuando la cantidad de datos faltantes es muy pequeña. Para análisis más rigurosos, se prefieren métodos de imputación más avanzados.
