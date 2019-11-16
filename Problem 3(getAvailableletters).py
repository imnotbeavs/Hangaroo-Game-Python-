import string

def getAvailableletters(lettersGuessed3):
    l = list(string.ascii_lowercase)
    availletters = ''
    for indx3 in l:
        if indx3 not in lettersGuessed3:  availletters+=indx3
    return availletters