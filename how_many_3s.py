# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:46:07 2020

@author: ROSHAN
"""

a=int(input("enter number \t"))
count=0
while a!=0:
    x=a%10
    if(x==3):
        count+=1
    a=a//10
print("numbers of threes = "+str(count))