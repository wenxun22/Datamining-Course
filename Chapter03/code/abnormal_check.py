# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:29:42 2022

@author: wenxun
"""

#3-1 describe()方法查看数据基本情况
import pandas as pd #导入库
catering_sale = '../data/catering_sale.xls' #餐饮数据
data =  pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定索引列为日期
print(data.describe())


#3-2 餐饮销售额的数据异常检测实现
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示字符
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
p = data.boxplot(return_type='dict') #直接使用DataFrame方法，返回字典
x = p['fliers'][0].get_xdata() #fliers为异常值标签
y = p['fliers'][0].get_ydata()
y.sort() #从小到大排序 会直接改变对象

plt.show() #展示箱线图


