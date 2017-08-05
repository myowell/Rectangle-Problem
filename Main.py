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
    rect1 = Rectangle(Coordinate(3, 6), Coordinate(7, 6) , Coordinate(3, 3), Coordinate(7, 3))
    rect2 = Rectangle(Coordinate(4, 7), Coordinate(8, 7) , Coordinate(4, 4), Coordinate(8, 4))
    print(rect1.rectangleContains(rect2))