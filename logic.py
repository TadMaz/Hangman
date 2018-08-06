
from random import randint 
def access():
    '''opens txt file "Hangman" and selects random word'''
    
    #open file
    wrdfile = open("C:\\Users\\Tadi\\Documents\\Programming Projects\\Hangman.txt","r",encoding = 'utf-8')
    wrds = wrdfile.readlines()
    wrdfile.close()
    
    #remove empty space
    for wrd in wrds:
        wrd = wrd.strip()
    index = randint(0,len(wrds)-1)    
    r_wrd = wrds[index]
    r_wrd = r_wrd[0:]
    return r_wrd




def check_letter(letter, word):
    """checks if a specific single letter is in a word"""
    if letter in word:
        return True
    else:
        return False


def display_word(guessed_letters,word):
    """function displays a correct guessed letter and hides unguessed letters with an underscore"""
    for i in range(len(word)-1):
        if word[i] in guessed_letters:
            print (" "+word[i]+" ",end = "")
        else:
            print (" _ " ,end = "")


            

            
        
    

    
        
    
    
    
    
        
    
    
    

    
    
        
    
    
    
    
    
    

