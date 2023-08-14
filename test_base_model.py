#!/usr/bin/python3
from models.base_model import BaseModel

new_model = BaseModel()
new_model.name = "My First Model"
new_model.my_number = 89
print(new_model)
new_model.save()
print(new_model)

new_model_json = new_model.to_dict()
print(new_model_json)
print("JSON of new_model:")
for key in new_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(new_model_json[key]), new_model_json[key]))
