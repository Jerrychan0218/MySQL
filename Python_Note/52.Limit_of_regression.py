import statsmodels.formula.api as smf
results = smf.ols('INCOME2 ~ VEGESU1', data = brfss).fit() #ols是指模型，vegesu1預測income
results.params #params係數，輸出截距以及斜率


#example
# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()
# Make the DataFrame
df = pd.DataFrame() #因為我們只想看30歲不同教育水準的資料如何對收入有影響，所以我們可以創一個新的資料框架
df['educ'] = np.linspace(0, 20) 
df['age'] = 30 #常數，30歲比較常見，所以age都是30，age2=900
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2
# Generate and plot the predictions
pred = results.predict(df) #利用新建立的資料來執行results的公式
print(pred.head())

# Plot mean income in each age group
plt.clf()
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean() #先不同教育水準，在來世
plt.plot(mean_income_by_educ, 'o', alpha = 0.5)
# Plot the predictions
pred = results.predict(df)
plt.plot(df['educ'], pred, label='Age 30')
# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()

############### logit regression ###################

# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params

# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2

# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

plt.clf() #把plot圖清掉
grouped = gss.groupby('age')
favor_by_age = grouped['grass'].mean()
plt.plot(favor_by_age, 'o', alpha=0.5)

plt.plot(df['age'], pred1, label='Male')
plt.plot(df['age'], pred2, label='Female')

plt.xlabel('Age')
plt.ylabel('Probability of favoring legalization')
plt.legend()
plt.show()