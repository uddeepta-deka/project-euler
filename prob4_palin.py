#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:32:49 2021

@author: uddeepta
"""
# Finding the largest palindrome number
# formed by the product of two 3 digit numbers

import numpy as np
from itertools import product
def is_palindrome(num):
    nstr = str(num)
    match = 0
    checklen = int(len(nstr)/2)
    for i in range(checklen):
        if nstr[i] == nstr[-i-1]:
            match+=1
    if match == checklen:
        return 1
    else:
        return 0

def largest_palin():
    x = np.arange(999,99,-1)
    multiplied_vec = [m*n for m,n in product(x,x)]
    palin_vec = []
    for num in multiplied_vec:
        if is_palindrome(num)==1:
            palin_vec.append(num)
    print(max(palin_vec))

    
largest_palin()
