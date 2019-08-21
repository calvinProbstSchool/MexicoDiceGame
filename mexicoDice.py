#mexicoDie.py
#A class for dice for the game mexico

from random import randint

class Die :
    def __init__( self, numSidesInput = 6 ) :
        self.faceVal = randint( 1, 6 )
        if numSidesInput < 2 :
            numSidesInput = 6
            print "Number of sides is invalid, set to default(6)."
        self.numSides = numSidesInput

    def __str__( self ) :
        print str( self.faceVal )

    def roll( self )
        self.faceVal = randint( 1, 6 )

    

    
        
        
