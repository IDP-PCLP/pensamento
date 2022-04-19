#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:21:09 2021

@author: cafe
"""
import random

def jogar():
    jogadas = ['pedra', 'papel', 'tesoura']
    # gerar um número entre 1 e 3
    adversario = jogadas[random.randint(0,3)]
    
    a = input("pedra [0], papel [1] ou tesoura [2]? ")
    print(f"O adversário jogou {adversario} e você jogou {jogadas[int(a)]}")
    if jogadas[int(a)] == adversario:
        print("Empate!")
    elif jogadas[int(a)] == 'pedra' and adversario == 'papel':
        print("Perdeu!")
    elif jogadas[int(a)] == 'pedra' and adversario == 'tesoura':
        print("Ganhou!")
    elif jogadas[int(a)] == 'papel' and adversario == 'pedra':
        print("Ganhou!")
    elif jogadas[int(a)] == 'papel' and adversario == 'tesoura':
        print("Perdeu!")
    elif jogadas[int(a)] == 'tesoura' and adversario == 'pedra':
        print("Perdeu!")
    elif jogadas[int(a)] == 'tesoura' and adversario == 'papel':
        print("Ganhou!")