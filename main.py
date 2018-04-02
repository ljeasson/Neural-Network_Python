# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:37:59 2017

@author: ljeas

Spirit Animal User ID: creativeBison
Date Last Edited: 5/5/2017
Challenge 5
Sources: Class instruction

"""

from __future__ import division
import numpy as np
import neuro
import linear_algebra

inputs = [[135,206,250],[0,250,154],[84,255,159],[0,0,128],[255,255,0],\
          [255,153,18],[72,118,255],[0,0,255],[238,169,184],[220,20,60],\
          [0,0,0],[0,0,255],[0,128,250],[34,145,240],[0,0,238]]
targets = [[1],[0],[0],[1],[0],[0],[1],[1],[0],[0],[0],[1],[1],[1],[1]]
reps = 1000

inputs = np.float32(inputs)/255.0

network = []

network = neuro.setup_network(inputs)

neuro.train(network, inputs, targets, reps)

#TAKE INPUT
red_value = input("Enter Red Value: ")
green_value = input("Enter Green Value: ")
blue_value = input("Enter Blue Value: ")

red_value = float(red_value)/255.0
green_value = float(green_value)/255.0
blue_value = float(blue_value)/255.0             

color = [red_value, green_value, blue_value]

pred = neuro.predict(network, color)

print("Is it blue?")
if (pred >= float(0.70)):
    print("YES")
else:
    print("NO")
        