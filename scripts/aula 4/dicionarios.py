#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:32:57 2022

@author: cafe
"""

# Estruturas de dados
# Listas e dicionários

# Dicionários são estruturas de dados relacionais, que associam valores e chaves
alunos = {"Álvaro":0, "Bernardo":1, "Beatriz":2}

for codigo,nome in enumerate(alunos):
    print(nome,codigo)
    
nomes = {}
continuar = True
iter = 0
while continuar:
    continuar = False
    nome = input("Qual é seu nome? ")
    print(f"Olá, {nome}!")
    iter = iter + 1
    nomes[nome] = iter
    cont = input("Continuar? ")
    if cont == "S" or cont == "s":
        continuar = True
    if cont in "SsSim":
        continuar = True

for codigo,nome in enumerate(nomes):
    print(nome,codigo)