#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/16

__author__ = 'zzh'

# 绘制填充表格热力图
#
# 所谓的填充表格热力图就是将原本为数字表（数组）的单元格以颜色来填充，颜色的深浅表示数值的大小。
# 我想，对于这样的图来说，总比直接看密密麻麻的数值表要轻松的多吧，毕竟颜色感官比数字感官要直接，
# 要具有更强的冲击。除了填充表格热力图，还有更为常见的地图热力图等。
#
# 数据采集—气温数据
#
# http://lishi.tianqi.com/shanghai/201809.html

import calendar
# 导入包
import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from bs4 import BeautifulSoup

# 采集数据
# 上海的数据
url = 'https://www.huoche.net/lishitianqi/shanghai/month.html'

# 发送爬虫请求
response = requests.get(url).text
# print(response)

soup = BeautifulSoup(response, 'html.parser')
# print(soup)

# 根据html标记语言,查询目标记下的数据
datas = soup.findAll('table', {'class': 'yuBaoTable'})
datas = datas[0].findAll('tr')[1:]
# print(datas)

# 抓取日期数据
date = [i.findAll('td')[0].text for i in datas]
# print(date)
# 抓取最高温数据
high = [i.findAll('td')[1].text.replace('℃', '') for i in datas]
# print(high)

# 创建数据框
df = pd.DataFrame({'date': date, 'high': high})

# ==================数据整理=====================

# 将date变量转换成日期类型
df['date'] = pd.to_datetime(df['date'])

# 将high变量转换成数值型
df['high'] = df['high'].astype('int')

# 数据处理
# 由日期型数据衍生出weekday
df['weekday'] = df['date'].apply(pd.datetime.weekday)


# df.sort_values('date', inplace=True)
# print(df.head())


# 由日期型数据计算week_of_month，即当前日期在本月中是第几周
# 由于没有现成的函数，这里自定义一个函数来计算week_of_month

def week_of_month(tgtdate):
    # 由日期型参数tgtdate计算该月的天数
    days_this_month = calendar.mdays[tgtdate.month]  # 通过循环当月的所有天数，找出第二周的第一个日期
    for i in range(1, days_this_month + 1):
        d = datetime.datetime(tgtdate.year, tgtdate.month, i)
        if d.day - d.weekday() > 0:
            startdate = d
            break
    # 返回日期所属月份的第一周
    return (tgtdate - startdate).days // 7 + 1


df['week_of_month'] = df['date'].apply(week_of_month)
print(df.head())
# df.to_excel('temp.xlsx')


# 到此为止，我们就完成了数据的采集和清洗过程，接下来我们就可以借助该数据完成填充热力（日历）图的绘制。

# 填充热力图的绘制
#
# 基于matplotlib绘制热力图
# 其实，我需要绘制的是一个数据表，只不过把表中的每一个单元格用颜色填充起来。
# 而表的结构是：列代表周一到周日，行代表9月份第一周到第五周。
# 很显然，我们刚刚完成的数据并不符合这样的结构，故需要通过pandas模块中的pivot_table函数制作一个透视表，然后才可以绘图。
# 关于热力图，我们可以使用matplotlib模块中的pcolor函数，具体我们可以看下方的绘图语句：

# ==================绘图前的数据整理=====================
# 构建数据表（日历）
# print(df.iloc[:, 1:])  # 横行所有,列从第二列开始,去掉0列
# 制表,表数据是high值, 横行(行)是week_of_month,表示第几周,columns列是weekday,表示星期几
target = pd.pivot_table(data=df.iloc[:, 1:], values='high', index='week_of_month', columns='weekday')
print(target)

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def use_mlp():
    # 缺失值填充（不填充的话pcolor函数无法绘制）
    target.fillna(0, inplace=True)
    # print(target)

    # 删除表格的索引名称
    target.index.name = None
    print(target)

    # 对索引排序（为了让“第一周”到“第五周”的刻度从y轴的高到底显示）
    target.sort_index(ascending=False, inplace=True)
    # print(target)

    # ======================开始绘图=========================

    plt.pcolor(target,
               cmap=plt.cm.Reds,  # 指定填充色
               edgecolors='white'  # 指点单元格之间的边框色
               )

    # 添加x轴和y轴刻度标签(加0.5是为了让刻度标签居中显示)
    plt.xticks(np.arange(7) + 0.5, ['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
    plt.yticks(np.arange(6) + 0.5, ['第六周', '第五周', '第四周', '第三周', '第二周', '第一周'])

    # 消除图框顶部和右部的刻度线
    plt.tick_params(top='off', right='off')
    plt.title('上海2018-12每日最高气温分布图')
    plt.show()
    return


# use_mlp()

# OK，一张填充表格热力图就奇迹般的显示了，而且看上去还蛮舒服的。
# 从图框看，9月份的第一天是周五，之后的每一天都有对应的颜色显示。但我在绘图过程中发现几个问题：
#   1,绘图用的数据，不能包含缺失值，否则填充图是绘制不出来的，所有需要对缺失值做填充处理；
#   2,最终的图例无法实现，即颜色的深浅，代表了具体的数值范围是什么？
#   3,不方便将具体的温度值显示在每个单元格内；
# 为解决上面的三个问题，我们借助于seaborn模块中的heatmap函数重新绘制一下热力图，而且这些问题在heatmap函数看来根本不算问题。

def use_sns():
    # 绘图
    ax = sns.heatmap(target,
                     cmap=plt.cm.Blues,
                     linewidths=.1,  # 设置每个单元方块的间隔
                     annot=True  # 显示数值
                     )

    # 添加x轴刻度标签(加0.5是为了让刻度标签居中显示)
    plt.xticks(np.arange(7) + 0.5, ['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
    # 可以将刻度标签置于顶部显示
    # ax.xaxis.tick_top()

    # 添加y轴刻度标签
    plt.yticks(np.arange(6) + 0.5, ['第一周', '第二周', '第三周', '第四周', '第五周'])
    # 旋转y刻度0度，即水平显示
    plt.yticks(rotation=0)

    plt.title('上海2018-12每日最高气温分布图')
    # ax.set_title('上海2018-12每日最高气温分布图')
    ax.set_xlabel('')
    ax.set_ylabel('')
    plt.show()
    return


# use_sns()
