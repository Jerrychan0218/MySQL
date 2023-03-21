#要進行回歸分析
from statsmodels.formula.api import ols
a_vs_b = ols('a ~ b', data = c) #獨變項寫右邊，依變項在左邊
a_vs_b = a_vs_b.fit()
print(a_vs_b.params) #會回覆截距與斜率參數

#種類回歸
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(data = c, x= 'a', col = 'species', col_wrap = 2, bins = 9) 
#col 以甚麼作為分組，col_wrap，每一行顯示幾個col

# Calculate the mean of price_twd_msq, grouped by house age
mean_price_by_age = taiwan_real_estate.groupby('house_age_years')['price_twd_msq'].mean()
#要分組的在groupby裡，要顯示數值的，放在[]裡
# Print the result
print(mean_price_by_age)

# Update the model formula to remove the intercept
mdl_price_vs_age0 = ols("price_twd_msq ~ house_age_years + 0" , data=taiwan_real_estate).fit()
########### +0 會使截距歸零，斜率會以0為基準全部變為正數，讓數據比較好理解。

# Print the parameters of the fitted model
print(mdl_price_vs_age0.params)

#我們也可以弄一個我們預期的線，而用真實數據與預期線比較
# Import numpy with alias np
import numpy as np

# Create the explanatory_data #首先弄個dataframe 用來當預設的 x 值
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})

# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq
price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)
#這邊是用mdl_price_vs_conv的這個模型公式，然後代入explanatory_data，生成對應explanatory的y值

# Create prediction_data
prediction_data = explanatory_data.assign(
    response_var = price_twd_msq)
#assign 可以把括號中的資料抽取到DataFrame，這邊DataFrame是explanatory_data
#在DataFrame裡增加response_var的一列，這一列的數值是price_twd_msq

# Print it
print(explanatory_data)

# Create a new figure, fig
fig = plt.figure()

sns.regplot(x="n_convenience",
            y="price_twd_msq",
            data=taiwan_real_estate,
            ci=None)
# Add a scatter plot layer to the regplot #畫一條預測線
sns.scatterplot(x="n_convenience",
            y="price_twd_msq",
            data=prediction_data,
            ci=None,
            color = 'r')

# Show the layered plot
plt.show()

###我們要生成一個預測線其實不用那麼麻煩
mdl_mass_vs_length.fittedvalues = 

explanatory_data = bream['length_cm']
print(mdl_mass_vs_length.predict(explanatory_data))

#當我們要了解殘差數值
print(mdl_mass_vs_length.resid)

# response(y) = intercept + slope * explanatory(x)
# Get the coefficients of mdl_price_vs_conv
coeffs = mdl_price_vs_conv.params
print(coeffs)
# Get the intercept
intercept = coeffs.iloc[0]
print(intercept)
# Get the slope
slope = coeffs.iloc[1]

# Manually calculate the predictions
price_twd_msq = intercept + slope * explanatory_data
print(price_twd_msq)

# Compare to the results from .predict()
print(price_twd_msq.assign(predictions_auto=mdl_price_vs_conv.predict(explanatory_data)))


#弄出一條xy相等的線，並且讓他跟回歸線比較
# Create a new figure, fig
fig = plt.figure()

# Plot the first layer: y = x
plt.axline(xy1=(0,0), slope=1, linewidth=2, color="green") #xy在0時會一樣

# Add scatter plot with linear regression trend line
sns.regplot(x = 'return_2018', y = 'return_2019', data = sp500_yearly_returns, ci = None)

# Set the axes so that the distances along the x and y axes look the same
plt.axis('equal')

# Show the plot
plt.show()

#如果回歸不是直線關係，可以:
# Create sqrt_dist_to_mrt_m 變化數據
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

# Run a linear regression of price_twd_msq vs. sqrt_dist_to_mrt_m 計算出公式
mdl_price_vs_dist = ols("price_twd_msq ~ sqrt_dist_to_mrt_m", data=taiwan_real_estate).fit()

# Use this explanatory data 形成一個預計資料框架，x值。np.arange(0,81,10)是指0-80，以10作為分隔。所以會有0,10,20...80這樣
explanatory_data = pd.DataFrame({"sqrt_dist_to_mrt_m": np.sqrt(np.arange(0, 81, 10) ** 2),
                                "dist_to_mrt_m": np.arange(0, 81, 10) ** 2})

# Use mdl_price_vs_dist to predict explanatory_data 
# #用mdl_price_vs_dist公式帶入x來生成y，並且在資料框架中加上去
prediction_data = explanatory_data.assign(
    price_twd_msq = mdl_price_vs_dist.predict(explanatory_data)
)

#畫圖
fig = plt.figure()
sns.regplot(x="sqrt_dist_to_mrt_m", y="price_twd_msq", data=taiwan_real_estate, ci=None)

# Add a layer of your prediction points #在圖中畫上預計的可能值
sns.scatterplot(data = prediction_data,x = 'sqrt_dist_to_mrt_m' , y = 'price_twd_msq', color= 'r')
plt.show()

