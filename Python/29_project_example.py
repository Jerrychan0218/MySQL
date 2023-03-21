# Loading in required libraries
# ... YOUR CODE FOR TASK 1 ...
import pandas as pd
import seaborn as sns
import numpy as np
# Reading in the Nobel Prize data
nobel = pd.read_csv('datasets/nobel.csv')
# Taking a look at the first several winners
nobel.head(n = 6)
# Display the number of (possibly shared) Nobel Prizes handed
# out between 1901 and 2016
# ... YOUR CODE FOR TASK 2 ...
display(len(nobel['prize']))
# Display the number of prizes won by male and female recipients.
# ... YOUR CODE FOR TASK 2 ...
display(nobel['sex'].value_counts())
# Display the number of prizes won by the top 10 nationalities.
# ... YOUR CODE FOR TASK 2 ...
nobel['birth_country'].value_counts().head(10)
# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (np.floor(nobel['year']/10)*10).astype(int) #np.floor是向下整取，即2.5 = 2, 3.2 = 3 
prop_usa_winners = nobel.groupby('decade', as_index = False)['usa_born_winner'].mean()
# Display the proportions of USA born winners per decade
display(prop_ysa_winners)

# Setting the plotting theme
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7] #圖片像素

# Plotting USA born winners 
ax = sns.lineplot(data = nobel, x = 'decade', y = 'usa_born_winner')

# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
import matplotlib.ticker as mtick
# ... YOUR CODE FOR TASK 4 ...
ax.yaxis.set_major_formatter(mtick.PercentFormatter()) #把y軸變成%呈現

# Picking out the first woman to win a Nobel Prize
nobel[nobel.sex == 'Female'].nsmallest(1, 'year') #nsmallest(print出幾個值，哪個column)

# Selecting the laureates that have received 2 or more prizes.
nobel.groupby('full_name').filter(lambda x: len(x) >= 2)

# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date']) 

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year # nobel['birth_date'].dt.year 讓python讀到日期中的年分

# Plotting the age of Nobel Prize winners
sns.lmplot(data = nobel, x = 'year', y = 'age', lowess=True, aspect = 2, line_kws={'color' : 'black'}) #lowess是平滑化，aspect是把圖伸縮讓每個點可以呈現的清楚一點，line_kws是針對線進行調整

# Same plot as above, but separate plots for each type of Nobel Prize
sns.lmplot(data = nobel, x = 'year', y = 'age', row = 'category') # 根據category中的內容來分別呈現x = year, y = age的圖們

# The oldest winner of a Nobel Prize as of 2016
# ... YOUR CODE FOR TASK 10 ...
display(nobel.nlargest(1, 'age'))

# The youngest winner of a Nobel Prize as of 2016
# ... YOUR CODE FOR TASK 10 ...
nobel.nsmallest(1, 'age')
