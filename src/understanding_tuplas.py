# hoy

"""

    tuples
   Las tuples son lists de elementos que no cambias de tamaño
   Las tuples son lists inmutables

   se utilizan los parentecis () para definir una tupla
   
   Ejemplos
       
       si tenemos un rectángulo (largo, ancho) que siempre va a tener 
       sierto tamaño, podemos asegurar que sus dimensiones 
       no va a cambiar si colocamossus valores en una tupla.

"""
dimensions = (200, 50) # 200 de largo x 50 de ancho
print(dimensions)

# Vamos a imprimir elementos de una tupla
# Se realiza de la misma forma que con una lista
print(dimensions[0])
print(dimensions[1])

print(dir(dimensions))

# Lista
dimensions_2 = [200, 50]
print(dir( dimensions_2))

# vamos a modificar una lista
names = ["carlos", "charly", "juan", "wendy"]
print(names)
names[0] = "mercury"
names[1] = "mercury"
names[2] = "mercury"
print(names)

# dimensions_2[0] = 300 # Esta operación no está permitida
# Looping throgh a tuple
for dimension in dimensions:
    print(dimension)

"""
    no podemos modificar una tupla 
    lo que si podemos hacer es cambiar 
    la asignación de un variable que 
    almacena una tupla

"""
dimensions = (500, 1000, 20)
print("tupla re-definida:", dimensions)

# Tipos de datos booleanos
answer = True
print(dir(answer))



# tarea boleanos 