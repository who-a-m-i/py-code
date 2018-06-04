#-*- coding: utf-8 -*-
'''
Created on 2018年5月5日

@author: LSH8880
'''

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('Bad operand type.')
#     if x > 0:
#         return x
#     else:
#         return -x
# 
# print(my_abs(-3))


# import math
# def quadratic(a,b,c):
#     n = b**2-4*a*c
#     if not isinstance(a,(int,float))\
#         or not isinstance(b,(int,float))\
#         or not isinstance(c,(int,float)):
#         raise TypeError("Bad Operand type.")
#     
#     if n >= 0 and a != 0:
#         x1 = (-b-math.sqrt(n))/(2*a)
#         x2 = (-b+math.sqrt(n))/(2*a)
#         return x1,x2
#     elif a == 0:
#         x1=x2= -c/b
#         return x1    
#     else:
#         print("None")
# 
# a = float(input("input a:"))
# b = float(input("input b:"))
# c = float(input("input c:"))
# 
# print(quadratic(a,b,c))


'''
函数
'''

# def hello(greeting, *args):
#     if (len(args)==0):
#         print('%s!' % greeting)
#     else:
#         print('%s, %s!' % (greeting, ', '.join(args)))
# 
# hello('Hi') # => greeting='Hi', args=()
# 
# hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
# hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')
# 
# names = ('Bart', 'Lisa')
# hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')


'''
闭包
'''
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax += n
#         return ax
#     return sum
# 
# f = lazy_sum(1,3,5,7,9)
# print(f())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#     print fs
# 
# f1, f2, f3 = count()


# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()




import logging

# def log(func):
#     def wrapper():
#         logging.warn("%s is running" % func.__name__)
#         return func()
#     return wrapper
# 
# def foo():
#     print("I am foo")
# 
# foo = log(foo)
# foo()

# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             elif level == "info":
#                 logging.info("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
# 
#     return decorator
# 
# @use_logging(level="warn")
# def foo(name='foo'):
#     print("i am %s" % name)
# 
# foo()

# def logged(func):
#     def with_logging(*args, **kwargs):
#         print(func.__name__)      # 输出 'with_logging'
#         print(func.__doc__)     # 输出 None
#         return func(*args, **kwargs)
#     return with_logging
# 
# # 函数
# @logged
# def f(x):
#    """does some math"""
#    return x + x * x
# 
# logged(f)

'''
__getattr__
'''
# class Chain(object):
# 
#     def __init__(self, path=''):
#         self._path = path
# 
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
# 
#     def __str__(self):
#         return self._path
# 
#     __repr__ = __str__
# 
# 
# can = Chain()
# can2 = can.status
# can3 = can.status.user
# can4 = can.status.user.timeline
# can5 = can.status.user.timeline.list
# 
# print(can)
# print(can2,can3,can4,can5)
# print('-----------')
# print(Chain().status.user.timeline.list)


# class Chain(object):
#     
#     def __init__(self,path=''):
#         self._path = path
#     
#     def __call__(self, param):
#         return Chain("%s/:%s" % (self._path, param))
#     
#     def __getattr__(self, path):
#         return Chain("%s/%s" % (self._path, path))
#     
#     def __str__(self):
#         return self._path
#     
#     __repr__ = __str__
#     
# print(Chain().api.server.user("point").timeline.api)

class A(object):
    def __init__(self, a=1):
        self.a = a

    @classmethod
    def put(cls, a):
        return cls(a)

    def get(self):
        print(self.a)
Exercise_Def
B = A.put(1)
B.get()

B = A(2)
B.get()
B.put(3)
B.get()

print('---', B.a)
C = B.put(3)
print('---', C.a)
C.get()
C.a = 5
C.get()

D = C.put(6)
D.get()