#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:12:34 2021

@author: cafe
"""

import random
# cara ou coroa
resultado = []

numCaras = 0
for i in range(10000):
    if round(random.random()) == 0:
        resultado.append("Cara")
        numCaras = numCaras + 1
    else:
        resultado.append("Coroa")

    
print(numCaras/len(resultado))