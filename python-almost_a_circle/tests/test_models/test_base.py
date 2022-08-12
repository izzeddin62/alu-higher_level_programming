#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_initialization(self):
        """test when not id is passed the base is initialized with the class id"""
        base = Base()
        base2 = Base()
        self.assertEqual(str(type(base)), "<class 'models.base.Base'>")
        self.assertEqual(base.id, 1)
        self.assertEqual(base2.id, 2)

if __name__ == "__main__":
    unittest.main()
