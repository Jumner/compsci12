import csv
data = open('ramen-ratings.csv', 'r')

line = data.readline()
ramenDict = {}

for line in csv.reader(data):
	if line[4] not in ramenDict:
		ramenDict[line[4]] = {}
	if line[3] not in ramenDict[line[4]]:
		ramenDict[line[4]][line[3]] = []
	ramenDict[line[4]][line[3]].append([line[1],line[2],line[5]])
print(ramenDict)