"""
A module to show off how to use the keyboard.

This module is like animation.py, except that it looks at the key presses
to perform the animation.

Author: Walker M. White (wmw2)
Date:   November 20, 2019
"""
import introcs
import random
import math
from game2d import *


############# CONSTANTS #############
# Window Size
WINDOW_WIDTH  = 512
WINDOW_HEIGHT = 512

# Distance from Window Center
ANIMATION_RADIUS = 100
# AMOUNT TO CHANGE THE ANGLE
ANIMATION_STEP   = 0.1
# Ellipse Radius
ELLIPSE_RADIUS = 20
# Ellipse Color
ELLIPSE_COLOR = introcs.RGB(255,0,0)


############# CONTROLLER CLASS #############
class Arrows(GameApp):
    """
    This class is an application to animate an ellipse about a center.
    
    At each step, the update() method looks at the key presses.  If neither
    the left nor right arrow is pressed, nothing happens.  Otherwise, it
    computes a new angle in the appropriate direction.  It finds the (x,y)
    coordinate that corresponds to the polar coordinate (ANIMATION_RADIUS,angle)
    and puts the ellipse there.
    
    Attribute view : the view (inherited from GameApp) 
    Invariant: view is an instance of GView
    
    Attribute input : the input (inherited from GameApp) 
    Invariant: input is an instance of GInput
    
    Attribute angle: ellipse angle from center
    Invariant: angle is a float
    
    Attribute ellipse: the ellipse to animate
    Invariant: ellipse is a GEllipse whose center is (RADIUS,self.angle) in polar
    """
    
    # THE THREE MAIN METHODS
    def start(self):
        """
        Initializes the application, creating new attributes.
        """
        self.angle = 0
        pos=self._polar_to_coord(ANIMATION_RADIUS,self.angle)
        self.ellipse = GEllipse(x=pos[0],y=pos[1],
                                width=ELLIPSE_RADIUS,height=ELLIPSE_RADIUS,
                                fillcolor=ELLIPSE_COLOR)
    
    def update(self,dt):
        """
        Animates the ellipse.
        
        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        # Look at the key presses
        # Doing this way cause left and right to cancel each other out
        da = 0
        if self.input.is_key_down('left'):
            da += ANIMATION_STEP
        if self.input.is_key_down('right'):
            da -= ANIMATION_STEP
        
        # Change the angle
        self.angle = self.angle+da % (2*math.pi)
        pos=self._polar_to_coord(ANIMATION_RADIUS,self.angle)
        self.ellipse.x = pos[0]
        self.ellipse.y = pos[1]
    
    def draw(self):
        """
        Draws the ellipse
        """
        self.ellipse.draw(self.view)
    
    
    # HELPER METHOD
    def _polar_to_coord(self,r,a):
        """
        Returns: Tuple (x,y) equal to polar coord (r,a)
        """
        return (r*math.cos(a)+self.width/2.0,r*math.sin(a)+self.height/2.0)


# Application Code
if __name__ == '__main__':
    Arrows(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()
