# Lesson plan
  
**Input**

Opposite of Output
How we interact with the computer

input() -> prompt goes inside the brackets
MUST be assigned to a variable to save the value

Program waits until enter is pressed to move on with the rest of the code (stalls at the line that has input)

**concatenation** 
combining strings with the + symbol.

**f Strings**
Using a placeholder to put a string inside another one.

example 1:

word = "World"
print(f"Hello {word}")

example 2:

student1 = "Kalie"
student2 = "Steve"

print(f"Students: {student1} and {student2}")

Example Lesson:

'''
Lesson 3 - Input, concatenation and placeholders
Author: Mr. Kalisz
Date Created: September 4th, 2023
Date Last Modified: September 4th, 2023
'''

#Input is the opposite of output.  It is what the user can send into our code by interacting with it.  This is done while the code is running.

#Input will wait until the user finishes typing out their input before it proceeds on in the code.  Until enter is pressed, the code will wait.

input("This is a prompt") #Notice how whatever is typed in the brackets will appear when I run my code.  This is a prompt so that the user knows what to enter

#If input is not assigned to a variable, it will not be saved and will disappear after you press enter.  You must assigned input to a variable if you want to use it in your code

userWord = input("This input will be saved into the variable userWord: ")

#You can then output the input back to the user
#By using a + symbol with two strings, we can concatenation them together (put them side by side)  Notice there is no space between the words that is not already in the strings.
print("You typed: " + userWord)

#Or you can edit it first and then output it to the user.

userWord = userWord + " I added this on to your input."
print(userWord)

#F STRINGS
#Using a string literals to put a string inside another one.

#example 1: notice that there needs to be an _f_ before the quotations

word = "World"
print(f"Hello {word}")

#example 2: multiple string literals

student1 = "Kalie"
student2 = "Steve"

print(f"Students: {student1} and {student2}")