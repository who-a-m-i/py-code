#-*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,oth):
        return Point(self.x + oth.x,self.y + oth.y)
    
    def info(self):
        print(self.x,self.y)

if __name__ == '__main__':
    pa = Point(1,2)
    pb = Point(3,4)
    pc = pa + pb
    pc.info()