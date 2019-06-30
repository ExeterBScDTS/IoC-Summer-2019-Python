import json
from datetime import datetime


data = json.load(open('sample.json'))

currently = data['currently']

print(datetime.fromtimestamp(currently['time']))
print(currently['summary'], str(currently['temperature'])+'C')

input("more Y/N ?")

hourly = data['hourly']['data']

for hour in hourly:
       print(datetime.fromtimestamp(hour['time']), end = "  ")
       print(hour['summary'], str(hour['temperature'])+'C')


