# Agregando un elemento a una lista
motorcycles = ['honda', "mortalica", 'yamaha']
print(motorcycles)  # ['honda', 'mortalica', 'yamaha']


motorcycles_2 = [] # lista vacia
print(motorcycles_2)

motorcycles_2 = ["ducati"]
motorcycles_2.append(" .")
motorcycles_2.append("suzuki")
motorcycles_2.append("yamaha")
print(motorcycles_2)
motorcycles = "angel"
print(motorcycles_2)
motorcycles_2.append(motorcycles)
print(motorcycles_2)

# el metodo .insert() nos ayuda a agregar elementos 
# a una lista en un indice especifico
motorcycles_3 = ["angel", 'juan', "rojo"] 
print("\nLista original")
print(motorcycles_3)
motorcycles_3.insert(0, "acuña")
print("listas después del método insert")
print(motorcycles_3)

## metodo .pop() Elimina el ultimo elemento de una lista 
# pero nos permite utilizar el elemento despues de eliminarlo.
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
motorcycles_4.pop() 
print(motorcycles_4)
# deleted_motorcycles = motorcycles_4.pop() 
print(f"Tu motocicleta borrada es : [deleted_motorcycles]")
print(motorcycles_4)
# se puede utilizar tambien para eliminar un elemento especifico.
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
motorcycles_4.pop(0)
print(motorcycles_4)

# Metodod .remove(), permite eliminar elementos por su valor.
motorcycles_5 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_5)
motorcycles_5.remove('hd')
print(motorcycles_5)

# Ordenr listas
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() #ordena la lista de manera permanente
# Argumento opcional de sort(reverse=true)
print(cars)
# tarea estudiar el metodo de las listas .reverse()
# estudiar metodos build-in: sorted(). len()
several_items = ["angel"]
print(several_items[0])