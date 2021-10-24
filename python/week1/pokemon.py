data = open('Pokemon.csv', 'r')
# data.readline() 
# for line in data:
# 	print(line)
line = data.readline()
pokidict = {}
for line in data:
	line = line.split(',')
	if line[2] not in pokidict:
		pokidict[line[2]] = []
	pokidict[line[2]].append([line[1],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]])
print(pokidict)