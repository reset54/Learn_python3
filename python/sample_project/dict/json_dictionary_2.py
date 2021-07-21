<<<<<<< HEAD
import json
# even % 2 = 0
# odd % 2 = 1
# simple input:     name Пётр phone 02 sex male balance 50000
# simple output:    {"name": "Пётр", "phone": "02", "sex": "male", "balance": "50000"}

array_words = input().split(" ")
dict_my = {}
list_odd = []
list_even = []
for index in range(len(array_words)):
    if index % 2 == 0:
        list_odd.insert(index, array_words[index]) 
        # print(f'odd {array_words[index]}')
    else:
        list_even.insert(index, array_words[index]) 
        # print(f'even {array_words[index]}')
# print(list_odd)
# print(list_even)
dict_my = dict(zip(list_odd, list_even))
print(json.dumps(dict_my, ensure_ascii=False))

=======
import json
# even % 2 = 0
# odd % 2 = 1
# simple input:     name Пётр phone 02 sex male balance 50000
# simple output:    {"name": "Пётр", "phone": "02", "sex": "male", "balance": "50000"}

array_words = input().split(" ")
dict_my = {}
list_odd = []
list_even = []
for index in range(len(array_words)):
    if index % 2 == 0:
        list_odd.insert(index, array_words[index]) 
        # print(f'odd {array_words[index]}')
    else:
        list_even.insert(index, array_words[index]) 
        # print(f'even {array_words[index]}')
# print(list_odd)
# print(list_even)
dict_my = dict(zip(list_odd, list_even))
print(json.dumps(dict_my, ensure_ascii=False))

>>>>>>> refs/remotes/origin/readme
