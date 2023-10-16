import random

logo = """
  _________    _____   ____  
  / ___\__  \  /     \_/ __ \ 
 / /_/  > __ \|  Y Y  \  ___/ 
 \___  (____  /__|_|  /\___  >
/_____/     \/      \/     \/ 

"""
print(logo)
print("Welcome to the Number Guessing Game!")


def easy_level(z):
    i = z
    num = random.randint(1, 100)
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number.")
        userinput = int(input("Make a guess : "))
        if userinput == num:
            print("You won")
            break
        elif userinput < num:
            print("You are two low.")
            i -= 1
        elif userinput > num:
            print("You are two high")
            i -= 1
        else:
            print("Sorry !")
    print(f"This is the number {num}")


def game_here():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        easy_level(10)
    elif level == 'hard':
        easy_level(5)


game_here()
