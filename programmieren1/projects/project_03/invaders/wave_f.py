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
import random
from os import walk

from consts import *
from game2d import *
from models import *

# from numpy import source

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)


class Wave:
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
    _ship = None
    _dline = None
    _aliens = []
    _bolts = []
    _lives = None
    _time = 0
    _direction = "right"

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        self.init_dline()
        self.init_ship()
        self.init_alien()

    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self, dt, input: GInput):
        self._time += dt
        if self._time >= ALIEN_SPEED:
            self._direction = self.calculate_direction()

            self.move_aliens(self._direction)
            # if self._direction == "right":
            #     self.move_aliens("right")
            # elif self._direction == "left":
            #     self.move_aliens("left")
            # elif self._direction == "down":
            #     self.move_aliens("down")

            if self._bolts:
                for bolt in self._bolts:
                    self.move_bolt(bolt)

        if input.is_key_down("left") or input.is_key_down("j"):
            self.move_ship_left(self._ship)

        if input.is_key_down("right") or input.is_key_down("l"):
            self.move_ship_right(self._ship)

        if (
            input.is_key_down("spacebar")
            or input.is_key_down("up")
            or input.is_key_down("f")
        ):
            bolt = Bolt()
            if self._ship:
                bolt.x = self._ship.x
                bolt.y = self._ship.y + 0.5 * SHIP_HEIGHT
            self._bolts.append(bolt)

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self, view):
        for row in self._aliens:
            for alien in row:
                alien.draw(view)

        if self._ship:
            self._ship.draw(view)

        if self._dline:
            self._dline.draw(view)

        for bolt in self._bolts:
            bolt.draw(view)

    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

    # HELPER METHODS FOR COLLISION DETECTION
    def init_dline(self):
        self._dline = GPath(
            points=[0, DEFENSE_LINE, GAME_WIDTH, DEFENSE_LINE],
            linewidth=2,
            linecolor="black",
        )

    def init_ship(self):
        self._ship = Ship(
            x=GAME_WIDTH // 2,
            y=SHIP_HEIGHT // 2 + SHIP_BOTTOM,
            width=SHIP_WIDTH,
            height=SHIP_HEIGHT,
            source="../Images/" + SHIP_IMAGE,
        )

    def init_alien(self):
        self._aliens = [
            [
                Alien(source="../Images/" + ALIEN_IMAGES[2])
                for _ in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 1
            ],
            [
                Alien(source="../Images/" + ALIEN_IMAGES[1])
                for _ in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 2
            ],
            [
                Alien(source="../Images/" + ALIEN_IMAGES[1])
                for _ in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 3
            ],
            [
                Alien(source="../Images/" + ALIEN_IMAGES[0])
                for _ in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 4
            ],
            [
                Alien(source="../Images/" + ALIEN_IMAGES[0])
                for _ in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 5
            ],
        ]

        for row_idx in range(ALIEN_ROWS):
            for col_idx in range(ALIENS_IN_ROW):
                self._aliens[row_idx][col_idx].width = ALIEN_WIDTH
                self._aliens[row_idx][col_idx].height = ALIEN_HEIGHT
                self._aliens[row_idx][col_idx].x = (
                    ALIEN_H_SEP
                    + 1 / 2 * ALIEN_WIDTH
                    + col_idx * (ALIEN_H_SEP + ALIEN_WIDTH)
                )
                self._aliens[row_idx][col_idx].y = (
                    GAME_HEIGHT
                    - ALIEN_CEILING
                    - 1 / 2 * ALIEN_HEIGHT
                    - row_idx * (ALIEN_V_SEP + ALIEN_HEIGHT)
                )

    def move_ship_right(self, game_object):
        if game_object.x < GAME_WIDTH - 1 / 2 * SHIP_WIDTH:
            game_object.x += SHIP_MOVEMENT

    def move_ship_left(self, game_object):
        if game_object.x > 1 / 2 * SHIP_WIDTH:
            game_object.x -= SHIP_MOVEMENT

    def move_alien_right(self, game_object):
        game_object.x += ALIEN_H_WALK

    def move_alien_left(self, game_object):
        game_object.x -= ALIEN_H_WALK

    def move_alien_down(self, game_object):
        game_object.y -= ALIEN_V_WALK

    def move_aliens(self, direction: str):
        for row in self._aliens:
            for alien in row:
                if direction == "right":
                    self.move_alien_right(alien)
                elif direction == "left":
                    self.move_alien_left(alien)
                elif direction == "down":
                    self.move_alien_down(alien)
        self._time = 0

    def calculate_direction(self):
        if (
            self.leftmost_alien_x() <= ALIEN_H_SEP + 0.5 * ALIEN_WIDTH
            and self._direction == "down"
        ):
            return "right"
        if (
            self.rightmost_alien_x() >= GAME_WIDTH - ALIEN_H_SEP - 0.5 * ALIEN_WIDTH
            and self._direction == "down"
        ):
            return "left"
        if (
            self.leftmost_alien_x() <= ALIEN_H_SEP + 0.5 * ALIEN_WIDTH
            or self.rightmost_alien_x() >= GAME_WIDTH - ALIEN_H_SEP - 0.5 * ALIEN_WIDTH
        ):
            return "down"

        return self._direction

    def rightmost_alien_x(self):  # TODO: Loop through aliens and find highest x value
        max_value = -float("inf")
        for row in self._aliens:
            row_max = max([alien.x for alien in row])
            if row_max > max_value:
                max_value = row_max
        return max_value

    def leftmost_alien_x(self):  # TODO: Loop through aliens and find lowest x value
        min_value = float("inf")
        for row in self._aliens:
            row_min = min([alien.x for alien in row])
            if row_min < min_value:
                min_value = row_min
        return min_value

    def move_bolt(self, bolt: Bolt):
        bolt.y += BOLT_SPEED
