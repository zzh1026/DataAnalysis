#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/10

__author__ = 'zzh'

import pandas as pd

#
# 借助于pandas模块进行数据的预处理，内容包括数据集变量与观测的筛选、变量的重命名、数据类型的变换、排序、重复观测的删除、和数据集的抽样。
#

# 主要内容:
#
# 一、数据筛选
#   名称索引 iris['headname'] ,取headename列
#   变量观测筛选 iris.loc[条件,[选取的列名称集合]]  条件要用圆括号把条件括起来。
# 二、变量的删除
#   iris.drop([要删除的列名称集合],axis=1,inplace=True)  axis=0表示删除行, =1表示删除列
# 三、变量重命名
#   iris.rename(columns={传入要删除和要修改成的名称字典: 'a':'b', 代表a改名为b},inplace=True)  axis=0表示删除行, =1表示删除列
# 四、数据类型转化
#   iris.dtypes  查看列表的对象类型
#   iris.astypes({'a':'int'}) 要修改的名称,要修改成的类型
# 五、数据集的排序
#   iris.sort_values(by=['a'],ascending=[True]) 要修改的名称,要修改成的类型 by处理通过那个key的列来进行排序,第二个代表是否升序排序
# 六、数据去重
#   iris.duplicated(subset=None) 检测是否重复,默认所有数据均一致代表重复,如果有subset,则subset一致就代表重复 subset='a',或 subset=['a','b']
#   iris.drop_duplicated(subset=None) 去除重复,参数和检测重复一致
# 七、抽样
#   iris.sample(n=None, frac=None, replace=False, weights=None, random_state=None)
#   iris.loc[~iris.index.isin(train.index),:]   代表选择条件是iris中和排除train中的索引的集合
#
#


#
# 一、数据筛选
# 以iris数据集为例，想从数据集中取出某列（序列对象）或某几列该如何操作？
#
# 在pandas取出一列有两种方法，一种是比较普遍适用的名称索引法，另一种则是点取法。看看下面的例子就可以理解了：
# 如果使用点取法取出数据集中的某列，需要注意的是列的名称必须是一个整体，例如stu age或stu.age等格式的变量名就不能使用点取法。
# 所以一般使用索引法即可,这个东西即是向量
#
# 使用read_table
# books = pd.read_table('saves.txt', header=None, names=['type', 'number'])
# print(books)
# booksHead = books.head()
# print(booksHead)
# print(books['type'].head())

iris = pd.read_excel('give.xlsx', names=['type', 'number'])
# 名称索引法
# print(iris['type'].head())
# 点取法
# print(iris.number1.head())

#
# 在Python中通过索引的方式获取数据的部分子集，虽然有loc和iloc两种方法都可以实现取子集，但我更推荐loc函数的应用，
# 因为个人觉得iloc应用的场景比较少，它是基于行或列的位置进行数据筛选的。例如
#
# 取出前5行,第2列和第4列
# iris.iloc[0:5,[1,3]]
#
# loc和iloc其实是在不同的场景下有不同的使用方式
# 当确定取 第 xxx列的时候使用iloc 更加方便, 如:iris.iloc[:,0:5] 可以方便的取出每行的前四列,因为iloc的第二个参数可以使用pos角标进行获取
# 而loc 获取方式则是逗号后面要获取的列名称列表,相对没有iloc简单,总之第一个参数是条件或者其他,主要是对行进行限定,后面对列进行限定
#
# loc函数使用是
# iris.loc[(),[]]
# 逗号前面代表条件,逗号后面代表要获取的列名称
#
# 一个变量的观测筛选
b = iris.loc[(iris['number'] >= 409178886), :].head()
# print(b)

#
# 一个变量的观测筛选
b = iris.loc[(iris['number'] > 409178886) & (iris['type'] == 'AX-108974123'), :]
# print(b)

# 需要注意的是：多个变量的筛选，可以是或(|)关系、可以是且(&)关系还可以是非(~)关系，一定要用圆括号把条件括起来。
#
# 两个变量的观测筛选并筛选部分变量
b = iris.loc[(iris['number'] > 409178886) & (iris['type'] == 'AX-108974123'), ['number']]
# print(b)

#
#
# 二、变量的删除
#
# 有时，在一张表里你可能需要删除与建模或分析无关紧要的变量，如用户id、姓名、邮编号码等。在Python中，你可以借助于drop函数非常轻松的删除指定的变量。
# print(iris)

