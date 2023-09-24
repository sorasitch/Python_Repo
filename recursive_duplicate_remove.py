# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:25:56 2021

@author: schomsin
"""

ls1 = [10,10,10,8,7,6,5,4,4,3,2,2,2,1,1,10,0,0]

def dup_rm(ls=[],size=0):
    pass

    #initail
    if size==0 :
        pass
        size=len(ls)

    #return end/last of recuresive
    if size==1 :
        pass
        return ls
    
    #call recuresive
    ls=dup_rm(ls,size-1)
    
    #do duplicate remove
    for i in range(size):
        pass
        if size==1 or size==0 :
            pass
            break
        if i==0 : 
            continue
        if i>=len(ls):break #prevent the index out of bound
        if ls[i]==ls[i-1] :
            ls.pop(i)
    return ls


def dup_rm1(ls=[],dp=[],size=0):
    pass

    #initail
    if size==0 :
        pass
        size=len(ls)

    #return end/last of recuresive
    if size==1 :
        pass
        return ls,dp
    
    #call recuresive
    ls,dp=dup_rm1(ls,dp,size-1)
    
    #do duplicate remove
    for i in range(size):
        pass
        if size==1 or size==0 :
            pass
            break
        if i==0 : 
            continue
        if i>=len(ls):break #prevent the index out of bound
        if ls[i]==ls[i-1] :
            dp.append(ls[i])
            ls.pop(i)
    return ls,dp

def dup_rm2(ls=[],dp=[],size=0):
    pass

    #initail
    if size==0 :
        pass
        size=len(ls)

    #return end/last of recuresive
    if size==1 :
        pass
        return ls,dp
    
    #call recuresive
    ls,dp=dup_rm2(ls,dp,size-1)
    
    #do duplicate remove
    for i in range(size):
        pass
    
        if i>=len(ls):break #prevent the index out of bound
    
        if ls[i] in dp : # check in dp
            ls.pop(i)
    
        if size==1 or size==0 :
            pass
            break
        
        if i==0 : 
            continue
        
        if i>=len(ls):break #prevent the index out of bound
        
        if ls[i]==ls[i-1] :
            dp.append(ls[i])
            ls.pop(i)
            ls.pop(i-1)
            
    return ls,dp

ls2 = ls1.copy()# non pointer
ls3 = ls2.copy()# non pointer
ls4 = ls3.copy()# non pointer

print("remove duplicate")
print(ls1)
dup_rm(ls1)#pointer
print(ls1)

print("remove duplicate and posisition 0 to " + str(int(len(ls2)/2)))
print(ls2)
dup_rm(ls2,int(len(ls2)/2)) #pointer
print(ls2)

print("remove duplicate and return duplicate")
print(ls3)
dp1=[]
dup_rm1(ls3,dp1) #pointer
print(ls3)
dup_rm(dp1)
print(dp1)

print("remove all duplicate and return duplicate")
print(ls4)
dp2=[]
dup_rm2(ls4,dp2) #pointer
print(ls4)
dup_rm(dp2)
print(dp2)




print("------------------------------------------------------")
ls1 = [10,10,10,8,7,6,5,4,4,3,2,2,2,1,1,0,0,0]
print(ls1)
ls=[]
dp=[]
for x in ls1:
    if x in dp :
        pass
        continue
    
    if x in ls :
        pass 
        dp.append(x)
        ls.remove(x)
        continue
    
    ls.append(x)
    
print(ls)
print(dp)
print("------------------------------------------------------")
ls1 = [10,10,10,8,7,6,5,4,4,3,2,2,2,1,1,0,0,0]
print(ls1)
ls=[]
dp=[]
for x in ls1:
    if x in dp :
        pass
        continue
    
    if x in ls :
        pass 
        dp.append(x)
        #ls.remove(x)
        continue
    
    ls.append(x)
    
print(ls)
print(dp)













