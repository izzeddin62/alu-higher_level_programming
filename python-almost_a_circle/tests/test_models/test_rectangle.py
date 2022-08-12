#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Rectangle.__nb_objects = 0
        
    def test_right_argument(self):
        rect_1 = Rectangle(4, 2)
        rect_2 = Rectangle(2, 3, 8)
        rect_3 = Rectangle(2, 3, 8, 4)
        self.assertEqual(rect_1.x, 0)
        self.assertEqual(rect_1.y, 0)
        self.assertEqual(rect_1.width, 4)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_2.x, 8)
        self.assertEqual(rect_1.y, 0)
        self.assertEqual(rect_3.x, 8)
        self.assertEqual(rect_3.y, 4)

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

    def test_invalid_height(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(3, "2")
        message = "height must be an integer"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(4, -4)
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
