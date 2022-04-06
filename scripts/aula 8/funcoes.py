#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 08:25:07 2021

@author: cafe
"""

print("A variável __name__ terá o valor '__main__' se o programa não for importado por outro script. Receberá o nome do script se for.")
print(__name__)

print("Sempre vai rodar.")

def main():
    print("Vai rodar se rodar como script.")

def somar_numeros(a=1,b=1):
    """
    Somar Números

    Parameters
    ----------
    a : TYPE, optional
        DESCRIPTION. The default is 1.
    b : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    print("Minha função somar números rodou!")
    return a + b
    

if __name__ == '__main__':
    main()