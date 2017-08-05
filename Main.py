'''
Rectangle Aessessment for Apprenda Inc.

This program will take the coordinates of two rectangles and determine the following:
- If one or more lines of the two rectangles intersect
- If one rectangle contains another
- If the two rectangles share any adjacent lines

@author: Michael Yowell - michael.yowell@gmail.com
'''

from classes.rectangle import Rectangle
from classes.coordinate import Coordinate

if __name__ == '__main__':
    rect1 = Rectangle(Coordinate(1, 5), Coordinate(3, 5) , Coordinate(1, 2), Coordinate(3, 2))
    rect2 = Rectangle(Coordinate(1, 8), Coordinate(3, 8) , Coordinate(1, 7), Coordinate(3, 7))
    print(rect1.rectangleIntersects(rect2))