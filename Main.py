'''
Rectangle Aessessment for Apprenda Inc.

This program will take the coordinates of two rectangles and determine the following:
- If one or more lines of the two rectangles intersect
- If one rectangle contains another
- If the two rectangles share any adjacent lines

@author: Michael Yowell - michael.yowell@gmail.com
'''

from classes.rectangle import Rectangle

if __name__ == '__main__':
    rect1 = Rectangle(1, 1, 4, 5)
    print(rect1.getUpperLeft())