'''快速入门python'''
print('hello world!')
a = 1       #整数
b = 1.2     #浮点数
c = True    #布尔类型
d = "false" #字符串
e = None    #Nonetype
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
a = 1 #1756382864

b = a #1756382864
c = 1 #1756382864
print(id(a))
print(id(b))
print(id(c))

b = 2 #1756382880
print(id(b))

a = 2
b = 2.3
c = 3
print(a + b)  # 2 + 2.3 = 4.3
print(c - a)  # 3 - 2  = 1
print(a / b)  #整数除以浮点数运算以浮点数为准，2/2.3 = 0.8695652173913044
print(a / c)  #python2中，整数除法，向下取整，0.6666666666666666
print(a ** c) #a的c次方，8
a += 1        #python中没有i++的用法，此为自增
print(a)
c -=3
print(c)      #c变成0了
d = "hello"
print(d + ' world')    #相当于字符串拼接
print(d + ' "world"!') #相当于把字符串接在当前字符串尾
e = r'\n\t\\'
print(e) #\n\t\\       #字符串前加r表示字符串严格按照输入的样子，好处是不用转义符

a = True
b = False
print(a and b)
print(a or b)
print(not a)

a = 1
b = 2
print(a,b)
a,b = b,a
print(a,b) #life is short,you need python

print(~8)    #按位翻转，1000 ——> -(1000+1) = -9
print(8>>3)  #右移3位，1000 ——> 0001 = 1
print(1<<3)  #左移3位,0001 ——> 1000 = 8
print(5&2)   #按位与，101 & 010 ——> 000 = 0
print(5|2)   #按位或，101|010 ——> 111 = 7
print(4^1)   #按位异或，100 ^ 001 ——> 101 = 5

a = 1
b = 1.0
c = 1
print(a == b) #True,值相等
print(a is b) #False,指向的不是一个对象，这个语句等效为id(a) == id(b)
print(a is c) #True,指向的都是整型值1

print(id(type)) #1353108384
type = 1
print(id(type)) #1353248560
id = 2          #id成了指向2的变量

'''cos(pi)的四种计算方式'''
#直接导入python的内置基础数学库
import math
print(math.cos(math.pi))

#从math中导入cos函数和Pi变量
from math import cos,pi
print(cos(pi))

#如果是个模块，在导入的时候可以起个别名，避免名字冲突或是方便懒得打字的人使用
import math as m
print(m.cos(m.pi))

#从math中导入所有的东西,不推荐
from math import *
print(cos(pi))

#容器，包括列表(list)，元组(tuple)，字典(dict)和集合(set)
#列表(lsit)
a = [1,2,3,4]
b = [1]
c = [1]
d = b
e = [1,"hello world!",c,False]
print(b == c)
f = list("abcd")
print(f)
g = [0]*3 + [1]*4 + [2]*2
print(g)
a.pop()  #把最后一个值从列表中移除并作为pop的返回值
print(a)
a.append(5) #末尾插入值，[1,2,3,5]
print(a)
print(a[2])      #取下标，即3
a += [4,3,2]     #拼接
print(a)         #a = [1,2,3,5,4,3,2]
a.insert(1,0)    #在1处插入值0
print(a)         #a = [1,0,2,3,5,4,3,2]
a.remove(2)      #移除第一个2
print(a)         #a = [1,0,3,5,4,3,2]
a.reverse()      #倒序
print(a)         #a = [2,3,4,5,3,0,1]
a[3] = 9         #指定下标处赋值
print(a)         #a = [2,3,4,9,3,0,1]
b = a[2:5]       #取值a[2],a[3],a[4]
print(b)         #b = [4,9,3]
c = a[2:-2]      #取值,下标倒着数
print(c)         #c = [4,9,3]
d = a[2:]        #取值，取a[2],a[3],a[4],a[5],a[6]
print(d)         #d = [4,9,3,0,1]
e = a[:5]        #取值，a[0]~a[4]
print(e)         #e = [2,3,4,9,3]
f = a[:]         #取整个列表，相当于拷贝
print(f)         #f = [2,3,4,5,3,0,1]
a[2:-2] = [1,2,3] #赋值按照一段来
print(a)         #a = [2,3,1,2,3,0,1]
g = a[::-1]      #也是倒序，通过slicing实现并赋值，效率低于reverse
print(g)         #g = [1,0,3,2,1,3,2]
a.sort()         #列表内排序
print(a)         #a = [0,1,1,2,2,3,3]

