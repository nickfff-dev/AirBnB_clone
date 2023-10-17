#!/usr/bin/python3
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

    def __init__(self, *args, **kwargs):
        """initialises a BaseModel instance
        args(list): wont be used.
        kwargs: key name pairs of instance attributes.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """"prints the string rep of a class"""
        return "[" + self.__class__.__name__ + "]" + \
            "(" + self.id + ") " + str(self.__dict__)

    def save(self):
        """method that saves the instance to json"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        method for creating a dict of instance __dict__ keys and values.
        Returns:
            updated_dict(dict): a copy of self.__dict__ .
        """
        updated_dict = {}
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                updated_dict[k] = datetime.isoformat(v)
            else:
                updated_dict[k] = v
        updated_dict["__class__"] = self.__class__.__name__
        return updated_dict
