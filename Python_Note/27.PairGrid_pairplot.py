#PairGrid可以一次使用兩種不一樣的plot來看多個變項的關係，用於分布及回歸圖，設定如同FacetGrid
# Create a PairGrid with a scatter plot for fatal_collisions and premiums
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map(plt.scatter)
plt.show()
plt.clf()

# Create the same PairGrid but map a histogram on the diag
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(plt.hist) #diag是diagonal對角線，這行會生成左上及右下的圖
g3 = g2.map_offdiag(plt.scatter) #這會生成右上左下的圖
plt.show()
plt.clf()

# Create a pairwise plot of the variables using a scatter plot
#pairplot是PairGrid的簡易版
sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='reg') #這邊是右上跟左下要回歸線的意思，也可以只用scatter來代表，另外可以再加diag_kind = 'hist'，代表左上跟右下的圖示長方圖
plt.show()
plt.clf()


# Plot the same data but use a different color palette and color code by Region
sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='scatter',
        hue='Region', #填色
        palette='RdBu', #要甚麼色或色系
        diag_kws={'alpha':.5}) #圖要透明的程度
plt.show()
plt.clf()

# Build a pairplot with different x and y variables
sns.pairplot(data=df,
        x_vars=["fatal_collisions_speeding", "fatal_collisions_alc"], #設定X
        y_vars=['premiums', 'insurance_losses'], #設定y
        kind='scatter',
        hue='Region',
        palette='husl')
plt.show()
plt.clf()

# plot relationships between insurance_losses and premiums

sns.pairplot(data=df,
             vars=["insurance_losses", "premiums"],
             kind='reg',
             palette='BrBG',
             diag_kind = 'kde', #kde核密度分布估計
             hue='Region')
plt.show()
plt.clf()


