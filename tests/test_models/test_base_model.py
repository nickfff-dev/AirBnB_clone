#!/usr/bin/python3
"""This module Defines a class for the unittest of class BaseModel
"""
import unittest
from models.base_model import BaseModel
import inspect


class test_base_model(unittest.TestCase):
    """a class for the unittest of class BaseModel"""

    def setUp(self):
        """setting up test instance"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()
        self.old_updated_at = self.base1.updated_at

    def tearDown(self):
        """tearing down  test instance"""
        del self.base1
        del self.base2

    @classmethod
    def setUpClass(cls):
        """Set up class method for the doc tests"""
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)
        cls.itexists = False

    @classmethod
    def tearDownClass(cls):
        """tear down test class"""
        cls.itexists = False

    def test_class_docstring(self):
        """Tests if class docstring documentation exist"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests if methods docstring documntation exist"""
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_method_save(self):
        """This function tests the method save of BaseModel."""
        for func in self.setup:
            if func[0] == "save":
                self.itexists = True
        self.assertTrue(self.itexists)

    def test_method_to_dict(self):
        """This function tests if the method to_dict exists."""
        for func in self.setup:
            if func[0] == "to_dict":
                self.itexists = True
        self.assertTrue(self.itexists)

    def test_module_docstring(self):
        """Tests if module docstring documentation exist"""
        self.assertTrue(len(BaseModel.__module__.__doc__) >= 1)

    def test_uuid(self):
        """This method tests the uuid of BaseModel Instances."""
        self.assertIsInstance(self.base1, BaseModel)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertIsNotNone(self.base1.id)
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertIsInstance(self.base1.id, str)
