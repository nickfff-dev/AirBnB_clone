#!/usr/bin/python3
"""This module Defines a class for the unittest of class BaseModel
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """Defines tests for class City"""

    def setUp(self):
        """Set up testing instance"""
        self.city = City()

    def tearDown(self):
        """Tear down testing instance"""
        del self.city

    def test_instance(self):
        """Test if city is an instance of class City"""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attributes(self):
        """Test if city has necessary attributes"""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_created_at(self):
        """Test if created_at is datetime instance"""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is datetime instance"""
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method"""
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__, 'City')
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)

    def test_str(self):
        """Test the __str__ method"""
        city_str = self.city.__str__()
        self.assertEqual(city_str, "[City] ({}) {}".format(self.city.id,
                                                           self.city.__dict__))
