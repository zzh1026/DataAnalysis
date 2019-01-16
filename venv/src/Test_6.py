#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/10

__author__ = 'zzh'

#
# 在Python中可以通过pandas模块的DataFrame函数构造数据框

#
# 主要内容
#
# 1、数据框的构造
#   通过 panas 的 DataFrame()方法
#   1,通过列表: pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['v1','v2','v3'])
#   2,通过字典: pd.DataFrame({'id':[1,2,3],'name':['a','b','c']},columns=['name','id']) 因为通过字典会默认培训,可以通过columns校正
# 2、数据的读入
#   1, pd.read_table('a.txt')   读取文本
#   2, pd.read_csv('a.csv')     读取文本
#   3, pd.read_excel('a.xlsx')  读取电子表格excel
#   4, pd.read_sql('select * from user_info', conn)  读取sql数据库,前面是查询语句,后面是sql链接,通过 pymysql 库可以创建连接
# 3、数据的概览信息
#   通过pd读取后的内容标记为datas;该datas可以获取一些信息
#   1, datas.shape 可以获取数据的行和列 (5,6) 代表5行6列
#   2, datas.columns 可以获取数据的列表头名称
#   3, datas.describe(include=['number'])       数值型变量的概览信息,注意这里必须是数值型的数据才可以
#   4, datas.describe(include=['object'])       离散型变量的概览信息,注意这里必须是离散型的数据才可以
#           describe属性可以对数值型变量（include=['number']）和离散型变量（include=['object']）进行描述性统计；
#   5, datas.info()       离散型变量的概览信息,注意这里必须是离散型的数据才可以
#
#
#
#
#


#
# 1、数据框的构造
# 在Python中,可以借助于列表、元组、字典进行手工构建数据框，我们用例子说明：
# 通过列表创建数据框
import pandas as pd

tab1 = pd.DataFrame([[1, 2, 3], [10, 20, 30], [100, 200, 300], [1, 10, 100]], columns=['V1', 'V2', 'V3'])
# print(tab1)

# 通过字典创建数据框
tab2 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Tom', 'Lily', 'Jim'], 'age': [23, 24, 25]},
                    columns=['id', 'age', 'name'])
# print(tab2)

#
# 2、数据的读入
# 在更多的场景下我们是读取外部数据，然后基于外部数据进行数据分析、可视化、数据挖掘等研究。这里跟大家介绍一下文本文件、电子表格和MySQL数据库的读取。
#

#
# 文本文件的读取 , 用read_table 读取txt文本, 用read_csv读取csv文件
books = pd.read_table('saves.txt', sep='\t', header=None, usecols=[0, 1], names=['值', '数据'])
# books = pd.read_table('give.xlsx', sep=' ', header=None)
books.tail()
# print(books)
# pd.read_csv()

#
# read_table和read_csv两个函数都可以读文本文件数据，区别在于默认的sep参数不一致，
# read_table默认以制表符Tab键为字段间的间隔符，而read_csv默认以逗号为字段间的间隔符。
#
# 由于原始数据文件books.txt没有字段名称，故设置header=None，并用names参数给表字段加上名称，
# usecols则是设置读取原始数据的哪些列。下面再来看看使用read_table函数读取csv文件。


#
# 电子表格的读取
# pandas模块中read_excel函数可以非常方便的读取外部的xls和xlsx电子表格：
books2 = pd.read_excel('give.xlsx', names=['值', '数据'])
# print(books2)


#
# MySQL数据库数据的读取

# 创建连接
# conn = pymysql.connect(host='localhost', port=3306, user='root', password='wszzh19921026', database='pythondata',
#                        charset='utf8')
# 读取数据
# user_info = pd.read_sql('select * from user_info', conn)
# print(user_info.shape)
# user_info.describe(include=['number'])
# user_info.describe(include=['object'])
# print(user_info)


#
# 3、数据的概览信息
#
# shape属性和columns属性返回数据集的行列数及变量名；
