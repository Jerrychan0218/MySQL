from datetime import datetime, timedelta, timezone

ET = timezone(timedelta(hours=-5)) #時區
dt = datatime(2017,12,30,15,9,3, tzinfo = ET) #tzinfo也可以直接set做timezone.utc
print(dt)

#也可以
ist = timezone(timedelta(hours=5,minutes=30))
print(dt.astimezone(ist)) #直接套用這個時區的資訊，也可以用timezone.utc來代替ist得到英國標準時間

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours = -4))
# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = edt)
  trip['end'] = trip['end'].replace(tzinfo = edt)


# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start
  dt = trip['start']
  # Move dt to be in UTC
  dt = dt.astimezone(timezone.utc)
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())

#** 有一個時區的database tz
from datetime import datetime
from dateutil import tz #每年會更新3-4次
et = tz.gettz('America/New_York') #gettz 大洲/城市，America/New_York、America/Mexico_City
last = datetime(2017,2,18 12, 45, 10, tzinfo = et) #這樣datatime就會根據時區的數據庫來進行調整


# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))

trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])
  # Convert to UTC
  start = trip['start'].astimezone()
  end = trip['end'].astimezone()
  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)
# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))