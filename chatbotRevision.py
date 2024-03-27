#Nathan Lawson
#Exercise 4
#Last updated: October 4, 2021

import time
import sys
import random

def chatbot1():

    file = open("favoirteFoods.txt", "a")
    
    print("Hello, my name is Procrastination. I'm a chatbot designed to help you procrastinate during class!")

    time.sleep(1)

    name = input("What's your name?")

    time.sleep(2)

    food = input("It's nice to meet you "+ name +". I'd like to get to know you better, what's your favorite food?")

    print("Oh I've never tried " + food + " before, I'll add it my list of foods I have to try!")

    file.write('\n'+name+": "+food)

    file.close()

    time.sleep(2)

    print("But back to the task at hand, I offer two games you can play!")

    gameOptions = ["hangman", "number guess"]

    print("Here are your options: ")

    print(*gameOptions, sep = " ,")

    time.sleep(3)

    choice = input("What game would you like to play?")

    choice.lower()

    if choice == gameOptions[0]:

        hangman()

    elif choice == gameOptions[1]:

        guessNumber()

def chatbot2():

    print("Hope your having a good time, what would you like to play now?")

    time.sleep(1)

    gameOptions = ["hangman","guess the major","guess a number"]

    print("Here are your options: ")

    print(*gameOptions, sep = " ,")

    time.sleep(3)

    choice = input("What game would you like to play?")

    choice.lower()

    if choice == gameOptions[0]:

        hangman()

    elif choice == gameOptions[1]:

        guessNumber()

def hangman():

    listOfWords = {"Morgantown", "Interactive", "Design", "Media", "Reed", "Advertising", "Journalism", "Evansdale", "Mountaineer"}

    word = random.choice(listOfWords)

    time.sleep(2)

    print("Welcome to Hangman, all the words with this game are associated with the Reed College of Media and WVU.")

    guess = ''

    tries = 10

    # This while loop determines if the player input is correct and counts the number of tries the player has left.
    while tries > 0:

            #Player amount of incorrect guesses
            fails = 0

            #For loop to see if player guess is within the word
            for char in word:

                    if char in guess:

                            print(char)

                    else:

                            print("_")

                            #Wrong guess, # of fails increases by 1
                            fails += 1

            if fails == 0:
                    print("You Win")

                    print("The word is: ",word)

                    restart = print("Do you wish to play again? Press 1 for yes or 0 speak with Procrastination again.")

                    if restart == 1:

                        hangman()

                    elif restart == 0:

                        chatbot2()

            guesses = input("guess a character:")

            guess += guesses

            #For loop for lowering the value of tries by 1, when player incorrectly guesses
            if guesses not in word:

                    tries -= 1

                    print("Wrong")

                    print("You have", + tries, 'more guesses')

                    if tries == 0:
                            print("You Loose")

                            print("The word was: ",word)

                            restart = print("Do you wish to play again? Press 1 for yes or 0 speak with Procrastination again.")

                    if restart == 1:

                        hangman()

                    elif restart == 0:

                        chatbot2()

def guessNumber():

    print("Welcome to guess the Number!")

    playerGuesses = 0

    number = random.randint(1,100)

    while playerGuesses < 5:

        print("I'm thinking of a number between 1 & 100. Take a guess!")

        guess = input()

        guess = int(guess)

        playerGuesses +=1

        if guess < number:

            print("Your Guess is too low")

        if guess > number:

            print("Your guess is too high")

        if guess == number:

            break
        
    if playerGuesses == 5:

        print("You lose, the number was " +number)

    if guess == number:

        print("Congratulations, you Win! Your number was " + number)

        restart = print("Do you wish to play again? Press 1 for yes or 0 speak with Procrastination again.")

        if restart == 1:

            guessNumber()

        elif restart == 0:

            chatbot2()

        
chatbot1()
            

            

        
