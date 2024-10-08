import matplotlib.pyplot as plt
import numpy as np                          # Importacion de librerias para poder dibujar graficos
                                            # Crear un alias, para evitar teclear los nombres completos
                                            # de las librerias

# Semilla para reproducibilidad
np.random.seed(50)

# Datos
data=np.random.random((8,8))

# Mapa de calor
ax=plt.subplot()
im=ax.imshow(data)

# Agregar la leyenda
cbar=ax.figure.colorbar(im,ax=ax)
cbar.ax.set_xlabel("Semana",rotation=0,va="top")
cbar.ax.set_ylabel("Producción %",rotation=-90,va="bottom")

plt.show()