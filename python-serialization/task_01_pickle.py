#!/usr/bin/env python3
"""
Module task_01_pickle
CustomObject class with pickle serialization/deserialization.
"""


import pickle


class CustomObject:
    """Custom class with name (str), age (int), is_student
    (bool) attributes."""
    def __init__(self, name, age, is_student):
        """Initialize CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes in specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize current instance to filename using pickle.
        Args:
            filename (str): Path to save pickled object.
        Returns:
            None if success, None on exception (file issues).
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (IOError, pickle.PickleError):
            pass

    @classmethod
    def deserialize(cls, filename):
        """Deserialize CustomObject from filename using pickle.
        Args:
            filename (str): Path to load pickled object.
        Returns:
            CustomObject instance if success, None on exceptio
            (non-existent/malformed).
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (IOError, FileNotFoundError, pickle.UnpicklingError):
            return None
