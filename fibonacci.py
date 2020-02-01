# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:24:18 2020

@author: CEC
"""

def fibon (n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b     #a=b ; b= a+b es asignación múltiple
    print()
#fibon(8000)