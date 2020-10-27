'''
Justin Farnsworth
Regex Tester
October 22, 2020

This program will allow the user to test their regular expressions.
The user will be provided two fields: a regex field and a string field.
The regex will be tested if any field contains text. Once the fields 
are filled out, the user will click the button, where the program will 
determine if there is a match.
'''

# Imported modules
import tkinter as tk
from re import search


# RegexTester class
class RegexTester(object):
    # Constructor
    def __init__(self):
        # Initalize the window
        self.__window = tk.Tk()

        # Set the window title and dimensions
        self.__window.title("Regex Tester")
        self.__window.geometry("600x400")

        # Generate the font and size
        self.__font = ("Comic Sans MS", 20)

        # Regex label
        self.__regexLabel = tk.Label(
            self.__window, 
            text="Enter your regex:", 
            font=self.__font
        )
        self.__regexLabel.place(relx=0.5, y=25, anchor=tk.CENTER)

        # Regex input field
        self.__regex = tk.StringVar()
        self.__regexEntered = tk.Entry(
            self.__window, 
            textvariable=self.__regex, 
            font=self.__font
        )
        self.__regexEntered.place(relx=0.5, y=75, width=600, height=40, anchor=tk.CENTER)
        self.__regexEntered.bind("<Return>", self.__testRegex)

        # String label
        self.__stringLabel = tk.Label(
            self.__window, 
            text="Enter your text:", 
            font=self.__font
        )
        self.__stringLabel.place(relx=0.5, y=150, anchor=tk.CENTER)

        # String input field
        self.__string = tk.StringVar()
        self.__stringEntered = tk.Entry(
            self.__window, 
            textvariable=self.__string, 
            font=self.__font
        )
        self.__stringEntered.place(relx=0.5, y=200, width=600, height=40, anchor=tk.CENTER)
        self.__stringEntered.bind("<Return>", self.__testRegex)

        # Button (triggers regex test)
        self.__button = tk.Button(
            self.__window, 
            text="Test Regex", 
            command=self.__testRegex, 
            font=self.__font, 
            bg="#ffff00", # Yellow
            activebackground="#ffff00" # Yellow
        )
        self.__button.place(relx=0.5, y=300, width=300, anchor=tk.CENTER)

        # Match label
        self.__matchLabel = tk.Label(
            self.__window, 
            font=self.__font
        )
        self.__matchLabel.place(relx=0.5, y=375, anchor=tk.CENTER)

        # Run the tkinter loop
        self.__window.mainloop()
    

    # Check if there's a match between the regex and string
    # Triggered when the user clicks the button on the screen
    def __testRegex(self, event=None):
        input_regex = self.__regex.get()
        input_string = self.__string.get()

        # Run the test if any of the fields are not empty
        if input_regex or input_string:
            # Check for a match
            if search(input_regex, input_string):
                result = "There is a match!"
                match_bg = "#00ff00" # Green
            else:
                result = "There is no match."
                match_bg = "#ff0000" # Red
        else: # Both fields are empty
            result = "Please fill out the fields above."
            match_bg = "SystemButtonFace" # Default background color
        
        # Update the match label
        self.__matchLabel.config(text=result, bg=match_bg)


# Execute the program
if __name__ == "__main__":
    RegexTester()