import random
a = list(range(10)) #生成一个列表，从0开始+1递增到9
print(a)
random.shuffle(a)   #shuffle函数可以对可遍历和可变结构打乱顺序
print(a)            #a = [6, 8, 1, 7, 0, 9, 4, 3, 5, 2]
b = sorted(a)
print(b)
c = sorted(a,reverse = True)  #c = [9,8,7,6,5,4,3,2,1,0]
print(c)
#元组(tuple),与列表最大的区别在于不可变
a = (1,2)
print(a)
b = tuple(['3',4])  #也可从列表初始化
c = (5,)
print(c)            #(5,)
d = (6)
print(d)            #6
e = 3,4,5           #逗号间隔默认为tuple
print(e)
#集合(set)
A = set([1,2,3,4])
B = {3,4,5,6}
C = set([1,1,2,2,2,3,3,3,3])
print(C)      #集合的去重效果C = {1，2，3}
print(A | B)  #求并集，{1，2，3，4，5，6}
print(A & B)  #求交集，{3,4}
print(A - B)  #求差集，{1，2}
print(B - A)  #求差集，{5，6}
print(A ^ B)  #求对称差集，相当于(A - B)|(B - A) {1,2,5,6}
#字典(dict) "键-值"的对应形式 (Key-Value)
a = {'Tom':8,'Jerry':7}
print(a['Tom'])            #8
b = dict(Tom=8,Jerry=7)    #一种字符串作为键值得更方便的初始化方式
print(b['Jerry'])          #7
if 'Jerry' in a:
    print(a['Jerry'])      #7
print(a.get('Spike'))      #None
a['Tyke'] = 3
a.update({'Tuffy':2,'Mammy Two Shoes':42})
print(a)                         #a = {'Tom': 8, 'Jerry': 7, 'Tyke': 3, 'Tuffy': 2, 'Mammy Two Shoes': 42}
print(a.values())                #dict_values([8,7,3,2,42])
print(a.pop('Mammy Two Shoes'))  #移除'Mammy Two Shoes'的键值对，并返回42
print(a.keys())                  #dict_keys(['Tom', 'Jerry', 'Tyke', 'Tuffy'])
b = a.items()
print(b)                         #dict_items([('Tom', 8), ('Jerry', 7), ('Tyke', 3), ('Tuffy', 2)])

#给dict排序
from operator import itemgetter
c = sorted(a.items(),key=itemgetter(1))
print(c)                         #[('Tuffy', 2), ('Tyke', 3), ('Jerry', 7), ('Tom', 8)]
e = sorted(a)
print(e)                         #只对键排序，e = ['Jerry', 'Tom', 'Tuffy', 'Tyke']

from collections import OrderedDict
a = {1:2,3:4,5:6,7:8,9:10}
b = OrderedDict({1:2,3:4,5:6,7:8,9:10})
print(a)
print(b)                        #OrderedDict([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])

#for 循环
a = ['This','is','a','list','!']
b = ['This','is','a','tuple','!']
c = {'This':'is','an':'unordered','dict':'!'}

#依次输出：'This','is','a','list','!'
for x in a:
    print(x)

#依次输出：'This','is','a','tuple','!'
for x in b:
    print(x)

#键的遍历。不依次输出：'This','dict','an'
for key in c:
    print(key)

#依次输出0到9
for i in range(10):
    print(i)