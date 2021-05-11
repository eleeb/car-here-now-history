import json
import csv
from pprint import pprint

# Create empty lists for each day of the week, to hold all parking instances on that day
Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []
Saturday = []
Sunday = []

# Create variable for parsed parking data file
filename = 'parking_data_parsed.json'

# Open parsed parking data file
with open(filename, 'r') as jsonfile:
    data = json.load(jsonfile)

    # Loop through parsed parking data
    for instance in data:
        
        # Weed out all parking instances that are not in current neighborhood (Jackson Heights)
        if instance['neighborhood'] == 'Jackson Heights':
            
            # Match data for specific days of the week and then add to corresponding weekday lists
            if instance['weekday'] == 'Monday':
                Monday.append(instance)
            
            if instance['weekday'] == 'Tuesday':
                Tuesday.append(instance)
            
            if instance['weekday'] == 'Wednesday':
                Wednesday.append(instance)
            
            if instance['weekday'] == 'Thursday':
                Thursday.append(instance)

            if instance['weekday'] == 'Friday':
                Friday.append(instance)
            
            if instance['weekday'] == 'Saturday':
                Saturday.append(instance)

            if instance['weekday'] == 'Sunday':
                Sunday.append(instance)

# # Pretty print out a few lists to make sure the data is flowing to the right lists
# pprint(Monday)
# print('--------------------------------')
# pprint(Wednesday)
# print('--------------------------------')
# pprint(Saturday)

# Write out the data in the day of the week lists to csvs and save in parking_by_day folder in project repo
# JH at end of csv filename means its only records in Jackson Heights
with open ('parking_by_day/parks_mon_JH.csv', 'w', encoding='utf8', newline='') as output_mon:
    fc = csv.DictWriter(output_mon, fieldnames=Monday[0].keys())
    fc.writeheader()
    fc.writerows(Monday)

with open ('parking_by_day/parks_tues_JH.csv', 'w', encoding='utf8', newline='') as output_tues:
    fc = csv.DictWriter(output_tues, fieldnames=Tuesday[0].keys())
    fc.writeheader()
    fc.writerows(Tuesday)

with open ('parking_by_day/parks_wed_JH.csv', 'w', encoding='utf8', newline='') as output_wed:
    fc = csv.DictWriter(output_wed, fieldnames=Wednesday[0].keys())
    fc.writeheader()
    fc.writerows(Wednesday)

with open ('parking_by_day/parks_thurs_JH.csv', 'w', encoding='utf8', newline='') as output_thurs:
    fc = csv.DictWriter(output_thurs, fieldnames=Thursday[0].keys())
    fc.writeheader()
    fc.writerows(Thursday)

with open ('parking_by_day/parks_fri_JH.csv', 'w', encoding='utf8', newline='') as output_fri:
    fc = csv.DictWriter(output_fri, fieldnames=Friday[0].keys())
    fc.writeheader()
    fc.writerows(Friday)

with open ('parking_by_day/parks_sat_JH.csv', 'w', encoding='utf8', newline='') as output_sat:
    fc = csv.DictWriter(output_sat, fieldnames=Saturday[0].keys())
    fc.writeheader()
    fc.writerows(Saturday)

with open ('parking_by_day/parks_sun_JH.csv', 'w', encoding='utf8', newline='') as output_sun:
    fc = csv.DictWriter(output_sun, fieldnames=Sunday[0].keys())
    fc.writeheader()
    fc.writerows(Sunday)

# Print the number of Jackson Heights parking entries for each day of the week
print('Monday JH parking entries: ', len(Monday))
print('Tuesday JH parking entries: ', len(Tuesday))
print('Wednesday JH parking entries: ', len(Wednesday))
print('Thursday JH parking entries: ', len(Thursday))
print('Friday JH parking entries: ', len(Friday))
print('Saturday JH parking entries: ', len(Saturday))
print('Sunday JH parking entries: ', len(Sunday))

# Add up each days' entries and print out the total of times parked in Jackson Heights
total_JH_records = len(Monday) + len(Tuesday) + len(Wednesday) + len(Thursday) + len(Friday) + len(Saturday) + len(Sunday)
print('---------------------------')
print('Total JH parking entries: ', total_JH_records)

# # This is from when I sorted ONLY by day of week, and didn't weed out records based on neighorhood. Might be useful in future?
# # Check to make sure that the length is correct (should add up to 347)
# total_records = len(Monday) + len(Tuesday) + len(Wednesday) + len(Thursday) + len(Friday) + len(Saturday) + len(Sunday)
# if total_records == 347:
#       print('Hooray, your program worked correctly!')
# else:
#   print('Houston, we have a problem :(')