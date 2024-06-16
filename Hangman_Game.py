# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:44:45 2024

@author: Sawan Kumar
"""
import random

def choose_word():
    words={
        "Animals": ['elephant', 'tiger', 'lion', 'zebra'],
        "Fruits": ['mango', 'apple', 'banana', 'cherry', 'date'],
        "Programming": ['java', 'javascript', 'html', 'css', 'python']
    }
    
    category=random.choice(list(words.keys()))
    word=random.choice(words[category])
    return category,word

def display_word(word,guessed_letters):
    display_list=[]
    for letter in word:
        if letter in guessed_letters:
            display_list.append(letter)
        else:
            display_list.append('_ ')
    displayed_word=' '.join(display_list)
    return displayed_word

def play_hangman():
    category,word=choose_word()
    guessed_letters=set()
    incorrect_guessess=0
    max_incorrect_guessess=6
    
    print("Welcome to Hangman Game!")
    print("Category: ",category)
    
    while incorrect_guessess<max_incorrect_guessess:
        print("\nWord: ",display_word(word, guessed_letters))
        print("Guessed Letters: ",', '.join(sorted(guessed_letters)))
        print("Incorrect Guesses Left: ",max_incorrect_guessess-incorrect_guessess)
        
        guess=input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed this letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good Guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guessess +=1
            print("Wrong Guess!")
        
        if set(word).issubset(guessed_letters):
            print("\nCongratulations! You've guessed the word: ",word)
            break
    else:
        print("\nSorry, you've run out of guesses. The word was: ",word)

if __name__=="__main__":
    play_hangman()
        
input("\nPress any key to Exit...")        
        
    