# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 17:32:42 2021

@author: schomsin
"""

PhoneNumPad = {1:[''],
               2:['a','b','c'],
               3:['d','e','f'],
               4:['g','h','i'],
               5:['j','k','l'],
               6:['m','n','o'],
               7:['p','g','r','s'],
               8:['t','u','v'],
               9:['w','x','y','z'],
               0:['']
    } 

phone="3662277"
words=["foo","bar","baz","foobar","emo","cap","car","cat"]

def PheneVsWoerds_rev0(PhoneNumPad=dict(),phone="",words=[]):

    InverstPad = dict()
    for x in PhoneNumPad :
        #key->x , value->PhoneNumPad[x]->list[,,]
        for y in PhoneNumPad[x]:
            InverstPad[y]=x
            pass
        pass
    
    print(InverstPad)
    
    out_num=[]
    out=[]
    #for w in words:
    for w in range(len(words)):
        #transfer "foor"->366
        num=""
        for ch in words[w]:
            n=InverstPad[ch]
            num=num+str(n)
            pass
        #print(num)
        #check this in phone
        if phone.find(num) != -1 :
            out_num.append(num)
            out.append(words[w])
            
        pass
    
    print(out_num)
    print(out)
    
    return out

def PheneVsWoerds(PhoneNumPad=dict(),phone="",words=[]):
    return PheneVsWoerds_rev0(PhoneNumPad,phone,words)

print("---PhoneNumPad---")
print(PhoneNumPad)
print("---phone---")
print(phone)
print("---words---")
print(words)
print("---find words that in phone---")
out2=PheneVsWoerds(PhoneNumPad,phone,words)