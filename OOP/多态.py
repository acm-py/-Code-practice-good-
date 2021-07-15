# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     多台
   Description :
   Author :       bing
   date：          2021/7/8
-------------------------------------------------
   Change Activity:
                   2021/7/8:
-------------------------------------------------
"""
__author__ = 'bing'
class Animal:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return '''Animal{0.name},{0.speed} is printed
        name={0.name}
        speed={0.speed}
        '''.format(self)


class Cat(Animal):
    def __init__(self,name,speed,color,genre):
        super().__init__(name,speed)
        self.color = color
        self.genre = genre
    # 添加方法
    def getRunningSpeed(self):
        print('running speed of %s is %s' %(self.name, self._speed))
        return self._speed


class Bird(Animal):
    def __init__(self,name,speed,color,genre):
        super().__init__(name,speed)
        self.color = color
        self.genre = genre
    # 添加方法
    def getFlyingSpeed(self):
        print('flying speed of %s is %s' %(self.name, self._speed))
        return self._speed