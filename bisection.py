#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:21:02 2019

@author: toaha
"""
import re

def resfin(list1, list2, inc):
    res1 = 0
    for i in range(0, len(list2)): #finding a & b
        if i == len(list2)-1:
            if list2[i] == '+':
                res1 = res1 + list1[i]
            else:
                res1 = res1 - list1[i]
                    #print("from else")
        elif(list2[i] == '+'):
            res1 = res1 + pow(inc,list1[i])
                    #print(res1, "from positive")
        else :
            res1 = res1 - pow(inc,list1[i])
                    #print(res1, "from negative")
    return res1



def parser(st):
    x = st
    #x = "x3-x1-11"
    sym = []
    if x[0] == '-':
        print()
    else:
        sym = ['+']
    #sym = ['+']
    for i in x:
        if i == '+' or i == '-':
            sym.append(i)
    print(sym)
    tot = []
    lis1 = x.split('+')
    for i in lis1:
        tot = tot + i.split('-')
    if x[0] == '-':
        tot.remove('')
    print(tot)
    #val = int(tot[len(tot)-1])
    #print(type(val))
        
    """p = re.search("x.+?\d+", x)
    p = p.group()
    print(p)
    lis = p.split('+')"""
    
    r = []
    for i in tot:
        p = re.search("\d+", i)
        temp = int(p.group())
        r.append(temp)
    print(r)
    
    return r, sym

def solver(list1, list2):
    res1 = resfin(list1, list2, 1)
    print(res1)
    
    a = 1
    b = 1
    
    if(res1 == 0):
        print("1 is the root value")
    elif res1 > 0:
        inc = 0
        while res1 > 0:
            res1 = resfin(list1, list2, inc)
            b = a
            a = inc
            print(res1, inc)
            print(b, a)
            inc = inc - 1
    else:
        inc = 0
        while res1 < 0:
            res1 = resfin(list1, list2, inc)
            b = a
            a = inc
            print(inc, res1)
            print(b, a)
            inc = inc + 1
    
    for i in range(0, 5000):
        c = (a + b) / 2
        print(c)
        if(resfin(list1, list2, c) > 0):
            a = c
            print(i, "-->", a, b)
        else:
            b = c
            print(i, "-->", a, b)
        if round(a, 4) == round(b, 4):
            break
            
    print("root value is : " , round(a, 4))
    
if __name__ == "__main__" :
    inp = input()
    p, q = parser(inp)
    solver(p, q)

"""this code can find value for like [x3 - x1 - 11] OR [x^3 - x^1 - 11] OR [-x1 + x3 - 11] OR [-x^1 + x^3 - 11]"""
