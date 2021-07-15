# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     多态2
   Description :
   Author :       bing
   date：          2021/7/8
-------------------------------------------------
   Change Activity:
                   2021/7/8:
-------------------------------------------------
"""
__author__ = 'bing'
import time

class Manager():
    def __init__(self,animal):
        self.animal = animal

    def recordTime(self):
        self.__t = time.time()
        print('feeding time for %s（行走速度为:%s） is %.0f'%
        (self.animal.name,self.animal.speed,self.__t))

    def getFeedingTime(self):
        return '%0.f'%(self.__t,)