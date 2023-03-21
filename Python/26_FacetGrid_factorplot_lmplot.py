#FacetGrid factorplot lmplot都可以一次產生好多個小圖來呈現結果，很好用

# Create FacetGrid with Degree_Type and specify the order of the rows using row_order
g2 = sns.FacetGrid(df, #data來自哪
        row="Degree_Type", #用甚麼變項來分row 
        row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate']) #排序在Degree_Tyoe裡的幾個項目
# Map a pointplot of SAT_AVG_ALL onto the grid
g2.map(sns.pointplot, 'SAT_AVG_ALL') #畫圖，定義x軸的內容
# Show the plot
plt.show()
plt.clf()


# Create a factor plot that contains boxplots of Tuition values
sns.factorplot(data=df,
         x='Tuition',
         kind='box',
         row='Degree_Type')  #也可以用order來排序
# 用factorplot可以快速造出圖來，超方便
plt.show()
plt.clf()


# Create a FacetGrid varying by column and columns ordered with the degree_order variable
g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)
# Map a scatter plot of Undergrad Population compared to PCTPELL
g.map(plt.scatter, 'UG', 'PCTPELL') #可以設定xy值
plt.show()
plt.clf()

# Re-create the previous plot as an lmplot
#用lmplot也可以做出一樣的效果，不過設定不一樣
sns.lmplot(data=df,
        x='UG',
        y='PCTPELL',
        col="Degree_Type",
        col_order=degree_ord)
plt.show()
plt.clf()


# Create an lmplot that has a column for Ownership, a row for Degree_Type and hue based on the WOMENONLY column
#lmplot可以一次設定多個不同條件，就會做成相應多的圖
sns.lmplot(data=df,
        x='SAT_AVG_ALL',
        y='Tuition',
        col="Ownership", #直行是不同Ownership狀況
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors'],
        hue='WOMENONLY', #把womenonly分色
        col_order=inst_ord)
plt.show()
plt.clf()



