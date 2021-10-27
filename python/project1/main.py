# Data: https://github.com/CSSEGISandData/COVID-19
import csv, glob
data = {}

def check_key(line, key):
	return key in line and len(line[key]) > 0


def verify_region(line): # Find the region of the data and make sure it exists
	if check_key(line, 'Province'): # Look by province
		region = line['Province']
	elif check_key(line, 'Province_State'):
		region = line['Province_State']
	elif check_key(line, 'Country_Region'): # Otherwise look by country
		region = line['Country_Region']
	elif check_key(line, 'Country/Region'): # Sometimes it uses this key 🤷
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
# files = glob.glob('data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*1-2020.csv') # for fewer files for testing
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

print(data['Ontario']) # Print out whats in ontario
print('\n\n')
print(data['Ontario']['cases']) # Then print out whats in ontarios cases
print('\n\n')
print(data['Ontario']['cases'][0]) # Then print the first data point

# for region in data: # Print out all the different regions
# 	print(region)