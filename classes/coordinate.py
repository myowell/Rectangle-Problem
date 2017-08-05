class Coordinate(object):
    '''
    Coordinate class for Apprenda rectangle assessment
    
    This class contains and x value and y value of a point on a Cartesian plain 
    
    Attributes:
        x: x-axis (horizontal) value
        y: y-axis (verticle) value
    '''
    x = 0
    y = 0
    
    def __init__(self, x, y):
        '''
        Inits Coordinate class
        '''        
        self.x = x
        self.y = y
        
    def getX(self):
        '''
        Returns x-coordinate
        '''
        return self.x
    
    def getY(self):   
        '''
        Returns y-coordinate
        '''
        return self.y