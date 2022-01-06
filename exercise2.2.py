#Exercise 2.2
#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
print ('Exercise 2.2')
start_time_hr = 6 + 52 / 60.0
easy_pace_hr = (8 + 15 / 60.0 ) / 60.0
tempo_pace_hr = (7 + 12 / 60.0) / 60.0
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60

print ('breakfast_hr', int(breakfast_hr) )
print ('breakfast_min', int (breakfast_min) )
print ('breakfast_sec', int (breakfast_sec) )
