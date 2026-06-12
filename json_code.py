import json
food_ratings = {"organic dog food": 2, 3: False}
x = json.dumps(food_ratings)
x = json.dumps(food_ratings, skipkeys=True)
print(x)


# list and tuple data type serializes to array data type 


# dict list and tuple not allowed as json key value  , you can use skipkeys = True  to avoid seeing error 


# By providing the skipkeys argument, you can prevent getting a TypeError when creating JSON data with unsupported Python keys:
# serializing: python data to json
# deserializing:  json-data to python 



toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
x = json.dumps(toy_conditions, sort_keys=True,indent=2)

print(x)


import json

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking",],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading",],
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking",],
    },
  ],
}

with open("hello_frieda.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dog_data, write_file,indent=4)



# Json to python 

# Json.loads() ---- deserialize a string, bytes, or byte array
# Json.load() ---- deserialize a text file 


with open("hello_frieda.json", mode="r", encoding="utf-8") as read_file:
    frie_data = json.load(read_file)
    print(frie_data)
    type(frie_data)



# To test json syntax

# python -m json.tool hello_frieda.json
# python -m json.tool pretty_frieda.json mini_frieda.json --compact

