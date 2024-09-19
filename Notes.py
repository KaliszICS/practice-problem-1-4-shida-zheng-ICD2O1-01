'''
    Lesson: Input and F strings
    Author: Mr. Kalisz
    Date Created: Sept 19, 2024
    Date Last Modified: Spet 19, 2024
'''

#Input - the opposite of output

# input() # Python will stop at this line of code and wait until the user types something and presses enter

# Input needs to be stored and is always a String

words = input() #stores the input into the variable words
print(words) #Outputs what was saved by input

# Prompt

words = input("Enter your name: ") #Put your prompt inside the brackets
print("Your name is " + words)

#Review Concatentation - placing two strings side by side to create a new one

word = "Hello " + "World"
print(word)

#F Strings

num = 2

word = f"Hello {words}, I hope you {num} have a good day"

#requires f in front of the string
#variables that you want placed in the string need to be inside {}

print(word)

