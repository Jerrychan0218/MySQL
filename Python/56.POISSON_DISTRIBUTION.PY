from scipy.stats import poisson #poisson可以計算一段時間內某件事發生的機率 = lambda
poisson.pmf(5,8) # 一周有5次領養的機率，而平均是8
poisson.cdf(5,8) #一週五次或以下的領養機率
poisson,rvs(8, size = 10) #生成平均數為8，有10個樣本的分布

#指數分布 = 時間與poisson的關係 = 1/lambda
from scipy.stats import expon
expon.cdf(1, scale = 0.5) #等待時間小於1 分鐘的機率，等待時間平均在2.5小時

#相關
#一般會用圖代替相關值，因為可能有非線性的相關
#一般相關
a.corr(b)

#要對弄成對數才能測量非線性關系
m['log_a'] = np.log(m['a'])
sns.lmplot(x = 'log_a', y = b, data = c, ci = None)
plt.show()
