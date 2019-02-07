''' A Keyboard Program
Created Fall 2015
Final Project - Part 2
@author Sarah Griffioen (slg27)
'''

from tkinter import *
from controller import *
from key import *
import random

class Keyboard:
    def __init__(self, canvas):
        # Create a list of each key on the keyboard
        self.key_list = []
        self.key_list.append(Key('c-type', 50, 250, 'C (1)'))
        self.key_list.append(Key('black', 85, 50, 'C sharp (1)'))
        self.key_list.append(Key('d-type', 100, 250, 'D (1)'))
        self.key_list.append(Key('black', 135, 50, 'E flat (1)'))
        self.key_list.append(Key('e-type', 150, 250, 'E (1)'))
        self.key_list.append(Key('c-type', 200, 250, 'F (1)'))
        self.key_list.append(Key('black', 235, 50, 'F sharp (1)'))
        self.key_list.append(Key('d-type', 250, 250, 'G (1)'))
        self.key_list.append(Key('black', 285, 50, 'G sharp (1)'))
        self.key_list.append(Key('d-type', 300, 250, 'A (1)'))
        self.key_list.append(Key('black', 335, 50, 'B flat (1)'))
        self.key_list.append(Key('e-type', 350, 250, 'B (1)'))
        self.key_list.append(Key('c-type', 400, 250, 'C (2)'))
        self.key_list.append(Key('black', 435, 50, 'C sharp (2)'))
        self.key_list.append(Key('d-type', 450, 250, 'D (2)'))
        self.key_list.append(Key('black', 485, 50, 'E flat (2)'))
        self.key_list.append(Key('e-type', 500, 250, 'E (2)'))
        self.key_list.append(Key('c-type', 550, 250, 'F (2)'))
        self.key_list.append(Key('black', 585, 50, 'F sharp (2)'))
        self.key_list.append(Key('d-type', 600, 250, 'G (2)'))
        self.key_list.append(Key('black', 635, 50, 'G sharp (2)'))
        self.key_list.append(Key('d-type', 650, 250, 'A (2)'))
        self.key_list.append(Key('black', 685, 50, 'B flat (2)'))
        self.key_list.append(Key('e-type', 700, 250, 'B (2)'))
        
        # Create a dictionary for the names of the notes and their corresponding numbers 
        self.keys = {}
        self.keys['C (1)'] = 0
        self.keys["C sharp (1)"] = 0.5
        self.keys['D (1)'] = 1
        self.keys['E flat (1)'] = 1.5
        self.keys['E (1)'] = 2
        self.keys['F (1)'] = 2.5
        self.keys['F sharp (1)'] = 3
        self.keys['G (1)'] = 3.5
        self.keys['G sharp (1)'] = 4
        self.keys['A (1)'] = 4.5
        self.keys['B flat (1)'] = 5
        self.keys['B (1)'] = 5.5
        self.keys['C (2)'] = 6
        self.keys['C sharp (2)'] = 6.5
        self.keys['D (2)'] = 7
        self.keys['E flat (2)'] = 7.5
        self.keys['E (2)'] = 8
        self.keys['F (2)'] = 8.5
        self.keys['F sharp (2)'] = 9
        self.keys['G (2)'] = 9.5
        self.keys['G sharp (2)'] = 10
        self.keys['A (2)'] = 10.5
        self.keys['B flat (2)'] = 11
        self.keys['B (2)'] = 11.5
        
        # Create a list of types of chords
        self.list_of_chords = ['major triad', 'minor triad', 'major augmented triad', 'minor augmented triad', 'major diminished triad', 'minor diminished triad', 'major triad in first inversion', 'minor triad in first inversion', 'major triad in second inversion', 'minor triad in second inversion']
     
    # Draw each key on the keyboard    
    def render(self, canvas):
        for key in self.key_list:
            key.render(canvas)
    
    # Generate a random type of chord to prompt the user with
    def get_random_chord_type(self):
        chord_type = random.choice(self.list_of_chords)
        return chord_type
    
    # Generate a random tonic key to prompt the user with
    def get_random_start_key(self, chord_type):
        if (chord_type == 'major triad') or (chord_type == 'minor triad'):
            shortened_list = self.key_list[0:17]
            return random.choice(shortened_list)
        elif (chord_type == 'major augmented triad') or (chord_type == 'minor augmented triad'):
            shortened_list = self.key_list[0:16]
            return random.choice(shortened_list)
        elif (chord_type == 'major diminished triad') or (chord_type == 'minor diminished triad'):
            shortened_list = self.key_list[0:18]
            return random.choice(shortened_list)
        elif (chord_type == 'major triad in first inversion') or (chord_type == 'minor triad in first inversion'):
            shortened_list = self.key_list[0:12]
            return random.choice(shortened_list)
        elif (chord_type == 'major triad in second inversion') or (chord_type == 'minor triad in second inversion'):
            shortened_list = self.key_list[0:8]
            return random.choice(shortened_list)
    
    # Determine if the user clicked the correct key     
    def which_key_clicked(self, x, y):
        for key in self.key_list:
            if key.click(x, y):
                return(key)
        raise TypeError('This key does not exist.')
    
    # In the dictionary, reverse lookup what the next note in the chord is supposed to be
    def reverse_lookup(self, dictionary, val):
        for x in dictionary:
            if dictionary[x] == val:
                for i in self.key_list:
                    if i.get_name() == x:
                        return i
                    
    # Create a list of all the notes that are supposed to be in the prompted major triad
    def create_major_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        second = self.reverse_lookup(self.keys, (start_val + 2))
        third = self.reverse_lookup(self.keys, (start_val + 3.5))
        major_triad = [start, second, third]
        return major_triad
    
    # Create a list of all the notes that are supposed to be in the prompted minor triad
    def create_minor_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        second = self.reverse_lookup(self.keys, (start_val + 1.5))
        third = self.reverse_lookup(self.keys, (start_val + 3.5))
        minor_triad = [start, second, third]
        return minor_triad
    
    # Create a list of all the notes that are supposed to be in the prompted major augmented triad
    def create_major_augmented_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        second = self.reverse_lookup(self.keys, (start_val + 2))
        third = self.reverse_lookup(self.keys, (start_val + 4))
        major_triad = [start, second, third]
        return major_triad
    
    # Create a list of all the notes that are supposed to be in the prompted minor augmented triad
    def create_minor_augmented_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        second = self.reverse_lookup(self.keys, (start_val + 1.5))
        third = self.reverse_lookup(self.keys, (start_val + 4))
        minor_augmented_triad = [start, second, third]
        return minor_augmented_triad
    
    # Create a list of all the notes that are supposed to be in the prompted major diminished triad
    def create_major_diminished_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        second = self.reverse_lookup(self.keys, (start_val + 2))
        third = self.reverse_lookup(self.keys, (start_val + 3))
        major_diminished_triad = [start, second, third]
        return major_diminished_triad
    
    # Create a list of all the notes that are supposed to be in the prompted minor diminished triad
    def create_minor_diminished_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        second = self.reverse_lookup(self.keys, (start_val + 1.5))
        third = self.reverse_lookup(self.keys, (start_val + 3))
        minor_diminished_triad = [start, second, third]
        return minor_diminished_triad
    
    # Create a list of all the notes that are supposed to be in the prompted first inversion major triad
    def create_first_inversion_major_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        first = self.reverse_lookup(self.keys, (start_val + 6))
        second = self.reverse_lookup(self.keys, (start_val + 2))
        third = self.reverse_lookup(self.keys, (start_val + 3.5))
        first_inversion_major_triad = [second, third, first]
        return first_inversion_major_triad
     
    # Create a list of all the notes that are supposed to be in the prompted first inversion minor triad   
    def create_first_inversion_minor_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        first = self.reverse_lookup(self.keys, (start_val + 6))
        second = self.reverse_lookup(self.keys, (start_val + 1.5))
        third = self.reverse_lookup(self.keys, (start_val + 3.5))
        first_inversion_minor_triad = [second, third, first]
        return first_inversion_minor_triad
    
    # Create a list of all the notes that are supposed to be in the prompted second inversion major triad   
    def create_second_inversion_major_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        first = self.reverse_lookup(self.keys, (start_val + 6))
        second = self.reverse_lookup(self.keys, (start_val + 8))
        third = self.reverse_lookup(self.keys, (start_val + 3.5))
        second_inversion_major_triad = [third, first, second]
        return second_inversion_major_triad
    
    # Create a list of all the notes that are supposed to be in the prompted second inversion minor triad   
    def create_second_inversion_minor_triad(self, canvas, start):
        start_name = start.get_name()
        start_val = self.keys[start_name]
        
        first = self.reverse_lookup(self.keys, (start_val + 6))
        second = self.reverse_lookup(self.keys, (start_val + 7.5))
        third = self.reverse_lookup(self.keys, (start_val + 3.5))
        second_inversion_minor_triad = [third, first, second]
        return second_inversion_minor_triad
        


