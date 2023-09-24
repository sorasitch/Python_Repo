# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 10:43:21 2021

@author: schomsin
"""

def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
recursion(6)