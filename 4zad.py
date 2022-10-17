#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date
import math

def get_input():
    D = input("Введите число")
    return D

def test_input(b):
    f = b.isdigit()
    if f == True:
        return True
    else:
        False
    
def str_to_int(b):
    C= int(b)
    return C

def print_int(C):
    print(C)

        
if __name__ == '__main__':
   
    a = get_input()
    b = test_input(a)
    if b == True:
        C=str_to_int(a)
        print_int(C)
    else:
        print("ошибка")
