data = open('uni.txt','r')
parsedData = []
for line in data:
	seg = line.split(':')
	uniRough = seg[0].split(',  ')
	uni = []
	for item in uniRough:
		uni.append(item.strip())
	for program in seg[1].split(','):
		final = uni + [program.strip()]
		parsedData.append(final)
		print(final)