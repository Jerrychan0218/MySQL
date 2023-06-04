from datetime import timedelta
a.total_seconds() #把a變成秒數
delta1 = timedelta(days=1, seconds = 1) #也可以是weeks、months、years，數值也可以是負值

# Initialize a list for all the trip durations
onebike_durations = []
for trip in onebike_datetimes:
  # Create a timedelta object corresponding to the length of the trip
  trip_duration = trip['end'] - trip['start'] 
  # Get the total elapsed seconds in trip_duration
  trip_length_seconds = trip_duration.total_seconds() 
  # Append the results to our list
  onebike_durations.append(trip_length_seconds)

