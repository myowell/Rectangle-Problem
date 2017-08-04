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
    
    upperLeft = 0
    upperRight = 0
    bottomLeft = 0
    bottomRight = 0

    def __init__(self, upperLeft, upperRight, bottomLeft, bottomRight):
        '''
        Inits Rectangle class
        '''
        self.upperleft = upperLeft
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