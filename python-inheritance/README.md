# Python - Inheritance

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Description

This directory explores **Inheritance** in Python. It covers superclasses, subclasses, overriding methods, multiple inheritance, and built-in functions like `isinstance`, `issubclass`, `type`, and `dir`.

## Files

| File | Description |
| :--- | :--- |
| `0-lookup.py` | Returns the list of available attributes and methods of an object (using `dir()`). |
| `1-my_list.py` | A class `MyList` that inherits from Python's built-in `list` and implements a method to print the sorted list. |
| `2-is_same_class.py` | Returns `True` if the object is exactly an instance of the specified class, otherwise `False`. |
| `3-is_kind_of_class.py` | Returns `True` if the object is an instance of, or inherits from, the specified class. |
| `4-inherits_from.py` | Returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class. |
| `5-base_geometry.py` | An empty class `BaseGeometry`. |
| `6-base_geometry.py` | Adds an unimplemented public instance method `area()` to `BaseGeometry` that raises an Exception. |
| `7-base_geometry.py` | Adds a public instance method `integer_validator(name, value)` to validate properties. |
| `8-rectangle.py` | Defines a class `Rectangle` that inherits from `BaseGeometry`, including instantiation of width and height. |
| `9-rectangle.py` | Implements the `area()` method dynamically for the `Rectangle` subclass and overrides `__str__`. |
| `10-square.py` | Defines a class `Square` that inherits from `Rectangle`, maintaining the geometry hierarchy. |
| `11-square.py` | Overrides the `__str__` method for the `Square` subclass to print `[Square] <width>/<height>`. |

---

## Author

- **CERQUEIRA Loïc** - *Student at Holberton School*
