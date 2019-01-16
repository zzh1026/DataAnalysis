#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/14

__author__ = 'zzh'

#
# 展现数据的分布，我们还可以使用直方图来说明，通过图形的长相，就可以快速的判断数据是否近似服从正态分布。
# 之所以我们很关心数据的分布，是因为在统计学中，很多假设条件都会包括正态分布，故使用直方图来定性的判定数据的分布情况，尤其显得重要。
# 这期我们就来介绍Python中如何绘制一个直方图。
#
# hist函数的参数解读
# 绘图之前，我们先来讲解一下matplotlib包中hist函数的参数含义及使用方法：
#
# plt.hist(x, bins=10, range=None, normed=False,
#         weights=None, cumulative=False, bottom=None,
#         histtype='bar', align='mid', orientation='vertical',
#         rwidth=None, log=False, color=None,
#         label=None, stacked=False)
#
# x：指定要绘制直方图的数据；
# bins：指定直方图条形的个数
# range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值；
# normed：是否将直方图的频数转换成频率；
# weights：该参数可为每一个数据点设置权重；
# cumulative：是否需要计算累计频数或频率并排序；
# bottom：可以为直方图的每个条形添加基准线，默认为0；
# histtype：指定直方图的类型，默认为bar，除此还有’barstacked’, ‘step’,  ‘stepfilled’；
# align：设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’；
# orientation：设置直方图的摆放方向，默认为垂直方向；
# rwidth：设置直方图条形宽度的百分比；
# log：是否需要对绘图数据进行log变换；
# color：设置直方图的填充色；
# label：设置直方图的标签，可通过legend展示其图例；
# stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放；
#

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# 一元直方图的绘制
#
import numpy as np
import pandas as pd

# 中文乱码处理 -- 将字体配置为微软雅黑
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.style.use('ggplot')


def test_1():
    # 读取数据
    data = pd.read_excel('C:/Users/zhaozehui/PycharmProjects/DataAnalysis/venv/data/hengxiang/test1.xls')
    # print(data)
    # 检查缺失情况
    # print(any(data['语文'].isnull()))
    # 删除有缺失的行
    # data.dropna(subset=['语文'], inplace=True)
    # print(data)
    # print(data['语文'].describe())

    # 设置图形的显示风格

    datas = data['语文']
    print(datas.count())
    # 绘图：语文成绩的直方图
    plt.hist(datas,  # 绘图数据
             bins=15,  # 指定直方图的条形数为20个
             color='steelblue',  # 指定填充色
             align='left',
             edgecolor='k',  # 指定直方图的边界色
             label='直方图'  # 为直方图呈现标签
             )

    plt.xlabel('成绩')
    plt.ylabel('人数')
    plt.title('班级成绩分布直方图')

    # 去除图形顶部边界和右边界的刻度
    plt.tick_params(top='off', right='off')

    # 显示图例
    plt.legend()

    # 显示图形
    plt.show()
    return


# test_1()


#
# 上图绘制的是语文成绩的频数直方图，从整体的分布来看，有点像正态分布，两边低中间高的倒钟形状。
# 除此，我们还可以绘制累计频率直方图，并且设置3分为组距，如下代码可以表示成：
def test_2():
    # 读取数据
    data = pd.read_excel('C:/Users/zhaozehui/PycharmProjects/DataAnalysis/venv/data/hengxiang/test1.xls')
    # print(data)
    # 检查缺失情况
    # print(any(data['语文'].isnull()))
    # 删除有缺失的行
    # data.dropna(subset=['语文'], inplace=True)
    # print(data)
    # print(data['语文'].describe())

    # 设置图形的显示风格

    datas = data['语文']
    # print(datas.count())
    # result = np.arange(datas.min(), datas.max(), 5);
    # print(result)

    # 绘图：语文成绩的直方图
    plt.hist(datas,  # 绘图数据
             bins=np.arange(datas.min(), datas.max(), 5),  # 指定直方图的组距
             # normed=True,  # 设置为频率直方图
             # cumulative=True,  # 积累直方图
             color='steelblue',  # 指定填充色
             align='left',
             edgecolor='k',  # 指定直方图的边界色
             label='直方图'  # 为直方图呈现标签
             )

    plt.xlabel('成绩')
    plt.ylabel('人数')
    plt.title('累计频率')

    # 去除图形顶部边界和右边界的刻度
    plt.tick_params(top='off', right='off')

    # 显示图例
    plt.legend(loc='best')

    # 显示图形
    plt.show()
    return


