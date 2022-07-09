from random import randint as ri
from os import system



def findWord():
    wordfile = open('allmywords.txt', 'r')
    allwords = wordfile.readlines()
    wordfile.close()
    return allwords[ri(0, len(allwords)-1)][0:-1]

def createMan(incGuess):
    if incGuess == 0:
        return ''
    if incGuess == 1:
        return '|\n|\n|\n|\n|\n|'
    if incGuess == 2:
        return '________\n|/\n|\n|\n|\n|\n|'
    if incGuess == 3:
        return '________\n|/     |\n|\n|\n|\n|\n|'
    if incGuess == 4:
        return '________\n|/     |\n|       0\n|\n|\n|\n|'
    if incGuess == 5:
        return '________\n|/     |\n|       0\n|      /\\\n|\n|\n|'
    if incGuess == 6:
        return '________\n|/     |\n|       0\n|      /\\\n|        |\n|\n|'
    if incGuess == 7:
        return '________\n|/     |\n|       0\n|      /\\\n|        |\n|     /\\\n|'
    

def playGame():
    myWord = findWord()

if __name__ == '__main__':
    while True:
        print("Would you like to play hangman?")
        useranswer = input()
        if useranswer == "yes":
            playGame()
        if useranswer == "no":
            print("Goodbye")
            break






    
