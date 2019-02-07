''' A GUI Controller System For the Music Theory Game
Created Fall 2015
Final Project - Part 1
@author Sarah Griffioen (slg27)
'''

# This program requires a screen that is at least 700 pixels wide and 467 pixels high

from tkinter import *
from keyboard import *
from key import *

class Music_Theory_Game:
    def __init__(self, window):
        # Create a label for the game
        title_label = Label(window, text="Music Theory Quiz", bg = 'tan', font = ("Comic Sans MS", 45, 'bold', 'underline'))
        title_label.grid(sticky = W + E + N + S, padx = 20, pady = 20) # I found how to position these how I wanted and how to change the font from effbot.org
       
        # Create a label to ask the prompts for a chord
        self.chord_prompt_text = StringVar()
        chord_prompt = Label(window, textvariable = self.chord_prompt_text, bg = 'tan', font = ("Comic Sans MS", 18))
        chord_prompt.grid(row = 1, sticky = W, padx = 100, pady = 5)
        self.count = 0
        
        #Create a button to indicate the action
        self.action_button_text = StringVar()
        self.action_button_text.set('Start Quiz')
        action_button = Button(window, textvariable = self.action_button_text, command = self.determine_next_action, font = ("Comic Sans MS", 18))
        action_button.grid(row = 1, sticky = E, padx = 100)
        
        # Create a label that keeps track of what keys have been pressed
        self.key_tracker_text= StringVar()
        key_tracker = Label(window, textvariable = self.key_tracker_text, bg = 'tan', font = ("Comic Sans MS", 18))
        key_tracker.grid(row = 2, sticky = W, padx = 100, pady = 20)
        self.count_click = 0
       
        # Create a label that keeps track of the score
        self.score_tracker_text= StringVar()
        score_tracker = Label(window, textvariable = self.score_tracker_text, bg = 'tan', font = ("Comic Sans MS", 18))
        score_tracker.grid(row = 2, sticky = E, padx = 100, pady = 5)
        self.count_right = 0
             
        # Create a label that shows the status of the user's click
        self.truth_value_text = StringVar()
        truth_label = Label(window, textvariable = self.truth_value_text, bg = 'tan', font = ("Comic Sans MS", 18))
        truth_label.grid(row = 3, sticky = W, padx = 100, pady = 5)
        
        # Create a canvas
        self._canvas = Canvas(window, width = 800, height = 300, bg = 'turquoise')
        self._canvas.grid(sticky = W + E + N + S, padx = 100, pady = 50)
        self._canvas.bind("<Button>", self.processClick)
        
        # Draw the keyboard
        self._piano = Keyboard(self._canvas)
        self._piano.render(self._canvas)

  
    # Determine the next action that the button will do
    def determine_next_action(self):
        if self.count > 10:
            self.count = 0
            self.count_right = 0
        self.count += 1
        self.count_click = 0
        
        # Create an empty list for the keys that are clicked on and create list of correct keys for each chord
        self.guessed_chord = []
        self.type_chord = self._piano.get_random_chord_type()
        self.start_key = self._piano.get_random_start_key(self.type_chord)
        
        # Regular chords
        if self.type_chord == 'major triad':
            self.chord = self._piano.create_major_triad(self._canvas, self.start_key)
        elif self.type_chord == 'minor triad':
            self.chord = self._piano.create_minor_triad(self._canvas, self.start_key)
            
        # Augmented chords
        elif self.type_chord == 'major augmented triad':
            self.chord = self._piano.create_major_augmented_triad(self._canvas, self.start_key)
        elif self.type_chord == 'minor augmented triad':
            self.chord = self._piano.create_minor_augmented_triad(self._canvas, self.start_key)
            
        # Diminished chords
        elif self.type_chord == 'major diminished triad':
            self.chord = self._piano.create_major_diminished_triad(self._canvas, self.start_key)
        elif self.type_chord == 'minor diminished triad':
            self.chord = self._piano.create_minor_diminished_triad(self._canvas, self.start_key)
            
        # First inversion chords
        elif self.type_chord == 'major triad in first inversion':
            self.chord = self._piano.create_first_inversion_major_triad(self._canvas, self.start_key)
        elif self.type_chord == 'minor triad in first inversion':
            self.chord = self._piano.create_first_inversion_minor_triad(self._canvas, self.start_key)
            
        # Second inversion chords
        elif self.type_chord == 'major triad in second inversion':
            self.chord = self._piano.create_second_inversion_major_triad(self._canvas, self.start_key)
        elif self.type_chord == 'minor triad in second inversion':
            self.chord = self._piano.create_second_inversion_minor_triad(self._canvas, self.start_key)
        
        # Set the textvariables when the button is pressed
        self.chord_prompt_text.set('Question %d: Please play a(n) %s %s.' % (self.count, self.start_key.get_name(), self.type_chord))
        self.key_tracker_text.set('Current Answer:')
        self.truth_value_text.set('')
        self.action_button_text.set('Forfeit Question')
        
        # Communicate the current score
        if (self.count == 1) or (self.count == 12):
            self.score_tracker_text.set('Current Score:  /10')
        else:
            self.score_tracker_text.set('Current Score: %d/10' % self.count_right)
            
        # Change text once the user finishes the quiz
        if self.count == 11:
            self.chord_prompt_text.set('You have completed the quiz!')
            self.action_button_text.set('Start New Quiz')
            self.key_tracker_text.set('')
            self.compute_score()
      
      
    # Process the click and add each key that was clicked onto the guessed_list
    def processClick(self, event):
        try:
            self.count_click += 1
            self.guessed_chord.append(self._piano.which_key_clicked(event.x, event.y))
            if self.count == 11:
                self.count_click -= 1   
            elif self.count_click == 1:
                self.key_tracker_text.set(self.key_tracker_text.get() + ' ' + self.guessed_chord[-1].get_name())
                self.truth_value_text.set('')
            elif 1 < self.count_click < len(self.chord):
                self.key_tracker_text.set(self.key_tracker_text.get() + ', ' + self.guessed_chord[-1].get_name())
                self.truth_value_text.set('')
            elif len(self.guessed_chord) == len(self.chord):
                self.key_tracker_text.set(self.key_tracker_text.get() + ', ' + self.guessed_chord[-1].get_name())
                self.check_chord()
        
        # Handle if the user clicks on an invalid part of a key    
        except:
            if 0 < self.count < 11:
                self.truth_value_text.set('The click was invalid. Please click inside a valid key area.')
                self.count_click -= 1
              
              
    # Check to see if the user played the correct chord
    def check_chord(self):
        count_correct = 0
        for i in range(len(self.chord)):
            if self.count_click <= len(self.chord):
                n1 = self.chord[i].get_name()
                n2 = self.guessed_chord[i].get_name()
                if (n1 == n2):
                    count_correct += 1
                    
        # If the quiz is still in progress, set the textvariables accordingly
        if (count_correct == len(self.chord)) and (self.count < 10):
            self.truth_value_text.set('Correct. Good job!')
            self.count_right += 1
            self.score_tracker_text.set('Current Score: %d/10' % self.count_right)
            self.action_button_text.set('Next Question')
        elif (self.count_click == len(self.chord)) and (count_correct != 3) and (self.count < 10):
            self.truth_value_text.set('Incorrect.')
            self.score_tracker_text.set('Current Score: %d/10' % self.count_right)
            self.action_button_text.set('Next Question')
        
        # If the quiz is finished, set the textvariables accordingly
        if (count_correct == len(self.chord)) and (self.count == 10):
            self.truth_value_text.set('Correct. Good job!')
            self.count_right += 1
            self.score_tracker_text.set('Current Score: %d/10' % self.count_right)
            self.action_button_text.set('Continue')
        elif (self.count_click == len(self.chord)) and (count_correct != 3) and (self.count == 10):
            self.truth_value_text.set('Incorrect.')
            self.score_tracker_text.set('Current Score: %d/10' % self.count_right)
            self.action_button_text.set('Continue')
             
      
    # Compute the final score of the game        
    def compute_score(self):
        average = int((self.count_right / 10) * 100)
        self.score_tracker_text.set('Final Score: %d/10 = %d' % (self.count_right, average) + '%')
    

# Main Code          
if __name__ == '__main__':
    window = Tk()
    window.title("Music Theory Quiz")
    window.configure(bg = 'tan') # I found how to make the whole screen a certain color on stackoverflow.com
    piano = Music_Theory_Game(window)
    window.mainloop()
    
    

