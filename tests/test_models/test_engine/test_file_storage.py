#!/usr/bin/python3
"""This module Defines a class for the unittest of class FileStorage
"""
import unittest
from models.base_model import BaseModel
from models import FileStorage
from models import storage
import os
import inspect


class test_file_storage(unittest.TestCase):
    """This class runs various unit tests on class FileStorage"""

    def setUp(self):
        """initiate instance test"""
        self.storage = storage

    def tearDown(self):
        """remove instance"""
        del self.storage

    @classmethod
    def setUpClass(cls):
        """method to initiate test class"""
        cls.setup = inspect.getmembers(FileStorage, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        os.remove('file.json')

    def test_class_docstring(self):
        """Tests if class docstring documentation exist."""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests if methods docstring documntation exist."""
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_file_storage_init(self):
        """method to test if storage was initialized properly."""
        self.assertIsInstance(self.storage, FileStorage)

    def test_file_storage_save(self):
        """test serialization"""
        base1 = BaseModel()
        base1.save()
        self.assertEqual(len(self.storage.all()), 1)
        base2 = BaseModel()
        base2.save()
        self.assertEqual(len(self.storage.all()), 2)
        mydict = {f"{base1.__class__.__name__}.{base1.id}": base1.to_dict(),
                  f"{base2.__class__.__name__}.{base2.id}": base2.to_dict()
                  }
        self.assertEqual(self.storage.all(), mydict)
