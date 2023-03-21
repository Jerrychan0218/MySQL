# Import numpy with alias np
import numpy as np

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# Import numpy as np
import numpy as np

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country'] == "Belgium") | (food_consumption['country'] == 'USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))

#spread散布########################
np.var(a['age'], ddof = 1) #當使用的數據是樣本時，就要加ddof，如果是母群就不用
np.std(a['age'], ddof = 1)
np.quantile(a['age'], 0.5) # 0.5 = median
np.quantile(a['age'], [0, 0.25, 0.5, 0.75, 1])
np.quantile(a['age'], np.linspace(0,1,5)) #np.linspace(start, stop, num) ,num是分成幾份，start stop值都是%值
#iqr可以透過這邊計算出來的東西Q3-Q1得出，或是
from scipy.stats import ipr
iqr(a['age'])

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
# Show plot
plt.show()

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)

######## Sampling ###########
# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5, replace = False) #抽5次，replace false 代表不要重複、放回
print(sample_without_replacement)

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob'] #改column名

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob']) #期望值是數值*機率加總，得出理論的平均值

# Subset groups of size 4 or more
groups_4_or_more = restaurant_groups[restaurant_groups['group_size'] >= 4].value_counts() / len(restaurant_groups) #得出所有group_size大於4的機率

# Sum the probabilities of groups_4_or_more
prob_4_or_more = groups_4_or_more.sum() #所有大於4的機率
print(prob_4_or_more)

##### continuous uniform 均等分布 #########
from scipy.stats import uniform
uniform.cdf(7, 0, 12) #在等待時間最多為12分鐘時，等待的時間在7分鐘或以下的機率，其實算出來的就是一個面積，y是機率，x是時間。0 是最低值，12是最高值
1-uniform.cdf(7,0,12) #等待時間大於7的機率
uniform.rvs(0,5,size =10) #在均等分布中生成10個最大值為5，最小值為0的數值


# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform 

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5, 0, 30)
print(prob_less_than_5)

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20,0,30) - uniform.cdf(10, 0, 30)
print(prob_between_10_and_20)

# binom 丟硬幣分部 二次分布 ################
from scipy.stats import binom
binom.rvs(幾個硬幣, probability of heads/success, 幾次) #
binom.rvs(1, 0.5, 1) #一個硬幣，是公平的硬幣，丟一次 #會生成丟成功的次數array
binom.rvs(3, 0.5, 10) #回來10個數，代表每組成功的數，p = 0.5, n=10, np = mean = 期望值 = 5，我們預期的正面數量是5
binom.pmf(7, 10, 0.5) #丟十次硬幣，其中七次是正面，公平硬幣
binom.cdf(7, 10, 0.5) #cdf累積機率 = 小於丟十次硬幣，其中七次是正面的機率，公平硬幣

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size = 52)

# Print mean deals won per week
print(np.mean(deals))

# ppf
norm.ppf(0.9, 161, 7) #在161平均，7標準差的標準分布下，90%是甚麼數值

#cdf
norm.cdf(154, 161, 7) #154或以下占多少%

#生成sample
die = pd.Series([1,2,3,4,5,6])

samp_5 = die.sample(5, replace = True) #丟五次
print(samp_5)
np.mean(samp_5)
#跑10次
sample_means = [] #空list
for i in range(10):
    samp_5 = die.sample(5, replace = True)
    sample_means.append(np.mean(samp_5))
print(sample_means)

#Example
# Set seed to 104
np.random.seed(104)

# Sample 20 num_users with replacement from amir_deals and take mean
samp_20 = amir_deals['num_users'].sample(20, replace=True)
np.mean(samp_20)

sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()

#Example 2
# Set seed to 321
np.random.seed(321)

sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20, replace = True)
  # Take mean of cur_sample
  cur_mean = np.mean(cur_sample)
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)
# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals['num_users']))