passwords = ['ECOO()123abcd9876', '1234512345', 'ecoo2012', 'ecoo', 'Ecoo', 'EcooEcoo123', '(TheBest?)45(45)abCD', 'Ecoo123', '39283', 'foo()', 'foobar()]']
def getStrength(password):
	score = 0
	# Length
	score += 4*len(password) 
	# Upper Case
	upper = 0
	for letter in password:
		if ord(letter) >= 65 and ord(letter) <= 90:
			upper += 1
	if upper > 0:
		score += (len(password) - upper) * 2		
	# Lower Case
	lower = 0
	for letter in password:
		if ord(letter) >= 97 and ord(letter) <= 122:
			lower += 1
	if lower > 0:
		score += (len(password) - upper) * 2
	# Digits
	digits = 0
	for letter in password:
		if ord(letter) >= 48 and ord(letter) <= 57:
			digits += 1
	if digits < len(password):
		score += 4*digits
	# Symbols
	symbols = len(password) - (upper + lower + digits)
	score += 6*symbols
	# Basic requirements
	if len(password) >= 8:
		subscore = 2
		count = 0
		if upper:
			count += 1
		if lower:
			count += 1
		if digits:
			count += 1
		if symbols:
			count += 1
		if count >= 3:
			subscore += 2*count
			score += subscore

	return score
passwords = list(map(getStrength, passwords))
print(passwords)