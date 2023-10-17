#!/usr/bin/python3
"""This module Defines a class for the unittest of class Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down for the tests"""
        del self.amenity

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test the attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
