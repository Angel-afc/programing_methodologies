# Trabajando con listas
print("\n\n\thoy vamos a ver nuevas formas de listas".title())

magicians = ["severus", 'voldemort', "harry potter", "hermione"]
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])

# ciclo for
for magician in magicians:
    print(magician)

# A esto se le conoce como looping
# identacion en los for salta cuatro lineas de codigo

# ahora vamos a imprimir un mensaje para cada mago
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}\n")
print("Gracias a todos. Fue un gran espectáculo")

# identación
"""
    python utiliza la identacion para determinar 
    cuando una linea de código setá conectada a la linea 
    de código anterior.

    Básicamente, se utilizan 4 espacios en blanco para obligarlo
    a escribir código ordenado y estructurado.

"""
# no olvides identar -Traceback identationerror
magicians = ["alice", "david", 'caroline']
#for magician in magicians:
#print(magician) #Identation error

# Error de lógica - Logic Error - IdentationError
for magician in magicians:
    print(magician)
print(f"No puedo esperar a ver el siguiente truco, {magician}")

# Identación innecesaria
message = "Hello python world"
#    print(message)

# No olvides los dos puntos - Syntax Error
for magician: in magicians
#  print(magician)