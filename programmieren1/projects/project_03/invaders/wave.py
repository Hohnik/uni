"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in
the Alien Invaders game.  Instances of Wave represent a single wave. Whenever 
you move to a new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on 
screen. These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or 
models.py. Whether a helper method belongs in this module or models.py is 
often a complicated issue.  If you do not know, ask on Piazza and we will 
answer.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from game2d import *
from consts import *
from models import *
import random

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not 
# permitted to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.
    
    This subcontroller has a reference to the ship, aliens, and any laser bolts 
    on screen. It animates the laser bolts, removing any aliens as necessary. 
    It also marches the aliens back and forth across the screen until they are 
    all destroyed or they reach the defense line (at which point the player 
    loses). When the wave is complete, you  should create a NEW instance of 
    Wave (in Invaders) if you want to make a new wave of aliens.
    
    If you want to pause the game, tell this controller to draw, but do not 
    update.  See subcontrollers.py from Lecture 24 for an example.  This 
    class will be similar to than one in how it interacts with the main class 
    Invaders.
    
    All of the attributes of this class ar to be hidden. You may find that 
    you want to access an attribute in class Invaders. It is okay if you do, 
    but you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter 
    and/or setter for any attribute that you need to access in Invaders.  
    Only add the getters and setters that you need for Invaders. You can keep 
    everything else hidden.
    
    """
    # HIDDEN ATTRIBUTES:
    # Attribute _ship: the player ship to control 
    # Invariant: _ship is a Ship object or None
    #
    # Attribute _aliens: the 2d list of aliens in the wave 
    # Invariant: _aliens is a rectangular 2d list containing Alien objects or None 
    #
    # Attribute _bolts: the laser bolts currently on screen 
    # Invariant: _bolts is a list of Bolt objects, possibly empty
    #
    # Attribute _dline: the defensive line being protected 
    # Invariant : _dline is a GPath object
    #
    # Attribute _lives: the number of lives left
    # Invariant: _lives is an int >= 0
    #
    # Attribute _time: the amount of time since the last Alien "step" 
    # Invariant: _time is a float >= 0s
    #
    # You may change any attribute above, as long as you update the invariant
    # You may also add any new attributes as long as you document them.
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY

    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    
    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    
    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    
    # HELPER METHODS FOR COLLISION DETECTION
