import csv, glob
# https://github.com/CSSEGISandData/COVID-19
data = {}

def verify_country(line): # Find the country of the data and make sure it exists
	if 'Country_Region' in line: # Found in the case dataset
		country = line['Country_Region']
	elif 'Country/Region' in line: # Found in the case dataset
		country = line['Country/Region']
	elif 'country' in line: # Found in the vaccination dataset
		country = line['country']
	if country not in data: # Check if country exists in data structure
		data[country] = {} # Make sure it exists
	return country # Return the country

def create_datapoint(line, label, data_label, date): # Create the datapoint
	country = verify_country(line) # Grab the country
	if data_label in line and line[data_label]: # If line has data and data exists
		if label not in data[country]: # Check if the label exists for that country
			data[country][label] = {} # Make sure it exists
		if date not in data[country][label]: # If date doesn't exist in this label
			data[country][label][date] = 0 # Set it to 0
		data[country][label][date] += round(float(line[data_label])) # Add the value to it
		# This line just makes sure that different regions of the same country are summed

print('Vaccination data processed') # This file is done

files = glob.glob('data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*.csv')
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

# print(data['Canada']['current_cases'])
print(data) # Print it out