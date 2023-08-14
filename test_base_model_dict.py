#!/usr/bin/python3
from models.base_model import BaseModel

new_model = BaseModel()
new_model.name = "My_First_Model"
new_model.my_number = 89
print(new_model.id)
print(new_model)
print(type(new_model.created_at))
print("--")

new_model_json = new_model.to_dict()
print(new_model_json)
print("JSON of new_model:")
for key in new_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(new_model_json[key]), new_model_json[key]))
print("--")

my_new_model = BaseModel(**new_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("--")
print(new_model is my_new_model)
