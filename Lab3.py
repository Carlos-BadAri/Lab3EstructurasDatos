#Parte I y II
import random
datos = [random.randint(1, 100) for _ in range(20)]
print("Lista original:")
print(datos)

def bubble_sort(lista): #Para recibir la lista
    comparaciones = 0
    intercambios = 0
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparaciones += 1 #Cuenta las comparaciones
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #Ordenar de menor a mayor
                intercambios += 1 #Cuenta los intercambios
        print(f"Pasada {i + 1}: {lista}") #Muestra la lista despues de cada pasada

    return lista, comparaciones, intercambios


lista = datos.copy()
lista_ordenada, total_comparaciones, total_intercambios = bubble_sort(lista)

#Mostramos lo solicitado
print("\nLista final ordenada:", lista_ordenada)
print("Total de comparaciones:", total_comparaciones)
print("Total de intercambios:", total_intercambios)
