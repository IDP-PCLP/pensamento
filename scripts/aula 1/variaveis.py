#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:12:09 2022

@author: cafe
"""


# Variáveis em Python são declaradas com o sinal de =

numero = 1
texto = "Olá, mundo!"
booleano = True # ou False

# Podemos atribuir resultados de funções a variáveis
nome = input("Qual é seu nome? ")
print(f"Olá, {nome}!")

continuar = True
while continuar:
    continuar = False
    nome = input("Qual é seu nome? ")
    print(f"Olá, {nome}!")
    cont = input("Continuar? ")
    if cont == "S" or cont == "s":
        continuar = True
    if cont in "SsSim":
        continuar = True

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