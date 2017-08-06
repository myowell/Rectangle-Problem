import unittest
from classes.rectangle import Rectangle
from classes.coordinate import Coordinate

class TestContain(unittest.TestCase):
    def testContainOne(self):
        
        #One rectangle contains another
        
        rectangleOne = Rectangle(Coordinate(1, 5), Coordinate(7, 5), Coordinate(1, 1), Coordinate(7, 1))
        rectangleTwo = Rectangle(Coordinate(2,4), Coordinate(5, 4), Coordinate(2, 2), Coordinate(5, 2))
        
        result = rectangleTwo.rectangleContains(rectangleOne)
        
        self.assertEquals(result, True, "True")
        
    def testContainTwo(self):
        
        #Rectangles contain each other
        
        rectangleOne = Rectangle(Coordinate(1, 5), Coordinate(7, 5), Coordinate(1, 1), Coordinate(7, 1))
        rectangleTwo = Rectangle(Coordinate(1,5), Coordinate(7, 5), Coordinate(1, 1), Coordinate(7, 1))
        
        resultOne = rectangleTwo.rectangleContains(rectangleOne)
        resultTwo= rectangleOne.rectangleContains(rectangleTwo)
        
        result = resultOne or resultTwo
        
        self.assertEquals(result, True, "True")
        
    def testContainThree(self):
        
        #Rectangles are seperate
        
        rectangleOne = Rectangle(Coordinate(1, 5), Coordinate(7, 5), Coordinate(1, 1), Coordinate(7, 1))
        rectangleTwo = Rectangle(Coordinate(1,8), Coordinate(4, 8), Coordinate(1, 6), Coordinate(4, 6))
        
        resultOne = rectangleTwo.rectangleContains(rectangleOne)
        resultTwo= rectangleOne.rectangleContains(rectangleTwo)
        
        result = resultOne or resultTwo
        
        self.assertEquals(result, False, "False")
        
    def intersectTestOne(self):
        
        #Rectangles intersect
        
        rectangleOne = Rectangle(Coordinate(2, 4), Coordinate(5, 4), Coordinate(2, 2), Coordinate(5, 2))
        rectangleTwo = Rectangle(Coordinate(3, 5), Coordinate(4, 5), Coordinate(3, 3), Coordinate(4, 3))
        
        result = rectangleOne.rectangleIntersects(rectangleTwo)
        
        self.assertEquals(result, True, "True")
        
    def intersectTestTwo(self):
        
        #Rectangles are seperate
        
        rectangleOne = Rectangle(Coordinate(1, 5), Coordinate(7, 5), Coordinate(1, 1), Coordinate(7, 1))
        rectangleTwo = Rectangle(Coordinate(1,8), Coordinate(4, 8), Coordinate(1, 6), Coordinate(4, 6))
        
        result = rectangleOne.rectangleIntersects(rectangleTwo)
        
        self.assertEquals(result, False, "False")
        
    def AdjacencyTestOne(self):  
        
        #Rectangles are adjacent on the x-axis
        
        rectangleOne = Rectangle(Coordinate(1, 4), Coordinate(3, 4), Coordinate(1, 2), Coordinate(3, 2))
        rectangleTwo = Rectangle(Coordinate(3, 4), Coordinate(5, 4), Coordinate(3, 2), Coordinate(5, 2))
        
        result = rectangleOne.rectangleAdjacent(rectangleTwo) or rectangleTwo.rectangleAdjacent(rectangleOne)
        
        self.assertEquals(result, True, "True")
        
    def AdjacencyTestTwo(self):
        
        #Rectangles are adjacent on the y-axis 
        
        rectangleOne = Rectangle(Coordinate(1, 3), Coordinate(3, 3), Coordinate(1, 1), Coordinate(3, 1))
        rectangleTwo = Rectangle(Coordinate(1, 5), Coordinate(3, 5), Coordinate(1, 3), Coordinate(3, 3))
        
        result = rectangleOne.rectangleAdjacent(rectangleTwo) or rectangleTwo.rectangleAdjacent(rectangleOne)
        
        self.assertEquals(result, True, "True")
    
    def AdjacenyTestThree(self):
        
        #Rectangles are seperate
        
        rectangleOne = Rectangle(Coordinate(1, 5), Coordinate(7, 5), Coordinate(1, 1), Coordinate(7, 1))
        rectangleTwo = Rectangle(Coordinate(1,8), Coordinate(4, 8), Coordinate(1, 6), Coordinate(4, 6))
        
        result = rectangleOne.rectangleIntersects(rectangleTwo)
        
        self.assertEquals(result, False, "False")