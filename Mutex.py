# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:58:05 2021

@author: schomsin
"""

import asyncio
import time

async def myWorker(mutex,num):
    await mutex.acquire()
    print("Successfully acquired the Mutex(share resourse) by " + num)
    await asyncio.sleep(3)
    print("Releasing Mutex(share resourse) by " + num)
    mutex.release()

async def main(loop):
    myMutex = asyncio.Lock()
    await asyncio.wait([myWorker(myMutex,"1"), myWorker(myMutex,"2"), myWorker(myMutex,"3")])
    print("Main Coroutine")

loop = asyncio.get_event_loop()
"""
loop.run_until_complete(main(loop))
print("All Workers Completed")
loop.close()
"""

try:
    asyncio.ensure_future(main(loop))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
    
"""
Successfully acquired the Mutex(share resourse) by 3
Releasing Mutex(share resourse) by 3
Successfully acquired the Mutex(share resourse) by 1
Releasing Mutex(share resourse) by 1
Successfully acquired the Mutex(share resourse) by 2
Releasing Mutex(share resourse) by 2
Main Coroutine
"""