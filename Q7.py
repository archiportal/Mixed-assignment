# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:53:45 2020

@author: ARCHISMAN ROY
"""

def Calculate_Bill(StoreList,Customer_List):
    total = 0
    for item in Customer_List:
        if item in StoreList:
            cost = StoreList[item] * Customer_List[item]
            total += cost
        else:
            return -1
    return total

Products = { "Football": 2500, "Spikes": 5200, "Shin Guard": 900, "Jersey": 3500}
print(Products)
CProd = { "Football": 3,"Spikes": 2, "Jersey": 3 }
print(CProd)
print("Yor total bill : Rs " , Calculate_Bill(Products,CProd))
