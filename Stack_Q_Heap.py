# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:58:30 2021

@author: schomsin
"""

#stack

ls = []

# Let's push some letters into our list
ls.append('1')
ls.append('2')
ls.append('3')
ls.append('4')
print(ls) 

last_item = ls.pop()
print(last_item)

last_item = ls.pop()
print(last_item)

print(ls)


#queue

ls = []

# Let's push some letters into our list
ls.append('1')
ls.append('2')
ls.append('3')
ls.append('4')
print(ls) 

last_item = ls.pop(0)
print(last_item)

last_item = ls.pop(0)
print(last_item)

print(ls)



import heapq
  
# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify to convert list into heap
heapq.heapify(li)
  
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
  
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
  
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))
  
# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))
print (list(li))

"""
['1', '2', '3', '4']
4
3
['1', '2']
['1', '2', '3', '4']
1
2
['3', '4']
The created heap is : [1, 3, 9, 7, 5]
The modified heap after push is : [1, 3, 4, 7, 5, 9]
The popped and smallest element is : 1

"""