import random
import time

def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def tupla(input_tupla):
    lista = list(input_tupla)
    lista_ordenada = seleccion(lista)
    return tuple(lista_ordenada)

datos = tuple(random.randint(0, 10000) for _ in range(10000))

inicio = time.time()
tupla_ordenada = tupla(datos)
fin = time.time()

print(f"Tiempo de ordenación: {fin - inicio:.6f} segundos")
