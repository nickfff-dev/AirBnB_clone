#!/usr/bin/python3
"""This module Defines a class for the unittest of class BaseModel
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def tearDown(self):
        """Tear down for the tests"""
        del self.state

    def test_is_instance_base_model(self):
        """Test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attr_types(self):
        """Test if attributes are the correct types"""
        self.assertIsInstance(self.state.name, str)

    def test_save(self):
        """Test if the save method works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)
