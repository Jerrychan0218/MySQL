import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('xxx.csv')
sns.scatterplot(x = 'good', data = df, hue = 'smoker', hue_order = ['Yes', 'No'], palette = {'a':'blue', 'b':'black'})
# hue 是指要填色的變項，hue_order 是重新排序legend裡面的東西
#palette 可以用dictionary的方式制定變項顏色

sns.relplot(x = 'a', y = 'b', data = c, kind ='scatter', col = 'study_time', row = 'd', col_order = ['',''])
#relplot這個功能跟上一節裡面fig, ax = plt.subplots(2, 1) 一樣，可以把變項分別產出小圖
#col就是要以什麼來分小圖，然後是以縱式去分;row則是以橫式去分
# 這邊先後順序要用col_order
# 另外也可以加size = 'a' 代表用不同大小表示不同值
# 用style = 'b' 表示用不同圖案代表不同值
# alpha = 0~1 可設定點的透明度，0是完全透明

sns.relplot(x = 'a', y = 'b', data = c, kind = 'line', ci = 'sd')
# 改為線性圖，如果x有多於一個點，圖會顯示信賴區間，
# ci 就是confidence interval 的意思，sd就是標準差的意思
# 這邊代表圖裡的信賴區間是顯示標準差，我們也可以用None來取消信賴區間
# 加入style = 'd', hue = 'd', marker = True, dashes = False
#style是不同值用不同圖案來表示，hue是不同顏色，marker是要不要把點標出來，
# dashes是因為python默認會把不同值用不同類型的線分別出來，所以如果都要用一個類型的線，就把他False掉

sns.catplot(x= , y= , data=, kind='count', order = [...], ci =  ) #catplot可以顯示類別變項的圖
# kind = 'count' / 'bar'比較常見, bar會自動顯示數據的mean與sd
# order 把長條圖依照想要的方式排序
# ci 跟上面一樣

sns.catplot(x = 'a', y = 'b', data = c, kind = 'box', sym = '')
# sym是處理離群值的方式，空白就是忽視他

import numpy as np
from numpy import median
sns.catplot(x = 'a', y= 'b', data = c, kind = 'point', join = False, estimator = median, capsize = 0.2)
#capsize是信賴區間的上下兩條橫線，可以選擇加或不加
#join 是指連接兩個點的線，False可以把它去掉
#estimator 是numpy（記得要喚出numpy）的其中一個function可以把原來的平均改為其他，比如median

sns.set_style() #調背景
sns.set_palette('顏色','顏色') #調色
sns.set_context() #調整整體比例
a.fig.suptitle('abc', y = 2) 
#y是標題的高度
# relplot, catplot是fig層級的，所以他們可以設定col, row等等的小圖，就像matplotlib的fig
# scatterplot, countplot等就是ax等級的
# fig.suptitle 是為fig等級的圖設定標題
a.set_title('abc', y = 2)
# 改ax等級的標題
a.set(xlabel = 'a', ylabel = 'b')
# 改軸名稱
plt.xticks(rotations = 90)
#直接用matplotlib的function來改x軸的角度

#Seaborn EP2 
sns.distplot(df['Award_Amount']) #分布圖
plt.show()
plt.clf()

# Create a distplot
sns.distplot(df['Award_Amount'], #KDE = Kernal Density Esitmate
             kde= False,  # 沒有密度線
             bins= 20)
# Display the plot
plt.show()

# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False, #不加長方圖
             rug=True,   #使得分布圖與密度條有一個小空隙
             kde_kws={'shade': True}) #使得分布圖有顏色

# Plot the results
plt.show()