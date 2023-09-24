# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 18:49:48 2021

@author: schomsin
"""

blocks=[ 
        {"gym":False,
          "school":True,
          "store":True,
          "office":True,
          "mall":False,
          "bar":False,
          },
        {"gym":False,
          "school":True,
          "store":False,
          "office":False,
          "mall":False,
          "bar":False,
          },
        {"gym":True,
          "school":False,
          "store":False,
          "office":False,
          "mall":False,
          "bar":False,
          },
        {"gym":False,
          "school":False,
          "store":False,
          "office":False,
          "mall":True,
          "bar":True,
          }, 
        {"gym":True,
          "school":True,
          "store":False,
          "office":False,
          "mall":False,
          "bar":False,
          },
        {"gym":False,
          "school":True,
          "store":False,
          "office":True,
          "mall":False,
          "bar":False,
          },
        {"gym":False,
          "school":True,
          "store":True,
          "office":False,
          "mall":False,
          "bar":False,
          },
        ]

#reqs=["gym","school","store","office"]
#reqs=["office","school","store","gym"] #piority
#reqs=["office","school","store","gym","cacino"] #piority
#reqs=["bar","office","school","store","gym","cacino"] #piority
reqs=["school","office","store","gym","cacino"] #piority
    
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

def blocks_request(blocks=dict(),reqs=[]) :
#intail
    print("---intail---")
    req_block_dict=dict()
    cnt_req_dict=dict()
    cnt_sort_list=[]
    #cnt_req_list=[]
    blk_last=0
    #creat dict {"gym":[]}
    #for x in blocks:
   
    #pirority per reqs
    for x in reqs:
        req_block_dict[x]=[]
        pass
    blk_last=len(blocks)-1
        
    #pirority per blocks
    # for x in range(len(blocks)):
    #     for k in blocks[x].keys():
    #         #if blocks[x][k]==True : 
    #             #req_block_dict[k]=list_.append(x)
    #         req_block_dict[k]=[]
    #         pass
    #     blk_last+=1
        
    print(req_block_dict)
    print(blk_last)
    #creat dict {"gym":[1]}
    for x in range(len(blocks)):
        for k in blocks[x].keys():
            if blocks[x][k]==True : 
                if k not in req_block_dict.keys() : 
                    req_block_dict[k]=[]
                else :
                    req_block_dict[k].append(x)
            #req_block_dict[k]=[]
            pass
        
    #creat dict {2:[]}
    for k in req_block_dict.keys():
        #len(req_block_dict[k])#len(list)
        cnt_req_dict[len(req_block_dict[k])]=[]
        pass
    print(cnt_sort_list)
    
    #creat dict {2:[gym]}    
    for k in req_block_dict.keys():
        #len(req_block_dict[k])#len(list)
        o= cnt_req_dict[len(req_block_dict[k])]
        o.append(k)
        cnt_req_dict[len(req_block_dict[k])]=o
        pass
    
    cnt_sort_list+=cnt_req_dict.keys() 
    cnt_sort_list.sort()
    #remove 0
    sz=len(cnt_sort_list)
    for i in range(sz):
        if cnt_sort_list[0]>0:
            break
        cnt_sort_list.pop(0)
    #print(cnt_sort_list)
    #sort_min(cnt_sort_list)
    
    print(req_block_dict)
    print(cnt_req_dict)
    print(cnt_sort_list)
    #print(reqs)
    #print(req_block_dict.keys())
    #check request vs req of blocks.
    for k in reqs:
        if k in req_block_dict.keys() : 
            if len(req_block_dict[k])==0 :
                print(f'Wearning ! blocks dont have {k}')
                #return []
    # for k in reqs:
    #     if k not in blocks[0].keys() : 
    #         print(f'Wearning ! blocks dont have {k}')
    #         #return []
    
    #return
    
    #################
#functional
    print("---functional---")
    #cnt_sort_list,cnt_req_dict,req_block_dict,blk_last,reqs,blocks
    result=[]
    x=-1
    for x1 in range(len(cnt_sort_list)):
        #req_list=[] 
        #req_list=req_block_dict[cnt_req_dict[cnt_sort_list[x]]]#dict[dict[[list]]]=list
        #print(req_list)
        for regu in cnt_req_dict[cnt_sort_list[x1]]:
            req_list=[] 
            req_list= req_block_dict[regu]
            x+=1
            # print("result")
            # print(result)
            # print(x)
            print(result)
            print(regu)
                    
            if x==0 :
                #[[5],[4],[3]]
                for y in range(len(req_list)):
                    #print(req_list[y])
                    #x=0
                    result.append([req_list[y]])
                pass
    
                pass
            #x=1
            if x==1 :
                #result
                #0=[[5],[4],[3]]
                #1=[[5,4],[4,3],[]]
                
                for i in range(len(result)) :
                    #check duplicate
                    # for j in i:
                    #     #j
                    #     if j in req_list :
                    #         result[i].append(j)
                    #         break
                    #         pass
                    if len(result[i])>1:continue #check if previous make at item1
                    j=result[i][-1]
                    if j in req_list : 
                        result[i].append(j)
                        continue
                    #check rule
                    if j==0 :
                        result[i].append(req_list[0])
                        continue
                        pass
                    if j==blk_last :
                        result[i].append(req_list[-1])
                        continue
                        pass
                    size=len(req_list)
                    max_=-1
                    min_=-1
                    for a in range(size):
                        b=size-1-a
                        if req_list[a]>j :
                            max_=req_list[a]
                            pass
                        if req_list[b]<j :
                            min_=req_list[b]
                            pass
                        if (max_!=-1)and(min_!=-1) :
                            break
                            pass
                        pass
                    
                    if abs(max_-j)==abs(j-min_) : #here item1
                         result.append(result[i].append(min_))
                         result.append(result[i].append(max_))
                         continue
                    if abs(max_-j)>abs(j-min_) :
                        result[i].append(min_)
                        continue
                    else :
                        result[i].append(max_)
                        continue
                        
            #x>1
            if x>1 :
                #result
                #0=[[5],[4],[3]]
                #1=[[5,4],[4,3],[...]]
                #2=[[5,4,3],[4,3,2],[...]]
                #3=[[5,4,3,2],[4,3,2,1],[...]]
    
                for i in range(len(result)) :
                 
                    if len(result[i])>x:continue #check if previous make at item1
    
                    
                    b_duplicate=False
                    size_i=len(result[i])
                    for k in range(size_i):
                        l=size_i-1-k
                        # if j in req_list :
                        #     result[i].append(j)
                        #     break
                        #     pass
                        #check duplicate
                        #if len(result[i])>1:continue #check if previous make at item1
                        j=result[i][l]
                        if j in req_list : 
                            result[i].append(j)
                            b_duplicate=True
                            break
                    if b_duplicate : continue
                
                
                    #check rule
                    j=result[i][-1]
                    if j==0 :
                        result[i].append(req_list[0])
                        continue
                        pass
                    if j==blk_last :
                        result[i].append(req_list[-1])
                        continue
                        pass
                    
                    lt=result[i]
                    # print(lt)
                    # print(i)
                    # print("here")
                    # print(lt)
                    lt.sort()
                    # print(lt)
                    lt_min=lt[0]
                    lt_max=lt[-1]
                    size=len(req_list)
                    max_=-1
                    min_=-1
                    for a in range(size):
                        b=size-1-a
                        if req_list[a]>j :
                            max_=req_list[a]
                            pass
                        if req_list[b]<j :
                            min_=req_list[b]
                            pass
                        if (max_!=-1)and(min_!=-1) :
                            break
                            pass
                        pass
                    
                    if (lt_min<=min_)and(min_<=lt_max) :
                        result[i].append(min_)
                        continue
                        pass
                    if (lt_min<=max_)and(max_<=lt_max) :
                        result[i].append(max_)
                        continue
                        pass
                    
                    if abs(max_-j)==abs(j-min_) : #here item1
                        result.append(result[i].append(min_))
                        result.append(result[i].append(max_))
                        continue
                    if abs(max_-j)>abs(j-min_) :
                        result[i].append(min_)
                        continue
                    else :
                        result[i].append(max_)
                        continue
                pass
            pass

    print(result)

    

    return result



print("---blocks---")
print(blocks)
print("---reqs at piority in order---")
print(reqs)
result=blocks_request(blocks,reqs)
print("The best pactic offer will the same distance to travel so choice which block in list[offer1=[block-choice1,block-choice2,..,],offer2=[block-choice1,block-choice2,..,],..]")
print(result)