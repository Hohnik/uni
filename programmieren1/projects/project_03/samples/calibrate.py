"""
Module to calibrate Game2d

Some graphics cards (particularly on Windows) do a poor job coordinating mouse clicks to
pixels.  This is test program to see if everything is okay.

Author: Walker M. White (wmw2)
Date:   November 20, 2019
"""
import introcs
from game2d import *
from kivy.metrics import dp, sp, Metrics

############# CONSTANTS #############
# Window Size
WINDOW_WIDTH  = 512
WINDOW_HEIGHT = 512


############# CONTROLLER CLASS #############
class Calibrate(GameApp):
    """
    This class is to test the drawing size in game2d on weird graphics cards.
    
    Attribute view : the view (inherited from GameApp) 
    Invariant: view is an instance of GView
    
    Attribute blocks:  the four corners 
    Invariant: blocks is a list of GRectangle objects
    
    Attribute crosses: hatches for the four corners
    Invariant: crosses is a list of GPath objects
    """
    
    # THE THREE MAIN METHODS
    def start(self):
        """
        Initializes the application, creating new attributes.
        """
        size = 40
        rect1 = GRectangle(left=0,bottom=0,width=size,height=size,fillcolor='red')
        rect2 = GRectangle(left=0,top=WINDOW_HEIGHT,width=size,height=size,fillcolor='green')
        rect3 = GRectangle(right=WINDOW_WIDTH,bottom=0,width=size,height=size,fillcolor='blue')
        rect4 = GRectangle(right=WINDOW_WIDTH,top=WINDOW_HEIGHT,width=size,height=size,fillcolor='black')
        self.blocks = [rect1,rect2,rect3,rect4]
        
        cross1 = GPath(points=[size//2,0,size//2,size],linewidth=1.1,linecolor='white')
        cross2 = GPath(points=[0,size//2,size,size//2],linewidth=1.1,linecolor='white')
        cross3 = GPath(points=[size//2,WINDOW_HEIGHT,size//2,WINDOW_HEIGHT-size],linewidth=1.1,linecolor='white')
        cross4 = GPath(points=[0,WINDOW_HEIGHT-size//2,size,WINDOW_HEIGHT-size//2],linewidth=1.1,linecolor='white')
        cross5 = GPath(points=[WINDOW_WIDTH-size//2,0,WINDOW_WIDTH-size//2,size],linewidth=1.1,linecolor='white')
        cross6 = GPath(points=[WINDOW_WIDTH,size//2,WINDOW_WIDTH-size,size//2],linewidth=1.1,linecolor='white')
        cross7 = GPath(points=[WINDOW_WIDTH-size//2,WINDOW_HEIGHT,WINDOW_WIDTH-size//2,WINDOW_HEIGHT-size],linewidth=1.1,linecolor='white')
        cross8 = GPath(points=[WINDOW_WIDTH,WINDOW_HEIGHT-size//2,WINDOW_WIDTH-size,WINDOW_HEIGHT-size//2],linewidth=1.1,linecolor='white')
        self.crosses = [cross1,cross2,cross3,cross4,cross5,cross6,cross7,cross8]
        print('Scale Factor',dp(1))
        print('Font Factor', sp(1))
        print('Dimensions',512*dp(1))
        print('Density',Metrics.density)
        print('DPI Flat',Metrics.dpi)
        print('Rounded',Metrics.dpi_rounded)
        
    
    def update(self,dt):
        """
        Updates the application.
        
        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        pass
    
    def draw(self):
        """
        Draws the four corners
        """
        for block in self.blocks:
            block.draw(self.view)
            
        for cross in self.crosses:
           cross.draw(self.view)


# Application Code
if __name__ == '__main__':
    Calibrate(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()
