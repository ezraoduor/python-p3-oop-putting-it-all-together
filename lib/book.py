#!/usr/bin/env python3
class Book:
    def __init__(self, title, page_count):
        """Initialize a Book instance with title and page_count."""
        self._title = title
        self._page_count = page_count

    # Property for title
    def get_title(self):
        return self._title

    def set_title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    title = property(get_title, set_title)

    # Property for page_count
    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return  # Exit without updating the value
        if value <= 0:
            raise ValueError("Page count must be a positive integer")
        self._page_count = value

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        """Print a message when turning the page."""
        print("Flipping the page...wow, you read fast!")