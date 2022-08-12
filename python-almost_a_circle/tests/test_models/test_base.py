#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_initialization(self):
        obj_1 = Base(2)
        obj_2 = Base()
        self.assertEqual(obj_1.id, 2)
        self.assertEqual(obj_2.id, 1)


if __name__ == "__main__":
    unittest.main()
