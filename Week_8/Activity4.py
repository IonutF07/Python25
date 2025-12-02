#Json to Python Dictionary
import json
json_data = '{"name": "John", "age": 25, "city": "New York"}'
python_dict = json.loads(json_data)
print(python_dict) # Print all
print(python_dict["name"]) #john

