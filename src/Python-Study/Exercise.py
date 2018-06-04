#-*- coding: utf-8 -*
'''
Created on 2018年5月3日

@author: LSH8880
'''
# from Scripts.pilconvert import output_format

'''
1.一元二次方程
'''
# import math
# def quadrand(a,b,c):
#     n = b**2-4*a*c
#     if not isinstance(a,(int,float)) \
#         or not isinstance(b,(int,float))\
#         or not isinstance(c,(int,float)):
#         raise TypeError("Bad Operand Type.")
#     
#     if n >= 0 and a != 0:
#         x1 = (-b-math.sqrt(n))/(2*a)
#         x2 = (-b+math.sqrt(n))/(2*a)
#         return x1,x2
#     if a == 0:
#         x1=x2= -c / b
#         return x1
#     else:
#         print("None.")
# 
# a = float(input("input a:"))
# b = float(input("input b:"))
# c = float(input("input c:"))
# 
# print(quadrand(a,b,c))


'''
2.多位乘积
'''
# def product(*args):
#     sum = 1
#     for i in args:
#         sum *= i
#     return sum
# 
# print(product(5,6,7,9))

'''
3.汉诺塔
'''

# def hanoi(n,x,y,z):
#     if n == 1:
#         print(x,"-->",y)
#     else:
#         hanoi(n-1, x, z, y)
#         print(x,"-->",z)
#         hanoi(n-1,y,x,z)
# n = int(input('请输入汉诺塔的层数：'))
# hanoi(n,'x','y','z')

# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)
# 
# move(3, 'A', 'B', 'C')


'''
4.切片
'''

# def strim(s):
#     if len(s) == 0:
#         print(s)
#     elif (s[0] == " "):
#         return s[1:]
#     elif (s[-1] == " "):
#         return s[:-1]
#     elif (s[0] == " ") and (s[-1] == " "):
#         return s[1:-1]
#     else:
#         return s
# 
# print(strim(" Hello world "))


'''
5.请使用迭代查找一个list中最小和最大值，并返回一个tuple
'''

# def FindMinAndMax(L):
#     if L != []:
#         max = L[0]
#         min = L[0]
#         for i in L:
#             if max < i:
#                 max = i
#             if min > i:
#                 min = i
#         print ((min,max))
#     else:
#         return (None,None)
#  
# A = [1,3,5,7,9]
#  
# FindMinAndMax(A)


'''
6.剔除列表中非字符串类型值，并将字符串转换成小写
'''
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L1 if isinstance(x,str)]
# print(L2)


'''
7.杨辉三角形
'''
# def triangles():
#     result = [1]
#     while True:
#         yield result
#         result = [1] + [result[x] + result[x+1] for x in range(len(result)-1)] + [1]
# 
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n += 1
#     if n == 10:
#         break

'''
8.利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''
# def normalize(name):
#     return name.capitalize()
# # capitalize() 此方法会将首字母大写，其余字母小写
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


'''
9.Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
'''
# from functools import reduce
# 
# def prod(L):
#     return reduce(lambda x, y: x * y , L)
# 
# print("3 * 5 * 7 * 9 =", prod([3, 5, 7, 9]))

'''
10.利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
'''
# from functools import reduce
# 
# def str2float(s):
#     digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     figure = reduce(lambda x, y: x * 10 + y, map(lambda x:digit[x], s.replace('.', '')))
#     return figure / (10 ** len(s.split('.')[1]))
#  
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功！')
# else:
#     print('测试失败！')


'''
11. 1000以内的素数
'''
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#         
# def _not_divisible(n):
#     return lambda x: x % n > 0
# 
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# 
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

'''
12.1000以内的回数
'''

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
# 
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1,200))) == [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151,161,171,181,191]:
#     print('测试成功!')
# else:
#     print('测试失败!')
#     

'''
13.对列表中信息，按名字排序
'''

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 
# def by_name(t):
#     return t[0]
# 
# L2 = sorted(L, key=by_name)
# print(L2)

# ##写法2
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L, key=lambda t: t[0]))

'''
14.对列表中信息，按成绩排序
'''
## 写法1
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 
# def by_name(t):
#     return t[1]
# 
# L2 = sorted(L, key=by_name)
# print(L2)

##写法2
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L, key=lambda t: t[1]))

'''
15.利用闭包返回一个计数器函数，每次调用它返回递增整数
'''
# 小结
#一个函数可以返回一个计算结果，也可以返回一个函数。
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量

# def createCounter():
#     n = 0
#     def counter():
#         nonlocal n
#         n += 1
#         return n
#     return counter
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

'''
16.使用匿名函数计算出20以内基数
'''
# 
# L=list(filter(lambda x: x % 2 == 1, range(1,20)))
# print(L)

'''
17. class 的私有属性


需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
'''

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender = gender
# 
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


'''
18.为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
'''

# class Student(object):
#     count = 0
#     
#     def __init__(self,name):
#         self.name = name
#         Student.count += 1
# 
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过')


'''
19.请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
'''
# 
# class Screen(object):
#     @property
#     def width(self):
#         return self._width
# 
#     @width.setter
#     def width(self, width):
#         self._width = width
# 
#     @property
#     def height(self):
#         return self._height
# 
#     @height.setter
#     def height(self, height):
#         self._height = height
# 
#     @property
#     def resolution(self):
#         return self._width * self._height
# 
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print("测试通过!")
# else:
#     print("测试失败!")


'''
20.metaclass(元类)
'''

# class Field(object):
# 
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
# 
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
# 
# class StringField(Field):
# 
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
# 
# class IntegerField(Field):
# 
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
# 
# class ModelMetaclass(type):
# 
#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings # 保存属性和列的映射关系
#         attrs['__table__'] = name # 假设表名和类名一致
#         return type.__new__(cls, name, bases, attrs)
# 
# class Model(dict, metaclass=ModelMetaclass):
# 
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
# 
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
# 
#     def __setattr__(self, key, value):
#         self[key] = value
# 
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))
#         
#         
# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
# 
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()


'''
21.classmethod
'''

# class Data_test2(object):
#     day=0
#     month=0
#     year=0
#     def __init__(self,year=0,month=0,day=0):
#         self.day=day
#         self.month=month
#         self.year=year
# 
#     @classmethod
#     def get_date(cls,string_date):
#         #这里第一个参数是cls， 表示调用当前的类名
#         year,month,day=map(int,string_date.split('-'))
#         date1=cls(year,month,day)
#         #返回的是一个初始化后的类
#         return date1
# 
#     def out_date(self):
#         print ("year :")
#         print (self.year)
#         print ("month :")
#         print (self.month)
#         print ("day :")
#         print (self.day)
# 
# r = Data_test2.get_date("2018-6-4")
# r.out_date()


'''
22.闭包
'''

def adder(x):
    def wrapper(y):
        return x + y
    return wrapper

adder5 = adder(5)
# 输出 15
print(adder5(10))
# 输出 11
print(adder5(6))

#__closure__判断是否为闭包
print(adder.__closure__)
print(adder5.__closure__)
print(adder5.__closure__[0].cell_contents)



