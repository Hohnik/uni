"""
Models module for Alien Invaders

This module contains the model classes for the Alien Invaders game. Anything 
that you interact with on the screen is model: the ship, the laser bolts, and 
the aliens.

Just because something is a model does not mean there has to be a special 
class for it. Unless you need something special for your extra gameplay 
features, Ship and Aliens could just be an instance of GImage that you move 
across the screen. You only need a new class when you add extra features to 
an object. So technically Bolt, which has a velocity, is really the only model 
that needs to have its own class.

With that said, we have included the subclasses for Ship and Aliens. That is 
because there are a lot of constants in consts.py for initializing the 
objects, and you might want to add a custom initializer.  With that said, 
feel free to keep the pass underneath the class definitions if you do not want 
to do that.

You are free to add even more models to this module.  You may wish to do this 
when you add new features to your game, such as power-ups.  If you are unsure 
about whether to make a new class or not, please ask on Piazza.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""

from typing import Literal, Union

from consts import *
from game2d import *

# PRIMARY RULE: Models are not allowed to access anything in any module other
# than consts.py.  If you need extra information from Gameplay, then it should
# be a parameter in your method, and Wave should pass it as a argument when it
# calls the method.


class Ship(GImage):
    """
    A class to represent the game ship.

    At the very least, you want a __init__ method to initialize the ships
    dimensions. These dimensions are all specified in consts.py.

    You should probably add a method for moving the ship.  While moving a
    ship just means changing the x attribute (which you can do directly),
    you want to prevent the player from moving the ship offscreen.  This
    is an ideal thing to do in a method.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like animation).
    """

    def __init__(self, wave):
        super().__init__(
            x=GAME_WIDTH // 2,
            y=SHIP_HEIGHT // 2 + SHIP_BOTTOM,
            width=SHIP_WIDTH,
            height=SHIP_HEIGHT,
            source="../Images/" + SHIP_IMAGE,
        )
        self._wave = wave

    def update(self, input):
        # # Godmode
        # if (
        #     input.is_key_down("spacebar")
        #     or input.is_key_down("up")
        #     or input.is_key_down("f")
        # ):
        #     self.shoot()

        # Shoot form ship
        if not list(filter(lambda bolt: bolt.is_player_bolt, self._wave._bolts)):
            if (
                input.is_key_down("spacebar")
                or input.is_key_down("up")
                or input.is_key_down("f")
            ):
                self.shoot()

        # Movement
        if input.is_key_down("left") or input.is_key_down("j"):
            self.move_left()

        if input.is_key_down("right") or input.is_key_down("l"):
            self.move_right()

    def move_right(self):
        if self.x < GAME_WIDTH - 1 / 2 * SHIP_WIDTH:
            self.x += SHIP_MOVEMENT

    def move_left(self):
        if self.x > 1 / 2 * SHIP_WIDTH:
            self.x -= SHIP_MOVEMENT

    def shoot(self):
        self._wave._bolts.append(Bolt(self, "up", is_player_bolt=True))

    def get_wave(self):
        return self._wave

    def collides(self, bolt):
        if bolt.is_player_bolt:
            return False

        for corner in bolt.get_corners():
            if self.contains(corner):
                return True

        return False


class Alien(GImage):
    """
    A class to represent a single alien.

    At the very least, you want a __init__ method to initialize the alien
    dimensions. These dimensions are all specified in consts.py.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like giving each alien a score value).
    """

    #  IF YOU ADD ATTRIBUTES, LIST THEM BELOW

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN

    # METHOD TO CHECK FOR COLLISION (IF DESIRED)

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

    def __init__(self, wave, col_number, **keywords):
        super().__init__(**keywords)
        self._wave = wave
        self._col_number = col_number

    def move_right(self):
        self.x += ALIEN_H_WALK

    def move_left(self):
        self.x -= ALIEN_H_WALK

    def move_down(self):
        self.y -= ALIEN_V_WALK

    def get_wave(self):
        return self._wave

    def get_column(self):
        return self._col_number

    def shoot(self):
        if self._wave:
            self._wave._bolts.append(Bolt(self, "down"))

    def collides(self, bolt):
        if not bolt.is_player_bolt:
            return False

        for corner in bolt.get_corners():
            if self.contains(corner):
                return True

        return False


class Bolt(GRectangle):
    """
    A class representing a laser bolt.

    Laser bolts are often just thin, white rectangles. The size of the bolt
    is determined by constants in consts.py. We MUST subclass GRectangle,
    because we need to add an extra (hidden) attribute for the velocity of
    the bolt.

    The class Wave will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with
    no setters for the velocities.  That is because the velocity is fixed and
    cannot change once the bolt is fired.

    In addition to the getters, you need to write the __init__ method to set
    the starting velocity. This __init__ method will need to call the __init__
    from GRectangle as a  helper.

    You also MIGHT want to create a method to move the bolt.  You move the
    bolt by adding the velocity to the y-position.  However, the getter
    allows Wave to do this on its own, so this method is not required.
    """

    # INSTANCE ATTRIBUTES:
    # Attribute _velocity: the velocity in y direction
    # Invariant: _velocity is an int or float

    _direction: Literal["up", "down"] = "up"
    is_player_bolt: bool = False

    def __init__(
        self,
        game_object: Union[Alien, Ship],
        direction: Literal["up", "down"],
        is_player_bolt=False,
    ):
        super().__init__()
        self.height = BOLT_HEIGHT
        self.width = BOLT_WIDTH
        self.linewidth = 2
        self.linecolor = [0, 0, 0, 1]

        self._direction = direction
        self.is_player_bolt = is_player_bolt

        if is_player_bolt:
            self.x = game_object.x
            self.y = game_object.y + 0.5 * SHIP_HEIGHT
        else:
            self.x = game_object.x
            self.y = game_object.y - 0.5 * ALIEN_HEIGHT

        self._wave = game_object.get_wave()

    def update(self):
        if self.bottom > GAME_HEIGHT or self.top < 0:
            if self._wave:
                if self._wave._bolts:
                    self._wave._bolts.remove(self)

        if self._direction == "up":
            self.move_up()

        elif self._direction == "down":
            self.move_down()

    def move_up(self):
        self.y += BOLT_SPEED

    def move_down(self):
        self.y -= BOLT_SPEED

    def corner(self, dx, dy):
        x, y = self.x, self.y
        x -= dx * (1 / 2 * BOLT_WIDTH)
        y += dy * (1 / 2 * BOLT_HEIGHT)
        return x, y

    def get_corners(self):
        tr = self.corner(1, 1)
        br = self.corner(1, -1)
        tl = self.corner(-1, 1)
        bl = self.corner(-1, -1)

        return tl, tr, br, bl


# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE
