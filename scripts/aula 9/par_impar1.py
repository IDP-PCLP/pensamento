#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:45:16 2021

@author: cafe
"""

import random

def jogar():
    while True:
        jogada = input("Par ou ímpar? ")
        adversario = random.randint(0,10)%2
        if adversario == 0:
            if jogada == "par":
                print("Venceu!!")
            else:
                print("Perdeu!!")
        else:
            if jogada == "par":
                print("Perdeu!!")        
            else:
                print("Venceu!!")

if __name__ == '__main__':
    jogar()   