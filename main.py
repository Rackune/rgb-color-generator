# add random import to the top of the file
import os
import random
from os import system

#output the integers to use for the color picker
val = [random.randint(0, 255) for _ in range(3)]
def genColor():
    rgb = [random.randint(0, 255) for _ in range(3)]
    value = f"R:{rgb[0]} G:{rgb[1]} B:{rgb[2]}"
    print("Your random color is:\n", value)
    return rgb

print("Welcome to the Random Color Picker!")
input("Press Enter to generate a color: ")

while True:
    genColor()
    option = input("Press Enter to generate a new color, or 'q' to quit: ")
    if option == 'q':
        break


# add a while loop to continue generating colors



    # FIx the continue `while` loop


 # rewrite the loop for new color generation




# create function using val to determine the color hues(Primary, Secondary,etc)





