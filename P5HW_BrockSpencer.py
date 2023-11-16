#Spencer Brock
#11/16/2023
#using if else, loop, fuctions and random numbers

import random

def show_menu():
    print()
    print("Welcome to Math Quiz")
    print("MAIN MENU")
    print("-----------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")


def adding():
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    print(num1, "+", num2)
    my_sum = num1 + num2
    
    #print("The sum is: ", my_sum)
    return my_sum

def subtracting():
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    print(num1, "-", num2)
    my_diff = num1 - num2
    #print("The difference is: ", my_sum)
    return my_diff

def guessing(guess, value):
    num_guesses = 1
    while guess != value:
            num_guesses += 1 
            if guess > value:
                print("Your guess is too high")
                guess = int(input("Enter your guess: "))
            else:
                print("Your guess is too low")
                guess = int(input("Enter your guess: "))
    print("Congrats, your guess is correct!")
    print("It took you", num_guesses, "tries to get it right")
    
#Main function that runs the program
def main():
    
    
    while True:
        
        show_menu()
        user_choice = int(input("please choose one of the menu option: "))
        if user_choice == 1:
            value = adding()
            guess = int(input("Enter your guess: "))
            guessing(guess, value)
     
        if user_choice == 2:
            value = subtracting()
            guess = int(input("Enter your guess: "))
            guessing(guess, value)
           
        if user_choice == 3:
            print("The program has ended.")
            break
        
        
#Call the main fuction
if __name__ == "__main__":
    main()
