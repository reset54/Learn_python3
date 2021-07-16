from pprint import pprint
import json


try:
	sample_input = [{"phone": "01", "name": "John"}, "2", {"phone": "033", "name": "Vasya"}, "4", {"phone": "777", "name": "Daniel"}]
	pprint(sample_input)

	new_json = json.dumps(sample_input, indent=2)
	pprint(new_json)
except Exception:
	print("Невалидный json")
