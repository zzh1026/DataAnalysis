#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/9

__author__ = 'zzh'

# 数值计算及正则表达式

# 运算符

# 1,数值运算
#
# +、-、*、/ , % (求余数) ,// (注意Python中的整除是floor除，即向下除法,和 java中的int类型的  / 一直)

# print(23//2)
# print(-23//2)


# 2,比较运算
#
# >、>=、<、<=、== (判断两个对象是否相等) ,!= (判断两个对象是否不相等)

# a = 12;
# b = 12;
# print(type(a))
# print(type(b))
# print(a == b)
#
# a = 12
# b = '12'
# c = int(b)
# print(type(a))
# print(type(b))
# print(type(c))
# print(a == c)


# 3,逻辑运算
#
# or (或) and (且) not (非)


# 数值函数

# 1,Python自带的数值函数
#
# abs  # 绝对值  ,
# divmod  # 返回除法的整数和余数 ,
# round  # 四舍五入 ,
# pow  # 幂指数运算
print(divmod(17, 5))

# 2, math模块
#
# math.pi,
# math.e ,
# math.cell(x)  # 向上取整,
# math.floor(x) # 向下取整,
# math.modf(expression) # 商的小数部分与整数部分,
# math.log2(x) # 以2为底的对数,
# math.log10(x) # 以10为底的对数,
# math.log(x) # 以e为底的对数 ,
# math.log(x, base) # 以base为底的对数 ,
# math.exp() # 指数 ,
# math.sqrt() # 算术平方根 ,
# math.factorial() # 阶乘 ,
# math.fmod() # 返回浮点型余数

import math

# print(math.factorial(5))

# 字符串重复（字符串的乘法）
# print('123123' * 40)

# 字符串中的正则表达式
#
# 1,正则表达式含义
#
# .             # 点可代表一切字符
# \             # 起转义作用
# [...]         # 指代方括号中的任意字符
# \d            # 指代数字0-9
# \D            # 指代非数字
# \s            # 指代一切空格，包括tab制表符、空格、换行等
# \S            # 指代非空格
# \w            # 指代大小写字母、数字和下划线
# \W            # 指代非大小写字母、数字和下划线
# *             # 匹配前面字符 >=0 次
# +             # 匹配前面字符1次及以上
# ?             # 匹配前面字符0次或1次
# {m}           # 匹配m次
# {m,n}         # 匹配m到n次
# {m,}          # 至少匹配m次

# 2,结合re模块完成字符串的匹配

# 1,找
# re.findall(pattern, string, flags=0)
#
# pattern-->正则表达式
# string-->需要处理的字符串
# flags-->说明匹配模式，如是否大小写re.I
#

import re

s1 = '''
    name:sim,Gender:f,
    age:27,address:JiangSu,
    Edu:yjs
'''

keys = re.findall(r'([a-z]+):', s1, re.I)
values = re.findall(':(\w+)', s1)
print(keys)
print(values)

myDict = {}
for i in list(range(0, len(keys))):
    myDict[keys[i]] = values[i]

print(myDict)

# 2,切
# re.split(pattern, string, maxsplit=0, flags=0)
# pattern-->正则表达式
# string-->需要处理的字符串
# maxSplit-->最大匹配次数。0表示匹配所有次

# 3,替
# re.sub(pattern, repl, string, count=0, flags=0)
# pattern-->正则表达式
# repl-->新的替换内容
# string-->需要处理的字符串
# count-->替换次数。0表示匹配替换所有次
# flags-->匹配模式

# 将1.5l,1.5L,1.5t,1.5T,替换为1.5L
s = '1.5ldfn1.5LdLad1.5tsdf1.5Tadfg1.5sd'
subResult = re.sub('1.5[lLtT]', '1.5L', s)
print(subResult)
