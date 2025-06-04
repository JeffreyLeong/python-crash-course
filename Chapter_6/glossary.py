"""
A Python dictionary can be used to model an acutal dictionary.
However, to avoid confusion, let's call it a glossary.

- Think of five programming words you've learned about in the 
previous chapters. Use these words as the keys in your glossary,
and store their meanings as values.

- Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning,
or print the word on one line and then print its meaning indented 
on a second line. Use the newline character (\n) to insert a blank 
line between each word-meaning pair in your output.
"""

glossary = {
    "print": "shows the output of your code on the terminal.",
    "input": "asks user to type in a input that is used to produce results.",
    "type": "a way to check on what type is the variable.",
    "import": "brings in a module from a different libary.",
    "for loop": "a loop that executes a number of times",
}

for word, meaning in glossary.items():
    print(f"{word.title()}\n - {meaning.capitalize()}")