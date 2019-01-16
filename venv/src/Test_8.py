#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/10

__author__ = 'zzh'

#
#
# 继续介绍pandas模块的其他新知识点。包括频数统计、缺失值处理、数据映射、数据汇总。

# 总结:
#
# 一、频数统计
#   向量的数据列表可以进行统计某个离散变量各水平的频次
#   1, datas['a'].value_count()  统计a在数据中的个数,注意 value_count()是一个方法,需要加()
#   2, datas['a'].value_count()/sum(datas['a'].value_count())  比例
# 二、缺失值处理
#   1,any(datas.isnull()) 判断数据是否存在缺失
#   2,any(pd.isnull('datas')) 判断向量是否存在缺失
#   3,datas.dropna(how=None) 删除缺失行,how可以设置删除方式, how='all' 如果某行都是None删除,否则不删除
#   4,datas.fillna(method='填补方式') 填补,填补方式有 'ffill'想前填补, 'bfill'向后填补
#   5,datas.fillna(value={'填补的列名称':data['函数替补名称'].mean()}) 填补,填补方式有 'ffill'想前填补, 'bfill'向后填补
# 三、数据映射
#   1,data.apply(func=映射方法,axis=1) axis=1 表示将方法映射到各行, =0表示映射到各列
#   2,data.iloc[:,[0,5]] 和 data.loc[:,['a','b']] 的区别,iloc取值更加方便,loc取值更加具体,容易阅读,因为iloc是使用pos取值,而loc是通过key取值
# 四、数据汇总
#   数据汇总主要用于数据分析处理,主要两个函数
#   1,groupby  groupbyData = datas.groupby([性别]) ,获取到了通过性别的分析对象,这是一个对象,参数是一个列表 可以是 ['a','b']
#   2,aggregate  groupbyData.aggregate(分析方法,如 np.mean 代表分析平均值) ,得到了数据向量 ,默认会对所有数值型变量作性别的均值统计。
#   3,aggregate  groupbyData.aggregate({分析的名称:分析方法}) ,限制限制的列
#   4,对数据做某一个方面的分析  groupbyData.aggregate({'列名称':分析方法})
#   5,对多个数据数据做多个方面的分析  groupbyData.aggregate({'列名称':分析方法,'列名称2':分析方法2})
#
#


import pandas as pd

# xlsxPath = 'C:/Users/zhaozehui/Desktop/student_score.xls'
xlsxPath = 'student_score.xls'
# datas = pd.read_excel(xlsxPath, names=['type', 'number'])
datas = pd.read_excel(xlsxPath)
# print(datas)

#
# 一、频数统计
#
# 我们以被调查用户的收入数据为例，来谈谈频数统计函数value_counts。

# 取数据前5行
tops = datas.head()
# print(tops)
# 频数统计，顾名思义就是统计某个离散变量各水平的频次。
# 这里统计的是性别男女的人数，是一个绝对值，如果想进一步查看男女的百分比例，可以通过下面的方式实现：
# print(datas['语文'].value_counts())
# print(datas['语文'].value_counts()/sum(datas['语文'].value_counts()))

# 如果需要统计两个离散变量的交叉统计表,需要使用 pandas模块提供了crosstab 函数
# cross = pd.crosstab(index=datas['语文'], columns=datas['数学'])
# print(cross)


#
# 二、缺失值处理
# 在数据分析或建模过程中，我们希望数据集是干净的，没有缺失、异常之类，但面临的实际情况确实数据集很脏，例如对于缺失值我们该如何解决？
# 一般情况，缺失值可以通过删除或替补的方式来处理。
# 首先是要监控每个变量是否存在缺失，缺失的比例如何？
# 这里我们借助于pandas模块中的isnull函数、dropna函数和fillna函数。
# 总览数据集是否存在缺失
hasNull = any(datas.isnull())
print(hasNull)

# 每一列是否有缺失
if hasNull:
    is_null = []
    null_ratio = []
    for col in datas.columns:
        is_null.append(any(pd.isnull(datas[col])))
        null_ratio.append(float(round(sum(pd.isnull(datas[col])) / datas.shape[0], 2)))

# print(is_null, '\n', null_ratio)

# 每一行是否有缺失
is_null = []
# datas = datas.head()
for index in list(datas.index):
    is_null.append(any(pd.isnull(datas.loc[index, :])))

# print(is_null)


