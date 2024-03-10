#!/usr/bin/python3
"""Module contains base model for this AirBnB clone project"""

import uuid
import datetime


class BaseModel:
    """This is the parent class for all other classes in this project"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dict. containing keys/values of __dict__ wrt instance"""
        dicts = self.__dict__
        dicts["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dicts["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dicts["__class__"] = self.__class__.__name__

        return dicts
