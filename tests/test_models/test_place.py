#!/usr/bin/python3
"""This module Defines a class for the unittest of class BaseModel
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up for the tests"""
        self.place = Place()

    def tearDown(self):
        """Tear down for the tests"""
        del self.place

    def test_is_instance_base_model(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attr_types(self):
        """Test if attributes are the correct types"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_save(self):
        """Test if the save method works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)