# 对缺失数据进行处理：
#
# 删除法
# dropna函数，有两种删除模式，一种是对含有缺失的行(任意一列)进行删除，另一种是删除那些全是缺失(所有列)的行，具体如下：
# 删除任何缺失的观测 ,删除时候相当于重新复制对新的数据集进行操作,不会对原来的数据有影响
dropDatas = datas.dropna()
# 删除每行中所有变量都为缺失的观测,所以当某行中有一个变量不为缺失状态就不会删除
# dropDatas = datas.dropna(how='all')  # 由于datas数据集不存在行全为缺失的观测，故没有实现删除。
# print(dropDatas)

# 替补法
# fillna函数提供前向替补、后向替补和函数替补的几种方法，具体可参见下面的代码示例：
# 通过method 来添加替补方法,  'ffill'表示向前替补 , 'bfill'表示向后替补
# 不同的列用不同的函数替补 使用 value的方式
# fillDatas = datas.fillna(method='ffill')
fillDatas = datas.fillna(method='bfill')
# fillDatas = datas.fillna(value={'性别':datas['班名次'].min()})
# print(fillDatas)


#
# 三、数据映射
# 大家都知道，Python和R在做循环时，效率还是很低的，如何避开循环达到相同的效果呢？这就是接下来我们要研究的映射函数apply。
# 该函数的目的就是将用户指定的函数运用到数据集的纵轴即各个变量或横轴即各个行。
# 现在通过映射函数可以这样简介而快速的实现：
# 查看各个行和列是否有缺失
# 创建一个判断对象是否包含缺失的匿名函数
isNull = lambda x: any(pd.isnull(x))
# 使用apply映射函数
# axis=0 表示将isNull函数映射到各列,axis=1,表示应用到各行
# datas = datas.head()
fillDatas = datas.apply(func=isNull, axis=0)
# fillDatas = datas.apply(func=isNull, axis=1)
# print(fillDatas)

#
# 计算每个学生的总成绩，或各科的平均分，也可以用apply函数实现：
print(datas.head())
import numpy as np


# 计算每个学生的总成绩
# print(datas)
# datas['tot'] = datas.iloc[:, 2:5].apply(func=np.sum, axis=1)
# print(datas)
# datas['tot'] = datas.loc[:, ['语文', '数学', '英语']].apply(func=np.sum, axis=1)
# print(datas)

# 计算每个学生的平均成绩
# print(datas.head())
def getScoreType(x):
    meanScore = np.mean(x)
    if meanScore < 60:
        result = '不及格'
    elif meanScore < 80:
        result = '及格'
    elif meanScore < 100:
        result = '高等'
    else:
        result = '优秀'
    return result


datas['平均成绩'] = datas.iloc[:, 2:5].apply(func=np.mean, axis=1)
datas['成绩属性'] = datas.iloc[:, 2:5].apply(func=getScoreType, axis=1)
# print(datas)

# 计算每门学科的平均成绩 ,所有行参与统计,3到6列参与统计
result = datas.iloc[:, 2:6].apply(func=np.mean, axis=0)
# print(result)


#
# 四、数据汇总
#
# 如果你想要做类似SQL中的聚合操作，pandas也提供了实现该功能的函数，即groupby函数与aggregate函数的搭配使用，我们以上面的收入数据集为例作为演示：
# 对性别做分组统计
groupby_gender = datas.groupby(['成绩属性'])
groupby_mean = groupby_gender.aggregate(np.max)
# print(groupby_mean)
# 以上结果，默认会对所有数值型变量作性别的均值统计。如果不符合统计的需求就不会进行统计
# 如果需要限定,可以使用夏明的方式
# groupby_mean = groupby_gender.aggregate({'语文': np.mean})    # 限定一个
groupby_mean = groupby_gender.aggregate({'语文': np.mean, '数学': np.mean})  # 限定多个
# print(groupby_mean)

groupby_gender = datas.groupby(['成绩属性', '性别'])
groupby_mean = groupby_gender.aggregate(np.mean)
# print(groupby_mean)

# 对成绩属性和性别两个变量做分组统计,但不同的变量做不同的聚合
grouped = datas.groupby(['成绩属性', '性别'])
# 例如, 对语文算平均值,对数学算中位数
group_gate = grouped.aggregate({'语文': np.mean, '数学': np.median})
# print(group_gate)
