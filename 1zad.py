#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

def test():
    x = int(input())
    if x >= 0:
        positive()
    else:
        negative()
        

def positive():
    print("положительное")

    
def negative():
    print("Отрицательное") 
    
        
if __name__ == '__main__':
    test()
