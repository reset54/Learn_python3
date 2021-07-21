<<<<<<< HEAD
# m h
string = input()
divided = string.split(" ")
m = divided[0]
m = m.replace(",",".")

# print(m) # for test

mass = float(m)
height = float(divided[1])
=======
# m h
string = input()
divided = string.split(" ")
m = divided[0]
m = m.replace(",",".")

# print(m) # for test

mass = float(m)
height = float(divided[1])
>>>>>>> refs/remotes/origin/readme
print(round(mass/height ** 2, 1))