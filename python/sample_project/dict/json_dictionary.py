import json


my_dict = json.loads(input())
print(f'Key for min value : {min(my_dict, key=my_dict.get)}')
# example input():
# {"key1": 123, "key2": 11, "key3": 110000, "key4": 50}


english_to_russian = {
    'pencil' : 'ручка',
    'love':'любовь',
    'tea':'чай',
    'table':'стол',
}

users = [
    {'name': 'Alexey', 'phone' : '+7992245789'},
    {'name': 'Petr', 'phone' : '+7922742356'}
]
print(users[0]["name"])