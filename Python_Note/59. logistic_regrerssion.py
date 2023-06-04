from statsmodels.formula.api import logit
mdl_churn_vs_recency_logit = logit('has_churned ~ time_since_last_purchase', data = churn).fit() #類別變項預測連續變項
print(mdl_churn_vs_recency_logit.params)

sns.regplot(x = 'time_since_last_purchase', y = 'has_churned', data = churn, ci = None, logistic = True)
plt.axline(xy=(0, intercept), slope = slope, color = 'black') #logistic regression 會是曲線

# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x = 'time_since_first_purchase', y = 'has_churned',data = churn,
            line_kws={"color": "red"})
# line_kws 可以呈現資料點的分布範圍           

plt.show()# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned

# 
sns.regplot(x="time_since_first_purchase",
            y="has_churned",
            data=churn, 
            ci=None,
            line_kws={"color": "red"})

# Draw a logistic regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x="time_since_first_purchase",
            y="has_churned",
            data=churn, 
            ci=None,
            line_kws={"color": "blue"},
            logistic = True)


#要看logistic回歸有沒有對上預期線跟普通作法是一樣的
# Create prediction_data
prediction_data = explanatory_data.assign(
    has_churned = mdl_churn_vs_relationship.predict(explanatory_data)
)

fig = plt.figure()

# Create a scatter plot with logistic trend line
sns.regplot(x = 'time_since_first_purchase', y = 'has_churned', data = churn, logistic = True)

# Overlay with prediction_data, colored red
sns.scatterplot(data = prediction_data, x = 'time_since_first_purchase', y = 'has_churned', color = 'r')

plt.show()


#計算會員隨著時間過去喪失顧客的比率會不會比較少
# Update prediction data with odds_ratio
prediction_data["odds_ratio"] = prediction_data["has_churned"] / (1 - prediction_data["has_churned"])

fig = plt.figure()

# Create a line plot of odds_ratio vs time_since_first_purchase
sns.lineplot(x = 'time_since_first_purchase', y = 'odds_ratio', data = prediction_data)

# Add a dotted horizontal line at odds_ratio = 1
plt.axhline(y=1, linestyle="dotted")

plt.show()

#用log來使原本曲線的關係變為直線關係
# Update prediction data with log_odds_ratio
prediction_data["log_odds_ratio"] = np.log(prediction_data["odds_ratio"])

fig = plt.figure()

# Update the line plot: log_odds_ratio vs. time_since_first_purchase
sns.lineplot(x="time_since_first_purchase",
             y="log_odds_ratio",
             data=prediction_data)

# Add a dotted horizontal line at log_odds_ratio = 0
plt.axhline(y=0, linestyle="dotted")

plt.show()

#####true negative  false positive
#####false negative true positive  
from statsmodels.graphics.mosaicplot import mosaic
conf_matrix = mdl_recency.pred_table()
print(conf_matrix)

mosaic(conf_matrix) #會畫出四個區域的count圖
plt.show()
#也可以
actual_response = churn['has_churned'] #是0或1
predicted_response = np.round(mdl_recency.predict()) #np.round四捨五入為0或1
outcome = pd.DataFrame({'actural_response': actual_response,
                        'predicted_response': predicted_response})
print(outcome.value_counts(sort = False))

####正確預測的1比例 準確性 = accurancy
# 公式為 (TN + TP)/ (TN + FP+ FN+ TP)

####實際觀測值比例:預期是真而的確是真 靈敏度 = sensitivity
# 公式為(TP)/TP + FN

# Extract TN, TP, FN and FP from conf_matrix
TN = conf_matrix[(0,0)]
TP = conf_matrix[(1,1)]
FN = conf_matrix[(1,0)]
FP = conf_matrix[(0,1)]

# Calculate and print the accuracy
accuracy = (TN+TP) / (TN+TP+FN+FP)
print("accuracy: ", accuracy)

# Calculate and print the sensitivity
sensitivity = TP / (TP+FN)
print("sensitivity: ", sensitivity)

# Calculate and print the specificity
specificity = TN / (TN+FP)
print("specificity: ", specificity)