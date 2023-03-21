#JointGrid可以做出詳細關係圖並在top及right side畫出分布圖，主要用在分布圖及回歸圖
# Build a JointGrid comparing humidity and total_rentals
sns.set_style("whitegrid")
g = sns.JointGrid(x="hum",
            y="total_rentals",
            data=df,
            xlim=(0.1, 1.0)) 
g.plot(sns.regplot, sns.distplot)
plt.show()
plt.clf()

# Create a jointplot similar to the JointGrid 
#jointplot是JointGrid的簡易版
sns.jointplot(x="hum",
        y="total_rentals",
        kind='reg',
        data=df)
plt.show()
plt.clf()

# Plot temp vs. total_rentals as a regression plot
sns.jointplot(x="temp",
         y="total_rentals",
         kind='reg', #回歸
         data=df,
         order=2,
         xlim=(0, 1))
plt.show()
plt.clf()

# Plot a jointplot showing the residuals
#用jointplot來看殘差分布會更為清楚
sns.jointplot(x="temp",
        y="total_rentals",
        kind='resid', #殘差
        data=df,
        order=2)

plt.show()
plt.clf()

# Replicate the previous plot but only for registered riders
g = (sns.jointplot(x="temp",
             y="registered",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True)) #marginal_kws是用來控制圖周邊的直方圖，rug是小鬚鬚圖，放在直方圖下方，True的話就可以把直方圖往上挪一點，讓rug不會擋到直方圖
    .plot_joint(sns.kdeplot))
plt.show()
plt.clf()