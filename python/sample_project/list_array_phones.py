<<<<<<< HEAD
names = "Иван,Джон,Фёдор,Пётр" # input()
telephones = "89001234567,89001112233,890055566377,890055566300" # input()

names_array = names.split(",")
telephones = telephones.split(",")

for n in range(len(names)):
    for t in range(len(telephones)):
        print(names_array[t] + ": " + telephones[t])
=======
names = "Иван,Джон,Фёдор,Пётр" # input()
telephones = "89001234567,89001112233,890055566377,890055566300" # input()

names_array = names.split(",")
telephones = telephones.split(",")

for n in range(len(names)):
    for t in range(len(telephones)):
        print(names_array[t] + ": " + telephones[t])
>>>>>>> refs/remotes/origin/readme
    break