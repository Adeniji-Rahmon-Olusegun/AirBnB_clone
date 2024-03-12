#!/usr/bin/python3
"""This module contain the file storage engine"""

import os
import json


class FileStorage:
    """Serializes and deserializes JSON files"""

    def __init__(self):
        """Initializes FileStorage classs attributes"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key(classname.id)"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        with open(self.__file_path, "w") as file_obj:
            s_obj = {k: obj.to_dict() for k, obj in self.__objects.items()}
            json.dump(s_obj, file_obj)

    def reload(self):
        """ deserializes the JSON file to __objects if file exist"""

        from models.base_model import BaseModel
        from models.user import User

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file_obj:
                try:
                    self.__objects = json.load(file_obj)
                    obj_collection = {}
                    for key, value in self.__objects.items():
                        class_obj_name = value["__class__"]
                        instance = eval(class_obj_name)(**value)
                        obj_collection[key] = instance
                    self.__objects = obj_collection
                except json.JSONDecodeError:
                    pass
