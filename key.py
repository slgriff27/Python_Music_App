''' A Key Program
Created Fall 2015
Final Project - Part 3
@author Sarah Griffioen (slg27)
'''

from tkinter import *

class Key:
    def __init__(self, type, x, y, name):
        self._type = type
        self._x = x
        self._y = y
        self._name = name
    
    # Access the name of the key    
    def get_name(self):
        return self._name
    
    # Draw the keys onto the canvas    
    def render(self, canvas):
        if self._type == 'c-type':
            # Create c and f keys
            canvas.create_polygon(self._x, self._y, self._x, (self._y - 200), (self._x + 35), (self._y - 200), (self._x + 35), (self._y - 75), (self._x + 50), (self._y - 75), (self._x + 50), self._y, self._x, self._y, outline = 'black', fill = 'white', width = 2, activefill = 'tan')
            
        elif self._type == 'd-type':
            # Create d, g, and a keys
            canvas.create_polygon(self._x, self._y, self._x, (self._y - 75), (self._x + 15), (self._y - 75), (self._x + 15), (self._y - 200), (self._x + 35), (self._y - 200), (self._x + 35), (self._y - 75), (self._x + 50), (self._y - 75), (self._x + 50), self._y, self._x, self._y, outline = 'black', fill = 'white', width = 2, activefill = 'tan')
             
        elif self._type == 'e-type':
            # Create e and b keys
            canvas.create_polygon(self._x, self._y, self._x, (self._y - 75), (self._x + 15), (self._y - 75), (self._x + 15), (self._y - 200), (self._x + 50), (self._y - 200), (self._x + 50), self._y, self._x, self._y , outline = 'black', fill = 'white', width = 2, activefill = 'tan')
            
        elif self._type == 'black':
            # Create black keys
            canvas.create_rectangle(self._x, self._y, (self._x + 30), (self._y + 125), outline = 'black', fill = 'black', width = 2, activefill = 'tan')
            
            
    # Determine if the user clicked on the key that was asked for     
    def click(self, x, y):       
        if self._type == 'c-type':
            if (self._x <= x <= (self._x + 35)) and ((self._y - 200) <= y <= self._y):
                return True
            else:
                return False
        if self._type == 'd-type':
            if ((self._x + 15) <= x <= (self._x + 35)) and ((self._y - 200) <= y <= self._y):
                return True
            else:
                return False
        if self._type == 'e-type':
            if ((self._x + 15) <= x <= (self._x + 50)) and ((self._y - 200) <= y <= self._y):
                return True
            else:
                return False
        if self._type == 'black':
            if (self._x <= x <= (self._x + 30)) and (self._y <= y <= (self._y + 125)):
                return True
            else:
                return False

          
                 
                 

