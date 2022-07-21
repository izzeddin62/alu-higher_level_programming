#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(45, (1, 1))
print(type(my_square))
print(my_square.__dict__)
