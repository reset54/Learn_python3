from pprint import pprint
import json


def is_valide_JSON(json_Data):
    try:
        pprint(json.loads(json_Data))
    except ValueError as err:
        print("Невалидный json")

InvalidJsonData = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com",}"""

validJsonData = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com"}"""

validJsonData2 = """[{"phone": "01", "name": "John"}, "2", {"phone": "033", "name": "Vasya"}, "4", {"phone": "777", "name": "Daniel"}]"""

is_valide_JSON(InvalidJsonData)
print()
is_valide_JSON(validJsonData)
print()
is_valide_JSON(validJsonData2)
print()