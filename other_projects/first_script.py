import tkinter as tk
from random import choice

# Tech-related vocabulary
tech_words = ['cache', 'cloud', 'debug', 'array', 'proxy',]

# Function to compare guesses with the actual word
def check_word(guess, word):
    result = ['gray'] * len(word)
    word_chars = list(word)
    
    # First pass: check correct letters in the correct place
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result[i] = 'green'
            word_chars[i] = None  # Mark this character as used
    
    # Second pass: check correct letters in the wrong place
    for i in range(len(guess)):
        if result[i] == 'gray' and guess[i] in word_chars:
            result[i] = 'yellow'
            word_chars[word_chars.index(guess[i])] = None  # Mark this character as used
            
    return result

# Function to process the guess
def process_guess():
    guess = entry.get().lower()
    if len(guess) != 5:
        feedback_label.config(text="Word must be 5 letters long!", fg='red')
        return

    if guess not in tech_words:
        feedback_label.config(text="Word not in tech vocabulary!", fg='red')
        return

    result = check_word(guess, word)
    
    # Update the result labels with colors
    for i in range(5):
        guess_labels[i].config(text=guess[i].upper(), bg=result[i])

    if guess == word:
        feedback_label.config(text="You guessed it right!", fg='green')
        guess_button.config(state='disabled')  # Disable guessing after win
    else:
        feedback_label.config(text="Try again!", fg='blue')

# Initialize the game window
root = tk.Tk()
root.title("Tech Wordle")

# Pick a random word from the tech vocabulary
word = choice(tech_words)

# Create the input entry
entry_label = tk.Label(root, text="Enter your guess (5-letter tech word):")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create the guess button
guess_button = tk.Button(root, text="Guess", command=process_guess)
guess_button.pack()

# Create labels to display guess results
guess_labels = [tk.Label(root, text="_", width=5, height=2, font=('Helvetica', 24), bg='white') for _ in range(5)]
for label in guess_labels:
    label.pack(side=tk.LEFT, padx=5, pady=10)

# Feedback label
feedback_label = tk.Label(root, text="")
feedback_label.pack()

# Start the GUI event loop
root.mainloop()