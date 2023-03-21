from datetime import date
ab = [date(2016, 10, 7), date(2017, 6, 21)] #年月日
print(ab[0].year) #輸出ab裡第一個日期中的year
print(ab[0].weekday()) #可以問它那一天是星期幾，0代表禮拜一

#日期計算
import datetime import date
#Create our date
d1 = date(2017,11,5)
d2 = date(2017,12,4)
l = [d1,d2]
print(min(l))

#我們也可以直接減日期得到天數
delta = d2-d1
print(delta)

#另一種方法
from datetime import timedelta

#create a 29 day timedelta
td = timedelta(days=29)
print(d1+td)
#會輸出d1後29天的日期

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0} #設定1-12月為0的字典
# Loop over all hurricanes
for hurricane in florida_hurricane_dates: #所有florida_hurricane_dates裡的東西
  # Pull out the month
  month = hurricane.month #現在把所有這些東西的月份項存在一個名為month的變項裡
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1 #month裡對應到hurricanes_each_month 1-12月的key值的，就該項+1
print(hurricanes_each_month)
#結果:{1: 0, 2: 1, 3: 0, 4: 1, 5: 8, 6: 32, 7: 21, 8: 49, 9: 70, 10: 43, 11: 9, 12: 1}


# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])
# Put the dates in order
dates_ordered = sorted(dates_scrambled) #排序dates_scrambled
# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])


#我們也可以靈活地改變日期的樣子: strftime，預設為YYYY-MM-DD
d = date(2022, 6, 12)
print(d.strftime('Year is %Y'))
#結果會變成[Year is 2022]
print(d.strftime('%Y/%m/%d'))
#結果為[2022/06/12]


# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates) #篩選出最小值
# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat() #改為yyyy-mm-dd格式
us = "Our earliest hurricane date: " + first_date.strftime('%m/%d/%Y') #改為m/d/y
print("ISO: " + iso)
print("US: " + us)

# Import date
from datetime import date
# Create a date object
andrew = date(1992, 8, 26)
# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)')) #%B是顯示月份的全名

# Import date
from datetime import date
# Create a date object
andrew = date(1992, 8, 26)
# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j')) #%j 是顯示這天是整年裡的第幾天，這邊是第239天