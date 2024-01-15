"""
A module to show off how to use states.

This module is like animation.py, except that it looks at it can animate the ellipse
in a circle, horizontally or vertically.  We use key presses to switch between states.
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
# Amount to change the angle
ANIMATION_STEP   = 0.1
# Ellipse Radius
ELLIPSE_RADIUS = 20
# Ellipse Color
ELLIPSE_COLOR = introcs.RGB(255,0,0)


############# ANIMATION STATES #############
NUM_STATES = 3
STATE_CIRCLE     = 0
STATE_HORIZONTAL = 1
STATE_VERTICAL   = 2


############# CONTROLLER CLASS #############
class State(GameApp):
    """
    This class is an application to animate an ellipse about a center.

    At each step, the update() method computes a new angle. It finds the (x,y)
    coordinate that corresponds to the polar coordinate (ANIMATION_RADIUS,angle)
    and puts the ellipse there.

    Attribute view : the view (inherited from GameApp)
    Invariant: view is an instance of GView

    Attribute input : the input (inherited from GameApp)
    Invariant: input is an instance of GInput

    Attribute angle: ellipse angle from center
    Invariant: angle is a float

    Attribute factor:   the ellipse animation factor
    Invariant: factor is a float and 0 if state changed

    Attribute state: the animation state
    Invariant: state is one of STATE_CIRCLE, STATE_HORIZONTAL, STATE_VERTICAL

    Attribute ellipse: the ellipse to animate
    Invariant: ellipse is a GEllipse whose center (in polar coordinates) is
    (RADIUS,self.angle) if STATE_CIRCLE, (factor+width/2,height/2) if STATE_HORIZONTAL,
    and (width/2,height/2+factor) if STATE_VERTICAL
    """

    # THREE MAIN METHODS
    def start(self):
        """
        Initializes the program state.
        """
        self.state    = STATE_CIRCLE
        self.factor   = 0
        self.ellipse  = GEllipse(x=0,y=0,width=ELLIPSE_RADIUS,height=ELLIPSE_RADIUS,
                                 fillcolor=ELLIPSE_COLOR)

    def update(self,dt):
        """
        Determines the current state and animates the ellipse.

        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        # Determine the current state
        self._determineState()

        # Process the states.  Send to helper methods
        if self.state == STATE_CIRCLE:
            self._animateCircle()
        elif self.state == STATE_HORIZONTAL:
            self._animateHorizontal()
        elif self.state == STATE_VERTICAL:
            self._animateVertical()

        # Increment factor
        self.factor = (self.factor+ANIMATION_STEP) % (2*math.pi)

    def draw(self):
        """
        Draws the ellipse
        """
        self.ellipse.draw(self.view)


    # HELPER METHODS
    def _determineState(self):
        """
        Determines the current state and assigns it to self.state

        This method checks for a key press, and if there is one, changes the state
        to the next value.  A key press is when a key is pressed for the FIRST TIME.
        We do not want the state to continue to change as we hold down the key.  The
        user must release the key and press it again to change the state.
        """
        # Only change if we have just pressed the keys this animation frame
        # The empty string here means we will take ANY key.
        change = self.input.is_key_pressed('')

        if change:
            # Click happened.  Change the state
            self.state = (self.state + 1) % NUM_STATES
            # State changed; reset factor
            self.factor = 0

    def _animateCircle(self):
        """
        Animates on a circle.
        """
        x = ANIMATION_RADIUS*math.cos(self.factor)+self.width/2.0
        y = ANIMATION_RADIUS*math.sin(self.factor)+self.height/2.0
        self.ellipse.x = x
        self.ellipse.y = y

    def _animateHorizontal(self):
        """
        Animates on the horizontal access.
        """
        x = ANIMATION_RADIUS*math.cos(self.factor)+self.width/2.0
        self.ellipse.x = x
        self.ellipse.y = self.height/2.0

    def _animateVertical(self):
        """
        Animates on the vertical access.
        """
        y = ANIMATION_RADIUS*math.sin(self.factor)+self.height/2.0
        self.ellipse.x = self.width/2.0
        self.ellipse.y = y



# Application Code
if __name__ == '__main__':
    State(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()
