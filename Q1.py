# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:48:47 2020

@author: ARCHISMAN ROY
"""

list_of_words=['Bacon' , 'Steak' , 'Sausage' , 'Caramel' , 'Salmon']
print(list_of_words)
ls=[]

for i in range(0,len(list_of_words)):

    ls.append(list_of_words[i][:1])



print(ls)
