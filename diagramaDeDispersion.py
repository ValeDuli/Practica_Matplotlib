import matplotlib.pyplot as plt
import numpy as np                          # Importacion de librerias para poder dibujar graficos
                                            # Crear un alias, para evitar teclear los nombres completos
                                            # de las librerias
# Datos 1
x1=np.array([1,1,2,3,8,7])
y1=np.array([2,6,5,4,1,5])
plt.scatter(x1,y1,c="green",label="Grupo 1")

# Datos 2
x2=np.array([3,2,3,5,7,9])
y2=np.array([2,4,6,5,3,1])
plt.scatter(x2,y2,c="salmon",label="Grupo 2")

# Leyenda
plt.legend()
plt.show()