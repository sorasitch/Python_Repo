# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:28:21 2021

@author: schomsin
"""

f = open("readme.csv", "r")
print(f)
#print(len(f.read())) #number of chars
ls=[]
dp=[]
for x in f:
    # print(x)
    # try :
    #     pass
    #     if dp.index(x)>=0 :
    #         break
    # except :
    #     pass
    if x in dp :
        pass
        continue
    ls_b=True
    for y in range(len(ls)) :
        pass
        if ls[y] == x :
            pass
            ls.pop(y)
            ls_b=False
            dp_b=True
            for z in range(len(dp)) :
                pass
                if dp[z] == x :
                    pass
                    dp_b=False
                    break;
                else :
                    pass
            if dp_b : dp.append((x))
            break;
        else :
            pass

    pass
    if ls_b : ls.append(x)
print(f.read())
f.close()
print(len(dp))
print(len(ls))
print("start write readme_duplicate.csv")
f = open("readme_duplicate.csv", "w")
for w in dp :
    f.write(str(w))
f.close()
print("start write readme_nonduplicate.csv")
f = open("readme_nonduplicate.csv", "w")
for w in ls :
    f.write(str(w))
f.close()









print("---------------------------------------------------------")
print("start new era")
f = open("readme.csv", "r")
print(f)
#print(len(f.read())) #number of chars
ls=[]
dp=[]
for x in f:
    if x in dp :
        pass
        continue
    
    if x in ls :
        pass 
        dp.append(x)
        ls.remove(x)
        continue
    
    ls.append(x)
    

print(f.read())
f.close()
print(len(dp))
print(len(ls))
print("start write readme_duplicate.csv")
f = open("readme_duplicate.csv", "w")
for w in dp :
    f.write(str(w))
f.close()
print("start write readme_nonduplicate.csv")
f = open("readme_nonduplicate.csv", "w")
for w in ls :
    f.write(str(w))
f.close()








print("---------------------------------------------------------")
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

print("start new era")
f = open("readme.csv", "r")
print(f)
ls1=[]
for x in f:
    pass
    ls1.append(x)
f.close()
print(len(ls1))

#dup_rm(ls1)#pointer   

print("end new era") 