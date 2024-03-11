#!/usr/bin/python3
"""Module contains base model for this AirBnB clone project"""

import uuid
#from models import storage
from datetime import datetime


class BaseModel:
    """This is the parent class for all other classes in this project"""

    def __init__(self):
        """Initializes the class with this attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns the string representation of the instances"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        keys_values = self.__dict__.copy()
        keys_values["created_at"] = self.created_at.isoformat()
        keys_values["updated_at"] = self.updated_at.isoformat()
        keys_values["__class__"] = self.__class__.__name__

        return keys_values
