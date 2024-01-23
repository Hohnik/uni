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
from collections import defaultdict
from os import walk
from typing import List, Union

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
    _aliens: List[List[Alien]] = []
    _bolts: List[Bolt] = []
    _lives = None
    _time = 0
    _direction = "right"
    _next_bolt_counter = random.choice([x for x in range(1, BOLT_RATE)])

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        self.init_dline()
        self.init_ship()
        self.init_alien()

    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self, dt, input: GInput):
        self._time += dt

        # Check alien collisions
        for row_idx, row in enumerate(self._aliens):
            for alien in row:
                for bolt in self._bolts:
                    if alien.collides(bolt):
                        try:
                            self._aliens[row_idx].remove(alien)
                            self._bolts.remove(bolt)
                        except:
                            pass

        # Check ship collisions
        for bolt in self._bolts:
            if self._ship and self._ship.collides(bolt):
                self._ship = None
                self._bolts.remove(bolt)

        # Update ship
        if self._ship:
            self._ship.update(input)

        # Update bolts
        if self._bolts:
            for bolt in self._bolts:
                bolt.update()

        # Move aliens
        if self._time >= ALIEN_SPEED:
            self._direction = self.calculate_alien_movement_direction()
            self.move_aliens(self._direction)

            # Shoot from downmost random alien
            shooter_alien = random.choice(self.downmost_aliens())
            self._next_bolt_counter -= 1
            if self._next_bolt_counter == 0:
                shooter_alien.shoot()
                self._next_bolt_counter = random.choice(
                    [x for x in range(1, BOLT_RATE)]
                )

        # Reset boltcounter
        if self._next_bolt_counter <= 0:
            self._next_bolt_counter = random.choice([x for x in range(1, BOLT_RATE)])

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self, view):
        for row in self._aliens:
            for alien in row:
                if alien:
                    alien.draw(view)

        if self._ship:
            self._ship.draw(view)

        if self._dline:
            self._dline.draw(view)

        for bolt in self._bolts:
            if bolt:
                bolt.draw(view)

    # HELPER METHODS FOR COLLISION DETECTION
    def init_dline(self):
        self._dline = GPath(
            points=[0, DEFENSE_LINE, GAME_WIDTH, DEFENSE_LINE],
            linewidth=2,
            linecolor="black",
        )

    def init_ship(self):
        self._ship = Ship(self)

    def init_alien(self):
        self._aliens = [
            [
                Alien(self, i, source="../Images/" + ALIEN_IMAGES[2])
                for i in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 1
            ],
            [
                Alien(self, i, source="../Images/" + ALIEN_IMAGES[1])
                for i in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 2
            ],
            [
                Alien(self, i, source="../Images/" + ALIEN_IMAGES[1])
                for i in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 3
            ],
            [
                Alien(self, i, source="../Images/" + ALIEN_IMAGES[0])
                for i in range(ALIENS_IN_ROW)
                if ALIEN_ROWS >= 4
            ],
            [
                Alien(self, i, source="../Images/" + ALIEN_IMAGES[0])
                for i in range(ALIENS_IN_ROW)
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

    def move_aliens(self, direction: str):
        for row in self._aliens:
            for alien in row:
                if direction == "right":
                    alien.move_right()
                elif direction == "left":
                    alien.move_left()
                elif direction == "down":
                    alien.move_down()

        self._time = 0

    def calculate_alien_movement_direction(self):
        if self._direction == "down":
            if self.leftmost_alien_x() <= ALIEN_H_SEP + 0.5 * ALIEN_WIDTH:
                return "right"
            if self.rightmost_alien_x() >= GAME_WIDTH - ALIEN_H_SEP - 0.5 * ALIEN_WIDTH:
                return "left"

        if (
            self.leftmost_alien_x() <= ALIEN_H_SEP + 0.5 * ALIEN_WIDTH
            or self.rightmost_alien_x() >= GAME_WIDTH - ALIEN_H_SEP - 0.5 * ALIEN_WIDTH
        ):
            return "down"

        return self._direction

    def rightmost_alien_x(self):
        max_value = -float("inf")

        for row in self._aliens:
            if row[-1].x > max_value:
                max_value = row[-1].x

        return max_value

    def leftmost_alien_x(self):
        min_value = float("inf")
        for row in self._aliens:
            if row[0].x < min_value:
                min_value = row[0].x

        return min_value

    def downmost_aliens(self):  # Downmost alien of every column
        aliens_by_column = defaultdict(list)
        for row_number, row in enumerate(self._aliens):
            if row_number == ALIEN_ROWS - 1:
                return row
            if len(row) == ALIEN_ROWS:
                continue

            for alien in row:
                aliens_by_column[alien.get_column()].append(alien)

        return [alien[-1] for _, alien in aliens_by_column]
