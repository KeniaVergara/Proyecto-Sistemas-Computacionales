
# coding: utf-8

# # Codigo para la conversion de imagenes en RGB a escala de grises

# In[1]:


from PIL import Image   #importando el modulo

for i in range(1, 16):                 #recorriendo las imagenes
  foto = Image.open(str(i)+".jpg")     #abriendo imagen a color
  datos = list(foto.getdata())         #guardando datos de colores de la imagen en una lista

  #tomando el valor de los coeficientes de ITU-BT.709 para la conversion de la imagen en RGB a escala de grises
  grises = [round((0.2125 * datos[x][0]) + (0.7154 * datos[x][1]) + (0.072 * datos[x][2])) for x in range(len(datos))]

  imagen_gris = Image.new("L", foto.size)     #creando la nueva imagen del tamaño de la imagen vieja  
  imagen_gris.putdata(grises)                 #generando la imagen a escala de grises
  imagen_gris.save("imagen%s.jpg" % str(i))   #guardando la imagen con el nuevo nombre
  foto.close()            #cerrando imagen a color
  imagen_gris.close()     #cerrando imagen a escala de grises

print("Se han convertido las imagenes a escala de grises")

