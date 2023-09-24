# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 08:45:55 2021

@author: schomsin
"""
ls1 = [10,9,8,7,6,5,4,3,2,1,0]

def sort_ls_min(ls=[],size=0): 
    pass

    #initail
    if(size==0): 
        pass
        size=len(ls)

    #return end/last of recuresive
    if(size==1):
        return ls #return pointer
    
    #call recuresive
    ls=sort_ls_min(ls,size-1) # get pointer
    
    #do sort
    for i in range(size) :
        pass
        j=size-1-i 
        if j==0 :
            break
        if ls[j-1]>ls[j]:
            pass
            _max=ls[j-1]
            ls[j-1]=ls[j]
            ls[j]=_max
        
    return ls #return pointer

def sort_ls_max(ls,size=0):
    pass

    #initail
    if(size==0): 
        pass
        size=len(ls)

    #return end/last of recuresive
    if(size==1):
        return ls
    
    #call recuresive
    newls=sort_ls_max(ls,size-1)
    
    #do sort
    for i in range(size) :
        pass
        j=size-1-i 
        if j==0 :
            break
        if newls[j-1]<newls[j]:
            pass
            _max=newls[j-1]
            newls[j-1]=newls[j]
            newls[j]=_max
        
    return newls
   
print(ls1)
print(len(ls1))

ls1_=ls1.copy()  # non pointer
#ls1_=ls1  # pointer
print("sort_ls_min")
ls2=sort_ls_min(ls1_,int(len(ls1_)/2))# pointer
ls2[5]=999
print(ls1)
print(ls2)
print(ls1_)

#ls2_=ls2.copy() # non pointer
#ls2_=ls2 # pointer
print("sort_ls_max")
ls3=sort_ls_max(ls2,len(ls2))# pointer
print(ls1)
print(ls2)
print(ls3)
print(ls1_)
#print(ls2_)

print("pointer")
sort_ls_min(ls1)# pointer
print(ls1)
print(ls2)
print(ls3)




print("------------------------------------------------------")
ls1 = [10,9,8,8,7,6,5,4,3,2,1,0]

def sort_min(ls=[]): 
    pass

    for j in range(len(ls)):
        pass
        if j==0 : continue
        for z in range(j):
            i=j-z
            if ls[i-1]>ls[i] :
                pass
                min_=ls[i]
                ls[i]=ls[i-1]
                ls[i-1]=min_
    
        
    return ls #return pointer

def sort_max(ls=[]): 
    pass

    for j in range(len(ls)):
        pass
        if j==0 : continue
        for z in range(j):
            i=j-z
            if ls[i-1]<ls[i] :
                pass
                max_=ls[i]
                ls[i]=ls[i-1]
                ls[i-1]=max_
    
        
    return ls #return pointer

print(ls1)
sort_min(ls1)
print(ls1)
sort_max(ls1)
print(ls1)