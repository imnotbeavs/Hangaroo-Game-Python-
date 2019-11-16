import string
def isWordGuessed(secretWord, guessed):
    for indx in guessed:
        if indx in secretWord:
            guesss = True
        else:
            guesss = False
    return guesss

def getGuessedWord(secretWord, lettersGuessed):
    guessedlist = list(lettersGuessed)
    guessedWord = ''
    for indx2 in secretWord:
        if indx2 in guessedlist:
            guessedWord = guessedWord + indx2
        else:guessedWord = guessedWord + '_'
    return guessedWord

def getAvailableletters(lettersGuessed):
    l = list(string.ascii_lowercase)
    availletters = ''
    for indx3 in l:
        if indx3 not in lettersGuessed:availletters+=indx3
    return availletters

def Hangaroo(secretWord):
    tries = 0
    lettersGuessed = []
    availletters = string.ascii_lowercase
    guessedWord = ''
    
    print("Let's play Hangaroo!")
    print('The secret word has ',len(secretWord),' letters. Can you guess it?')
    while guessedWord != secretWord:
        casesensitive_guessed = input("Enter a letter(press 0 to quit) ") 
        guessed = casesensitive_guessed.lower()
        
        if guessed =='0':break
        if guessed not in string.ascii_letters:
            print('Invalid input. Pleas enter a letter') 
            continue
        if guessed not in availletters:
            print('You have already entered that')
            print(guessedWord)
            print('Available letters:',availletters)
            continue
        
        lettersGuessed.append(guessed)
        rightletter = isWordGuessed(secretWord,guessed)  

        if rightletter == False: 
            tries += 1
            print('Wrong')
            print("You've already made ",tries, 'mistakes')
        else:print('Correct! ',guessed,'is in the mystery word!')
            
        guessedWord = getGuessedWord(secretWord,lettersGuessed)
        print(guessedWord)
        
        availletters = getAvailableletters(lettersGuessed)  
        print('Available letters: ',availletters)

    if guessedWord == secretWord:
        print("Congratulations!!! You've guesses the right word!!") 
    else: print('Oh no,you did not guess the right word. It is ',secretWord)
   
    return
            
        
    
                    
                
                    
                
            

