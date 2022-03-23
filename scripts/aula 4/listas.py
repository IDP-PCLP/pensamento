#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:32:57 2022

@author: cafe
"""

# Estruturas de dados
# Listas e dicionários

# A lista é ordenada, por isso é fácil acessar seus elementos em ordem, um processo chamado iterar pela lista
nomes = ["Álvaro", "Bernardo", "Beatriz"]

nomes[0] # Acessando elementos de uma lista
for nome in nomes: # Definindo um laço for
    print(nome)

nomes = []
continuar = True
while continuar:
    continuar = False
    nome = input("Qual é seu nome? ")
    print(f"Olá, {nome}!")
    nomes.append(nome)
    cont = input("Continuar? ")
    if cont == "S" or cont == "s":
        continuar = True
    if cont in "SsSim":
        continuar = True

# Controle de fluxo é o processo de determinar o fluxo de operações ou seja a ordem e repetições
for nome in nomes: # Definindo um laço for
    if nome == "Álvaro":
        print(f"Bom dia, professor {nome}")
    else:
        print(f"Bom dia, {nome}")
