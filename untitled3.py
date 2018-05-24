#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 23:37:57 2018

@author: pt
"""


for i in range(1,10) :
    print(str(i) + '\r')
    
    

from IPython.display import clear_output

for f in range(10):
    clear_output(wait=True)
    print(f)
    time.sleep(.1)
    
    
import sys
import time

for f in range(10):
    #delete "\r" to append instead of overwrite
    sys.stdout.write("\r" + str(f))
    sys.stdout.flush()
    time.sleep(.1)