# Import modules
import json
from pprint import pprint
from datetime import datetime
import csv

# Create empty lists to sort pre and post covid timestamps as well as full entries for pre and post covid
pre_covid_timestamps = []
post_covid_timestamps = []
pre_covid = []
post_covid = []

# Create variable for parsed parking data file
filename = 'parking_data_parsed.json'

# Open parsed parking data file
with open(filename, 'r') as jsonfile:
  data = json.load(jsonfile)

  # Sort entries into 2 lists based on pre-and post-covid
  for instance in data:
    if instance['timestamp'] < "2020-03-16 00:00:00":
      pre_covid_timestamps.append(instance['timestamp'])
      pre_covid.append(instance)
    else:
      post_covid_timestamps.append(instance['timestamp'])
      post_covid.append(instance)

# Write out the pre and post covid parking data to csvs and save in parking_covid folder in project repo
with open ('parking_covid/pre_covid_parks.csv', 'w', encoding='utf8', newline='') as output_pre:
    fc = csv.DictWriter(output_pre, fieldnames=pre_covid[0].keys())
    fc.writeheader()
    fc.writerows(pre_covid)

with open ('parking_covid/post_covid_parks.csv', 'w', encoding='utf8', newline='') as output_post:
    fc = csv.DictWriter(output_post, fieldnames=post_covid[0].keys())
    fc.writeheader()
    fc.writerows(post_covid)

# Use datetime module to figure out timespans for app use pre and post COVID
list_of_pre = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in pre_covid_timestamps]
list_of_post = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in post_covid_timestamps]

# Determine earliest and newest parking dates pre-COVID
newest_pre = max(list_of_pre)
oldest_pre = min(list_of_pre)

# Determine earliest and most recent parking dates post-COVID
newest_post = max(list_of_post)
oldest_post = min(list_of_post)

# Subtract most recent timestamps from oldest timestamps
pre_days = newest_pre - oldest_pre
post_days = newest_post - oldest_post

# Define span of days using the app pre and post-COVID
pre_covid_timespan = pre_days.days
post_covid_timespan = post_days.days

# Define total number of parks
total_pre_parks = len(pre_covid)
total_post_parks = len(post_covid)

# Do math to determine average parks per week pre and post-COVID, round to 1 decimal point
pre_weekly_avg = round((total_pre_parks / pre_covid_timespan) * 7, 1)
post_weekly_avg = round((total_post_parks / post_covid_timespan) * 7, 1)
print ('Average parks per week pre-COVID: ', pre_weekly_avg)
print ('Average parks per week post-COVID: ', post_weekly_avg)

# Determine percent decrease in weekly parking average, and round to nearest whole number
prcnt_decrease = round(((pre_weekly_avg - post_weekly_avg) / abs(pre_weekly_avg)) * 100)
print('On average, we parked ',prcnt_decrease, 'percent less during COVID.')