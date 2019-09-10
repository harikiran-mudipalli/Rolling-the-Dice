#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:46:20 2019

@author: hk
"""

import random
choice = ''
option = 1
print("Ready to roll the dice?\nPress 'Y' to continue")
if(str(input(choice)).upper() == 'Y'):
    roll = random.randint(1,6)
    while(option == 1):
        
        print('Number you rolled is -->',roll,'\n Congratulations!!!\n'
              'Would you like to continue?\n'
          'Press "Enter" to continue or "q" to quit')
        
        if(input(choice) == 'q'):
            option = 0
        else:
            roll = random.randint(1,6)
else:
    print("I think you should better try this.")