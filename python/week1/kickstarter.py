import csv
data = open('ks-projects-201801.csv','r')
# print(data.readline())
kickstarter = {}
# for line in csv.reader(data):
# 	if line[2] not in kickstarter:
# 		kickstarter[line[2]] = []
# 	kickstarter[line[2]].append([line[9],line[11], line[4], line[1], line[5], line[6], line[7], line[8], line[10]])
for line in csv.DictReader(data):
	if line['category'] not in kickstarter:
		kickstarter[line['category']] = []
	kickstarter[line['category']].append([line['state'], line['country'], line['currency'], line['name'], line['deadline'], line['goal'], line['usd pledged'], line['backers']])
# Application:  Calculate the %successful, %failed, %cancelled for each category.  Print the results in a formatted chart to the shell.
print(kickstarter)