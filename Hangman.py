def findWord():
    wordfile = open('words.txt', 'r')
    allwords = wordfile.readlines()
    wordfile.close()

def createMan(numIncorrectGuesses):

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





    
