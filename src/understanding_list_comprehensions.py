"""
    una list comprehension combina
    el for loop y la creación de nuevos elementos
    en una solo linea y automaticámente agrega
    cada nuevo elemento a la lista, es decir,
    sin utilizar el método append.
"""
squares = [value**2 for value in range(0,11)]
print(squares)