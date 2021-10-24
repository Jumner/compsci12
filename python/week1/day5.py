# Q1
import random,math
testDict = {}
for i in range(10):
	testDict[i] = 0
for i in range(1000):
	num = math.floor(random.random()*10)
	testDict[num] += 1
print('Random number frequencies')
for i in range(10):
	print(f'num {i+1:>2}, chosen {testDict[i]*100/1000:>3.0f}% time')
# Q2
# A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number to store it in the form of a  tuple of ( y , m , d ).
# The function will accept a date in the "dd-MMM-yy" format and returns the  tuple of ( y , m , d ).

# Create a dictsuitable for decoding month names to numbers. 
# Create a function which uses string operations to split the date into 3 items using the "-" character. 
# HINT ... str.split("-") will split a string based on the - 
# Translate the month, correct the year to include all 4 of the digits
# monthDict = {
#     'JAN': 1,
#     'FEB': 2,
#     'MAR': 3,
#     'APR': 4,
#     'MAY': 5,
#     'JUN': 6,
#     'JUL': 7,
#     'AUG': 8,
#     'SEP': 9,
#     'OCT': 10,
#     'NOV': 11,
#     'DEC': 12
# }
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
monthDict = {}
for i in range(len(months)):
	monthDict[months[i]] = i+1
date = '8-MAR-85'
date = date.split('-')
day = int(date[0])
mon = monthDict[date[1]]
ann = int(date[2])
if ann < 100:
	if ann > 21:
		ann += 1900
	else:
		ann += 2000
date = (day, mon, ann)
print(date)
# Q 3
# Create a dictionary dynamically that can be used as a ROT13 or other substitution cipher.
# Revisit the question from Strings and Lists Review and rewrite it to create the unique dictionary before you encode a message. By creating the dictionary first you don't have to perform the calculations on each letter of the message during encoding, you can just use the dictionary.

# Example / 
# letterMap = {'c':'j', 'h':'o', 'e':'l'     etc}
# print letterMap['e']   #will print l to the screen
import string
letters = string.ascii_lowercase
letterMap = {}
rot = 1
for i in range(len(letters)):
	letterMap[letters[i]] = letters[(i+rot) % len(letters)]
print(letterMap)

# Q 4
morse = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--..", "0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", "." : ".-.-.-", "," : "--..--"," " : " "}
reverse = {} # Reverse the dict
for key in morse:
	reverse[morse[key]] = key
morse = reverse
morseCode = '.... ..- -- .--. - -.--   -.. ..- -- .--. - -.--   ... .- -   --- -.   .-   .-- .- .-.. .-.. .-.-.- .... ..- -- .--. - -.--   -.. ..- -- .--. - -.--   .... .- -..   .-   --. .-. . .- -   ..-. .- .-.. .-.. .-.-.- .- .-.. .-..   - .... .   -.- .. -. --. ...   .... --- .-. ... . ...   .- -. -..   .- .-.. .-..   - .... .   -.- .. -. --. ...   -- . -. .-.-.- -.-. --- ..- .-.. -.. -. -   .--. ..- -   .... ..- -- .--. - -.--   - --- --. . - .... . .-.   .- --. .- .. -. .-.-.-'
decoded = ''
morseCode = morseCode.split(' ')
print(morseCode)
for letter in morseCode:
	if letter:
		# key = list(morse.keys())[list(morse.values()).index(letter)] # Also works
		decoded += morse[letter]
		if key == '.':
			decoded += '\n'
	else:
		decoded += ' '
print(decoded)

# Q 5
# Create a dictionary of inventory item to price using the lists here. The first inventory item should match with the first price. 
# Note ... one of the lists made a little longer on purpose. Deal with it, don't fix it by deleting the extra values.

# Extra ... Google Python zip( ) function and come up with a shorter (2 line) solution.

prices = [3.98, 0.97, 2.97, 3.99, 3.98, 1.98, 3.98, 1.98, 1.98, 3.98, 2.98, 2.99, 3.97, 0.97, 1.99, 0.98, 0.97, 3.99, 2.99, 3.97, 3.99, 0.98, 3.97, 1.98, 2.99, 1.97, 2.98, 1.97, 0.98, 2.97, 3.97, 0.99, 1.97, 2.97, 2.99, 1.98, 0.98, 1.98, 1.97, 1.98, 2.99, 1.97, 0.98, 0.97, 1.99, 3.97, 2.99, 0.99, 3.98, 3.97, 3.97, 1.99, 3.97, 3.98, 1.98, 2.99, 2.97, 3.97, 3.99, 3.98, 3.99, 2.97, 0.97, 0.99, 1.97, 0.97, 2.99, 3.99, 0.99, 2.97, 0.98, 3.97, 1.99, 0.99, 1.97, 0.97, 0.97, 2.99, 0.99, 0.97, 3.97, 1.99, 2.98, 3.97, 3.99]
items = ['advil', 'aspirin', 'antacids', 'antibiotic ointment', 'anti-bacerial toweletters', 'automotive repair kits', 'baking tin', 'bandages', 'bandannas', 'baking soda', 'lighters', 'boxed food', 'bungee cords', 'cable ties', 'camping fuel', 'candles', 'canned fruits', 'canned meat', 'canned veggies', 'can openers', 'car towels', 'chewing gum', 'clothesline', 'coffee filters', 'combs', 'compact mirror', 'condiments', 'cotton balls', 'cokkie tins', 'cough drops', 'cutting boards', 'dental floss', 'digital thermometer', 'dish towels', 'dog food', 'duct tape', 'drop cloth', 'ear plugs', 'elastic hair bands', 'emergency cell phone chargers', 'epsom salts', 'eyeglass repair kit', 'facial tissues', 'gauze', 'gardening globes', 'hard candies', 'hydrogen peroxide', 'hand sanitizer', 'jarred foods', 'instant ice packs', 'knives', 'latex dishwashing gloves', 'lip balms', 'lotions', 'magnifying glass', 'matches', 'mesh laundry bag', 'nails', 'screws', 'plastic shoe container', 'rubbing alcohol', 'safety pins', 'salt with iodine', 'scrub buddies', 'sewing kit', 'shoe laces', 'soaps', 'socks', 'solar lights', 'spices', 'stell wool', 'sponges', 'sugar', 'super glue', 'sun hat', 'toothbrushes', 'tote bags', 'travel bottles', 'twine', 'utility pail', 'water', 'wet wipes']
inventory = dict(zip(items, prices))
print(inventory)

# Q6. Dice Odds. 

# There are 36 possible combinations of two dice. A sim→ple pair of loops over range(6)+1 will enumerate all combinations. The sum of the two dice is more interesting than the actual combination. Create a dict of all combinations, using the sum of the two dice as the key.

# Each value in the dict should be a list of tuples; each tuple has the value of two dice. The general outline is something like the following:

# d= {}
# Loop with d1 from 1 to 6
#     Loop with d2 from 1 to 6
#         newTuple ← ( d1, d2 ) # create the tuple
#         oldList ← dictionary entry for sum d1+d2
#         newList ← oldList + newTuple
#         replace entry in dictionary with newList

# Loop over all values in the dictionary
#     print the key and the length of the list
dice = {}
for i in range(1,7):
	for o in range(1,7):
		if i+o not in dice:
			dice[i+o] = [(i,o)]
		else:
			dice[i+o].append((i,o))
print(dice)