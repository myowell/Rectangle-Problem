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
    
    def isValidRectangle(self):
        '''
        Determines if a rectangle is valid
        
        A rectangle is valid iff it meets the following criteria:
        ALL x and y coordinates are greater than zero
        The upper left's x-coordinate equals the x-coordinate of the bottom left and its y-coordinate matches the y-coordinate of the top right
        The bottom left's x-coordinate equals the y-coordinate of the bottom right
        The bottom right's x-coordinate equals the x-coordinate of the top right
        
        Return true if a rectangle is valid
        
        Return false if a rectangle is invalid
        '''
        
        if self.getUpperLeft().getX() == self.getBottomLeft().getX() \
        and self.getUpperLeft().getY() == self.getUpperRight().getY() \
        and self.getBottomLeft().getX() == self.getBottomRight().getY() \
        and self.getBottomRight().getX() == self.getUpperRight().getX():
            return True
        else:
            return False
        
    def rectangleContains(self, rectangleTwo):
        '''
        Determines if this rectangle is contained within another
        
        A rectangle is considered contained iff the x and y-coordinates for vertex are less than or equal to the vertices of another rectangle
        
        Return true if this rectangle is contained within rectangleTwo
        
        Return false if this rectangle is not contained within rectangleTwo
        '''
        
        if self.getUpperLeft().getX() <= rectangleTwo.getUpperLeft().getX() and self.getUpperLeft().getY() <= rectangleTwo.getUpperLeft().getY() \
        and self.getUpperRight().getX() <= rectangleTwo.getUpperRight().getX() and self.getUpperRight().getY() <= rectangleTwo.getUpperRight().getY() \
        and self.getBottomLeft().getX() <= rectangleTwo.getBottomLeft().getX() and self.getBottomLeft().getY() <= rectangleTwo.getBottomLeft().getY() \
        and self.getBottomRight().getX() <= rectangleTwo.getBottomRight().getX() and self.getBottomRight().getY() <= rectangleTwo.getBottomRight().getY():
            return True
        else:
            return False
         
        