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
    rect1 = Rectangle(Coordinate(1, 5), Coordinate(4, 5) , Coordinate(2, 3), Coordinate(4, 3))
    rect2 = Rectangle(Coordinate(1, 3), Coordinate(4, 3) , Coordinate(1, 1), Coordinate(4, 1))
    print(rect1.rectangleAdjacent(rect2))
    print(rect2.rectangleAdjacent(rect1))