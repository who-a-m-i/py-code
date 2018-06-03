# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''

class MyMeta(type):
    def __init__(self,name,bases,dicts):
        print('Init Instance.')
    
    def __new__(cls,name,bases,dicts):
        dicts['info'] = lambda self:print('Point.')
        res = type.__new__(cls,name,bases,dicts)
        res.company = 'Maizi'
        return res

class custom(metaclass=MyMeta):
    pass

if __name__ == '__main__':
    cus = custom()
    cus.info()
    print(cus.company)