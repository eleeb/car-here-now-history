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

# Create another set empty lists for each day of the week for holding just Jackson Heights related information
Monday_JH = []
Tuesday_JH = []
Wednesday_JH = []
Thursday_JH = []
Friday_JH = []
Saturday_JH = []
Sunday_JH = []

# Create variable for parsed parking data file
filename = 'parking_data_parsed.json'

# Open parsed parking data file
with open(filename, 'r') as jsonfile:
    data = json.load(jsonfile)

    # Loop through parsed parking data
    for instance in data:
           
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
        
        # Weed out all parking instances that are not in current neighborhood (Jackson Heights)
        if instance['neighborhood'] == 'Jackson Heights':
            
            # Match data for specific days of the week and then add to corresponding weekday lists
            if instance['weekday'] == 'Monday':
                Monday_JH.append(instance)
            
            if instance['weekday'] == 'Tuesday':
                Tuesday_JH.append(instance)
            
            if instance['weekday'] == 'Wednesday':
                Wednesday_JH.append(instance)
            
            if instance['weekday'] == 'Thursday':
                Thursday_JH.append(instance)

            if instance['weekday'] == 'Friday':
                Friday_JH.append(instance)
            
            if instance['weekday'] == 'Saturday':
                Saturday_JH.append(instance)

            if instance['weekday'] == 'Sunday':
                Sunday_JH.append(instance)
        
# # Pretty print out a few lists to make sure the data is flowing to the right lists
# pprint(Monday)
# print('--------------------------------')
# pprint(Wednesday)
# print('--------------------------------')
# pprint(Saturday)
# print('--------------------------------')
# pprint(Monday_JH)
# print('--------------------------------')
# pprint(Wednesday_JH)
# print('--------------------------------')
# pprint(Saturday_JH)

# Write out the data in the day of the week lists to csvs and save in parking_by_day folder in project repo
with open ('parking_by_day/parks_mon.csv', 'w', encoding='utf8', newline='') as output_mon:
    fc = csv.DictWriter(output_mon, fieldnames=Monday[0].keys())
    fc.writeheader()
    fc.writerows(Monday)

with open ('parking_by_day/parks_tues.csv', 'w', encoding='utf8', newline='') as output_tues:
    fc = csv.DictWriter(output_tues, fieldnames=Tuesday[0].keys())
    fc.writeheader()
    fc.writerows(Tuesday)

with open ('parking_by_day/parks_wed.csv', 'w', encoding='utf8', newline='') as output_wed:
    fc = csv.DictWriter(output_wed, fieldnames=Wednesday[0].keys())
    fc.writeheader()
    fc.writerows(Wednesday)

with open ('parking_by_day/parks_thurs.csv', 'w', encoding='utf8', newline='') as output_thurs:
    fc = csv.DictWriter(output_thurs, fieldnames=Thursday[0].keys())
    fc.writeheader()
    fc.writerows(Thursday)

with open ('parking_by_day/parks_fri.csv', 'w', encoding='utf8', newline='') as output_fri:
    fc = csv.DictWriter(output_fri, fieldnames=Friday[0].keys())
    fc.writeheader()
    fc.writerows(Friday)

with open ('parking_by_day/parks_sat.csv', 'w', encoding='utf8', newline='') as output_sat:
    fc = csv.DictWriter(output_sat, fieldnames=Saturday[0].keys())
    fc.writeheader()
    fc.writerows(Saturday)

with open ('parking_by_day/parks_sun.csv', 'w', encoding='utf8', newline='') as output_sun:
    fc = csv.DictWriter(output_sun, fieldnames=Sunday[0].keys())
    fc.writeheader()
    fc.writerows(Sunday)

with open ('parking_by_day/parks_mon_JH.csv', 'w', encoding='utf8', newline='') as output_mon_JH:
    fc = csv.DictWriter(output_mon_JH, fieldnames=Monday_JH[0].keys())
    fc.writeheader()
    fc.writerows(Monday_JH)

with open ('parking_by_day/parks_tues_JH.csv', 'w', encoding='utf8', newline='') as output_tues_JH:
    fc = csv.DictWriter(output_tues_JH, fieldnames=Tuesday_JH[0].keys())
    fc.writeheader()
    fc.writerows(Tuesday_JH)

with open ('parking_by_day/parks_wed_JH.csv', 'w', encoding='utf8', newline='') as output_wed_JH:
    fc = csv.DictWriter(output_wed_JH, fieldnames=Wednesday_JH[0].keys())
    fc.writeheader()
    fc.writerows(Wednesday_JH)

with open ('parking_by_day/parks_thurs_JH.csv', 'w', encoding='utf8', newline='') as output_thurs_JH:
    fc = csv.DictWriter(output_thurs_JH, fieldnames=Thursday_JH[0].keys())
    fc.writeheader()
    fc.writerows(Thursday_JH)

with open ('parking_by_day/parks_fri_JH.csv', 'w', encoding='utf8', newline='') as output_fri_JH:
    fc = csv.DictWriter(output_fri_JH, fieldnames=Friday_JH[0].keys())
    fc.writeheader()
    fc.writerows(Friday_JH)

with open ('parking_by_day/parks_sat_JH.csv', 'w', encoding='utf8', newline='') as output_sat_JH:
    fc = csv.DictWriter(output_sat_JH, fieldnames=Saturday_JH[0].keys())
    fc.writeheader()
    fc.writerows(Saturday_JH)

with open ('parking_by_day/parks_sun_JH.csv', 'w', encoding='utf8', newline='') as output_sun_JH:
    fc = csv.DictWriter(output_sun_JH, fieldnames=Sunday_JH[0].keys())
    fc.writeheader()
    fc.writerows(Sunday_JH)

# Check to make sure that the length is correct (should add up to 347)
total_records = len(Monday) + len(Tuesday) + len(Wednesday) + len(Thursday) + len(Friday) + len(Saturday) + len(Sunday)
if total_records == 347:
      print('Hooray, your program worked correctly!')
else:
  print('Houston, we have a problem :(')

print ('------------------------------------------------------')
print ('------------------------------------------------------')


# Print the number of parking entries for each day of the week
print('Monday parking entries: ', len(Monday))
print('Tuesday parking entries: ', len(Tuesday))
print('Wednesday parking entries: ', len(Wednesday))
print('Thursday parking entries: ', len(Thursday))
print('Friday parking entries: ', len(Friday))
print('Saturday parking entries: ', len(Saturday))
print('Sunday parking entries: ', len(Sunday))
print('---------------------------')
print('Total parking entries: ', total_records)

print ('------------------------------------------------------')
print ('------------------------------------------------------')

# Print the number of Jackson Heights parking entries for each day of the week
print('Monday JH parking entries: ', len(Monday_JH))
print('Tuesday JH parking entries: ', len(Tuesday_JH))
print('Wednesday JH parking entries: ', len(Wednesday_JH))
print('Thursday JH parking entries: ', len(Thursday_JH))
print('Friday JH parking entries: ', len(Friday_JH))
print('Saturday JH parking entries: ', len(Saturday_JH))
print('Sunday JH parking entries: ', len(Sunday_JH))

# Add up each days' entries and print out the total of times parked in Jackson Heights
total_JH_records = len(Monday_JH) + len(Tuesday_JH) + len(Wednesday_JH) + len(Thursday_JH) + len(Friday_JH) + len(Saturday_JH) + len(Sunday_JH)
print('---------------------------')
print('Total JH parking entries: ', total_JH_records)