def getGuessedWord(secretWord2, lettersGuessed2):
    guessed = ''
    for indx2 in secretWord2:
        if indx2 in lettersGuessed2:
            guessed += indx2
        else: guessed = guessed + '_'
    
    return guessed