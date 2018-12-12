
import time

import random

#Welcome title beg
welcome = "Welcome to Wheel of Fortune"
for i in range(2):
    for i in range(len(welcome)+4):
        print (".", end="")
    print ("")

print( ".." + welcome + "..")

for i in range(2):
    for i in range(len(welcome)+4):
        print (".", end="")
    print ("")

print ("")
print ("")
#welcome end

#categories beg
print ("Choose a number corresponding to your word category: ")
print ("1. Foods")
print ("2. Places")
print ("3. Common Sayings")
print ("4. Sport Terminolgies")
category = input("You choose number: ")
#categories end


#guess word beg
#open file corresponding with chosen category
inFile = open('foods.txt', 'r')
content =  inFile.read().splitlines()
inFile.close()

rand = random.randint(0,len(content)-1)
guessWord = content[rand]

splitWord = list(guessWord)

#create hangman emply lines to guess
for i in range(len(splitWord)):
    print ("_ ", end="")
print ("")

#guess letters
guessLetter = input("Guess a letter: ")

correctLetter = 0

while correctLetter < len(splitWord):
    if guessLetter in splitWord:
        correctLetter +=1
        print ("Yes")

    else:
        guessLetter = input("Please guess again: ")
