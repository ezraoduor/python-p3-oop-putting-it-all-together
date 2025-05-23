#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color=None, is_clean=True):
        """Initialize a Shoe instance."""
        self._brand = brand
        self._size = size
        self._color = color
        self._is_clean = is_clean
        self._is_worn = False

    # Property for brand with validation
    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Brand must be a non-empty string")
        self._brand = value

    brand = property(get_brand, set_brand)

    # Property for size with validation
    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return  # Exit without updating the value
        if value <= 0:
            raise ValueError("Size must be a positive integer")
        self._size = value

    size = property(get_size, set_size)

    # Property for color with validation
    def get_color(self):
        return self._color

    def set_color(self, value):
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError("Color must be a non-empty string or None")
        self._color = value

    color = property(get_color, set_color)

    # Property for is_clean
    def get_is_clean(self):
        return self._is_clean

    def set_is_clean(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_clean must be a boolean")
        self._is_clean = value

    is_clean = property(get_is_clean, set_is_clean)

    # Method to wear the shoe
    def wear(self):
        self._is_worn = True
        self._is_clean = False

    # Method to clean the shoe
    def clean(self):
        if self._is_worn:
            self._is_clean = True
        else:
            raise ValueError("Shoe hasn't been worn yet")

    # Method to cobble (repair) the shoe
    def cobble(self):
        print("Your shoe is as good as new!")
        self._is_worn = False
        self._is_clean = True
        self.condition = "New"