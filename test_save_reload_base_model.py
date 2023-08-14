#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
new_model = BaseModel()
new_model.name = "My_First_Model"
new_model.my_number = 89
new_model.save()
print(new_model)
