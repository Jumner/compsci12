import csv
students = []
with open('test1.txt', 'r') as data:
	reader = csv.reader(data)
	for line in reader:
		students.append([line[0], line[1], []])

with open('test2.txt', 'r') as data:
	course = ""
	for line in data:
		if ',' not in line:
			course = line.strip()
		else:
			line = line.split(',')
			for student in students:
				if student[0] == line[0].strip():
					student[2].append(line[1].strip())
print(students)