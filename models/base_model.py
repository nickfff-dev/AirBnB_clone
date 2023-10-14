#!/usr/bin/env python3
"""
This module defines a class BaseModel which will be inherited
by all BaseModelInstances.
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    defines a base class BaseModel.
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """initialises a BaseModel instance
        id(string): a unique identifier generated from uuid.
        created_at(datetime): the timestamp on creation.
        updated_at(datetime): the timestamp on update.
        """
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """"prints the string rep of a class"""
        return "[" + self.__class__.__name__ + "] " + \
            "(" + self.id + ") " + str(self.__dict__)

    def save(self):
        """method that updates the instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        method for creating a dict of instance __dict__ keys and values
        Returns:
            dict: a copy of self.__dict__
        """
        updated_dict = {}
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                updated_dict[k] = datetime.isoformat(v)
            else:
                updated_dict[k] = v
        updated_dict["__class__"] = self.__class__.__name__
        return updated_dict
