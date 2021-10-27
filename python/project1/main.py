# Data: https://github.com/CSSEGISandData/COVID-19
import csv, glob
data = {}

def verify_region(line): # Find the region of the data and make sure it exists
	if 'Province' in line: # Look by province
		region = line['Province']
	elif 'Country_Region' in line: # Otherwise look by country
		region = line['Country_Region']
	elif 'Country/Region' in line: # Sometimes it uses this key 🤷
		region = line['Country/Region']
	if region not in data: # Check if region exists in data structure
		data[region] = {} # Make sure it exists
	return region # Return the region

def create_datapoint(line, label, data_label, date): # Create the datapoint
	region = verify_region(line) # Grab the region
	if data_label in line and line[data_label]: # If line has data and data exists
		if label not in data[region]: # Check if the label exists for that region
			data[region][label] = [] # Make sure it exists
		data[region][label].append((date, round(float(line[data_label])))) # Append the value to it

files = glob.glob('data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*.csv') # I love glob
# files = glob.glob('data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*1-2020.csv') # for testing
# Grab all needed files
for file_name in files: # Iterate through files
	with open(file_name, 'r') as file: # Open date file
		date = file_name.split('/')[-1].split('.')[0] # Get date (Each file is one day) Also regex would be really nice here
		for line in csv.DictReader(file): # Iterate through file
			create_datapoint(line, 'cases', 'Confirmed' ,date) # Create datapoints
			create_datapoint(line, 'current_cases', 'Active', date)
			create_datapoint(line, 'deaths', 'Deaths', date)
			create_datapoint(line, 'recoveries', 'Recovered', date)
	print(f'{file_name} proccessed') # This file is done
print('Case data processed') # All files done

# print(data['Canada']['current_cases']) # Just so you see better how it works
print(data) # Print it out
for region in data: # Print out all the regions
	print(region)