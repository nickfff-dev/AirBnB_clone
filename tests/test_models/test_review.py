#!/usr/bin/python3
"""This module Defines a class for the unittest of class BaseModel
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up for the tests"""
        self.review = Review()

    def tearDown(self):
        """Tear down for the tests"""
        del self.review

    def test_is_instance_base_model(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attr_types(self):
        """Test if attributes are the correct types"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_save(self):
        """Test if the save method works"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)
