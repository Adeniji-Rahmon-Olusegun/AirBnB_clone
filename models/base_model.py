#!/usr/bin/python3
"""Module contains base model for this AirBnB clone project"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the parent class for all other classes in this project"""

    def __init__(self):
        """Initializes the class with this attributes"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of instances"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict. containing keys/values of __dict__ wrt instance"""

        dicts = self.__dict__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        dicts["__class__"] = self.__class__.__name__

        return dicts
