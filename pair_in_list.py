# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 20:46:39 2021

@author: schomsin
"""

# lt=[1,2,3,4,4,5,5,6,6,7,7]
# lt=[7,7,6,6,5,5,4,4,3,2,1]
lt=[1,6,2,7,3,6,4,7,5,5,4]

#one_pair same result both pair_noorder,pair_order_adjective
#no one_pair same result only adjective data for pair_order_adjective pair_noorder , pair_order_adjective no good
def pair_noorder(lt=[],one_pair=True):
    result_index=[]
    result_pair=[]
    sz=len(lt)
    stack_inx=[]
    #print(sz)
    for i in range(sz):
        if i >= sz-1 : break
        if one_pair :
            if i in stack_inx : continue
        for j in range(i+1,sz):
            if one_pair : 
                if j in stack_inx : continue
            #print(f'{i} {j}')
            if lt[i]+lt[j]==8 :
                result_index.append([i,j])
                result_pair.append([lt[i],lt[j]])
                stack_inx.append(j)
                if one_pair : break #only one piar
                
    return result_index,result_pair
            
result_index,result_pair=pair_noorder(lt)
# result_index,result_pair=pair_noorder(lt,False)
print(f'index : {result_index}')
print(f'result : {result_pair}')
            
        
def pair_order_adjective(lt=[],one_pair=True):        
    result_index=[]
    result_pair=[]
    stack=[]
    stack_inv=[]
    sz=len(lt)
    #print(sz)
    for i in range(sz):
        if i==0 :
            stack.append(lt[i])
            stack_inv.append(8-lt[i])
            continue
        
        if lt[i] in stack_inv :
            p_inv = stack_inv.index(lt[i]) # p_index 0..n
            value = stack[p_inv]
            p_index = lt.index(value)
            value = stack[p_inv]
            result_index.append([p_index,i])
            result_pair.append([value,lt[i]])
            if one_pair : stack.pop(p_inv)#only one piar
            if one_pair : stack_inv.pop(p_inv)#only one piar
        else:
            stack.append(lt[i])
            stack_inv.append(8-lt[i])
    return result_index,result_pair
       
result_index,result_pair=pair_order_adjective(lt) 
# result_index,result_pair=pair_order_adjective(lt,False) 
print(f'index : {result_index}')
print(f'result : {result_pair}')
        