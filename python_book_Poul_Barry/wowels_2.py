vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Milliways'
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:					# если letter находится в word, то:
	if letter in vowels:			# если letter находится в vowels, то: 
		if letter not in found:		# если letter не находится в списке found, то:
			found.append(letter) 	# добавить в список found параметр letter

for vowel in found:					# если vowel находится в found:
	print(vowel)					# выведем в консоль vowel