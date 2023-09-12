"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def set_values(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle:
    def set_values(self, width, height):
        self.width = width
        self.height = height

    def set_values(self, width, height):
        self.width = width
        self.height = height
        self._width = width
        self._height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())

    rect.set_values(5, 4)

    # Print out the area function
    print("area:", rect.area())
