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
