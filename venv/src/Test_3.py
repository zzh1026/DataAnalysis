#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/9

__author__ = 'zzh'

# 控制流与自定义函数

# 控制流
#
# if判断
# if判断可以处理两分支判断和多分支判断，对于两分支类似于Excel中的if函数、
# R中的ifelse函数，处理的是某种条件满足时则如何如何，否则又如何如何；
# 而多分支无非是Excel中if函数或R中ifelse函数的多层嵌套而已。

# 双分支语法
b = True
if b:
    print(b)
else:
    print(b)

# 多分支语法
c = True
if b:
    print(b)
elif c:
    print(c)
elif b == c:
    print(b == c)
else:
    print(c)

# 关键词if、elif、else所在行的末尾必须要有英文冒号；
# 冒号的下一行必须要有缩进；
# else后面不要再写条件；

# num = int(input('penter a number: '))
# if num > 88:
#     print('Great')
# else:
#     print('too bad')

# 根据身份证号获取出生日期和性别

# import datetime
#
# # id = str(input('enter the idcard: '))
# id = '140524188409081234'
# if len(id) == 18:
#     # 通过切片方式获取出生日期,并转化为日期
#     birthday = datetime.datetime.strptime(id[6:14], '%Y%m%d').date()
#     if int(id[-2]) % 2 == 0:  #以身份证倒数第二个数字的就判断性别
#         gender = 'F'
#     else:
#         gender = 'M'
# print(birthday)
# print(gender)

# for循环

# for循环可以对一切可迭代对象（如列表、元组、字典、字符串、序列等）按照指定的方式进行循环处理。
# 这里的for循环和kotlin是一致的, java中的字符串不能循环

# 语法
# for c in iterable:
#     c(拿到c)
#
# 可以和if搭配使用,对c进行判断

# sum = 0
# for i in range(1, 101):  # 含首不含尾
#     sum += i
# print(sum)

# while 循环
# while循环与for循环比较类似，两者基本上都是可以互换的，即for循环也可以用while循环完成，反之亦可。
#
# for循环好的地方在于 i 可以放在内部处理,而while需要将i放在外部
#
# 对于可知循环次数的while循环，一般需要给一个初始的计数器i，i可以是任何值（这要根据你实际的情况来了，如我只是计算1....100的和，那i可以从0开始也可以从1开始）；
# 对于可知循环次数的while循环，有了初始的计数器，也要有循环体内的累加器，即 i+=1，每循环一次则累加记录一次；
# 对于未知循环次数的while循环，可以用True关键词接在while关键词后面，但一定要记得通过if分支实现break操作，否则将会进入死循环。

# 自定义函数
#
# lambda函数
#
# lambda函数又称匿名函数，是一种精简版的小函数，可以非常方便的嵌套在任何地方。先来看一下lambda函数的语法和例子。
#
# 语法
# fun_name = lambda parameters : expression
#
# 1）parameters形参可以是多个，用英文逗号隔开；
# 2）参数与函数体之间用英文冒号隔开，且不需要换行；
# 3）函数体expression不可写的复杂，即一个表达式即可；

# 计算一个两元二次函数
z = lambda x, y: x ** 2 + 3.14 * y - x * y
result = z(10, 20)
# print(result)

dict1 = {'a': 3, 'b': 1, 'c': 4, 'd': 2, 'e': 4, 'f': 8, 'g': 6}
ls = list(dict1.items())
# print(ls)

ls.sort()
# print(ls)

# 按照第二个元素排序
sort2element = lambda x: x[1]
ls.sort(key=sort2element)


# print(ls)


# 自定义函数语法
#
# 语法
#
# def function_name(params):
#   params
#   return value
#
# 注意的点：
# 1）以关键词def开头，说明准备开始自定义函数；
# 2）function_name是用户指定要的一个函数名称；
# 3）形参放在括号内，即使没有参数，括号也保留着；主要使用括号来区分是否是函数
# 4）def行末尾记得加上英文冒号，并换行缩进写入函数体
# 5）一般需要加上关键词return，将函数的运算结果返回出来；
def y(x):
    return x ** 2 - 2 * x + 1


result = [y(i) for i in range(-5, 6)]


# print(result)


# Python的自定义函数，有四种类型的形参，分别是必选参数、默认参数、可变参数和关键词参数，我们通过例子一一道来。
# fun最好以return结尾来标记fun完毕
#
# 1,必选参数
# 自定义函数时，传入了某个形参，为保证函数正常运行则必须为其传入实参。
def fun1(a, b, c):
    print(a, b, c)


# fun1(10, 20, 30)

def game(min, max):
    import random
    number = random.randint(min, max)
    while True:
        guess = int(input('请输入您猜的数字: '))
        if guess < number:
            min = guess
            print('猜错了,猜的偏小!请在%d到%d之间才一个数!' % (min, max))
        elif guess > number:
            max = guess
            print('猜错了,猜的偏大!请在%d到%d之间才一个数!' % (min, max))
        else:
            print('猜对了')
            print('结束')
            break


# game(1, 100)

#
# 2,默认参数
# 默认参数就是在自定义函数的时候,就已经给了函数一个初始值的参数,那么,在函数运行时,就可以不用为该默认参数传值了,当然也可以根据实际情况为默认参数传入其他值。
#
def game2(min=1, max=10):
    game(min, max)
    return


# game2(max=12)


#
# 3,可变参数
# 有的时候,你在构造一个函数时都不知道会有多少参数,即参数的数量是可变的,故衍生出了可变参数。可变参数前面需要加一个星号(*),
# 用来区分必选参数和默认参数,可变参数是以元组的形式传给函数的,

def func2(income, outcome, *name):
    return


# 参数name前面有一个星号,说明该参数就是可变参数,而income,outcome则为必选参数,
# 故给函数func2传入6个参数时,前面两个分别为income和outcome的实参,后面4个则以捆绑的元组作为name的实参。


#
# 4,关键字参数
# 该参数与可变参数类似,区别有二,一是关键字参数前面需要以双星号(**);二是关键字参数是以字典的形式传给函数的。同样举个例子说明:
def starts(name, **score):
    print(name)
    print(score)
    print('%s的平均成绩为%.2f' % (name, sum(score.values()) / len(score)))
    return


# starts('Sim', math=90, english=79, chinese=82)

#
# 在构造自定义函数时,如果你的函数比较复杂,需要考虑到使用上面介绍的4种参数,切记4种参数是有顺序的,即必须参数,默认参数,可变参数和关键字参数。

def myFun(a, b=10, *c, **d):
    print('')
    return
