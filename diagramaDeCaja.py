import matplotlib.pyplot as plt
import numpy as np                          # Importacion de librerias para poder dibujar graficos
                                            # Crear un alias, para evitar teclear los nombres completos
                                            # de las librerias
# Semilla para reproducibilidad
np.random.seed(5)

# Simulación de datos
x1=np.random.normal(0,1,200)
x2=np.random.normal(1,1,250)
x3=np.random.normal(5,1,100)
x=[x1,x2,x3]                                # Utilizando la libreria de numpy, se generan datos
                                            # aleatorios para cada una las categorias deseadas.
                                            # *Los datos se pueden cargar de un archivo.
#Box plot
ax=plt.subplot()
plt.boxplot(x,whiskerprops=dict(color="blue", linewidth=2))
plt.show()