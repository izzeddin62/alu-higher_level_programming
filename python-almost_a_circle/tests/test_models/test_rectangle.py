#!/usr/bin/python3
import unittest
from unittest.mock import patch, call
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        
    def test_right_argument(self):
        rect_1 = Rectangle(4, 2)
        rect_2 = Rectangle(2, 3, 8)
        rect_3 = Rectangle(2, 3, 8, 4)
        rect_4 = Rectangle(2, 3, 7, 3, 5)
        self.assertEqual(rect_1.x, 0)
        self.assertEqual(rect_1.y, 0)
        self.assertEqual(rect_1.width, 4)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_2.x, 8)
        self.assertEqual(rect_1.y, 0)
        self.assertEqual(rect_3.x, 8)
        self.assertEqual(rect_3.y, 4)
        self.assertEqual(rect_4.id, 5)

    def test_no_position_argument_type(self):
        with self.assertRaises(TypeError) as error:
            Rectangle()
        message = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error: 
            Rectangle(3)
        message = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Rectangle(4, 4, 5, 6, 7, 8)
        message = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(error.exception), message)

    def test_invalid_width(self):
        with self.assertRaises(TypeError) as error:
            Rectangle("3", 2)
        message = "width must be an integer"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(-4, 4)
        message = "width must be > 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(0, 4)
        message = "width must be > 0"
        self.assertEqual(str(error.exception), message)

    def test_invalid_height(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(3, "2")
        message = "height must be an integer"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(4, -4)
        message = "height must be > 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(4, 0)
        message = "height must be > 0"
        self.assertEqual(str(error.exception), message)

    def test_invalid_x(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(4, 4, -3)
        message = "x must be >= 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Rectangle(4, 4, "4")
        message = "x must be an integer"
        self.assertEqual(str(error.exception), message)

    def test_invalid_y(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(4, 4, 5, -6)
        message = "y must be >= 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Rectangle(4, 4, 5, 'er')
        message = "y must be an integer"
        self.assertEqual(str(error.exception), message)

    def test_area(self):
        rect_1 = Rectangle(2, 2)
        self.assertEqual(rect_1.area(), 4)

    def test_str(self):
        shape = Rectangle(2, 2)
        shape2 = Rectangle(2, 5, 1, 3)
        self.assertEqual(str(shape), "[Rectangle] (1) 0/0 - 2/2")
        self.assertEqual(str(shape2), "[Rectangle] (2) 1/3 - 2/5")

    @patch("builtins.print")
    def test_display(self, mock_print):
        shape = Rectangle(2, 2)
        shape_2 = Rectangle(2, 2, 3)
        shape_3 = Rectangle(2, 2, 0, 1)
        shape.display()
        self.assertEqual(mock_print.mock_calls, [call("##"), call("##")])
        mock_print.reset_mock()
        shape_2.display()
        self.assertEqual(mock_print.mock_calls, [call("   ##"), call("   ##")])
        mock_print.reset_mock()
        shape_3.display()
        self.assertEqual(mock_print.mock_calls, [call(""), call("##"), call("##")])

    def test_to_dictionary(self):
        shape = Rectangle(2, 2)
        self.assertEqual(shape.to_dictionary(), {"id": 1, 'width': 2, 'height': 2, 'x': 0, 'y': 0})

    def test_update(self):
        shape = Rectangle(2, 2)
        shape.update(10)
        self.assertEqual(shape.id, 10)
        shape.update(10, 30)
        self.assertEqual(shape.width, 30)
        shape.update(2, 2, 3)
        self.assertEqual(shape.height, 3)
        shape.update(2, 2, 3, 10)
        self.assertEqual(shape.x, 10)
        shape.update(2, 2, 2, 2, 22)
        self.assertEqual(shape.y, 22)
        shape.update(**{"id": 24})
        self.assertEqual(shape.id, 24)
        shape.update(id=15, width=10)
        self.assertEqual(shape.width, 10)
        shape.update(id=15, width=10, height=14)
        self.assertEqual(shape.height, 14)
        shape.update(id=12, width=34, height=2, x=5)
        self.assertEqual(shape.x, 5)
        shape.update(id=8, width=89, height=100, x=9, y=28)
        self.assertEqual(shape.y, 28)
        
    def test_rectangle_create(self):
        shape = Rectangle.create(**{ 'id': 89})
        self.assertEqual(shape.to_dictionary(), {'id': 89, 'width': 1, 'height': 1, 'x': 0, 'y': 0})
        shape = Rectangle.create(**{ 'id': 22, 'width': 12})
        self.assertEqual(shape.to_dictionary(), {'id': 22, 'width': 12, 'height': 1, 'x': 0, 'y': 0})
        shape = Rectangle.create(**{ 'id': 8, 'width': 45, 'height': 34 })
        self.assertEqual(shape.to_dictionary(), {'id': 8, 'width': 45, 'height': 34, 'x': 0, 'y': 0})
        shape = Rectangle.create(**{ 'id': 4, 'width': 19, 'height': 25, 'x': 33 })
        self.assertEqual(shape.to_dictionary(), {'id': 4, 'width': 19, 'height': 25, 'x': 33, 'y': 0})
        shape = Rectangle.create(**{ 'id': 1, 'width': 29, 'height': 45, 'x': 23, 'y': 100 })
        self.assertEqual(shape.to_dictionary(), {'id': 1, 'width': 29, 'height': 45, 'x': 23, 'y': 100})
