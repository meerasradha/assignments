# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:44:31 2021

@author: meera
"""

maxticket=5
participants=[]
import random
for i in range (0,5):
    participants=str( input("enter names:"))
n=random.randint(0,maxticket-1)
print("winner:",participants)