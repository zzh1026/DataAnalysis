#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/9

__author__ = 'zzh'

import datetime

dt = '2018/04/23 23:34:34'
d = '2018-04-24'

str2datetime = datetime.datetime.strptime(dt, '%Y/%m/%d %H:%M:%S')

str2date1 = datetime.datetime.strptime(d, '%Y-%m-%d')

str2date2 = datetime.datetime.strptime(d, '%Y-%m-%d').date()

# print(str2datetime)
# print(str2date1)
# print(str2date2)

a = int(float("12.345"))
b = str(12)
c = 12
# print(type(a))
# print(type(b))
# print(type(c))

ls = [1, 2, 4, 'a', 'b', 'c', '2017-04-12']  # 创建列表,列表可变,可以进行增删改查
print(ls)

# 查
# print(ls[2])            # 表示取角标为position的元素 , pos从0开始
# print(ls[4:5])          # 切片方式取position - pos的元素, 含首不含尾
# print(ls[:2])           # 切片方式取0 - position, 含首不含尾
# print(ls[2:])           # 切片方式取从 position 取到后面所有的元素, 含首不含尾
# print(ls[-3])           # 索引获取倒数第 position 个元素,从 -1 表示倒数第一个元素, 因为0代表正数第一个数字
# print(ls[-3:])          # 切片方式取倒数第 position - 后面所有元素,
# print(ls[-2:-5:-1])     # 切片方式倒序取元素,  a:b:c 双冒号代表按步长来去, 从 a - b ,
#                         # 步长为c 去列表, 含首不含尾,表示从 倒数第二个(含)到倒数第五个(不含),步长为1去列表
# print(ls[::2])          # 切片方式步长为2取列表 ,a,b不标出代表整个数列

# 增
# ls.append('sim')        # 在末位追加
# print(ls)
# ls.extend(['sims', 23])    # 在末位另一个集合,另一个集合可以包含多个元素
# print(ls)
# ls.insert(-5, 'month')  # 在指定位置插入,倒数第五个位置插入
# print(ls)

# 删

# ls.pop()                # 删除末尾的一个元素
# print(ls)
# ls.pop(-2)              # 删除指定位置的一个元素, 因为该方法参数默认为1,所以直接调用不声明位置就删除末尾的元素了
# print(ls)
# ls.remove("c")          # 删除指定元素值
# print(ls)
# ls.remove("S")          # 删除指定元素值,如果该值不存在与列表中,会报错 list.remove(x): x not in list ,所以该方法有风险
# print(ls)

# ls2 = ls.copy()
# print(ls2)
#
# ls2.clear()             # 清空列表元素；但是 ls2 对象仍存在
# print(ls2)
#
# del ls2                 # del 方法删除对象,使该对象不再存在
# print(ls2)              # 此时ls2已经被删除 ,name 'ls2' is not defined


# 总结
# pop方法在不指定参数时默认删除末尾元素，也可以指定删除某个位置的元素；
#
# remove方法删除指定的元素值；
#
# clear方法清空列表元素；
#
# del函数删除列表对象；


# 改

# ls[2] = 33
# print(ls)

# ls[3:6] = [1, 2, 3]  # 通过索引的方式将旧值换成新值
# print(ls)

# ls[2] = [1, 2, 3, 4]   # 使用列表元素对象来替换元素对象,这是对象和对象的替换
# print(ls)

# ls[3:6] = [1, 2, 3, 4, 5, 7]  # 通过列表元素替换列表元素
# print(ls)


# 其他方法

# ls3 = ['a', 'b', 'c', 'a', 'c', 'f', 'f', 'a', 'b', 'd', 'a']
# print(ls3)

# ls4 = ls3.copy()    # 复制方法

# aCount = ls3.count('a')  # 统计
# print(aCount)  # 统计 'a' 元素出现的次数
#
# ls3.index('f')  # 索引,返回f首次出现的位置
#
# ls3.reverse()  # 翻转
# print(ls3)
#
# ls3.sort()  # 排序, 默认从a-z, 从小到大
# print(ls3)
#
# ls3.sort(reverse=True)  # 排序, 默认从a-z, 从小到大,reverse表示默认完毕后是否再次翻转,如果翻转则表示从z-a,从大到小
# print(ls3)


# 总结
# copy方法复制一个物理对象，而非视图对象；
#
# count方法计数；
#
# index方法返回索引位置；
#
# reverse方法实现元素颠倒；
#
# sort方法排序；


# 创建一个元组 , 元组是不可变的序列，故其没有增、删、改的权限。只能进行查询（索引和切片）和一些简单的其他方法。
# t = (1, 2, 4, 'a', 'b', 'c', '2017-04-12')
# print(t)

# 查, 查询不会对元组进行修改, 所以列表的方法都适用

# 其他方法包括 技术 和 索引

# 由于元组没有copy方法，但如果你就是想复制一个物理对象给新的变量，可以考虑使用copy模块的copy方法
# import copy
# t2 = copy.copy(t)
# print(t2)

# 字典 字典的创建就不是通过上面的中括号[]和圆括号()方法构建了，而是通过花括号{}或dict函数来构造键-值对。

dict1 = {'id': [1, 2, 3], 'name': ['a', 'b', 'c'], 'age': [12, 32, 45]}
# dict2 = dict(id=list(range(1, 5)), name=['sdf', 'sdf', 'sdf'], gender=['f', '2', 's'])
# dict3 = {'name': 'slkdf', 'score': {'shuxue': 88, 'yingyu': 82}}
#
# print(dict1)
# print(dict2)
# print(dict3)

# 第一个字典通过花括号构建；
#
# 第二个字典通过dict函数构建；
#
# 第三个构造了一个嵌套的字典；

# 由于字典也是一个可变对象，故其也有增、删、改的操作

# print(dict1['id'])  # 通过字典键获取值,如果字典中没有id的键会报错,所以使用该方法有风险
# print(dict1.get('id'))  # key获取值,如果字典中没有id不会报错,该方法无风险
# print(dict1.setdefault('id'))  # 给键设置默认的值,如果不给值相当于get方法
# print(dict1.setdefault('age1'))  # 如果字典中没有该键就会添加该键.其get到none
# print(dict1)
# print(dict1.setdefault('age2', [2, 3, 4]))
# print(dict1)
# print(dict1.setdefault('id', [2, 3, 4]))
# print(dict1)

# 所以，setdefault方法既可以实现查的功能，又可以完成添加键值对的功能。但是不会修改键的值


# 增

# dict1['lll'] = [66, 66, 66]  # 通过索引的方式增加键值对；
# print(dict1)
#
# dict1.setdefault('222', [665, 665, 665])  # 通过setdefault方法增加键值对；
# print(dict1)
#
# dict1.update({'333':{333, 444, 555}})  # 通过update方法增加键值对；
# print(dict1)
#
# dict1.update({'222':{111, 222, 333}})  # 通过update方法增加键值对；update方法也可以更新数据
# print(dict1)
