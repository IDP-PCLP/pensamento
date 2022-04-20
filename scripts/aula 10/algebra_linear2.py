# -*- coding: utf-8 -*-
"""
Álgebra Linear - operações
Created on Thu Oct  7 10:12:31 2021

@author: alvar
"""

import numpy as np


A = np.array([[-1,0],[2,3]])
B = np.array([[1,2],[3,0]])

print(A*B == B*A)
print(np.matmul(A,B) == np.matmul(B,A))
print(A@B == B@A)
print(np.matmul(A,B) == A@B)
print(np.matmul(B,A) == B@A)

C = np.matmul(A,B)
D = np.matmul(B,A)
E = A*B


# Essas matrizes podem ser retangulares, isso é, ter um número de linhas diferente do número de colunas
zeros = np.zeros([10,5])
uns = np.ones([50,5]) 
# Matriz Identidade sempre tem que ser quadrada
identidade = np.eye(10) 

# Solução de sistemas de equações lineares
# A equação está na forma Ax = b
b = B[:,0] # Definir o vetor b
# Para resolver, encontra-se x = b\A
x = np.linalg.solve(A,b)
print(A@x == b)

# Transposta
print('Para a matriz A = ')
print(A)
print('A transposta é ')
print(A.T)

# Inversa
print('Para a matriz A = ')
print(A)
print('A inversa é ')
print(np.linalg.inv(A))
print('A multiplicação de A por inv(A) =')
print(A @ np.linalg.inv(A))
print('inv(A) multiplicado por A =')
print(np.linalg.inv(A) @ A)
print(np.linalg.inv(A) @ A == np.eye(2))

# Determinante
A = np.array([[3,1],[2,1]])
B = np.array([[-1,3],[5,8]])
print('Matriz A = ')
print(A)
print('Determinante de A = ')
print(np.linalg.det(A)) # O determinante mostra se a matriz é invertível
print('A inversa de A é ')
print(np.linalg.inv(A))

print('Matriz B = ')
print(B)
print('Determinante de B = ')
print(np.linalg.det(B))
print('A inversa de B é ')
print(np.linalg.inv(B))

print('Matriz C = ')
print(C)
print('Determinante de C = ')
print(np.linalg.det(C)) # O determinante mostra se a matriz é invertível
print('A inversa de C é ')
print(np.linalg.inv(C))

print('Matriz D = ')
print(D)
print('Determinante de D = ')
print(np.linalg.det(D))
print('A inversa de D é ')
print(np.linalg.inv(D))

print('Matriz E = ')
print(E)
print('Determinante de E = ')
print(np.linalg.det(E))
print('Se o determinante de uma matriz for igual a zero, essa matriz não pode ser invertida.')
# print('A inversa de E é ')
# print(np.linalg.inv(E)) # Vai ocasionar em erro