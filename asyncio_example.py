# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:45:12 2021

@author: schomsin
"""

import asyncio

async def work():
    while True:
        await asyncio.sleep(1)
        print("Task Executed")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(work())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()