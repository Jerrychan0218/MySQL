#處理遺漏值
# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace(8, np.nan, inplace = True) #8是遺漏值

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts()) #計算次數

#篩選資料
# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth'] >= 37

# Select the weights of full-term babies 
full_term_weight = birth_weight[full_term] #birth_weight中符合full_term的數值

# Compute the mean weight of full-term babies
print(full_term_weight.mean())

#畫圖，PMF,probability mass function，畫分布
# Compute the PMF for year
pmf_year = Pmf(gss['year'], normalize=False)

# Print the result
print(pmf_year)

#example
# Select the age column
age = gss['age']
# Make a PMF of age
pmf_age = Pmf(age)
# Plot the PMF
pmf_age.bar()
# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()

#cdf Cumulative distribution functions
# Select the age column
age = gss['age']
# Compute the CDF of age
cdf_age = Cdf(age)
# Calculate the CDF of 30
print(cdf_age(30))

# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75) #cdf 0.75 = 75% 換算成income的數值
# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)
# Calculate the interquartile range
iqr = percentile_75th - percentile_25th
# Print the interquartile range
print(iqr)

# Select realinc
income = gss['realinc']
# Make the CDF
cdf_income = Cdf(income)
# Plot it
cdf_income.plot() #預設是線lineplot
# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()

#example
# Select educ
educ = gss['educ']
# Bachelor's degree
bach = (educ >= 16)
# Associate degree
assc = (educ >= 14) & (educ < 16) #or 是 |
# High school
high = (educ <= 12)
print(high.mean())

#modeling distribution
#numpy scipy.stat seaborn 
#我們要找出分布有三個方法，CDF可以用於一般探索資料，PMF可以用於有少量獨特數值的資料，KDE可以用於有很多資料的數據
import numpy as np
sample = np.random.normal(size = 1000) #生乘常態分佈1000樣本
Cdf(sample).plot()

#method 2
from scipy.stats import norm
xs = np.linspace(-3, 3) #生成一組-3到3的等距數值
ys = norm(0, 1).cdf(xs)

plt.plot(xs, ys, color = 'gray') #會出現一個irt圖，x軸-3 到 3之間，0為平均，以1作為標準差，所以-3到3之間每1作相隔
#這個圖主要顯示累積的機率

#另外可以生成常態鐘型圖，pdf = probaility density function
from scipy.stats import norm
xs = np.linspace(-3, 3) #生成一組-3到3的等距數值
ys = norm(0, 1).pdf(xs) #cdf改為pdf #但pmf不可以跟pdf作比較，因為pmf是指每個數值的機率，而我們定義的情況下已經假設每個數值的機率是一樣的

import seaborn as sns
sns.kdeplot(sample)
#我們可以透過KDE = kernal density estimation 核密度估計，來轉換pmf到pdf從而進行比較
