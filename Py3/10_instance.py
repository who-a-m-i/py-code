#-*- coding: utf-8 -*-
'''
Created on 2018年4月30日
@author: LSH8880
'''

class Custom:
    def __init__(self):
        print('Init method.')
    
    def __new__(cls,*args,**kwargs):
        print('New Instance.')
        return object.__new__(cls,*args,**kwargs)

if __name__ == '__main__':
    Custom()