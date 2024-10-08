import matplotlib.pyplot as plt
import numpy as np                          # Importacion de librerias para poder dibujar graficos
                                            # Crear un alias, para evitar teclear los nombres completos
                                            # de las librerias

x1=np.random.normal(20,10,100)              
x2=np.random.normal(20,10,100)
x=[x1,x2]                                   # Utilizando la libreria de numpy, se generan datos 100
                                            # aleatorios para cada una las categorias deseadas.
                                            # *Los datos se pueden cargar de un archivo.
# Histograma
ax=plt.subplot()
ax.hist(x,color=["darkmagenta","mediumturquoise"])
plt.show()                                  # Utilizando la instrucción ax.hist y coocando
                                            # como parametros los datos y podemos cambiar 
                                            # los colores, uno por cada categoria.