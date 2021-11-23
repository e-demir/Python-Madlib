import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word  or ' ' in word:
        word = random.choice(words)    
    return word.upper()

def hangman():
    word = get_valid_word(words) # the word to guess
    word_letters = set(word) # collection of letters of selected word
    alphabet = set(string.ascii_uppercase) #all alphabet letters
    used_letters = set() # user guess letters, firstly empty
    lives = 6 # try count, firstly 6

    while len(word_letters) > 0 and lives > 0:  # still have life and has missing letters
        
        print("You have", lives, "lives left and used letters are : ", " ".join(used_letters))

        # what current word is (ie W - R D)
        letters_in_word = [letter if letter in used_letters else '-' for letter in word] # if iteration item in used_letter list, use item if not use "-"
        
        print('Current word: ', " ".join(letters_in_word)) # then join the list with empty spaces        
        
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters: # alphabet letters minus used letters. Remaining letters from alpahabet after extracting the used ones. Remaining alphabet letters
            
            used_letters.add(user_letter)

            if user_letter in word_letters: #successfull
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes a life if wrong
                print("Letter not in word")

        elif user_letter in used_letters: #already used the character
            print("You already used this character")

        else:
             print("Invalid character. Please try again")

    if lives == 0:
        print("Sorry, you died. The word was",word)
    else:
        print("You guessed the word :",word,"!!!")
    # gets here when len(word_letters) == 0 or when lives == 0

hangman()