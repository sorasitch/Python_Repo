# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:40:12 2021

@author: schomsin
"""

import asyncio
import time

async def myWorker(semaphore,num):
    await semaphore.acquire()
    print("Successfully acquired the semaphore(share resourse) by " + num)
    await asyncio.sleep(3)
    print("Releasing Semaphore(share resourse) by " + num)
    semaphore.release()

async def main(loop):
    mySemaphore = asyncio.Semaphore(value=2)
    await asyncio.wait([myWorker(mySemaphore,"1"), myWorker(mySemaphore,"2"), myWorker(mySemaphore,"3")])
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
Successfully acquired the semaphore(share resourse) by 3
Successfully acquired the semaphore(share resourse) by 1
Releasing Semaphore(share resourse) by 3
Releasing Semaphore(share resourse) by 1
Successfully acquired the semaphore(share resourse) by 2
Releasing Semaphore(share resourse) by 2
Main Coroutine
 
"""