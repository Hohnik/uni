"""
A module to show off how to process touches in game2d

If your computer is one of the ones with High-DPI display issues, this may not work
properly.

Author: Walker M. White (wmw2)
Date:   November 20, 2019
"""
import introcs
from game2d import *

############# CONSTANTS #############
# Window Size
WINDOW_WIDTH  = 512
WINDOW_HEIGHT = 512

# Animation Frames that constitute a click
CLICK_SPEED = 10
# The color of the drawing line
LINE_COLOR = introcs.RGB(255,0,0)


############# APPLICATION STATES #############
NUM_STATES = 3
STATE_ERASE = 0
STATE_DRAW  = 1
STATE_NONE  = 2


############# CONTROLLER CLASS #############
class Touch(GameApp):
    """
    This class tracks the mouse to draw freehand lines
    
    Attribute view : the view (inherited from GameApp) 
    Invariant: view is an instance of GView
    
    Attribute input : the input (inherited from GameApp) 
    Invariant: input is an instance of GInput
    
    Attribute lines: the set of lines to be drawn
    Invariant: lines is a list of GPath objects
    
    Attribute clicks: the # of fast clicks in a row 
    Invariant: clicks is an int >= 0
    
    Attribute last: the last mouse position
    Invariant: last is a Point2 or None if mouse was not down last frame
    
    Attribute time: the frames since mouse last changed (pressed, released)
    Invariant: time is an int >= 0, and 0 if mouse state changed
    """
    
    # THREE MAIN METHODS
    def start(self):
        """
        Initializes the application, creating new attributes.
        """
        self.last   = None  # The last click
        self.time   = 0
        self.clicks = 0
        self.lines  = []
        self.state  = STATE_NONE
    
    def update(self,dt):
        """
        Adds new lines or erases them all.
        
        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        # helper method to detect a click
        self._determineState()
        
        # Erase on double click
        if   self.state == STATE_ERASE:
            self._eraseScreen()
        elif self.state == STATE_DRAW:
            self._drawLines()
        # Else do nothing
        
        # Update mouse position (must do last)
        # This is like updating a loop variable at end of loop
        self.last = self.input.touch
    
    def draw(self):
        """
        Draws the lines
        """
        for line in self.lines:
            line.draw(self.view)
    
    
    # HELPER METHODS
    def _determineState(self):
        """
        Determines the current state and assigns it to self.state
        
        This method checks for either the mouse being held down (continuously) or
        a double click.  The mouse is held down if neither touch nor last are None.
        A double click occurs if the mouse was pressed and released quickly twice
        in succession.
        """
        touch = self.input.touch
        
        # Is this a press, release or a hold
        press   = self.input.is_touch_pressed()
        release = self.input.is_touch_released()
        hold    = not (touch is None or self.last is None)
        
        # Increment the timer
        self.time = self.time + 1
        
        # Reset timer on a press
        if press:
            # Reset clicks if not fast enought
            if self.time >= CLICK_SPEED:
                self.clicks = 0
            self.time = 0
        
        # Reset timer on release
        if release:
            # Add click if fast enough
            if self.time < CLICK_SPEED:
                self.clicks = self.clicks + 1
            else:
                self.clicks = 1
            self.time = 0
        
        # Now determine state
        if self.clicks >= 2:
            self.state  = STATE_ERASE
        elif hold:
            self.state = STATE_DRAW
        else:
            self.state = STATE_NONE
    
    def _eraseScreen(self):
        """
        Clears the screen and resets the click count.
        """
        self.clicks = 0
        self.lines = []
    
    def _drawLines(self):
        """
        Adds a new line from touch to last.
        """
        touch = self.input.touch
        
        # Specify a line as list of two points
        points = [self.last.x,self.last.y,touch.x,touch.y]
        line = GPath(points=points,linecolor=LINE_COLOR)
        self.lines.append(line)


# Script Code
if __name__ == '__main__':
    Touch(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()
