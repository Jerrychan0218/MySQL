from types import BuiltinMethodType
import matplotlib.pyplot as plt
a = pd.read_csv('weather_inf.csv', index_col = 0)
fig, ax = plt.subplots() #製作一個空的圖,fig=figure像是一張白紙，ax=axis像是在上面畫上軸
ax.plot(a_weather['month'], a_weather['rain'], marker ='o', linestyle = '--', color = 'r')
# x-axis是month, y-axis = rain
# marker = 'o', 點的型態，這邊改為圓形，v = 向下的三角形
#其他網上有
ax.set_xlabel('Time(months)')
ax.set_ylabel('y')
ax.set_title('title')
plt.show()

fig, ax = plt.subplots(2,1, sharey = True) #2,1 也可以用nrow = 2, ncol = 1來代表
#subplots(2,1) 2,1是指會畫上下兩個圖，sharey是指他們會使用一樣的y刻度

climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")
#當檔案中有日期，就要用parse_dates來表明那個變項是日期

ax
ax2 = ax.twinx()
#當我們想把兩個變項顯示在同一圖中，但他們的y項不同，
# 就可以使用twinx來說明兩個變項有一樣的x但有不一樣的y

ax.tick_params('y', colors ='blue')
ax.tick_params('y',)
#一般情況下y軸title都會跟著設定變色，但刻度還是黑色
# ax.tick_params('y', colors ='blue') 可以改刻度顏色

# 因為很繁瑣，所以可以考慮用成def打包code
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)
#要呼叫的話就是用
plot_timeseries(ax, climate_change.index, climate_change['co2'], "blue", 'Time (years)', 'CO2 levels')

#當我們需要特別標注某個/些值出來，就可以用這個code
ax.annotate('>1 degree', xy = (pd.Timestamp('2015-10-06'),1))
# >1 degree是要顯示的文字，xy = 是告知python該資料的位置，pd.Timestamp是告知python時間的位置，因為x現在是時間資料
#但很長會因為文字上去覺得很雜亂，所以會加上
ax.annotate('>1 degree', xy = (pd.Timestamp('2015-10-06'),1),xytext=(pd.Timestamp('2008-10-06'), -0.2))
#來表示xytext=(pd.Timestamp('2008-10-06'), -0.2 這個位置是最合適顯示文字的
#但顯示出來會離目標資料太遠，所以要加
ax.annotate('>1 degree', xy = (pd.Timestamp('2015-10-06'),1),xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops = {})
# 來增加箭頭，箭頭可以客製化arrowprops = {'arrowstyle':'->', 'color':'gray'} 設定箭頭樣式跟顏色

# 長條圖==================
import pandas as pd
fig, ax = plt.subplots()
ax.bar(medal.index, medal['Gold'], label = 'Gold') 
ax.bar(medals.index, medals['Silver'], bottom = medals['Gold'], label = 'Silver')#這樣Silver的資料會疊在Gold的資料上面，形成累積的獎牌數
ax.bar(medals.index, medals['Bronze'], bottom = medals['Gold']+medals['Silver'], label= 'Bronze')
ax.set_xticklabels(medals.index, rotation = 90) #xticklabels是刻度下的名稱，rotation旋轉90度，因為橫字會擋住
ax.set_ylabel('Number of medals')
ax.legend() #legend 會配合上面既 label = 'Gold' etc 在圖上標示哪個顏色是哪個獎牌
plt.show()

ax.hist(b['Weight'], label = 'Weight', histtype = 'step', bins = 5) #hist與bar最大分別是hist可以看到分佈
#histtype就是顯示類型step是透明，bins是要顯示幾個bar

#加誤差線
ax.bar('Rowing', b['Height'].mean(), yerr = b['Height'].std()) #yerr就是誤差線的code
#折線圖
ax.errorbar(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'], yerr = seattle_weather['MLY-TAVG-STDDEV'])
#箱型圖
ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])
# Add x-axis tick labels:
ax.set_xticklabels(['Rowing', 'Gymnastics'])
# Add a y-axis label
ax.set_ylabel('Height (cm)')
plt.show()

#點陣圖
fig, ax = plt.subplots()
# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change['co2'], climate_change['relative_temp'], c = climate_change.index)
# c 是keyword 會把 = 後的變項以漸變色來呈現，這邊climate_change.index是日期，1958-03-06...etc
# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel('CO2 (ppm)')
# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel('Relative temperature (C)')
plt.show()

#超屌改圖的呈現方式
plt.style.use('ggplot') #ggplot就是R的那個，出來就會像是R的介面
seaborn-colorblind
grayscale
tableau-colorblind10
bmh
#都是些例子

#輸出圖
fig.set_size_inches([5, 3]) #設定輸出圖的大小，先橫再縱
fig.savefig('gold_medals.png', dpi = 300)
fig.savefig('gold_medals.jpg', quality = 50)
# 還有svg但好像比較少用，聽說是用來PS的，dpi跟quality都是品質