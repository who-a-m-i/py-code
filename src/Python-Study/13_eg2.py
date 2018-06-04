#-*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''

class Water:
    def __init__(self):
        self.name = 'Water'
    
    def show(self):
        print(self.name)

class Deco:
    def show(self):
        print(self.name)

class Sugar(Deco):
    def __init__(self,water):
        self.name = 'Sugar'
        self.water = water
    
    def show(self):
        print(self.name)
        print(self.water.name)

class Salt(Deco):
    def __init__(self,water):
        self.name = 'Salt'
        self.water = water
    
    def show(self):
        print(self.name)
        print(self.water.name)

if __name__ == '__main__':
    w = Water()
    s = Sugar(w)
    s.show()
    
    s = Salt(w)
    s.show()