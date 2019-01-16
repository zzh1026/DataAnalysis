#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/1/14

__author__ = 'zzh'

#
# 在常见的统计图像中，还有一种图像可以表示离散变量各水平占比情况，这就是我们要讲解的饼图。
# 饼图的绘制可以使用matplotlib库中的pie函数，首先我们来看看这个函数的参数说明。
#
import matplotlib.pyplot as plt

#
# 总结
#
# 图形需要是百分比
#


#
# pie函数参数解读
# plt.pie(x, explode=None, labels=None, colors=None,
#         autopct=None, pctdistance=0.6, shadow=False,
#         labeldistance=1.1, startangle=None,
#         radius=None, counterclock=True, wedgeprops=None,
#         textprops=None, center=(0, 0), frame=False)
#
# x：指定绘图的数据；
# explode：指定饼图某些部分的突出显示，即呈现爆炸式；
# labels：为饼图添加标签说明，类似于图例说明；
# colors：指定饼图的填充色；
# autopct：自动添加百分比显示，可以采用格式化的方法显示；
# pctdistance：设置百分比标签与圆心的距离；
# shadow：是否添加饼图的阴影效果；
# labeldistance：设置各扇形标签（图例）与圆心的距离；
# startangle：设置饼图的初始摆放角度；
# radius：设置饼图的半径大小；
# counterclock：是否让饼图按逆时针顺序呈现；
# wedgeprops：设置饼图内外边界的属性，如边界线的粗细、颜色等；
# textprops：设置饼图中文本的属性，如字体大小、颜色等；
# center：指定饼图的中心点位置，默认为原点
# frame：是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心位置；
#

#
# 案例：芝麻信用失信用户分析
# 绘图数据借用芝麻信用近300万失信人群的样本统计数据，该数据显示，从受教育水平上来看，中专占比25.15%，大专占比37.24%，本科占比33.36%，
# 硕士占比3.68%，剩余的其他学历占比0.57%。

# 设置绘图的主题风格（不妨使用R中的ggplot分隔）
plt.style.use('ggplot')

# 构造数据,这里的数据是列表即可,会自动计算百分比,如果总值小于1会按照真实的数据进行显示
edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
lables = ['中专', '大专', '本科', '硕士', '其他']

# explode,指定饼图某些部分的突出显示，即呈现爆炸式；突出显示大专学历人群
explode = [0, 0.1, 0, 0, 0]
colors = ['#9999ff', '#ff9999', '#7777aa', '#2442aa', '#dd5555']  # 自定义颜色

# 中文乱码处理 -- 将字体配置为微软雅黑
plt.rcParams['font.sans-serif'] = ['SimHei']
# 不转化成unicode编码
plt.rcParams['axes.unicode_minus'] = False

# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的刻度范围
plt.xlim(0, 4)
plt.ylim(0, 4)  # ymin, ymax

# 绘制饼图
plt.pie(x=edu,  # 绘图数据
        explode=explode,  # 突出显示大专人群
        labels=lables,  # 添加教育水平标签
        colors=colors,  # 设置饼图的自定义填充色
        autopct='%.1f%%',  # 设置百分比的格式,这里保留一位小数
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance=1.12,  # 设置教育水平标签与圆心的距离
        startangle=180,  # 设置饼图的初始角度
        radius=1.5,  # 设置饼图的半径
        counterclock=False,  # 是否逆施展,这里设置顺时针方向
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
        textprops={'fontsize': 12, 'color': 'k'},  # 设置文本标签的属性值
        center=(2.0, 2.0),  # 设置饼图的原点
        frame=True  # 设置实付显示饼图的图框,这里设置显示
        )

# 删除x轴和y轴的刻度
# plt.xticks(())
# plt.yticks(())

# 添加图标题
plt.title('芝麻信用失信用户教育水平分布')

# 显示图形
plt.show()
