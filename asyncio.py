# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:25:10 2021

@author: schomsin
"""

#!/usr/bin/env python3
# countasync.py

import asyncio

async def count(num):
    print("One by " + num)
    await asyncio.sleep(1)
    print("Two by " + num)

async def main():
    await asyncio.gather(count("1"), count("2"), count("3"))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    
    #asyncio.run(main())
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(main())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
    
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


"""
One by 1
One by 2
One by 3
Two by 1
Two by 2
Two by 3
"""