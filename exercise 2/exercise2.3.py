#Exercise 2.3
#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
print ("exercise 3")
time = (6*3600)+(52*60) 
Easy_pace = (8*60+15)*2 
Tempo = (7*60+12)*3 
total_time = time + Easy_pace + Tempo
hour = total_time // 3600
hour_du = total_time % 3600 
minute = hour_du // 60
minute_du = hour_du % 60 
second = minute_du % 60
print ("I get home for breakfast at",hour,":",minute,":",second)