# _Car Here Now_ history
This is final project for the course INFO-664: [*Programming for Cultural Heritage*](http://pfch.nyc/ "Programming for Cultural Heritage") taught by [Matt Miller](https://github.com/thisismattmiller "Matt Miller"), which I took as a non-matriculating student while employed at the Pratt Institute School of Information in Spring 2021.

## Project Overview
The goal of the project was to analyze all of the data my partner and I collected over roughly the past year and a half on when and where we’ve parked our car. We have been tracking this information via a mobile parking app that we created called _Car Here Now_.

While it would have been ideal to work with the data in realtime, for the purposes of this project I downloaded a JSON export on May 8, 2021 of all of our parking data to work with.

### Project Steps
In order to traverse the data, I began by writing a program in Python to parse the raw information in the JSON file and make it easier to work with (`cardata_parse.py`). The geographic coordinates were stored in one string along with a code that indicated who parked the car, so I first split up those pieces of information. For clarity, I changed the parker IDs to our first names. There were also some entries missing IDs from a glitch in a previous version of the app, but we knew they all belonged to me so I added my name to those entries as well. I then utilized a few Python modules to determine the day of the week for each entry and to get more location information based on the latitude and longitude of each parking instance (e.g., street address, neighborhood, city, etc.). Finally, I wrote this out out to a new JSON file. 

Now that I had a clean new JSON file to work with, I wrote a second program in Python to explore our parking habits by days of the week (`parking_by_day.py`). I first sorted all of the the entries into 7 lists based on the days of the week. Since we moved about 9 months ago, I also wanted to just look at parking habits in my current neighborhood, as that is what I am currently most interested in. I weeded out all entries that weren’t in my current neighborhood and sorted those results into 7 more lists based on days of the week. I exported all 14 of these lists as separate CSV files (to be uploaded to Google My Maps\*). I also did counts to see what the numbers of parking entires were like based on days of the week (both in my current neighborhood and throughout our history using _Car Here Now_). Unsurprisingly, I learned that we park most often on weekends.

I was also interested in seeing our parking habits from before the COVID-19 pandemic and how those compared to our current parking habits, so I wrote a third program in Python (`parking_covid.py`). I separated all of our parking entries by pre- and post-COVID. I chose March 15, 2020 as the cutoff date for pre-COVID entries as the next day is when NYC schools closed and I transitioned to 100% remote work. I used the datetime Python module to figure out the oldest entry in our database (August 20, 2019) and calculate the total number of days we used _Car Here Now_ to track our parking both pre-COVID (206 days) and post-COVID (417 days). With this information, I could then use simple operations to determine the average number of times we parked per week pre-COVID (4.8) and post-COVID (3.4) as well the percentage decrease in parking since the start of the pandemic (29% less). 

## How to make the code work
In order to to run the programs in this repo, you will need a copy of the JSON export of my raw parking data (`cardata_export_raw.json`). For privacy reasons, this is not available on my public repo. Please reach out for access to this file.

Once you have access the file:
1. First, run the `cardata_parse.py` program to parse the data. This will create a new file called `parking_data_parsed.json`
2. In order to run the other 2 programs, you'll first need to create 2 new directories in your project folder: `parking_by_day` and `parking_covid`. These will hold the CSVs that will be created when you run the corresponding programs.
3. Now that you have the new parsed JSON file and have created these directories, you'll be able to run the other 2 programs: `parking_by_day.py` and `parking_covid.py`

**\*Note:** You may notice there is also directory titled `parker_icons` which contains 14 PNG files. These are custom icons I created to use in the 2 maps I created using Google My Maps (1 contains all the parking data separated by day, the other which only contains data on my current neighborhood by day). For privacy reasons, the URLs to these maps are not available publicly. Please reach out if you are interested in viewing them.
