#Hangman 
#Tadiwanashe Mazara
#Vacation project

import logic
import display

#*/*/*/*/*/*/*/* Beginning of program! */*/*/*/*/*/*/*#
def main():
    
    #display welcome and rules
    name = input("Enter your name to begin :")
    print("Hello "+str(name) + "!\n")
    display.welcome()
    
    #initial values and condition
    word = logic.access()
    gameOn = True
    disp_screen = 0
    chances = 6 
    guessed_letters = []
    
    
    
    #while in game
    print("The word is "+str(len(word) -1) + " letters long.\n")
    
    while gameOn:
        
        #prompt user for guess
        
        letter = input("Guess a letter(a-z) in the hidden word and press enter:\n").lower()
        valid = True
        
        #conditions to test letter input :
        
        if len(letter)>1:
            print("\nOops, seems like you entered too many characters\n")
            valid = False
            letter = input("Guess a letter(a-z) in the hidden word and press enter:\n")
            
            
        elif str(letter) in guessed_letters :
            print("You have already guessed that letter. Please try again!")
            valid = False
            letter = input("Guess a letter(a-z) in the hidden word and press enter:\n").lower()
        
        elif letter == "":
            cont = input("Do you want to quit the game?(yes/no)")
            if str(cont) == "yes":
                break
            else:
                letter = input("\nGuess a letter(a-z) in the hidden word and press enter:\n").lower()
                
        else:
            if not(letter.isalpha()):
                    
                print("Sorry, that's an invalid entry. Please try again!\n")
                valid = False
                letter = input("Guess a letter(a-z) in the hidden word and press enter:\n").lower()
                
                    
        #if guess is correct, remove the letter from the existing word and display Hangman and chances remaining
        
        if logic.check_letter(str(letter), word) == True:
            guessed_letters.append(letter)
            
            print ("\n Good Job! That's a correct guess!\n")
            display.Hangman(disp_screen)
            print()
            logic.display_word(guessed_letters, word)
            print()
            
            print("\n"+str(name)+" ,you have " + str(chances)+" chances remaining...\n")
            
            
        #if guess is incorrect, reduce chances ,display new hangman and chances remaining
        else:
            
            print("\n Sorry, that's an incorrect guess.\n")
            disp_screen +=1
            chances -=1
            display.Hangman(disp_screen)
            print()
            logic.display_word(guessed_letters, word)
            print()
            print("\n"+str(name)+" ,you have " + str(chances)+" chances remaining.\n")
            
        # Game Over Condition
        if chances == 0:
            print ("The hiddden word was: "+ word)
            again = input("<Press enter to finish>")
            gameOn = False
            
            
if __name__ == "__main__":
    main()            
        

        
    
    