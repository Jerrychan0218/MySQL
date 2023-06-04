import numpy as np
np.ramdom.seed(1) #設定seed
np.random.beta(a = 2, b = 2, size = 5000) #丟硬幣正反各兩次，5000次
np.random.normal(loc = 2, scale = 1.5, size = 2) #loc 是平均數、scale = 標準差、size = 回來的數
a.sample(n = 5, random_state = 1000) #n是樣本數，random_state = seed

#另外有一種抽樣方法是系統性取樣，是指我們在樣本中每隔幾個人取樣，10個人，抽5個人，所以會是每2位就抽一次，事實上用random sampling最好。
sample_size = 5 
pop_size = len(coffee_rating) #有1338種咖啡
print(pop_size)
interval = pop_size // smaple_size
print(interval) #266.6，四捨五入 = 267

#要每267抽一次
coffee_rating.iloc[::267]

#plot
coffee = coffee_ratings.reset_index()
coffee_rating.plot(x = 'index', y = 'aftertaste', kind = 'scatter')
plt.show() #但這樣可能會造成誤差，因為資料可能有經過排序，導致越後面的數值越大

#要改善就需要先random資料的順序
shuffled = coffee.ratings.sample(frac = 1) #可以random資料，frac設定隨機抽出多少原資料的比例，0.1就是從原資料裡隨機抽出10%的資料
coffee_ratings.reset_index(drop = True).reset_index()
shuffled.plot(x = 'index', y = 'aftertaste', kind = 'scatter')


#我們可以利用一些方法使python協助我們針對不同變項都跑隨機抽樣
top_counted_countries = ['a', 'b', 'c', 'd']
top_counted_subset = coffee_ratings['country_of_origin'].isin(top_counted_countries) #選取在coffee_ratings['country_of_origin']中有top_counted_countries裡的東西
coffee_rating_top = coffee_ratings[top_counted_subset]
coffee_ratings_samp = coffee_ratings_top.sample(frac = 0.1, random_state = 2021)
cooffee_ratings_samp['country_of_origin'].value_counts(normalize = True) #出來的結果是abcd分別具有多少比例(因為有用normalize，如果不是，就會顯示次數)

#我們可以先把資料分組，這樣就會變成在abcd中各抽10%，然後比較個國家佔母群多少
coffee_rating_strat = coffee_rating_top.groupby('country_of_origin').sample(frac = 0.1, random_state = 2021)

#另外也可以抽取一樣數量而不是比例
coffee_rating_strat = coffee_rating_top.groupby('country_of_origin').sample(n = 15, random_state = 2021)

#我們也可以把某國家設置為1，然後各國家與這個國家比
import numpy as np
coffee_rating_weight = coffee_rating_top 
condition = coffee_rating_weight['country_of_origin'] == 'Taiwan'
coffee_rating_weight['weight'] = np.where(condition, 2, 1) #np.where可以幫忙尋找跟條件一樣的東西，這邊設定一樣就換成2，不一樣就1
coffee_rating_weight = coffee_ratings_weight.sample(frac = 0.1, weights = 'weight')
coffee_rating_weight['country_of_origin'].value_counts(normalize = True)

#cluster
import random
varieties_pop = list(coffee_rating['variety'].unique())
varieties_samp = random.sample(varieties_pop, k = 3) #隨機從varieties_pop裡抽到3種咖啡豆
variety_condition = coffee_ratings['variety'].isin(varieties_samp)
coffee_ratings_cluster = coffee_ratings[variety_condition]
coffee_ratings_cluster['variety'] = coffee_ratings_cluster['variety'].cat.remove_unused_categories()#.cat.remove_unused_categories() 可以移除0項


#用numpy來做cluster
coffee_ratings_cluster.groupby('variety').sample(n = 5, random_state = 2021) #等計量抽樣，三種咖啡品種會有5筆資料

# Example
# Create a list of unique RelationshipSatisfaction values
satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())

# Randomly sample 2 unique satisfaction values
satisfaction_samp = random.sample(satisfaction_unique, k = 2)

# Filter for satisfaction_samp and clear unused categories from RelationshipSatisfaction
satis_condition = attrition_pop['RelationshipSatisfaction'].isin(satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition]
attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()

# Perform cluster sampling on the selected group, getting 0.25 of attrition_pop
attrition_clust = attrition_clust_prep.groupby('RelationshipSatisfaction').sample(n = len(attrition_pop)//4, random_state = 2022)


population_mean = coffee_ratings.sample(n=50)['total_cup_points'].mean()


#我們可以利用for loop來重複抽樣
mean_cup_point_1000 = []
for i in range(1000):
    mean_cup_points_1000.append(
        coffee_ratings.sample(n=30)['total_cup_point'].mean()
    )

# 製作滾動組合
# Expand a grid representing 5 8-sided dice
dice = expand_grid(
  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
   'die2': [1, 2, 3, 4, 5, 6, 7, 8],
   'die3': [1, 2, 3, 4, 5, 6, 7, 8],
   'die4': [1, 2, 3, 4, 5, 6, 7, 8],
   'die5': [1, 2, 3, 4, 5, 6, 7, 8]
  })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] + dice['die2'] + 
                     dice['die3'] + dice['die4'] + 
                     dice['die5']) / 5
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Draw a bar plot of mean_roll
dice['mean_roll'].value_counts(sort = False).plot(kind = 'bar')
plt.show()

np.random.choice(list(range(1,9)),size = 5, replace = True).mean() #replace 我們每一次是重甩，所以可以重複, choice用於根據條件生成一個隨機列表

sample_means_1000 = []
for i in range(1000):
    sample_means_1000.append(np.random.choice(list(range(1,9)), size = 5, replace = True).mean())

#bootstraping
import numpy as np
mean_flavors_1000 = []
for i  in range(1000):
    mean_flavors_1000.append(
        np.mean(coffee_sample.sample(frac = 1, replace = True)['flavor'])
    )

# confident interval 信賴區間
# Generate a 95% confidence interval using the quantile method
lower_quant = np.quantile(bootstrap_distribution, 0.025)
upper_quant = np.quantile(bootstrap_distribution, 0.975)

#另一種信賴區間計法-pandas
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975]) #boot_mean_diff 是一個mean list，高組平均-低組平均

# Print quantile method confidence interval
print((lower_quant, upper_quant))

# Find the mean and std dev of the bootstrap distribution
point_estimate = np.mean(bootstrap_distribution)
standard_error = np.std(bootstrap_distribution, ddof = 1)

# Find the lower limit of the confidence interval
lower_se = norm.ppf(0.025, loc = point_estimate, scale = standard_error) #CDF 累積分布的逆向, loc 放平均數，scale放標準誤

# Find the upper limit of the confidence interval
upper_se = norm.ppf(0.975, loc = point_estimate, scale = standard_error)

# Print standard error method confidence interval
print((lower_se, upper_se))
