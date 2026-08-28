#Parte I y II
"""import random
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
"""

#Parte VIII
"""import random
import time

def bubble_sort_tiempo(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


tamanios = [100, 500, 1000, 5000]
resultados_bubble = {}

for tam in tamanios:
    datos = [random.randint(1, 10000) for _ in range(tam)]
    lista = datos.copy()

    inicio = time.perf_counter()
    bubble_sort_tiempo(lista)
    fin = time.perf_counter()

    tiempo = fin - inicio
    resultados_bubble[tam] = tiempo
    print(f"Bubble Sort con {tam} elementos: {tiempo:.6f} segundos")
    """

#Parte IX
import random
import time

def bubbleSort(lista):
    comparaciones = 0
    intercambios = 0
    n = len(lista)

    for i in range(n - 1):
        intercambio_hecho = False
        for j in range(n - 1 - i):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
                intercambio_hecho = True
        if not intercambio_hecho:
            break  # si no hubo intercambios, la lista ya está ordenada

    return lista, comparaciones, intercambios

# Caso A, Aleatoria
listaAleatoria = random.sample(range(1, 10000), 1000)

# Caso B, Ordenada
listaOrdenada = list(range(1000))

# Caso C, Ordenada inversamente
listaInvertida = list(range(1000, 0, -1))

for nombre, datos in [("Aleatoria", listaAleatoria), ("Ordenada", listaOrdenada), ("Invertida", listaInvertida)]:
    copia = datos.copy()
    inicio = time.perf_counter()
    resultado, comparaciones, intercambios = bubbleSort(copia)
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    print(f"{nombre}: tiempo={tiempo_ms:.4f} ms, comparaciones={comparaciones}, intercambios={intercambios}")