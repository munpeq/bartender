#!/usr/bin/python
import os


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

os.system('clear')
def drinks(questions, ingredients):
    for question in questions:
        print questions[question]
        answer = raw_input("   yes or no : ")
        if answer == "yes" or answer == "y":
          os.system('clear')
          print "Here's how to make your drink: \n" , ingredients[question]
          break
        else:
          pass
    return question

    
if __name__ == '__main__':
  drinks(questions, ingredients)