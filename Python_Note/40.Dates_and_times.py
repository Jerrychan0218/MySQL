from datetime import datetime
dt = datetime(2017,10,1,15,23,25) #代表 2017-10-1 3:23:25 p.m. ，也可在25後面再加入500000代表毫秒 -> 20177-10-1 3:23:25.500000 pm

#我們也可以用replace function 取代原有時間
dt_hr = dt.replace(year = 0, month = 0, day = 0, hour =0, minute = 0, second = 0, microsecond = 0)
print(dt_hr)

#onebike_datetimes裡面是一大堆start: datetime.datetime(年月日時)的資料，我們想知道有多少是比中午要早，有哪些是比中午要晚的
# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
print(onebike_datetimes)  
# Loop over all trips
for trip in onebike_datetimes: #trip是指onebike_datetimes裡的所有資料
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12: #所以trip['start']就是指onebike_datetimes裡所有['start']的資料
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1 
print(trip_counts)

from datetime import datetime
dt = datetime.strptime('12/30/2017 15:19:13', '%m/%d/%Y %H:%M:%S') #把字串換成時間

#Unix時間
# 電腦很長預設時間是從1970-1-1到目前的秒數，因為1970是電腦誕生地時間
ts = 1514665153.0 #這是從1970到2017-12-30 15:19:13的秒數
print(datetime.fromtimestamp(ts)) #print出現在地時間

#把資料全部從string改成時間
# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"
# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []
# Loop over all trips
for (start, end) in onebike_datetime_strings:
    trip = {'start': datetime.strptime(start, fmt),
          'end': datetime.strptime(end, fmt)}
# Append the trip
    onebike_datetimes.append(trip)

#把資料都從秒數變為日期
# Import datetime
from datetime import datetime
# Starting timestamps
timestamps = [1514665153, 1514664543]
# Datetime objects
dts = []
# Loop
for ts in timestamps:
    dts.append(datetime.fromtimestamp(ts))  
# Print results
print(dts)

