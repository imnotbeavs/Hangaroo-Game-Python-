def isWordGuessed(secretWord, lettersGuessed):
    for indx in lettersGuessed:
        checker = indx in secretWord
        if checker == True:pass
        else: break
     
    return checker
