import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 要檢驗真實數據與bootstrap出來的分布是否一致
a = book.mean()

#bootstrap
book_shop = []
for i in range(5000):
    book_shop.append(
        b = np.mean(book.sample(frac = 1, replace = True))
    )

plt.hist(book_shop, bin = 50)
plt.show()    

std_error = np.std(book_shop, ddof = 1)

#z-score
# (x - mean) / std

a
mean_hyp = 100
std_error

(a - mean_hyp)/std_error 

#p-value
#首先計算z-score
from scipy.stats import norm
from scipy.stats import t
#左尾test 
norm.cdf(z_score, loc = 0, scale = 1)
#右尾
1 - norm.cdf(z_score, loc = 0, scale = 1) #出來的就是該zscore所對應的p-value

#t-test

1 - t.cdf(stat, df = degrees_of_freedom)

#pingouin ttest
import pingouin
pingouin.ttest(x =sample_data['diff'], y = 0, alternative = 'less') #ttest
#y = 虛無假設；alternative = 對立假設: two-sided, less, greater

pingouin.ttest(x = sample_data['repub_percent_08'],
               y = sample_data['repub_percent_12'],
                   paired = True, alternative = 'less') #ttest

#pingouin anova
pingouin.anova(data = data, dv ='dependent', between = 'independent')
# 事後比較
pingouin.pairwise_tests(data = data, dv = 'dependent', between = 'independent', padjust = 'none')
#padjust是調整過後的pvalue，能降低alpha的可能性，也就是我們認為有但其實沒有的錯誤
#常用的是bonf = bonferroni correction


#proportion 比較
n_hobbyists = np.array([812, 1021])
n_rows = np.array([812 + 238, 1021 + 190])
from statsmodels.stats.proportion import proportions_ztest
z_score, p_value = proportions_ztest(count = n_hobbyists, nobs = n_rows, alternative = 'two-sided')

#chi square###########
# Proportion of freight_cost_group grouped by vendor_inco_term
props = late_shipments.groupby('vendor_inco_term')['freight_cost_group'].value_counts(normalize=True)

# Convert props to wide format
wide_props = props.unstack()

# Proportional stacked bar plot of freight_cost_group vs. vendor_inco_term
wide_props.plot(kind="bar", stacked=True)
plt.show()

# Determine if freight_cost_group and vendor_inco_term are independent
expected, observed, stats = pingouin.chi2_independence(data = late_shipments, x = 'vendor_inco_term', y = 'freight_cost_group')

# Print results
print(stats[stats['test'] == 'pearson']) 

#**expected, observed, stats = pingouin.chi2_independence(data=stack_overflow, x = 'hobbyist', y = 'age_cat', correction = False)
#**chi square = z_score^2

###########goodness fit by chi2
a = data['c'].value_counts() #觀察值
a = a.rename_axis('c')\
     .reset_index(name = 'n')\
     .sort_values('c')

h = pd.DataFrame({  #預期值
    'c':['1','2','3','4'], #設定內容
    'd':[1/6, 1/6, 1/2, 1/6] #每個內容出現的佔比
})   

n_total = len(a)
h['n'] = h['d'] * n_total #預期佔比*總觀察樣本數 = 預期樣本佔比

import matplotlib.pyplot as plt
plt.bar(a['c'], a['n'], color = 'red', label = 'Observed')
plt.bar(h['c'], h['n'], alpha = 0.5, color = 'blue', label = 'Hypothesized') #alpha = 透明度
plt.legend()
plt.show()

from scipy.stats import chisquare

chisquare(f_obs = a['n'], f_exp = h['n']) #x = 觀察值分數、y = 預期分數


#當樣本很小時，我們不知道效果是不是真的有存在，所以我們會用非參數檢驗

#1.rank
x = [1,15,3,10,6]
from scipy.stats import rankdata
rankdata(x)
#結果會是 1, 5 , 2, 4, 3 排序出來

#用Wilcoxon-signed rank test
repub_votes_small['diff'] = repub_votes_small['08'] - repub_votes_smail['12'] #成對樣本，計算它們值的差異

repub_votes_small['abs_diff'] = repub_votes_small['diff'].abs() #計算差異列的絕對值

#然後排序
repub_votes_small['rank_abs_diff'] = rankdata(repub_votes_small['abs_diff'])

#計算W值

T_minus = 1+4+5+2+3 #這些值是diff出來後，所有負值經過絕對值後，再四捨五入後的加總
T_plus = 0 #就是diff裡是正值的數值加總，但此例子中沒有正值，所以是0

W = np.min([T_minus, T_plus]) #W值是兩個數值中比較小的那個，所以是0

#另一種方法計算W值，是用pingouin
pingouin.wilcoxon(x = repub_votes_small['08'], y = repub_votes_smail['12'], alternative = 'less')


#***非參數檢驗unpaired t & ANOVA - Wilcoxon-Mann-Whitney test  
age_vs_comp = stack_overflow[['converted_comp', 'age_first_code_cut']] 
age_vs_comp_wide = age_vs_comp.pivot(columns = 'age_first_code_cut', values = 'converted_comp') #要計算W值，先要把資料從直變橫
pingouin.mwu(x = age_vs_comp_wide['child'], y = age_vs_comp_wide['adult'], alternative = 'greater') 

#ANOVA - Wilcoxon-Mann-Whitney test
pingouin.kruskal(data = stack_overflow, dv = 'converted_comp', between = 'job_sat')
