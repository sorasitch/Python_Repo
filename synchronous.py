# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:43:54 2021

@author: schomsin
"""

#!/usr/bin/env python3
# countsync.py

import time

def count(num):
    print("One by " + num)
    time.sleep(1)
    print("Two by " + num)

def main():
    for n in range(3):
        count(str(n))

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    
"""
One by 0
Two by 0
One by 1
Two by 1
One by 2
Two by 2
"""