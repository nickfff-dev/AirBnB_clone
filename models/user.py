#!/usr/bin/python3
"""This module contains class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class defination"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
