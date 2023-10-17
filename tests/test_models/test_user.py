#!/usr/bin/python3
"""This module Defines a class for the unittest of class BaseModel
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Defines tests for class User"""

    def setUp(self):
        """Set up testing instance"""
        self.user = User()

    def tearDown(self):
        """Tear down testing instance"""
        del self.user

    def test_instance(self):
        """Test if user is an instance of class User"""
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def test_attributes(self):
        """Test if user has necessary attributes"""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_created_at(self):
        """Test if created_at is datetime instance"""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is datetime instance"""
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(self.user.__class__.__name__, 'User')
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)

    def test_str(self):
        """Test the __str__ method"""
        user_str = self.user.__str__()
        self.assertEqual(user_str,
                         "[User] ({}) {}".format(self.user.id,
                                                 self.user.__dict__))
