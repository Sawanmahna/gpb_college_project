# -*- coding: utf-8 -*-
"""
Created on Mon Jun  10 19:05:23 2024

@author: Sawan Kumar
"""

import nltk
from nltk.chat.util import Chat, reflections

#nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by Sawan Kumar. You can call me ChatGPT.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You?",]
    ],
    [
        r"(.*) fine",
        ["Nice to hear!",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse.",]
    ],
    [
        r"(.*) created ?",
        ["I was created by Sawan Kumar.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm based in the cloud.",]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is always great.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

chatbot = Chat(pairs, reflections)

def chat():
    print("Hi, how can I help? \n<<< Type 'quit' to exit. >>>\n")
    while True:
        user_input = input("User[🧑]: ")
        if user_input.lower() == "quit":
            print("ChatBot[🤖]: Bye for now. See you soon :)\n")
            break
        response = chatbot.respond(user_input)
        if response:
            print("ChatBot[🤖]:",response,"\n")
        else:
            print("ChatBot[🤖]: Sorry, I am unable to understand.\n")
            
if __name__ == "__main__":
    chat()
