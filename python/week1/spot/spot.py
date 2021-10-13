import glob, csv

files = glob.glob('regional-global-daily-*.csv')
songDict = {}

def getKey(line):
	result = ""
	result += line['Track Name']
	result += ' by '
	result += line['Artist']
	return result

for fileName in files:
	data = open(fileName, 'r')
	data.readline()
	for line in csv.DictReader(data):
		key = getKey(line)
		if key not in songDict:
			songDict[key] = {}
		date = '-'.join(fileName.split('.')[0].split('-')[3:])
		songDict[key][date] = line['Streams']
print(songDict)