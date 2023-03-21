import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.65] + pop
plt.plot(year, pop) # x先, y後 plot = 線
#plt.scatter(year, pop) #scatter = 點
# values = [0,0,0,0,0,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5]
# plt.hist(values, bins = 3)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],
           ['0','20','40','60','80','100']) #替代
plt.show()


