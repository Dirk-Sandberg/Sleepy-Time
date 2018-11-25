# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:59:41 2018

@author: Erik
"""

'''
PURPOSE:
    Shut down computer after 9:00pm every night to ensure getting a good night's sleep
'''
import os
import time

while True:
    time.sleep(60)
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    #if minute == 19:
    #    os.system("shutdown -s")
    if hour >= 21: # If it's passed 9:00 pm
        os.system("shutdown -s")
        