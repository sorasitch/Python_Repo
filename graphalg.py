# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 23:33:33 2021

@author: schomsin
"""
"""
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

#print(graph)

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            print(newpath)
            # if newpath: return newpath
    return None

p=find_path(graph, 'A', 'D')
print(p)

print("find_all_paths")
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            print(newpaths)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

p=find_all_paths(graph, 'A', 'D')
print(p)

print("find_shortest_path")
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            print(newpath)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


p2=find_shortest_path(graph, 'A', 'D')
print(p2)

s=None
print(not s)
"""



"""
print("------------------------------------------------------")
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

ls=[]
for node in graph :
    ls1=[]
    for direct in graph[node] :
        if direct in graph :
            ls1.append(node)
            ls1.append(direct)
            for node1 in graph[direct]:
                if node1 in graph :
                    ls1.append(node1)
            pass
    ls.append(ls1)
print(ls)
    

print("------------------------------------------------------")

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['F'],
         'E': ['F'],
         'F': ['C']}
def direction(graph=dict() ,start='' , stop='', rount=[]):
    #initial
    rount1=[]
    rount2=[]
    
    if start in rount :
        return None
    
    if start in graph.keys(): #key
        rount.append(start)
        pass
    else:
        return None
    
    #return end/last of recuresive
    if start in graph.keys(): #key
        if stop in graph[start]: # value
            rount1 = rount.copy()
            rount1.append(stop)
            return rount1
    
    #call recuresive
    #rount = direction(graph,start,stop,rount)

    #do functional
    if stop not in graph[start]: # value
        for node in graph[start]:
            result = direction(graph,node,stop,rount)
            if result != None :
                if stop in result :
                    print(result)       
                    rount2.append(result)
        print(rount2)       
        
    return rount2

line=[]
result=direction(graph,'A','F')
#print(result)
#print(line)
"""

print("------------------------------------------------------")
"""
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['F'],
         'E': ['F'],
         'F': ['C']}
"""
"""
graph = {'A': ['B', 'F'],
         'B': ['A', 'C', 'E'],
         'C': ['D', 'F'],
         'D': ['C', 'E'],
         'E': ['D', 'F', 'B'],
         'F': ['C', 'A']}

weight = {'AB':2,
          'AF':10,
          'BA':2,
          'BC':1,
          'BE':2,
          'CD':1,
          'CF':1,
          'DC':1,
          'DE':3,
          'ED':1,
          'EF':1,
          'EB':1,
          'FC':2,
          'FA':1
          
    }
"""

graph = {'A': ['B', 'F'],
         'B': ['A', 'C', 'E'],
         'C': ['F'],
         'D': ['C', 'E'],
         'E': ['F', 'B'],
         'F': ['C', 'A']}

weight = {'AB':2,
          'AF':10,
          'BA':2,
          'BC':1,
          'BE':2,
          #'CD':1,
          'CF':1,
          'DC':1,
          'DE':3,
          #'ED':1,
          'EF':1,
          'EB':1,
          'FC':2,
          'FA':1
          
    }

def direction_rev1(graph=dict() ,start='' , stop='', rount=[]):
    #initial
    rount1=[]
    rount2=[]
    if start in rount :
        return []
    if start not in graph.keys(): #key
        return []
    rount=rount+[start]
    
    #return end/last of recuresive
    if start==stop :
        return rount

    
    #call recuresive
    #rount = direction1(graph,start,stop,rount)
    for node in graph[start]:
        rount1 = direction_rev1(graph,node,stop,rount)
        print(rount1)
        if stop not in rount1 : #first return [A,...,D]
            for i in rount1 :
                rount2.append(i)
        else :
            rount2.append(rount1) #first return [A,...,D]
        #if start == 'A' : print(rount1)
        #return rount1
        

    #do functional
    return rount2


def weight_direction(weight=dict(), result=[]):
    w=0
    w1=0
    for i in range(len(result)) :
        if i ==0 : continue
        key=str(result[i-1]+result[i])

        if key in weight.keys() :
            #print(key)
            w=weight[key]
            w1+=w
        else:
            return -1
            pass
        
    return w1
  
print("graph")  
print(graph)
print("weight")
print(weight)
line=[]
# print("travel from A to F")
# result=direction_rev1(graph,'A','F')
print("travel from D to A")
result=direction_rev1(graph,'D','A')
print("direction result")
print(result)
path_max=[]
max_=0
path_min=[]
min_=0
i=0
x=9999
for path in range(len(result)) :
    #j=len(result[path])
    j=weight_direction(weight,result[path])
    if i<j :
        i=j
        max_=j
        path_max=result[path]
    if x>j :
        x=j
        min_=j
        path_min=result[path]
        
print("direction : max weight = "+str(max_))
print(path_max)
print("direction : min weight = "+str(min_))
print(path_min)


# r=['A', 'B', 'C', 'D', 'E', 'F']
# w=weight_direction(weight,r)
# print(w)


import threading
global reslt
reslt=[]


def direction_rev2(graph=dict() ,start='' , stop='', rount=[]):
    #initial
    global reslt
    rount1=[]
    rount2=[]
    if start in rount :
        reslt=[]
        return []
    if start not in graph.keys(): #key
        reslt=[]
        return []
    rount=rount+[start]
    
    #return end/last of recuresive
    if start==stop :
        return rount

    
    #call recuresive
    #rount = direction1(graph,start,stop,rount)
    for node in graph[start]:
        rount1 = direction_rev2(graph,node,stop,rount)
        print(rount1)
        if stop not in rount1 : #first return [A,...,D]
            for i in rount1 :
                rount2.append(i)
        else :
            rount2.append(rount1) #first return [A,...,D]
        #if start == 'A' : print(rount1)
        #return rount1
        

    #do functional
    reslt=rount2.copy()
    #print(reslt)
    return rount2


thr = threading.Thread(target=direction_rev2, args=[graph,'D','A'])
thr.start()
thr.join()
print(thr)
print(reslt)




import threading
global reslt3
reslt3=[]


def direction_rev3(graph=dict() ,start='' , stop='', rount=[]):
    #initial
    global reslt3
    #reslt3=[]
    rount1=[]
    rount2=[]
    if start in rount :
        reslt3=[]
        return []
    if start not in graph.keys(): #key
        reslt3=[]
        return []
    rount=rount+[start]
    
    #return end/last of recuresive
    if start==stop :
        return rount

    
    #call recuresive
    #rount = direction1(graph,start,stop,rount)
    for node in graph[start]:
        #rount1 = direction_rev3(graph,node,stop,rount)
        thr = threading.Thread(target=direction_rev3, args=[graph,node,stop,rount])
        thr.start()
        thr.join()
        print(thr)
        rount1=reslt3
        print(rount1)
        if stop not in rount1 : #first return [A,...,D]
            for i in rount1 :
                rount2.append(i)
        else :
            rount2.append(rount1) #first return [A,...,D]
        #if start == 'A' : print(rount1)
        #return rount1
        

    #do functional
    reslt3=rount2.copy()
    #print(reslt3)
    return rount2

result=direction_rev3(graph,'D','A')
# thr = threading.Thread(target=direction_rev3, args=[graph,'D','A'])
# thr.start()
# thr.join()
# print(thr)
print(reslt3)