# test_2()


def test_3():
    # 读取数据
    data = pd.read_excel('give.xlsx', names=['type', 'num'])
    # print(data)
    # 检查缺失情况
    print(any(data['num'].isnull()))
    # 删除有缺失的行
    # data.dropna(subset=['语文'], inplace=True)
    # print(data)
    datas = data['num'];

    # 设置图形的显示风格
    result = np.arange(0, datas.max() + 20000000, 20000000)

    # 绘图：语文成绩的直方图
    plt.hist(datas,  # 绘图数据
             bins=result,  # 指定直方图的组距
             color='steelblue',  # 指定填充色
             align='left',
             edgecolor='k',  # 指定直方图的边界色
             label='直方图'  # 为直方图呈现标签
             )

    plt.xlabel('值')
    plt.ylabel('次数')
    plt.title('直方图')

    # 去除图形顶部边界和右边界的刻度
    plt.tick_params(top='off', right='off')

    # 显示图例
    plt.legend(loc='best')

    # 显示图形
    plt.show()
    return


# test_3()

# 为了测试数据集是否近似服从正态分布，需要在直方图的基础上再绘制两条线，
# 一条表示理论的正态分布曲线，另一条为核密度曲线，目的就是比较两条曲线的吻合度，
# 越吻合就说明数据越近似于正态分布。接下来我们就在直方图的基础上再添加两条曲线：
def test_4():
    # 读取数据
    data = pd.read_excel('C:/Users/zhaozehui/PycharmProjects/DataAnalysis/venv/data/hengxiang/test1.xls')

    datas = data['语文']
    print(datas.count())
    # 绘图：语文成绩的直方图
    plt.hist(datas,  # 绘图数据
             bins=np.arange(datas.min(), datas.max(), 3),  # 指定直方图的条形数为20个
             normed=True,  # 设置为频率直方图
             color='steelblue',  # 指定填充色
             align='left',
             edgecolor='k',  # 指定直方图的边界色
             label='直方图'  # 为直方图呈现标签
             )

    plt.title('班级成绩分布直方图')
    plt.xlabel('成绩')
    plt.ylabel('人数')

    # 生成正态曲线的数据
    x1 = np.linspace(datas.min(), datas.max(), 1000)
    normal = mlab.normpdf(x1, datas.mean(), datas.std())
    # 绘制正态分布曲线
    line1, = plt.plot(x1, normal, 'r-', linewidth=2)

    # 生成核密度曲线的数据
    kde = mlab.GaussianKDE(datas)
    x2 = np.linspace(datas.min(), datas.max(), 1000)

    # 绘制
    line2, = plt.plot(x2, kde(x2), 'g-', linewidth=2)

    # 去除图形顶部边界和右边界的刻度
    plt.tick_params(top='off', right='off')

    # 显示图例
    plt.legend([line1, line2], ['正态分布曲线', '核密度曲线'], loc='best')

    # 显示图形
    plt.show()
    return


# test_4()

#
# 二元直方图的绘制
#
# 上面绘制的直方图都是基于所有乘客的年龄，如果想对比男女乘客的年龄直方图的话，我们可以通过两个hist将不同性别的直方图绘制到一张图内，具体代码如下：
# 本质上就是讲两种图放在一起
def test_5():
    # 读取数据
    data = pd.read_excel('student_score.xls')
    # print(any(data['性别'].isnull()))
    data.dropna(subset=['性别'], inplace=True)
    # print(data)
    datas = data['语文']
    score_female = datas[data['性别'] == '女']
    # print(score_female)
    score_male = datas[data['性别'] == '男']
    # print(score_male)

    # 设置直方图的组距
    bins = np.arange(datas.min(), datas.max(), 2)

    # 男性学生分数直方图
    plt.hist(score_male, bins=bins, edgecolor='k', label='男生', color='steelblue', alpha=0.3)
    # 女生分数直方图
    plt.hist(score_female, bins=bins, label='女生', edgecolor='#00000000', alpha=0.3)

    # 设置坐标轴标签和标题
    plt.title('学生成绩直方图')
    plt.xlabel('成绩')
    plt.ylabel('人数')

    # 去除图形顶部边界和右边界的刻度
    plt.tick_params(top='off', right='off')

    # 显示图例
    plt.legend()
    # 显示图形
    plt.show()
    return


test_5()
