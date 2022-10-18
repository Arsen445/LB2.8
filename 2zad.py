#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date
import math

cir = 1

def cylinder():    
    r = float(input("введите радиус "))
    h = float(input("введите высоту "))
    
    def circle(r):
        r = 3.14 * (r ** 2)
        global cir
        cir = r
      
    print("S: Полная-1  Боковая-2")
    d = int(input())
   
    if d == 1:
        print((2 * 3.14 * r) + h + (2 * cir))
    if d == 2:
        print((2 * 3.14 * r) + h)

        
if __name__ == '__main__':
    cylinder()
    
