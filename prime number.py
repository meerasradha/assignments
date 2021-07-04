# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 20:11:34 2021

@author: meera
"""
x=int(input("enter a number:"))
if x > 1:
  
   for i in range(2,x):
       if (x % i) == 0:
           print(x,"is not a prime number")
           break
   else:
       print(x,"is a prime number")
       

