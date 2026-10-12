# Listas de números
"""
    Las listas también puede almacenar números. Python

"""
# Método build-in range()
"""
    El metodo range() nos ayuda a crear fácilmente
    series de números
    Ejemplos
"""
for value in range(1,5):
    print(value)

# Crear una lista de numero utilizando range
numbers = list(range(1,6))
print(numbers)

# Lista de números pares
even_numbers = list(range(0,10,2))
#¿que pasa con un paso negativo?
print(even_numbers)
