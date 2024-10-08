import matplotlib.pyplot as plt
import numpy as np                          # Importacion de librerias para poder dibujar graficos
                                            # Crear un alias, para evitar teclear los nombres completos
                                            # de las librerias
x=np.array(["Comedia", "Acción", "Terror"])
y=np.array([3,1,10])
colores=["blue","red","mediumaquamarine"]   # Cargar datos donde un eje (x) es  para los argumentos
                                            # y el otro eje (y) es para los valores.
                                            # Es opcional asignar color a cada una de las barras,
                                            # si se desea hacerlo, se debe de escribir el color en inglés
plt.bar(x,y,color=colores)
plt.show()                                  # Las barras tienen varios parametros, el eje x crea una 
                                            # barra por cada argumento, el eje y es la altura de la barra
                                            # y al parámetro color se le asigna el color acada barra
                                            
