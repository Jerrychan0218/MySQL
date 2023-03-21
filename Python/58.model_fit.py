#fit() -> r^2
mdl_bream.rsquared

# Calculate mse_orig for mdl_click_vs_impression_orig
mse_orig = mdl_click_vs_impression_orig.mse_resid

# Calculate rse_orig for mdl_click_vs_impression_orig and print it
rse_orig = np.sqrt(mse_orig) # mse = rse^2
print("RSE of original model: ", rse_orig)

# Calculate mse_trans for mdl_click_vs_impression_trans
mse_trans = mdl_click_vs_impression_trans.mse_resid

# Calculate rse_trans for mdl_click_vs_impression_trans and print it
rse_trans = np.sqrt(mse_trans)
print("RSE of transformed model: ", rse_trans)

#要檢驗數據與模型是否適配，可以用幾種方法
#1. residplot
sns.residplot(x = 'a', y = 'b', data = c, lowess = True) 
#residplot會繪製殘差點，lowess會畫一條線表示預期值，這線跟點的重疊越多，代表殘差越小，越好

#2. qqplot
#看數據接近normal distribution的程度
from statsmodels.api import qqplot
qqplot(data = mdl_bream.resid, fit = True, line ='45') #line 線的角度

#3 scale-llocation plot
#看適配值大或小時的殘差與預測值是否不一樣，穩定性
model_norm_residuals_bream = mdl_bream.get_influence().resid_studentized_internal
#標準化(np.abs絕對值)，get_influence是取得模型影響力的方式，影響力代表觀察值拿走會對資料造成多大影響
#influence是用來看看數值與預測相差多遠，也是離群指標的一種
model_norm_residuals_abs_sqrt_bream = np.sqrt(np.abs(model_norm_residuals_bream))
sns.regplot(x = mdl_bream.fittedvalues, y = model_norm_residuals_abs_sqrt_bream, ci = None, lowess = True)


#1. example
# residplot
sns.residplot(x="n_convenience", y="price_twd_msq", data=taiwan_real_estate, lowess=True)
plt.xlabel("Fitted values")
plt.ylabel("Residuals")

# Show the plot
plt.show()

#2. qqplot example
# Import qqplot
from statsmodels.api import qqplot

# Create the Q-Q plot of the residuals
qqplot(data=mdl_price_vs_conv.resid, fit=True, line="45")

# Show the plot
plt.show()

#3. scale-llocation plot
# Preprocessing steps
model_norm_residuals = mdl_price_vs_conv.get_influence().resid_studentized_internal
model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))

# Create the scale-location plot
sns.regplot(x=mdl_price_vs_conv.fittedvalues, y=model_norm_residuals_abs_sqrt, ci=None, lowess=True)
plt.xlabel("Fitted values")
plt.ylabel("Sqrt of abs val of stdized residuals")

print(mdl_price_vs_conv.fittedvalues) # = mdl_price_vs_conv.predict(explantary_data)
# Show the plot
plt.show()


####outlier離群值
#有兩種，一種是極端值，一種是離開預測線=殘差較高的值
#leverage測量極端值有多極端
#influence測量我們拿掉殘差較高的離群值後重新跑一次模型會對資料造成的多少影響
mdl_roach = ols('g ~ cm', data = roach).fit()
summary_roach = mdl_roach.get_influence().summary_frame() #get_influence取得離群值帶來的影響力，在roach的觀察值裡加入leverage與influence的column
roach['leverage'] = summary_roach['hat_diag'] #summary frame裡原本就會有一個叫hat_diag的column來放置leverage, 現在改名
#roach 裡會有species mass_g length_cm leverage 幾個column
#leverage 會顯示length_cm (x) 裡每個值的極端程度
roach['cooks_dist'] = summary_roach['cooks_d'] #cooks_d裝的是influence的值，也就是這個值如果拿掉會對資料的影響力
print(roach.head())

print(roach.sort_values('cooks_dist', ascending = False)) #透過對influence的排序，可以知道哪些值影響力最大，則可能是離群值


