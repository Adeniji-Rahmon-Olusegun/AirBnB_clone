#!/usr/bin/python3
"""Module contains base model for this AirBnB clone project"""
import uuid
# from models import storage
from datetime import datetime


class BaseModel:
    """This is the parent class for all other classes in this project"""

    def __init__(self, *args, **kwargs):
        """Initializes the class with this attributes"""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, time_format)
                self.__dict__[key] = value


    def __str__(self):
        """Returns the string representation of the instances"""

        str_repr = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        
        return str_repr

    def save(self):
        """updates public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        keys_values = self.__dict__.copy()
        keys_values["__class__"] = self.__class__.__name__
        keys_values["created_at"] = self.created_at.isoformat()
        keys_values["updated_at"] = self.updated_at.isoformat()

        return keys_values
