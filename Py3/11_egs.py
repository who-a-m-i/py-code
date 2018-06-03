#-*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''
'''
python  单实例模式
'''
class Singleton:
    def __new__(cls,*args,**kwargs):
        
        if not hasattr(cls, '_sgl'):
            cls._sgl = super().__new__(cls,*args,**kwargs)
        return cls._sgl

if __name__ == '__main__':
    sa = Singleton()
    sb = Singleton()
    print(id(sa))
    print(id(sb))