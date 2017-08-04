from coordinate import Coordinate

class Rectangle(object):
    '''
    Rectangle class for the Apprenda rectangle assessment
    
    Contains the four coordinates of a rectangle
    
    Attributes:
        upperLeft: The upper left coordinate.
        upperRight: The upper right coordinate.
        bottomLeft: The bottom left coordinate.
        bottomRight: The bottom right coordinate.
    '''
    
    upperLeft = Coordinate(0, 0)
    upperRight = Coordinate(0, 0)
    bottomLeft = Coordinate(0, 0)
    bottomRight = Coordinate(0, 0)

    def __init__(self, upperLeft, upperRight, bottomLeft, bottomRight):
        '''
        Inits Rectangle class
        '''
        self.upperLeft = upperLeft
        self.upperRight = upperRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
                
    def getUpperLeft(self):
        '''
        Returns the upper left coordinate of a rectangle.
        '''
        return self.upperLeft
    
    def getUpperRight(self):
        '''
        Returns the upper right coordinate of a rectangle.
        '''
        return self.upperRight
        
    def getBottomLeft(self):
        '''
        Returns the bottom left coordinate of a rectangle.
        '''
        return self.bottomLeft
    
    def getBottomRight(self):
        '''
        Returns the bottom right coordinate of a rectangle.
        '''
        return self.bottomRight
    
    def validRectangle(self):
        '''
        Determines if a rectangle is valid
        
        A valid rectangle is meets the following criteria:
        
        '''
        