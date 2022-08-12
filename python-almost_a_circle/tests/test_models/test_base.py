#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base.__nb_objects = 0
    def test_initialization(self):
        """test when not id is passed the base is initialized with the class id"""
        base = Base()
        base2 = Base()
        self.assertEqual(str(type(base)), "<class 'models.base.Base'>")
        self.assertEqual(base.id, base2.id - 1)

    def test_id_given(self):
        base = Base(34)
        self.assertEqual(base.id, 34)

    def test_json_string(self):
        base = Base(2)
        with_none = Base.to_json_string(None)
        empty_list = Base.to_json_string([])
        list_el = Base.to_json_string([{"id": 1}])
        self.assertEqual(with_none, "[]")
        self.assertEqual(empty_list, "[]")
        self.assertEqual(list_el, '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        dict_rep = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(dict_rep, [{"id": 1}])

if __name__ == "__main__":
    unittest.main()
