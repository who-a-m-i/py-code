#-*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''

class Point:
    def __init__(self,y,x):
        self.x = x
        self.y = y
    
    def __lt__(self,oth):
        return self.x < oth.x
    
    def __gt__(self,oth):
        return self.y > oth.y

if __name__ == '__main__':
    pa = Point(0,1)
    pb = Point(1,0)
    print(pa < pb)
    print(pa > pb)