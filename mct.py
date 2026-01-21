import tkinter as tk
from tkinter import scrolledtext,Label
import winsound
import time
 
# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', 
    '-': '-....-', '\'' : '.----.' , '\"' : '.-..-.' , '(': '-.--.', 
    ')': '-.--.-', '&' : '.-...' , '@' : '.--.-.' , ':' : '---...' , 
    '=' : '-...-' , '!' : '-.-.--' , '+' : '.-.-.' ,' ' : ' '
}
# Function to translate Text into Morse Code ....
def text_to_morse(input_text):
    morse_code = ''
    for char in input_text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    return morse_code

# Function to translate Morse Code into Text ....
def morse_to_text(input_morse):
    words = input_morse.split('   ')
    translated_text = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            translated_text += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(letter)]
        translated_text += ' '
    return translated_text

# Function to play Morse Code as sound ....
def play_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(1000, 200)  # Beep for dot
        elif symbol == '-':
            winsound.Beep(1000, 600)  # Beep for dash
        elif symbol == ' ':
            time.sleep(0.6)  # Pause between alphabets
        elif symbol == '  ':
            time.sleep(1.4)  # Pause between words

# Function for Clear All button handler
def clear_textboxes():
    input_textbox.delete(1.0, tk.END)
    output_textbox.delete(1.0, tk.END)

# Function for Text to Morse button handler
def translate_text_to_morse():
    input_text = input_textbox.get(1.0, tk.END).strip()
    morse_code = text_to_morse(input_text.upper())
    output_textbox.delete(1.0, tk.END)
    output_textbox.insert(tk.END, morse_code)

# Function for Morse to Text button handler
def translate_morse_to_text():
    input_morse = input_textbox.get(1.0, tk.END).strip()
    text = morse_to_text(input_morse)
    output_textbox.delete(1.0, tk.END)
    output_textbox.insert(tk.END, text)

# Function for play Morse Code handler
def play_morse_code_button():
    morse_code1 = input_textbox.get(1.0, tk.END).strip()
    play_morse_code(morse_code1)
    morse_code2 = output_textbox.get(1.0, tk.END).strip()
    play_morse_code(morse_code2)

# Create the main root window
root = tk.Tk()
root.title("Morse Code Translator")
root.resizable(False, False)
root.config(bg='#6FAFE7')

# Set image in icon 
# icon=tk.PhotoImage(file='morse-code.png')
icon = tk.PhotoImage(file=r"c:\Users\Adarsh Trivedi\PROJECT\portfolio-responsive-complete-main\project\\morse-code.png")
root.iconphoto(False,icon)

# Create main heading
heading= Label(root,text="MORSE CODE TRANSLATOR",padx=50,pady=15,bg='#6FAFE7',font=("Algerian",25))
heading.pack()

# Create Scrolled Textbox for input field
input_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10,font=("Arial",12))
input_textbox.insert(tk.END, "Input goes here...")
input_textbox.pack(padx=50, pady=10)

# Create Scrolled Textbox for output field
output_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10,font=("Arial",12))
output_textbox.insert(tk.END, "Output comes here...")
output_textbox.pack(padx=50, pady=10)

# Create Clear All button
clear_button = tk.Button(root, text="Clear All ", command=clear_textboxes,font=("Arial",12))
clear_button.pack(pady=5)

# Create Text to Morse button
text_to_morse_button = tk.Button(root, text="Text to Morse", command=translate_text_to_morse,font=("Arial",12))
text_to_morse_button.pack(padx=50,pady=20,side= 'left')

# Create Morse to Text button
morse_to_text_button = tk.Button(root, text="Morse to Text", command=translate_morse_to_text,font=("Arial",12))
morse_to_text_button.pack(padx=50,pady=20,side='right')

# Create Play Morse button
play_morse_button = tk.Button(root, text="Play Morse Code", command=play_morse_code_button,fg="Green",font=("Arial",12))
play_morse_button.pack(pady=20)

# Run the main loop 
root.mainloop()