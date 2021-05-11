# Import modules
import json
import re
from datetime import datetime
from pprint import pprint
from geopy.geocoders import Nominatim

# Start an empty list to hold the parking instances data
parking_data = []

# Regex pattern for parsing parking instance details (lat, long, and name of the person who parked)
details_pattern = re.compile(r"(\D*[0-9]+\.[0-9]+)\,\s(\D*[0-9]+\.[0-9]+)\,*\s*(\w*)")

# Open up json export and load it as a json string (Tried the 'with open()' method and it never worked)
# (don't know why it works this way and not others, but this is the only way I could parse through it)
output_file = open('cardata_export_raw.json').read()
output_json = json.loads(output_file)

# Loop through keys and values of JSON file to parse data
for key, value in output_json.items():

  # Create new empty dictionary to hold parsed info
  instance = {
    'timestamp': None,
    'weekday' : None,
    'month' : None,
    'day' : None,
    'year' : None,
    'time' : None,
    'parker' : None,
    'lat' : None,
    'long' : None,
  }

  # Normalize inconsistencies in the timestamps and add to dictionary
  # via https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
  clean_timestamp = datetime.strptime(key, "%Y-%m-%d %H:%M:%S")
  instance['timestamp'] = clean_timestamp.strftime("%Y-%m-%d %H:%M:%S")

  # Add weekday, date, and time to dictionary in human-friendly form
  instance['weekday'] = clean_timestamp.strftime("%A")
  instance['month'] = clean_timestamp.strftime("%B")
  instance['day'] = clean_timestamp.strftime("%d")
  instance['year'] = clean_timestamp.strftime("%Y")
  instance['time'] = clean_timestamp.strftime("%I:%M %p")

  # Use regex pattern to iterate through values of JSON file
  details_results = details_pattern.search(value)

  # Give variable names to the 3 different groups of matches 
  latitude = details_results.group(1)
  longitude = details_results.group(2)
  parker = details_results.group(3)

  # Add geo coordinates to dictionary
  instance['lat'] = longitude
  instance['long'] = latitude

  # Get address based on lat & long coordinates via https://www.geeksforgeeks.org/how-to-get-geolocation-in-python/
  # and also via https://www.geeksforgeeks.org/get-the-city-state-and-country-names-from-latitude-and-longitude-using-python/
  # Call the Nominatim tool
  geolocator = Nominatim(user_agent="GetLoc")

  # Passing the coordinates
  location = geolocator.reverse(latitude+","+longitude)

  # Get location info parsed into a new dictionary with raw function
  address = location.raw['address']

  # # Check out what data is contained in address dictionary
  # print(address)
  # print('----------------------')

  # Traverse the data, add pertinent info to instance dictionary
  instance['address_no'] = address.get('house_number', '')
  instance['street_name'] = address.get('road', '')
  
  # Workaround to deal with the weird JH addresses that are listed as "The Greystones"
  if address.get('residential', '') == 'The Greystones':
    instance['neighborhood'] = 'Jackson Heights'
  else:
    instance['neighborhood'] = address.get('neighbourhood', '')
  
  instance['borough'] = address.get('suburb', '')
  instance['city'] = address.get('city', '')
  instance['state'] = address.get('state', '')
  instance['zipcode'] = address.get('postcode')
  instance['country'] = address.get('country', '')

  # Add names of parkers to instance dictionary
  # Change EEE codename to Erin
  if parker == 'EEE':
    instance['parker'] = 'Erin'
  
  # Change SSS codename to Steve
  elif parker == 'SSS':
    instance['parker'] = 'Steve'

  # Change blank parker entries to Erin (caused by an old, now fixed, glitch in parking app)
  else:
    instance['parker'] = 'Erin'

  # Append parking_data list with instance dictionary
  parking_data.append(instance)

# # Pretty print list to check and make sure everything parsed correctly
# pprint(parking_data)

# Count number of entries in the car parking data and check to make sure it's 347. If not, display an error msg.
if len(parking_data) == 347:
  print('Hooray, your program worked correctly!')
else:
  print('Houston, we have a problem :(')
       
# LEAVE THIS COMMENTED OUT UNTIL READY TO WRITE OUT LIST TO A NEW JSON FILE
with open('parking_data_parsed.json', 'w') as out:
    json.dump(parking_data,out,indent=2)