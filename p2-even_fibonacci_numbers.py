#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:10:24 2021

@author: uddeepta
"""
# Considering terms whose values do not exceed
# four million, find sum of the even valued terms

def fibonacci(Nmax):
    """
    Returns Fibonacci sequence whose max 
    value is <= Nmax

    """
    seq = []
    seq.append(1)
    seq.append(2)
    while seq[-1] <= Nmax:
        seq.append(seq[-1] + seq[-2])
    return seq[:-1]

def even_val_sum(Nmax):
    """
    Finds the sum of even valued terms in 
    a Fibonacci sequence

    Parameters
    ----------
    Nmax : max value of term in the Fibonacci sequence
    
    Returns
    -------
    res : sum of the even valued terms

    """
    seqn = fibonacci(Nmax)
    res = 0
    for el in seqn:
        if el % 2 == 0:
            res += el
    return res

if __name__=="__main__":
    print("This program finds the sum of the even-valued terms.")
    print(even_val_sum(4000000))