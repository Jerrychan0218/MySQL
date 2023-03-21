import missingno as msno
import matplotlib.pyplot as plt

a = pd.read_csv('a', sep = ',')
msno.matrix(a) #可以用點陣化方式顯示缺失
missing = a[a['co2'].isna()] #選取缺失值
complete = a[~a['co2'].isna()] #選取非缺失值
missing.describe() #看missing的摘要 然後我們發現，在溫度很低的情況下，co2都會是缺失值
complete.describe() 
#所以，我們用temperature column來排序
sorted_a = a.sort_values(by = 'temperature')
msno.matrix(sorted_a)
plt.show()
#得出可能是太低溫時感應器會無法運作
a_dropped = a.dropna(subset = ['co2']) #刪掉缺失值
co2_mean = a['co2'].mean() #用平均代替缺失值
a_imputed = a.fillna({'co2':co2_mean}) 
a_imputed.head()

