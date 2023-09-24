# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:14:09 2021

@author: schomsin
"""


from threading import Thread , Lock
import threading

class Counter(Thread):

    def __init__(self, end):
        Thread.__init__(self)
        self.lock = Lock()
        self.end = end
        self.start()
        self.join()

    def run(self):
        self.lock.acquire()
        print("Successfully acquired the spinlock(share resourse) by " + self.name)
        
        # for i in range(1, self.end + 1):
        #    # print("Successfully acquired the spinlock")
        #     print(self.name + ": " + str(i))
            
        i=0
        while i < 5 :
            # print("Successfully acquired the spinlock")
            print(self.name + ": " + str(i))
            i+=1
            
        self.lock.release()
        print("Successfully release the spinlock(share resourse) by " + self.name)
        

thr1 = Counter(5)
thr2 = Counter(5)
thr3 = Counter(5)
# thr1.start() 
# thr1.join()
# thr2.start()
# thr2.join()
# thr3.start()
# thr3.join()

#thr1.join()
#thr2.join()
#thr3.join()

# Block until thread 1 is done 
#thr1.join()

"""
Successfully acquired the spinlock(share resourse) by Thread-436: 1
Successfully acquired the spinlock(share resourse) by Thread-436: 2
Successfully acquired the spinlock(share resourse) by Thread-436: 3
Successfully acquired the spinlock(share resourse) by Thread-436: 4
Successfully acquired the spinlock(share resourse) by Thread-436: 5
Successfully acquired the spinlock(share resourse) by Thread-437: 1
Successfully acquired the spinlock(share resourse) by Thread-437: 2
Successfully acquired the spinlock(share resourse) by Thread-437: 3
Successfully acquired the spinlock(share resourse) by Thread-437: 4
Successfully acquired the spinlock(share resourse) by Thread-437: 5
Successfully acquired the spinlock(share resourse) by Thread-438: 1
Successfully acquired the spinlock(share resourse) by Thread-438: 2
Successfully acquired the spinlock(share resourse) by Thread-438: 3
Successfully acquired the spinlock(share resourse) by Thread-438: 4
Successfully acquired the spinlock(share resourse) by Thread-438: 5
"""

