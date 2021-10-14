import glob, csv

files = glob.glob('regional-global-daily-*.csv')
songDict = {}
for fileName in files:
	data = open(fileName, 'r')
	data.readline()
	for line in csv.DictReader(data):
		key = f'{line["Track Name"]} by {line["Artist"]}'
		print(key)
		if key not in songDict:
			songDict[key] = {}
		date = '-'.join(fileName.split('.')[0].split('-')[3:])
		songDict[key][date] = line['Streams']
print(songDict)