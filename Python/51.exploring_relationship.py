plt.plot(height, weight, 'o', marketsize = 1, alpha = 0.02) #alpha是透明度，marketsize 是每點的大小，調整後可以協助我們看清楚一些重疊的數據
plt.show()

#jittering
height_jitter = height + np.random.normal(0, 2, size = len(brfss)) #加入平均數為0、標準差為2 的常態 = jittering=抖動
weight_jitter = weight + np.random.normal(0, 2, size = lan(brfss)) #這樣可以讓數據呈現霧化狀，比較好看
plt.plot(height, weight, 'o', markersize = 1, alpha = 0.02)
plt.show()

#為了讓數距更好看，可以加入
plt.axis([140, 200, 0, 160]) # X為140-200，y=0-160，來縮小顯示範圍

# 例子
# Drop rows with missing data
data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])
# Make a box plot
sns.boxplot(x = data['WTKG3'], y = data['_HTMG10'], whis = 10) #whis可以使function減少計算一些東西，詳情可看seaborn介紹
# Plot the y-axis on a log scale
plt.yscale('log') #用對數log來換算yscale
# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.show()

#例子2
# Drop rows with missing data
data = brfss.dropna(subset=['INCOME2', 'HTM4'])
# Make a violin plot
sns.violinplot(x = 'INCOME2', y = 'HTM4', data = data, Inner = None)
# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Income level')
plt.ylabel('Height in cm')
plt.show()


#相關
columns = ['a', 'b', 'c']
subset = data[columns]
#會生成相關表

#回歸
from scipy.stats import linregress
res = linregress(xs, ys)
#生成slope, intercept, rvalue, pvalue,stderr
#用scipy.stats 來畫線，但好麻煩...
fx = np.array([xs.min(), xs.max()])
fx - res.intercept + res.slope*fx
plt.plot(fx, fy, '-')