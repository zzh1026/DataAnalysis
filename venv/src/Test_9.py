#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/10

__author__ = 'zzh'

#
# 关于pandas如何实现数据合并 、数据连接 、创建哑变量和连续数值的区间化的操作。
# 前两个操作在数据库中是非常常用的，即将多个数据集纵向合并和横向的扩展；
# 后两个操作在数据建模中会经常用到，即离散变量的哑变量化处理和连续变量的分段处理。
#

import os

import pandas as pd

# 总结
#
# 这一部分主要是实现数据合并 、数据连接 、创建哑变量和连续数值的区间化的操作。
#
# 一、数据集的纵向合并
#   1,pd.concat([合并的文件列表], ignore_index=True) pd.concat函数的第一个参数一定要是一个可迭代对象。故在代码中对dataframe初始化为列表结构。
# 二、数据集的横向扩展
#   1,pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
#          left_index=False, right_index=False, sort=False,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
#   纵向合并使用concat, ignore_index代表是否忽略pos角标
#   横向合并使用merge方法
# 三、离散变量的哑变量处理
#   1,pd.get_dummies(user_level, columns=['gender', 'level']) ,使用get_dummies方法对表的离散型字段进行哑变量处理
#   2,datas.drop([],axis=1,inplace=True) ,获得的结果再通过drop函数来进行删除多余的处理字段并刷新数据
# 四、连续变量的分段
#   1, 对于向量可以使用 pd.cut(数据,bins=[区间],right=False是否包含上限,laels=[区间的名称])
#
#
#


# 一、数据集的纵向合并
#
# 如果你手中有多张数据结构一致的excel表格，你需要将这些表格合并到一起，你会怎么做？复制粘贴？是不是太慢了，这里教你使用Python完成数据的批量合并。
# 完成数据堆叠
# 指定数据文件所在的路径
path = 'C:/Users/zhaozehui/PycharmProjects/DataAnalysis/venv/data/hengxiang/'
# 罗列路径下的文件名称
fileNames = os.listdir(path)
# print(fileNames)
dataframes = []
for file in fileNames:
    dataframes.append(pd.read_excel(path + file))
datas = pd.concat(dataframes, ignore_index=True)
# print(datas)

# pd.concat函数的第一个参数一定要是一个可迭代对象。故在代码中对dataframe初始化为列表结构。

# 二、数据集的横向扩展
#
# 如果你所需的数据集来自于多张表，而这些表之间存在一些公共的字段用于观测行的匹配，
# 换句话说，你需要在excel使用vlookup这样的函数完成数据的连接。要想实现该功能，在Python中应该如何实现呢？
path1 = 'C:/Users/zhaozehui/PycharmProjects/DataAnalysis/venv/data/shuxiang/test3.xls'
path2 = 'C:/Users/zhaozehui/PycharmProjects/DataAnalysis/venv/data/shuxiang/test4.xls'
datas1 = pd.read_excel(path1)
datas2 = pd.read_excel(path2)
print(datas2.loc[0, :][1:])
# print(datas1.head())
print(datas2.head())

# 借助于pandas中merge函数完成两个数据集的连接，即将economy_info表中的字段合并到user_info表中，形成一张宽表。
# 下merge函数的几个重要的参数：
# pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
#          left_index=False, right_index=False, sort=False,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
#   left,right：为需要连接的两张表；
#   how：默认对两张表进行内连，'right'，'left'为右连和左连，一般inner和left使用最多；
#   on：指定关连两张表的公共字段；
#   left_on,right_on：指定left表和right表中需要关连的字段；
#   left_index,right_index：指定left表和right表中需要关连的行索引
#
marge_data = pd.merge(datas1, datas2, how='inner')
# print(marge_data.head())

# 如果你的两张表有公共字段，而且字段名称完全一致，merge函数会自动查询这些字段，
# 并以这些字段作为连接的依据。如果两张表中含公共字段，但名称不一致，如Id与id，这个时候就需要left_on和right_on两个参数的使用了。
# 修改字段名称
user_info = datas1.rename(columns={'考号': '考试号', '姓名': '名字'})
marge_data = pd.merge(user_info, datas2, how='inner', left_on='考试号', right_on='考号')
# print(marge_data.head())

# marge_data.drop(['考号', '姓名'], axis=1, inplace=True)
# print(marge_data.head())

# 三、离散变量的哑变量处理
#
# 在建模过程中，往往会有一些离散变量，如学历、收入等级，用户会员等级。
# 这些变量直接放入到模型中（如回归模型）是有问题的（即使你已经用1,2,3...等数据表示）
# 为解决这个问题，我们通常是将这些变量进行哑变量处理。
# 如果离散变量有N种水平，就需要构造N-1个变量，每一个变量均用0和1的值来表示。
# 那这样的0-1编码，如何使用Python来实现呢？
# 如果你使用了pandas模块中的get_dummies函数，问题就会显得非常容易。
user_level = pd.read_csv('user_level.csv')
# print(user_level)
# 该数据集中的gender变量和level变量都属于离散变量，需要将这两个变量进行哑变量处理。
# 哑变量处理
dumms = pd.get_dummies(user_level, columns=['gender', 'level'])
# print(dumms)

# 是不是很方便。千万记得，如果你的变量进行了哑变量处理，建模时要记得删除原离散变量中的某一个水平，如性别中删除gender_F，
# 等级中删除level_V1。删除的变量，就表示性别中，以女性(F)为参照组；等级中，以V1为参照组。如下是变量的删除：
dumms.drop(['gender_F', 'level_V1'], axis=1, inplace=True)
# print(dumms)

# 四、连续变量的分段
#
# 最后，再来看一个知识点，那就是需要把连续变量进行分段处理，如年龄需要分成未成年、青年、中年和老年；
# 收入需要分成低收入群体、中等收入群体和高收入群体，数据中类似这样的问题还是蛮多的，
# 如何把这些连续数据进行分段处理呢？看看Python是如何达到目的的：

# 随机生成一列数据表示年龄
import numpy as np

age = np.random.randint(low=12, high=80, size=1000)
age = pd.Series(age)
# print(age.describe())

# 假如18岁以下为未成年；18~45岁为青年；45~60岁为中年；60岁以上为老年，接下来就根据这些阈值把年龄分为4段。
age_cut = pd.cut(age, bins=[0, 18, 45, 60, 80], right=False, labels=['未成年', '青年', '中年', '老年'])
# print(age_cut)

datas = pd.read_excel('give.xlsx', names=['type', 'num'])
# datas = datas['num']

start = 0
dT = 20000000
qujian = [start]
qujian_lable = []
datas = datas['num']
while True:
    end = start + dT
    qujian_lable.append('%s - %s' % (start, end))
    qujian.append(end)
    start = end
    if start > datas.max():
        break

result_cut = pd.cut(datas, bins=qujian, right=False, labels=qujian_lable)
# print(qujian)
# print(qujian_lable)
# print(result_cut)
lists = list(result_cut)
result_data = pd.Series(lists)
print('数据数量为: %s' % (lists.__len__()))
print(result_data.value_counts(sort=True, ascending=True))
# count = result_cut['40000000 - 60000000'].value_counts()
# print(count)
