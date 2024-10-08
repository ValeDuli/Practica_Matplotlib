import matplotlib.pyplot as plt
import numpy as np                          # Importacion de librerias para poder dibujar graficos
                                            # Crear un alias, para evitar teclear los nombres completos
                                            # de las librerias
# Datos
X,Y =np.meshgrid(np.linspace(0,12,180),
                 np.linspace(0,20,200))
Z=np.sqrt(X**2+Y**2)

# Contour relleno
fig,ax=plt.subplots()
cnt=ax.contourf(X,Y,Z)

# Color bar
cbar=ax.figure.colorbar(cnt,ax=ax)
cbar.ax.set_ylabel("Temperatura",rotation=-90,va="bottom")
plt.show()