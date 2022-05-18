#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:21:54 2022

@author: mac-prof
"""

import pandas as pd

estudantes = {"nome":["Álvaro","Pietra"],
              "curso":["Jor","Eco"]}
estudantes_df = pd.DataFrame(estudantes)

print(estudantes['nome'][0])
print(estudantes_df['nome'][0])
print(estudantes_df[estudantes_df['nome']== 'Álvaro'])

import numpy as np

b = np.array([1,4,7])
A = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(A + A)
print(2 * A)
print(A @ b)
print(A.T)
print(np.linalg.det(A))

from skimage import io
imagem = io.imread('bob.jpeg')

import matplotlib.pyplot as plt

plt.imshow(imagem)
print(imagem.shape)
plt.imshow(imagem[:,:,2])

plt.imshow(imagem[200:201,200:201,:])
plt.imshow(imagem[200:600,:,:])

# Webscrapping
# Deseja-se extrair os dados da tabela contida no url https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_Brazil
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_Brazil'
html = pd.read_html(url)
dados = html[0]

# Informações básicas
# Nomes das colunas
colunas = dados.columns
print(colunas)
# Selecionar colunas específicas
site = dados['Site']
print(site)
# Selecionar elementos específicos
print(dados['Criteria'][0:10])











