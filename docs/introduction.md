## 1. Introducción al Problema de los Datos Faltantes

Los **datos faltantes** (o *missing data* en inglés) son una ocurrencia común en la mayoría de los conjuntos de datos del mundo real. Se refieren a la ausencia de valores para una o más variables en una o más observaciones de un dataset. La presencia de datos faltantes puede deberse a una multitud de razones, desde errores en la recolección de datos, fallas en los sensores de medición, hasta la negativa de los encuestados a responder ciertas preguntas.

Independientemente de su origen, los datos faltantes representan un desafío significativo en el análisis de datos y el modelado estadístico. Si no se manejan adecuadamente, pueden llevar a conclusiones sesgadas, modelos de machine learning con menor poder predictivo y una reducción general en la validez de los resultados de una investigación.

### Categorías de Datos Faltantes

Para abordar el problema de los datos faltantes de manera efectiva, es crucial comprender la naturaleza de la ausencia. Little y Rubin (2002) propusieron una clasificación que se ha convertido en el estándar de la industria, dividiendo los datos faltantes en tres categorías principales según el mecanismo que los genera:

1.  **Missing Completely At Random (MCAR):** Se considera que los datos faltan de forma completamente aleatoria si la probabilidad de que un valor esté ausente es la misma para todas las observaciones. En otras palabras, la ausencia del dato no está relacionada ni con los valores observados de otras variables ni con los propios valores que faltan. Este es el escenario más simple de manejar, aunque también el menos común en la práctica.

2.  **Missing At Random (MAR):** Los datos se consideran ausentes al azar si la probabilidad de que un valor falte depende de los valores observados en otras variables del conjunto de datos, pero no del valor del dato faltante en sí mismo. Por ejemplo, si en una encuesta los hombres son menos propensos a responder una pregunta sobre su estado de salud que las mujeres, los datos faltantes en esa pregunta serían MAR, ya que la ausencia depende de la variable "género".

3.  **Missing Not At Random (MNAR):** Este es el escenario más complejo. Se produce cuando la probabilidad de que un valor esté ausente depende del propio valor que falta. Por ejemplo, las personas con ingresos muy altos pueden ser menos propensas a revelar sus ingresos en una encuesta. En este caso, la ausencia del dato está directamente relacionada con el nivel de ingresos, lo que puede introducir un sesgo significativo si no se trata adecuadamente.

Comprender estas categorías es el primer paso para seleccionar la estrategia de manejo de datos faltantes más apropiada para un problema de análisis de datos determinado.
