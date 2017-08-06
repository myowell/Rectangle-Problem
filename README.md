### Rectangle-Problem
## Overview
A Python approach to solving the Rectangle Assessment for Apprenda Inc.
Designed and built using Python 3.0 and the Tkinkter GUI package

For the purpose of this solution only well formed rectangles are accepted. A well formed rectangles is a rectangle that aligns with each axis and is an equiangular quadrilateral (all four angles are 90 degrees)
A valid rectangle input also must possess the following qualities:

ALL x and y coordinates are positive integers.
The upper left's x-coordinate equals the x-coordinate of the bottom left and its y-coordinate matches the y-coordinate of the top right.
The bottom left's x-coordinate equals the y-coordinate of the bottom right.
The bottom right's x-coordinate equals the x-coordinate of the top right.

Determines if two given rectangles possess any of the following qualities:
- If the two rectangles intersect at any point
- If one rectangle contains another or if each contain the other
- If the two rectangles are adjacent. Rectangles are only considered adjacent if a line shares a line or sub-line.

## Usage
The program contains a graphical interface for entry of rectangle coordinates as well as a canvas to present a visual representation of each rectangle.
The first rectangle is drawn in red while the second is drawn in blue.
A text field at the bottom will output any found properties or any input errors.

The GUI's menu contains two options:

Draw - This option will take in input from the entry field, validate all data, and either draw each rectangle on the canvas and or in the case of invalid input display an error message
If the program determines that the rectangles intersect, contain another rectangle, or are adjacent the result will be diplayed along the bottom text field.
A blank text field means no special properties were found for each rectangle.

***Note:***
To make use of the canvas it is suggested that the user make sure the dimensions entered are large enough to be visible.
Smaller rectangles will still render and the results of each check will still be displayed.

Clear - 
Clears the result label, canvas, and all input fields

## Functions

**rectangleIntersects()**

Determines if two rectangles intersect at any point

Examples of intersecting rectangles:
[(2, 4), (5, 4), (2, 2), (5, 2)] and [(3, 5), (4, 5), (3, 3), (4, 3)] intersect

**rectangleContains()**

Determines if one rectangle contains another

Examples of containment:
[(1, 5), (7, 5), (1, 1), (7, 1)] and [(2, 4), (5, 4), (2, 2), (5, 2)] the first rectangle contains the second
[(1, 5), (7, 5), (1, 1), (7, 1)] and [(1, 5), (7, 5), (1, 1), (7, 1)] each rectangle contains each other

**rectangleIsAdjacent()**

Determines if one rectangle is adjacent to another along the top or right sides. Both rectangles are checked within the program to ensure all each side of each rectangle is checked.

Rectangles are considered adjacent if they share a line or sub-line along one edge.

Examples of adjacent rectangles:
[(1, 4), (3, 4), (1, 2), (3, 2)] and [(3, 4), (5, 4), (3, 2), (5, 2)] are adjacent on the x-axis
[(1, 3), (3, 3), (1, 1), (3, 1)] and [(1, 5), (3, 5), (1, 3), (3, 3)] are adjacent on the y-axis
