w = 4
x = 3
y = 2
z = 1
while True:
    if w > x:
        w, x = x, w
        continue
    if x > y:
        x, y = y, x
        continue
    if y > z:
        y, z = z, y
        continue
    break

while w > x or x > y or y > z:
    if w > x:
        w, x = x, w
    if x > y:
        x, y = y, x
    if y > z:
        y, z = z, y

print(w, x, y, z)

# Power of 2
n = 100
i = 1
while n > i:
    i *= 2
i /= 2
print(i)

# Wind chill
print('    ', end="")
for t in range(40, -45, -5):
	print(f'{t:<4}', end="")
print()
for v in range(0, 40, 5):
	print(f'{v:<4}', end="")
	for t in range(40, -45, -5):
		w = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
		print(f'{w:<4.0f}', end="")
	print()
