# -*- coding: utf-8 -*-
"""Álgebra Linear
"""

# Vamos importar a biblioteca para álgebra linear em Python - Numpy
import numpy as np

# Operações com matrizes e vetores
# Arrays são a forma do Numpy de representar matrizes
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
b =  np.array([1,4,7])

print(type(A))
print(type(b))

print(A+A)
print(b+A)

# Operações algébricas básicas em Álgebra Linear
print('Matriz A: ')
print(A)
print('Vetor b: '+str(b))
# Adição/Subtração
print('Soma de dois vetores:')
print('b+b= ' + str(b+b)) # Soma-se elemento a elemento do vetor
c =  np.array([1,4,5,6]) 
#print(b+c) # Vai produzir um erro, os vetores tem que ter o mesmo tamanho
print('Soma de uma matriz e um vetor, A+b:')
print(A + b)
print('Soma entre matrizes, A+A:')
print(A+A)
print('Subtração entre matrizes, A-A:')
print(A-A)

# Multiplicação
print('Multiplicação de matrizes e vetores por um escalar.')
escalar = 0.1
print(str(escalar) + ' vezes A: ')
print(escalar * A)
print(str(escalar) +' vezes b: ')
print(escalar * b)

# Divisão
print('Divisão de matrizes e vetores por um escalar.')
escalar = 0.1
print('A dividido por '+ str(escalar) + ': ')
print(A/escalar)
print('b dividido por '+ str(escalar) + ': ')
print(b/escalar)

# Multiplicação
print('Multiplicação entre matrizes e vetores')
print('A vezes A: ')
print(A * A)
print('b vezes b: ')
print(b * b)
# Produto ponto
print('A ponto A: ')
print(np.dot(A,A))
print('b ponto b: ')
print(np.dot(b, b))

help(np.dot)

A = np.array([[1,4],[2,1]])
b = np.array([2,4])
# O problema A x = b
print('Matriz A: ')
print(A)
print('Vetor b: '+str(b))
# Para resolver para x = b\A
print('Para resolver o sistema Ax = b: ')
print('x = '+ str(np.linalg.solve(A,b)))

print('Transpor matrizes e vetores: ')
print('Transposta de A: ')
print(A.T)
print('Transposta de b: ')
print(b.T)

print('Construção de matrizes especiais')
print('Matriz de zeros: ')
idade = np.zeros(24)
print(idade)
for i in range(idade.size):
  idade[i] = i
print(idade)

print('Matrizes especiais:')
print('Zeros: ')
print(np.zeros(10))
print('Uns: ')
print(np.ones(10))
print('Identidade: ')
print(np.eye(10))