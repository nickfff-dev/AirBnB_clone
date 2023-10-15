#!/usr/bin/python3
"""This module defines a class FileStorage That will handle deserialization
    and deserialization of objects.
"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel


class FileStorage():
    """This class initiates an instance of FileStorage
        Attributes:
            filepath(string): private variable for the file path.
            objects(dict): store all objects using id as key
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """function that returns a dict of ids of class members"""
        return FileStorage.__objects

    def new(self, obj):
        """function for adding new object to __object dict"""
        if obj:
            objclsname = obj.__class__.__name__
            id = obj.id
            key = objclsname + "." + id
            FileStorage.__objects[key] = obj.__dict__

    def save(self):
        """function to serialize obj to str and store in file"""
        all_objs = self.all()
        myobjs = {}
        for k, v in all_objs.items():
            v_copy = {key: datetime.isoformat(value) if key in
                      ["created_at", "updated_at"] else value for key, value in
                      v.items()}
            v_copy['__class__'] = k.split('.')[0]
            myobjs[k] = v_copy
        with open(FileStorage.__file_path, "w", encoding='utf-8') \
                as json_file1:
            return json.dump(myobjs, json_file1)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') \
                    as json_file2:
                data = json.load(json_file2)
                for k, v in data.items():
                    class_name = k.split('.')[0]
                    cls = globals()[class_name]
                    obj = cls(**v)
                    FileStorage.__objects[k] = obj.__dict__
