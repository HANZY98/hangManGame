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
    gameProgress = ''
    for i in range (len(myWord)):
        gameProgress += '_'
    incorrect = 0
    guesses = []
    while True:
        _ = system('clear')
        # print(word)
        guessesString = ''
        for i in range(len(guesses)):
            if i != len(guesses) and i != 0:
                guessesString += ', '
            guessesString += guesses[i]
        print(f'Past guesses: {guessesString}')
        print(createMan(incorrect))
        if gameProgress == myWord:
            print(gameProgress)
            print("You win")
            break
        if incorrect >= 7:
            print('You Lose !')
            print(f'The word was {myWord}.')
            break
        print(gameProgress)
        print('Guess a letter!')
        guess = input()
        if guess not in guesses:
            guesses.append(guess)
        if guess in myWord:
            # print(f'The letter {guess} is in the word.')
            for i in range(len(myWord)):
                if guess == myWord[i]:
                    progressStart = gameProgress[0:i]
                    progressEnd = gameProgress[i+1:]
                    gameProgress = progressStart + guess + progressEnd
        else:
            incorrect += 1
            
        

if __name__ == '__main__':
    while True:
        print("Would you like to play hangman?")
        useranswer = input()
        if useranswer == "yes":
            playGame()
        if useranswer == "no":
            print("Goodbye")
            break






    
