#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/9

__author__ = 'zzh'

# numpy
#
# 该模块主要有这几个功能：数学领域的线性代数、傅里叶变换；统计学领域的统计计算、随机数生成等。
import numpy as np

arr1 = np.array([1, 3, 5, 7, 9])
# print(arr1)

arr2 = np.array([10, 20, 30, 40, 50])
# print(arr2)

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [3, 4, 5, 6]])
# print(arr3)

# print(arr1.shape)
# print(arr3.shape)

#
# 元素的获取
#
# 使用索引的方式，查询一维数组和二维数组的元素。
# 一维数组的索引与列表、元组的索引完全一致，这里就不在赘述；
# 二维数组的索引就稍微有点复杂，我们可以通过例子来说明：
print(arr3, '\n')

# 获取二维数据的某列
# print(arr3[:, 2])  # 先行后列, 这个表示 所有行的第三列
# 获取二维数据的某行
# print(arr3[1, :])  # 先行后列,这个表示第二所有数据
# 获取二维数据的某个元素
# print(arr3[2, 3])  # 先行后列,这个表示第三行第四列,因为pos从0开始

# 获取二维数组的某几列
# print(arr3[[0, 2], :])  # 先行后列,这个表示第一行和第三行的所有列
# print(arr3[:, [0, 1, 3]])  # 先行后列,这个表示所有行 ,第 1,2,4列

# 获取二维数组中的某几行某几列元素
# print(arr3[[0, 1], [2, 3]])  # 获取【0,2】和【1,3】对应的两个值。那该如何返回想要的2×2的矩阵呢？

# 获取2*2,取两次索引
# print(arr3[[0, 2], :][:, [2, 3]])

# 获取矩阵
# print(arr3[np.ix_([0, 2], [2, 3])])  # 使用np.ix_方法来获取矩阵

#
# 数学函数
# 1,取绝对值
# np.abs
# np.fabs
#
# 2,算术平方根
# np.sqrt
#
# 3,平方
# np.square
#
# 4,指数
# np.exp
#
# 5,对数
# np.log2
# np.log10
# np.log(x,base)
#
# 其他: https://mp.weixin.qq.com/s?__biz=MzI5NDY1MjQzNA==&mid=2247484662&idx=2&sn=d2d92d1a86ba431a6405342bac7f5da0&chksm=ec5edb8bdb29529d22fd2fdb8217fc046957c126641558d8641c0abd6138fcc918882c240132&scene=21#wechat_redirect
#
#
# 映射函数
#
# apply_along_axis
#
# 随机数生成
#
# numpy模块中的子模块random提供了很多产生随机数的方法，帮我们产生伪数据带来了极大的方便，
# 这里就介绍几种常用的分布随机数。有时候为了使每次产生的随机数都相同，就需要设置固定的随机种子，设
# 置随机种子可以调用seed函数实现。
#
#
# 离散分布
#
# 1,二项分布：在概率论和统计学中，二项分布是n个独立的是/非试验中成功的次数的离散概率分布，其中每次试验的成功概率为p。

# 设置随机种子,保证每次运行都会出现相同的随机数
np.random.seed(123)
# 二项分布
r1 = np.random.binomial(n=10, p=0.2, size=10)
# print(r1)

r2 = np.random.binomial(n=10, p=0.2, size=(3, 5))
# print(r2)

# size参数可以用来控制生成的随机数的形状，r1就是一个10个长度的一维数组；r2就是一个3×5的矩阵。


#
# 泊松分布
#
# 该分布适合于描述单位时间（或空间）内随机事件发生的次数。如某一服务设施在一定时间内到达的人数，
# 电话交换机接到呼叫的次数，汽车站台的候客人数，机器出现的故障数。
np.random.seed(2)

# 泊松分布
r3 = np.random.poisson(lam=6, size=10)
# print(r3)
r4 = np.random.poisson(lam=(10, 50, 20), size=(5, 3))
# print(r4)


# 连续分布
# 正态分布：该分布也成高斯分布，呈现两头低，中间高，左右对称的倒钟形状，是连续分布中使用最频繁的一种分布。
np.random.seed(2)
r5 = np.random.normal(loc=2, scale=3, size=10)
# print(r5)

r6 = np.random.normal(loc=2, scale=3, size=(3, 5))
# print(r6)

#
# 数据加载
# numpy模块还提供了读取数据与写数据的函数，方便我们将外部数据文件读入到Python的工作环境中。这里推荐两个读数据的函数：
#
# data1 = np.loadtxt(fname='loadtxt.txt', delimiter=',', skiprows=1)
data1 = np.genfromtxt(fname='saves3.txt', delimiter=' ', skip_header=1, defaultfmt='%.0f')
print(data1)

#
# fname：指定外部文件的路径
# delimiter：指定文件中数据列的分隔符
# skiprows：指定读数时跳过的行数
# skip_header：指定跳过首行
# usecols：指定读取的数据列

#
# 数据写出
# 通过使用numpy模块中的savetxt函数实现python数据的写出，函数语法如下：
#
# np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')
#
# fname：指定数据写出的路径
# X：指定需要写出的数据
# fmt：指定输出数据的格式，默认科学计算法
# delimiter：指定数据列之间的分隔符，默认空格符
# newline：指定新行的标识符，默认换行
# header：指定输出数据首行值
# footer：指定输出数据的末行值
# comments：指定注释符，默认“#”
b = np.savetxt('saves3.txt', [[1, 2, 3], [2, 3, 4], [3, 4, 5]], fmt='%.00f', header='start')
print(b)
