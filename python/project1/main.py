import csv, glob
# https://github.com/CSSEGISandData/COVID-19
data = {}

def create_datapoint(line, label, data_label, date):
	if label not in data[country]:
		data[country][label] = {}
	if data_label in line and line[data_label]:
		if date not in data[country][label]:
			data[country][label][date] = 0
		data[country][label][date] += round(float(line[data_label]))

def date_to_ymd(date):
	date_list = date.split('-')
	new_date = '-'.join([date_list[2], date_list[0], date_list[1]])
	return new_date

with open('data/country_vaccinations.csv', 'r') as file:
	for line in csv.DictReader(file):
		country = line['country']
		if country not in data:
			data[country] = {}
		create_datapoint(line, 'vaccinations', 'total_vaccinations', line['date'])
		create_datapoint(line, 'daily_vaccinations', 'daily_vaccinations', line['date'])

print('Vaccination data processed')

files = glob.glob('data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*.csv')
for file_name in files:
	with open(file_name, 'r') as file:
		for line in csv.DictReader(file):
			date = date_to_ymd(file_name.split('/')[-1].split('.')[0])
			if 'Country_Region' in line:
				country = line['Country_Region']
			elif 'Country/Region' in line:
				country = line['Country/Region']
			if country not in data:
				data[country] = {}
			create_datapoint(line, 'cases', 'Confirmed' ,date)
			create_datapoint(line, 'current_cases', 'Active', date)
			create_datapoint(line, 'deaths', 'Deaths', date)
			create_datapoint(line, 'recoveries', 'Recovered', date)
	print(f'{file_name} proccessed')
print('Case data processed')
# print(files)
# print(data['Canada']['current_cases'])
print(data)