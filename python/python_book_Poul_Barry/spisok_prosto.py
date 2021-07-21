<<<<<<< HEAD
vowels = ['a', 'e', 'i', 'o', 'u']

word = 'Milliways'

for letter in word:
    if letter in vowels:
        print(letter)


odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59
       ]

print("\n")
found = []
print(len(found))

found.append('a')
print(len(found))
found.append('i')
found.append('o')
found.append('e')

if 'u' not in found:
	found.append('u')
print(found)


print("\n")
right_this_minute = []
right_this_minute.append(5)
print(right_this_minute)

if right_this_minute in odds:
=======
vowels = ['a', 'e', 'i', 'o', 'u']

word = 'Milliways'

for letter in word:
    if letter in vowels:
        print(letter)


odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59
       ]

print("\n")
found = []
print(len(found))

found.append('a')
print(len(found))
found.append('i')
found.append('o')
found.append('e')

if 'u' not in found:
	found.append('u')
print(found)


print("\n")
right_this_minute = []
right_this_minute.append(5)
print(right_this_minute)

if right_this_minute in odds:
>>>>>>> refs/remotes/origin/readme
    print("This minute seems a little odd.")