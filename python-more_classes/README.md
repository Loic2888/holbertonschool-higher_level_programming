# Python - More Classes and Objects

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Description

This directory dives deeper into Object-Oriented Programming in Python. It explores class methods, static methods, class attributes vs instance attributes, and special memory hooks like `__str__`, `__repr__`, and `__del__`.

## Files

| File | Description |
| :--- | :--- |
| `0-rectangle.py` | Defines an empty class `Rectangle`. |
| `1-rectangle.py` | Defines `Rectangle` with private instance attributes `width` and `height`, along with property getters and setters. |
| `2-rectangle.py` | Adds public instance methods `area()` and `perimeter()`. |
| `3-rectangle.py` | Implements the `__str__` method to print the rectangle using `#`. |
| `4-rectangle.py` | Implements the `__repr__` method to return a string representation of the rectangle for recreation via `eval()`. |
| `5-rectangle.py` | Implements the `__del__` method to print a message when an instance of `Rectangle` is deleted. |
| `6-rectangle.py` | Adds a public class attribute `number_of_instances` to keep track of the active rectangles. |
| `7-rectangle.py` | Adds a public class attribute `print_symbol` to customize the symbol used for string representation. |
| `8-rectangle.py` | Defines a static method `bigger_or_equal(rect_1, rect_2)` that returns the biggest rectangle based on area. |
| `9-rectangle.py` | Defines a class method `square(cls, size)` that returns a new Rectangle instance with width == height == size. |

---

## Author

- **CERQUEIRA Loïc** - *Student at Holberton School*
