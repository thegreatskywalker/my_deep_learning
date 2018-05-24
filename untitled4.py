#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 02:30:41 2018

@author: pt
"""

from tqdm import tqdm

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    
    text = text + char
    
    
for i in tqdm(range(100)):
    pass


pbar = tqdm(["a", "b", "c", "d"])



pbar2 = tqdm(total=200,  desc='text', position=10)

    
pbar2.update(10)
    