#!/usr/bin/python3
"""Module contains base model for this AirBnB clone project"""

from uuid import uuid4
from models import storage
from datetime import datetime


class BaseModel:
    """This is the parent class for all other classes in this project"""

    def __init__(self, *args, **kwargs):
        """Initializes the class with this attributes"""

        time_4mat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.strptime(kwargs[key], time_4mat)
                    else:
                        setattr(key, kwargs[key])

        storage.new(self)

    def __str__(self):
        """Returns the string representation of instances"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict. containing keys/values of __dict__ wrt instance"""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dicts = self.__dict__.copy()
        for key, value in dicts.items():
            if isinstance(value, datetime):
                dicts[key] = value.strftime(time_format)
        dicts["__class__"] = self.__class__.__name__

        return dicts
