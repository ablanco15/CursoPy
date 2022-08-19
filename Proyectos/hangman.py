from glob import glob
import random
from threading import local
from words import words 
import string
import os

os.system('cls')
s = set(string.ascii_uppercase)
body = ["head", "body", "righ_arm", "left_arm", "righ_leg", "left_leg"]
used_letters =set()
    
def word_to_choose():
    word_choosen = random.choice(words)
    while(" " in word_choosen or "_" in word_choosen):
        word_choosen = random.choice(words)
    return word_choosen.upper()

def play():
    global word_choosen
    global spaces
    global letters_in_word_choosen
    global body
    global used_letters

    def add_letter(letter, word):
        global spaces
        for x, letter1 in enumerate(word):
            if letter1 == letter:
                spaces = spaces[:x] + letter + spaces[x+1:]        
        return spaces
    print()
    print()
    print("Playing...")
    print("word to guess: " + spaces)
    print()
    letter = ""
    while(letter not in s ):
        letter = input("Guess a letter: ")
        letter = letter.upper()

    print()    
    if(letter in letters_in_word_choosen ):
        print("pretty well, you found one letter")
        print()
        print()
        spaces = add_letter(letter,word_choosen)
        letters_in_word_choosen.discard(letter)
        used_letters.add(letter)
    
    elif( letter in used_letters ):
        print("This letter has already been used")
        print()
        print()
   
    else:
        print("this letter doesn't belong to the word")
        used_letters.add(letter)
        print()
        print("now your "+body[0] +" is hanging")
        if( body[0] == "righ_leg"):
            print()
            print("Choose carefully, you are about to die ")
            print()

        body.remove(body[0])
        print()
        print()
    
word_choosen = word_to_choose()
spaces = "_"*len(word_choosen)
letters_in_word_choosen = set(word_choosen)
i = 0

while( (spaces != word_choosen) and ( len(body) != 0 ) ):
    play()

if( spaces == word_choosen ):
    print("Congrats!!! the word was "+spaces+", You make it, and you'll keep living")
else:
    print("You've been hanged, We are so sorry, try in your next life")
