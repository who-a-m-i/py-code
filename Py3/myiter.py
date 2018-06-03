# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''

class MyIter:
    def __init__(self,start,end):
        self.count = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.end:
            r = self.count
            self.count += 1
            return r
        else:
            raise StopIteration

if __name__ == '__main__':
    for i in MyIter(1,10):
        print(i)
    