#!/usr/bin/python3
"""Module contains User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
