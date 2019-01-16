#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/14

__author__ = 'zzh'

# 总结
#
# 散点图, scatter 方法, 可以绘制单个变量的散点图,多个变量的散点图,气泡图,线性回归线


#
# 散点图
#
# 上一期中，我们通过折线图可以快速的发现时间序列的趋势图，当然他不仅仅只能用在时间序列中，也可以和其他图形配合使用，
# 正如本期要介绍的，可以将折线图绘制到散点图中。散点图可以反映两个变量间的相关关系，
# 即如果存在相关关系的话，它们之间是正向的线性关系还是反向的线性关系？
# 甚至于是非线性关系？
# 在绘制散点图之前，我们任然老规矩，先来介绍一下matplotlib包中的scatter函数用法及参数含义。
#
# scatter函数的参数解读
#
# plt.scatter(x, y, s=20,
#             c=None, marker='o',
#             cmap=None, norm=None,
#             vmin=None, vmax=None,
#             alpha=None, linewidths=None,
#             edgecolors=None)
#
# x：指定散点图的x轴数据；
# y：指定散点图的y轴数据；
# s：指定散点图点的大小，默认为20，通过传入新的变量，实现气泡图的绘制；
# c：指定散点图点的颜色，默认为蓝色；
# marker：指定散点图点的形状，默认为圆形；
# cmap：指定色图，只有当c参数是一个浮点型的数组的时候才起作用；
# norm：设置数据亮度，标准化到0~1之间，使用该参数仍需要c为浮点型的数组；
# vmin、vmax：亮度设置，与norm类似，如果使用了norm则该参数无效；
# alpha：设置散点的透明度；
# linewidths：设置散点边界线的宽度；
# edgecolors：设置散点边界线的颜色；
#

import matplotlib.pyplot as plt
import pandas as pd

# 设置绘图风格
plt.style.use('ggplot')
# 设置中文编码和负号的正常显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


#
# 一般散点图的绘制
# 案例：汽车速度与刹车距离的关系
def test_1():
    # 读入数据
    cars = pd.read_csv('C:\\Users\\zhaozehui\\PycharmProjects\\DataAnalysis\\venv\\data\\test_15\\cars.csv')

    print(cars.head())
    # 绘图
    plt.scatter(cars['speed'],  # x轴数据为汽车速度
                cars['dist'],  # y轴数据为汽车的刹车距离
                s=30,  # 设置点的大小
                c='steelblue',  # 设置点的颜色
                marker='s',  # 设置点的形状
                alpha=0.9,
                linewidths=0.3,  # 设置散点边界线的宽度
                edgecolors='red'  # 设置三点便捷的颜色
                )

    plt.title('汽车速度与刹车距离的关系')
    plt.xlabel('汽车速度')
    plt.ylabel('刹车距离')

    plt.tick_params(top='off', right='off')

    plt.show()
    return


# test_1()

# 这样一张简单的散点图就呈现出来了，很明显的发现，汽车的刹车速度与刹车距离存在正相关关系，
# 即随着速度的增加，刹车距离也在增加。其实这个常识不用绘图都能够发现，关键是通过这个简单的案例，
# 让大家学会如何通过python绘制一个散点图。
# 如果你需要画的散点图，是根据不同的类别进行绘制，如按不同的性别，将散点图区分开来等。这样的散点图该如何绘制呢？


# 分组散点图的绘制
def test_2():
    # 读入数据
    data = pd.read_csv('C:\\Users\\zhaozehui\\PycharmProjects\\DataAnalysis\\venv\\data\\test_15\\iris.csv')

    print(data.head())

    # 自定义颜色
    colors = ['steelblue', '#9999ff', '#ff9999']

    # 三种不同的花品种
    pecies = data['Species'].unique()
    print(pecies)

    # 通过循环的方式，完成分组散点图的绘制
    for i in range(len(pecies)):
        plt.scatter(data.loc[data['Species'] == pecies[i], 'Petal.Length'],
                    data.loc[data['Species'] == pecies[i], 'Petal.Width'],
                    s=35, c=colors[i], label=pecies[i]
                    )

    plt.title('花瓣长度与宽度的关系')
    plt.xlabel('花瓣长度')
    plt.ylabel('花瓣宽度')

    plt.tick_params(top='off', right='off')

    plt.legend(loc='best')
    plt.show()
    return


# test_2()

# 可以想怎么设置就怎么设置。从图中可以发现，三种花的花瓣长度与宽度之间都存在正向的关系，
# 只不过品种setasa的体型比较小，数据点比较聚集。

# 气泡图的绘制
#
# 案例：大区销售数据
def test_3():
    import numpy as np
    # 读入数据
    data = pd.read_excel('C:\\Users\\zhaozehui\\PycharmProjects\\DataAnalysis\\venv\\data\\test_15\\sales.xlsx')

    print(data.head())

    # 绘制气泡图
    plt.scatter(data['finish_ratio'],  # 横轴点
                data['profit_ratio'],
                c='steelblue',
                s=data['tot_target'] / 30,
                edgecolors='red',
                label='气泡'
                )

    # 修改刻度的显示方式
    plt.xticks(np.arange(0, 1, 0.1), [str(i * 100) + '%' for i in np.arange(0, 1, 0.1)])
    plt.yticks(np.arange(0, 1, 0.1), [str(i * 100) + '%' for i in np.arange(0, 1, 0.1)])

    # 调整轴的显示数值范围
    plt.xlim(0.25, 0.65)
    plt.ylim(0.3, 0.8)

    plt.title('完成率与利润率的关系')
    plt.xlabel('完成率')
    plt.ylabel('利润率')

    plt.tick_params(top='off', right='off')

    # plt.legend(loc='best')
    plt.show()
    return


# test_3()
# 这样一个气泡图，本质上就是将散点图放大


# 散点图+回归线的绘制，这里回归线的绘制数据需要加载sklearn这个机器学习的模块，通过这个模块来生成一个线性模型。
#
# 散点图+线性回归线
# 汽车速度与刹车距离的关系
def test_4():
    from sklearn.linear_model import LinearRegression
    # 读入数据
    cars = pd.read_csv('C:\\Users\\zhaozehui\\PycharmProjects\\DataAnalysis\\venv\\data\\test_15\\cars.csv')

    print(cars.head())
    # 散点图
    plt.scatter(cars['speed'],
                cars['dist'],
                s=20,
                c='black',
                marker='o',
                alpha=0.9,
                linewidths=0.3,
                edgecolors='red',
                label='观测点'
                )
    # 建模
    regression = LinearRegression()
    reg = regression.fit(cars['speed'].reshape(-1, 1), cars['dist'])

    # 回归预测值
    pred = reg.predict(cars['speed'].reshape(-1, 1))

    # 绘制回归线
    plt.plot(cars['speed'], pred, linewidth=2, label='回归线')

    plt.title('汽车速度与刹车距离的关系')
    plt.xlabel('汽车速度')
    plt.ylabel('刹车距离')

    plt.tick_params(top='off', right='off')

    plt.legend(loc='best')
    plt.show()
    return


test_4()
