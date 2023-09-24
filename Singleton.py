# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 07:53:08 2021

@author: schomsin

"""

# Singleton pattern
class Singleton:
 
    # state shared by each instance
    __sharedstate = dict()
    __sharedstate1 = list()
 
    # constructor method
    def __init__(self):
 
        self.__dict__ = self.__sharedstate
        self.state = 'Geeks'
        self.__list__ = self.__sharedstate1
        self.state1 = 'Geeks1'
 
    def __str__(self):
 
        return self.state1 #self.state
    
    def getv(self):
 
        return self.state1 , self.state
 
# main method
if __name__ == "__main__":
 
    person1 = Singleton()    # object of class 
    person2 = Singleton()    # object of class 
    person3 = Singleton()    # object of class 
 
    person1.state = 'Data' # person1 changed the state
    person1.state1 = 'Data1'
    person2.state = 'Alg'     # person2 changed the state
    person2.state1 = 'Alg1'
 
    print(person1)    # output --> Alg
    print(person2)    # output --> Alg
    print(person1.getv())    # output --> Alg
    print(person2.getv())    # output --> Alg
 
    person3.state = 'Geeks'  # person3 changed the
                         # the shared state
    person3.state1 = 'Geeks1'
 
    print(person1)    # output --> Geeks
    print(person2)    # output --> Geeks
    print(person3)    # output --> Geeks
    
    print(person1.getv())    # output --> Geeks
    print(person2.getv())    # output --> Geeks
    print(person3.getv())    # output --> Geeks
    
"""    
Alg1
Alg1
('Alg1', 'Alg')
('Alg1', 'Alg')
Geeks1
Geeks1
Geeks1
('Geeks1', 'Geeks')
('Geeks1', 'Geeks')
('Geeks1', 'Geeks')
"""    