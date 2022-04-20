# -*- coding: utf-8 -*-
"""
Álgebra Linear - Tempo de processamento
"""

import numpy as np
import time


primeiroNumero = 1.3
arredondado = np.round(primeiroNumero)
outroArredondamento = np.ceil(primeiroNumero)
print("Um número:")
print(primeiroNumero)
print("Arredondado: ")
print(arredondado)
print("Arredondado pra cima: ")
print(outroArredondamento)

# Declarando vetores e matrizes com Numpy
minhaLista = [1,4,7] 
meuVetor = np.array(minhaLista)
# Funções diferentes ficam disponíveis para listas e vetores
print("Uma lista: ")
print(minhaLista)
print("Um vetor: ")
print(meuVetor)
# Operações algébricas mudam quando estamos falando de listas e vetores
print("Operação de soma em listas: ")
print(minhaLista + minhaLista)
print("Operação de soma em vetores: ")
print(meuVetor + meuVetor)
print("Operação de multiplicação em listas: ")
print(minhaLista *3)
print("Operação de multiplicação em vetores: ")
print(meuVetor *3)


outraLista = [[1,2,3],[4,5,6],[7,8,9]]
outroVetor = np.array(outraLista)
print("Operação de multiplicação em listas de listas: ")
print(outraLista * 3)
print("Operação de multiplicação em matrizes: ")
print(outroVetor * 3)

# Comparação de tempo com e sem Numpy
# Soma de dois vetores
inicio = time.time()
listaDeTeste = [i for i in range(100000)]
print("Soma de dois vetores com lista: ")
for i in range(len(listaDeTeste)):
    listaDeTeste[i] += listaDeTeste[i]
fim = time.time()
print("tempo de processamento = " + str(fim-inicio))

inicio = time.time()
listaDeTeste = [i for i in range(100000)]
vetorDeTeste = np.array(listaDeTeste)
print("Soma de dois vetores com vetor: ")
vetorDeTeste += vetorDeTeste
fim = time.time()
print("tempo de processamento = " + str(fim-inicio))

# Soma de duas matrizes
inicio = time.time()
listaDeTeste = [i for i in range(1000)]
for i in range(1000):
    listaDeTeste[i] = [i for i in range(1000)]
print("Soma de duas matrizes com lista: ")
for i in range(len(listaDeTeste)):
    for j in range(len(listaDeTeste[i])):
        listaDeTeste[i][j] += listaDeTeste[i][j]
fim = time.time()
print("tempo de processamento = " + str(fim-inicio))

inicio = time.time()
listaDeTeste = [i for i in range(1000)]
for i in range(1000):
    listaDeTeste[i] = [i for i in range(1000)]
vetorDeTeste = np.array(listaDeTeste)
print("Soma de duas matrizes com vetor: ")
vetorDeTeste += vetorDeTeste
fim = time.time()
print("tempo de processamento = " + str(fim-inicio))
