import pandas as pd
import seaborn as sns
df = sns.regplot(x = 'a', y = 'b', data = c)

# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region") #針對不同國家用顏色的線來描繪
# Show the results
plt.show()

# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           col ="Region") #針對不同國家分成不同column圖來描繪，也可以改成row，就會變成橫式來呈現

# Show the plot
plt.show()

#Seaborn graph
# Plot the pandas histogram
df['fmr_2'].plot.hist() #普通版
plt.show()
plt.clf()

# Set the default seaborn style
sns.set() #這邊會更改為seaborn的樣式

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf() #生成出來的圖默認為darkgrid 背景暗灰有格子, 其他有white, dark, whitegrid, darkgrid

#畫一個style為dark的分布圖
sns.set_style('dark')
sns.distplot(df['fmr_2'])
plt.show()
plt.clf()

# Set the style to white
sns.set_style('white')
# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')
# Remove the spines
sns.despine(right = True, top = True) # spine是指圖的外框，原本會有正方形框著圖，這邊去掉右邊跟上面，就會剩下L字形的框，就是一般的XY軸
# Show the plot and clear the figure
plt.show()
plt.clf()

#Seaborn顏色
#普通方法
# Set style, enable color code, and create a magenta distplot
sns.set(color_codes=True)
sns.distplot(df['fmr_3'], color='m')
# Show the plot
plt.show()
#進階方法
for p in sns.palettes.SEABORN_PALETTES:
    sns.set_palette(p) #palette是調色板的意思
    sns.palplot(sns.color_palette('Paired', 12)) #palplot 可以為圖添上顏色，有非常多種，deep, muted, pastel, bright, dark, colorblind, paired, Blues, BrBG, husl，coolwarm數字是指生成幾種顏色
    plt.show()

# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']: #也可以先設定要甚麼
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()
    
    # Clear the plots    
    plt.clf()


#***Seaborn配合matplotlib的功能來造圖***
#Example 1
# Create a figure and axes
fig, ax = plt.subplots()
# Plot the distribution of 1 bedroom rents
sns.distplot(df['fmr_1'], ax=ax) #x =ax
# Modify the properties of the plot
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100,1500),
       title="US Rent")
# Display the plot
plt.show()


#Example 2
# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.distplot(df['fmr_1'], ax=ax)
# Customize the labels and limits
ax.set(xlabel ="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")
# Add vertical lines for the median and mean
ax.axvline(x=634.0, color='m', label='Median', linestyle='--', linewidth=2) #加一條線在634來帶屌
ax.axvline(x=706.3254351016984, color='b', label='Mean', linestyle='-', linewidth=2)
# Show the legend and plot the data
ax.legend()
plt.show()

#Example 3
# Create a plot with 1 row and 2 columns that share the y axis label
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)
# Plot the distribution of 1 bedroom apartments on ax0
sns.distplot(df['fmr_1'], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500))
# Plot the distribution of 2 bedroom apartments on ax1
sns.distplot(df['fmr_2'], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100,1500))
# Display the plot
plt.show()


# 類別變項的呈現
#stripplot & swarmplot(這個圖的點不會重疊再一起) 可以顯示全部觀察值
# boxplot，violinplot，lvplot顯示摘要性分布的訊息
# barplot，pointplot，countplot顯示具有統計估計值的資訊

# Create the stripplot
sns.stripplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         jitter=True) # jitter 可以刪掉一些重疊的值，使得圖比較好看
plt.show()

# Create and display a swarmplot with hue set to the Region
sns.swarmplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         hue='Region') # 不同國家需要用不同顏色分類的意思
plt.show()

# Create a violinplot with the husl palette
sns.violinplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='husl')
plt.show()
plt.clf()

# Create a lvplot with the Paired palette and the Region column as the hue
sns.lvplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='Paired',
         hue='Region')
plt.show()
plt.clf()

# Create a pointplot and include the capsize in order to show caps on the error bars
sns.pointplot(data=df,
         y='Award_Amount',
         x='Model Selected',
         capsize=.1) #誤差線的上下兩條界線的長度
plt.show()
plt.clf()

#*****Regression!!*****
# Display a regression plot for Tuition
sns.regplot(data=df,
         y='Tuition',
         x="SAT_AVG_ALL",
         marker='^', #點的樣式
         color='g') #綠色
plt.show()
plt.clf()

# Display the residual plot 
sns.residplot(data=df, #殘差線，如果殘差不太分散隨機的話，則可能有二階變項需要考慮
          y='Tuition',
          x="SAT_AVG_ALL",
          color='g')
plt.show()
plt.clf()

# Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)
plt.show()
plt.clf()

# The final plot should include a line using a 2nd order polynomial
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5,
            order=2) #設為二階
plt.show()
plt.clf()

# Create a scatter plot by disabling the regression line
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            fit_reg=False) #取消回歸線
plt.show()
plt.clf()

#**** 超重要 ****
# Create a crosstab table of the data
pd_crosstab = 
 #可以直接弄成一個矩陣x=Group y= YEAR
print(pd_crosstab)

# Plot a heatmap of the table
sns.heatmap(pd_crosstab) #弄成類似空氣汙染的濃度圖，越深數值越高

# Rotate tick marks for visibility
plt.yticks(rotation=0) #y 的 文字本來是橫的，但會重疊在一起，所以要轉成0度
plt.xticks(rotation=90)
plt.show()


# Create the crosstab DataFrame
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
# Plot a heatmap of the table with no color bar and using the BuGn palette
sns.heatmap(pd_crosstab, values= df['total_rentals'], aggfunc = 'mean', annot = True, fmt = 'd', cbar=True, cmap="BuGn", linewidths=0.3, center = df_crosstab.loc[9,6]) 
#value 是影響濃度深淺的值，annot是在heatmap的每一格中加入數值顯示，fmt是顯示整數，cbar是代表濃度的legend，cmap是深淺的顏色，這邊代表藍到綠，linewidth是值與值之間的寬度，center是選出想要的數值，然後會讓他比較特別一點
# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)
#Show the plot
plt.show()
plt.clf()

#相關
sns.heatmap(df.corr()) #可以求全部的相關
