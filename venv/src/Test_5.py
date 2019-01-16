#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/10

__author__ = 'zzh'

import pandas as pd

#
# pandas
# 是对向量、数据框的处理
#
# 序列
# ls1 = [1, 2, 5]
# 将列表转换为序列
# seriesl = pd.Series(ls1)

# print(seriesl)
# seriesl + 10
# print(seriesl)

#
# 序列的索引：
#
# 统计运算
# pandas模块提供了比numpy模块更丰富的统计运算函数，而且还提供了类似于R语言中的summary汇总函数，即describe函数。
import numpy as np

np.random.seed(1234)
ls1 = np.random.randint(size=30, low=10, high=30)
# print(ls1)
s = pd.Series(ls1)
# print(s)
c = s.describe()
# print(c)

# 判断一个序列元素是否为缺失可以使用isnull函数
# 缺失值的判定
s = pd.Series([1, 2, np.nan, 4, np.nan, 6])
print(s)
print(s.isnull)

#
# 其他常用的统计函数
# s.min()  # 最小值
# s.quantile(q=[0,0.25,0.5,0.75,1]) # 分位数函数
# s.median()  # 中位数
# s.mode()  # 众数
# s.mean()  # 平均值
# s.mad()  # 平均绝对误差
# s.max  # 最大值
# s.sum()  # 和
# s.std()  # 标准差
# s.var()  # 方差
# s.skew()  # 偏度
# s.kurtosis()  # 峰度
# s.cumsum()  # 和的累计，返回序列
# s.cumprod()  # 乘积的累积，返回序列
# s.product()  # 序列元素乘积
# s.diff()  # 序列差异（微分），返回序列
# s.abs()  # 绝对值，返回序列
# s.pct_change()  # 百分比变化 ，返回序列
# s.corr(s2)  # 相关系数
# s.ptp()  # 极差  R中的range函数
# https://mp.weixin.qq.com/s?__biz=MzI5NDY1MjQzNA==&mid=2247484680&idx=2&sn=7092e508351fadb0aee534f9ad8255e4&chksm=ec5eda75db29536350f75cf1ff7b7c68cf248c832e8f845a090abf57a41562ba68cf8cb16c1e&scene=21#wechat_redirect
