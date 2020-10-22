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


# Main function
def main():
    # Check if there's a match between the regex and string
    # Triggered when the user clicks the button on the screen
    def testRegex():
        input_regex = regex.get()
        input_string = string.get()

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
            match_bg="SystemButtonFace" # Default background color
        
        # Update the match label
        matchLabel.config(text=result, bg=match_bg)
    
    
    # Initalize the window
    window = tk.Tk()

    # Set the window title and dimensions
    window.title("Regex Tester")
    window.geometry("600x400")

    # Generate the font and size
    font = ("Comic Sans MS", 20)

    # Regex label
    regexLabel = tk.Label(window, text="Enter your regex:", font=font)
    regexLabel.place(relx=0.5, y=25, anchor=tk.CENTER)

    # Regex input field
    regex = tk.StringVar()
    regexEntered = tk.Entry(window, textvariable=regex, font=font)
    regexEntered.place(relx=0.5, y=75, width=600, height=40, anchor=tk.CENTER)

    # String label
    stringLabel = tk.Label(window, text="Enter your text:", font=font)
    stringLabel.place(relx=0.5, y=150, anchor=tk.CENTER)

    # String input field
    string = tk.StringVar()
    stringEntered = tk.Entry(window, textvariable=string, font=font)
    stringEntered.place(relx=0.5, y=200, width=600, height=40, anchor=tk.CENTER)

    # Button (triggers regex test)
    button = tk.Button(window, text="Test Regex", command=testRegex, font=font, bg="#ffff00")
    button.place(relx=0.5, y=300, width=300, anchor=tk.CENTER)

    # Match label
    matchLabel = tk.Label(window, font=font)
    matchLabel.place(relx=0.5, y=375, anchor=tk.CENTER)

    # Run the tkinter loop
    window.mainloop()


# Execute the program
if __name__ == "__main__":
    main()
