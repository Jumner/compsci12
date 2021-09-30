def parse_braille_file(filename):
	data = open(filename, 'r')
	roughBraille = ['','','']
	lines = data.readlines()
	data.close()
	for i in range(len(lines)):
		roughBraille[i%3] += lines[i].strip('\n') + 'xx'
	braille = []
	for i in range(0, len(roughBraille[0]), 2):
		letter = ''
		for o in range(3):
			letter += roughBraille[o][i:i+2]
		braille.append(letter)

	return braille

brailleDict = {
	'xxxxxx':'\n',
	'oooooo':' ',
	'xooooo':'a',
	'xoxooo':'b',
	'xxoooo':'c',
	'xxoxoo':'d',
	'xooxoo':'e',
	'xxxooo':'f',
	'xxxxoo':'g',
	'xoxxoo':'h',
	'oxxooo':'i',
	'oxxxoo':'j',
	'xoooxo':'k',
	'xoxoxo':'l',
	'xxooxo':'m',
	'xxoxxo':'n',
	'xooxxo':'o',
	'xxxoxo':'p',
	'xxxxxo':'q',
	'xoxxxo':'r',
	'oxxoxo':'s',
	'oxxxxo':'t',
	'xoooxx':'u',
	'xoxoxx':'v',
	'oxxxox':'w',
	'xxooxx':'x',
	'xxoxxx':'y',
	'xooxxx':'z'
}
braille = parse_braille_file('data.txt')
def decode_phrase(some_braille, braille_dict):
	phrase = ''
	for letter in some_braille:
		phrase += braille_dict[letter]
	return phrase

print(decode_phrase(braille,brailleDict))