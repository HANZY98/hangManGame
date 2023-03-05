import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["beans", "chocolate", "teeth"]

correctGuess = False

ran_word = random.choice(words)

word = []

length_word = []

inc_guesses = 0

usererror = False

def sortWords():
    i = 0
    while i < len(ran_word):
        length_word.append('_')
        newPos = ran_word[i]
        word.append(newPos)
        i += 1

def reset():
    inc_guesses = 0
    ran_word = random.choice(words)
    word.clear()
    length_word.clear()

sortWords()

print('Welcome to Hangman !')

print('\n')

myinp = input('This will contain rules, press y to explain the rules or any other key to continue straight to the game\n')

myinp.lower()

if myinp == 'y':
    print('print rules')
else:
    print('continuing to game...')
    print('\n')

while correctGuess == False:

    if str(length_word).strip('[]') == str(word).strip('[]'):
        print(*length_word)
        print('You have won !')
        break
    
    print('\n')
    print(*length_word)
    print('\n')
    letter_Guess = input('please take a guess !')
    letter_Guess.lower()

    
    if letter_Guess not in word:
        print('This is incorrect\n')
        print(HANGMANPICS[inc_guesses] + '\n')
        inc_guesses += 1
        if(inc_guesses > 7):
            print('Oh no ! Frankie is nearly hung')
        if(inc_guesses == 7):
            print('Unfortunately Frankie has been hung, all is lost')
            playagain = input('Would You like to play again ? (Y/N)')
            playagain.lower()
            if playagain == 'n':
                correctGuess = True
            elif playagain == 'y':
                reset()
                sortWords()
            else:
                playagain2 = input('Please enter (Y/N)')
                if playagain2 == 'n':
                    correctGuess = True
                elif playagain2 == 'y':
                    reset()
                    sortWords()
                else:
                    break
        
    if letter_Guess in length_word and j == len(word):
        print('You have already used that letter')
        
     
    j=0
    while j < len(word):
        
        if letter_Guess == word[j] and length_word[j] == "_":
            length_word.pop(j)
            length_word.insert(j, letter_Guess)
        
        j += 1

print('Thanks for playing ! See you again soon !')



#THINGS TO DO!
#add more words
#if play again is not entered correctly, then make sure it asks them again
#Make sure that re-setting the game makes it fully playable.
#Re-factor, turn correct guess loop into a playgame function





    


        
    
        
    

            



        
    




    


