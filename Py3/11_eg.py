#-*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''

class SingleClass:
    def __init__(self,x=0):
        self.x = 0

sc = SingleClass()

def tsc():
    print(sc.x)
    sc.x = 10
    print(sc.x)

def tsc2():
    print(sc.x)
    sc.x = 9
    print(sc.x)

if __name__ == '__main__':
    tsc()
    tsc2()