# 需要注意的是，该函数默认的axis=0，表示删除行观测，如果需要删除列，就要将asix设置为1。
# 记住，此时虽然删除了两个变量，但iris数据集本身是没有变化的，如果你需要改变iris数据集，需要设置inplace为True。
# iris.drop(['type'], axis=1, inplace=True)
# print(iris.head())

#
# 三、变量重命名
#
# 如iris数据集，由于第一个变量的名称为“Sepal.Length”，中间有句点号，故Python不可以使用点取法获得该数据集的第一个变量，而只能通过索引获取。
# 如果把该变量的名称改为“Sepal_Length”，就可以使用点取法了，该如何更换变量名呢？rename函数可以帮助我们解决问题：
# iris.rename(columns={'type': 'types'}, inplace=True)
# print(iris.head())

#
# 四、数据类型转化
#
# 使用Python进行建模的话，需要所有的输入变量均为数值型变量，然而手中的实际数据集并非全是数值型变量，该如何把字符型数值变量转化为数值变量呢？
# 使用dtype方法来查看各列字段的类型,然后通过astype方法来对字段类型进行转换

# datas = iris.head()
# print(datas.dtypes)

# 上面创建的表，显示types变量字符型变量，就需要将其转化为整数型和浮点型，具体可以通过astype函数实现：
# datas = datas.astype({'number': 'int'})
# print(datas.dtypes)

#
# 五、数据集的排序
# 如果你需要对你的数据集进行排序，Python中pandas模块也提供了非常好用的sort_values函数。我们举例说明：
# print(iris)
# 可以随意的按某些变量升序或降序排序
datas = iris.sort_values(by=['number', 'type'], ascending=[True, False]).head()
# print(datas)


#
# 六、数据去重
#
# 在数据清洗中，往往都要检查一下数据集的观测行是否有重复，如果存在重复的话必须将其删除，来看看Python的pandas模块是如何检查数据集是否重复，
# 并完成数据集的去重：
datas = pd.DataFrame({'name': ['Liu', 'Li', 'Chen', 'Liu'], 'age': [28, 12, 13, 28], 'gender': ['M', 'M', 'M', 'M']})
# print(datas)

# 检测观测是否重复
# duplicated() 方法
dupli = datas.duplicated()
# print(dupli)

# 删除重复观测
# drop_duplicates()
result = datas.drop_duplicates()
# print(result)

#
# 由上面的例子可知，duplicated函数可以用来检查数据集是否重复，如果重复，则会在重复的行显示True。
# 然后，通过drop_duplicates函数对数据集的重复观测进行删除。
#
# 这两个函数均有subset参数，默认对数据集的所有变量进行重复性检测和删除，如果你需要指定某些变量的重复性检查和删除就可以往subset参数传递变量，
# 区别在于如果不传 subset 代表所有数据都一致认为重复,如果传 subset 则代表 subset内容一致就代表重复
dupli = datas.duplicated(subset=['gender', 'name'])
dupli = datas.duplicated(subset='gender')
# print(dupli)

#
# 七、抽样
# 最后，我们再来讲讲如何使用pandas模块进行数据集的抽样，毕竟抽样在建模或机器学习中还是非常常用的，通过抽样构建训练集和测试集，训练集用来模型的生成，
# 测试集用来模型的检验。pandas模块有一个sample函数可以帮助我们完成抽样的任务：
#
# 先来看一下sample函数的几个重要参数
#
# sample(n=None, frac=None, replace=False, weights=None, random_state=None)
# n：指定抽样的个数
# frac：指定抽样的比例
# replace：指定是否有放回的抽样，默认为无放回抽样
# weights：指定每个样本被抽中的概率，默认每个样本抽中的概率相等
# random_state：指定抽样的随机种子，默认无固定的随机种子，即每次抽样的结果都不一样
#
# 抽样实例
# 训练集
train = iris.sample(frac=0.8, random_state=1)
# print(train)
# 测试集
tests = iris.loc[~iris.index.isin(train.index), :]
# print(tests)

# 训练集可以直接从sample函数中抽取出来，测试集则通过索引的方式，将训练集中的行号排除出去。
print('训练集的行,列数: ', train.shape)
print('测试集的行,列数: ', tests.shape)
