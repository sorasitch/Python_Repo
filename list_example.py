# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 07:43:37 2021

@author: schomsin
"""
l=[]
l0=[1,2]
l1=[[1,2],[3,4]]
l2=l0+l1
print(l2)
l3=[]
l3.append(l0)
l3.append(l1)
print(l3)
l4=[]
l4.extend(l0)
l4.extend(l1)
print(l4)
l5=[]
l5=l0+l1[1]
print(l5)
l6=[]
l6=l+l0
l6=l6+[99]
print(l6)

l7=[]
for i in l1 :
    print(i)
    l7.append(i)
print(l7)

if 1 in l1 :
    print(l1)
else:
    print("no")
    
    # not work
# n = 123456789
# for m in n:
#     print(m)