w = 3
x = 4
y = 2
z = 1
while True:
	if w > x:
		temp = w
		w = x
		x = temp
		continue
	if x > y:
		temp = x
		x = y
		y = temp
		continue
	if y > z:
		temp = y
		y = z
		z = temp
		continue
	break

print(w,x,y,z)