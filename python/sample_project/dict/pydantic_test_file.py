from pydantic import BaseModel, ValidationError
# https://www.youtube.com/watch?v=dOO3GmX6ukU&t=959s&ab_channel=%D0%94%D0%B8%D0%B4%D0%B6%D0%B8%D1%82%D0%B0%D0%BB%D0%B8%D0%B7%D0%B8%D1%80%D1%83%D0%B9%21


class City(BaseModel):
	city_id: int
	name: str
	population: int

input_json = """
{
	"city_id": kjhju,
	"name": "Moscow",
	"population": "wow!"}
}
"""

city = City.parse_raw(
	"""{"city_id": 123, "name": "Moscow", "population": 10000000}"""
)
print(city)
print(city.name)

try:
	city = City.parse_raw(input_json)
except ValidationError as e:
	print(e.json())
# print(city)
