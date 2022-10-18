#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date
import math

f = 1

def cola():    
    r = float(input("введите число "))
    global f
    
    if r == 0:
        print(f)
        return
    
    else:
        f = f * r
        
    print(f)
    cola()    
    
if __name__ == '__main__':
    cola()
    
