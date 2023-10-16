import random

logo1 = """
                                       /\ 
    .__                  /\|\/\        / / 
  __|  |___    ______   _)    (__     / /  
 /__    __/   /_____/   \_     _/    / /   
    |__|                  )    \    / /    
                          \/\|\/    \/     


"""
print(logo1)
bored = True
userinterest = input("Do you wanna play a math game ? Type 'yes' or 'no': ")
if userinterest == 'no':
    bored = False
    exit()
score = 0
numofrounds = 0
while bored:
    operator = ['+', '-', '*', '/']
    num1 = random.randint(1, 101)
    num2 = random.randint(1, 101)
    opchoice = random.choice(operator)
    answer = int(input(f"{num1} {opchoice} {num2} = "))
    if answer == int(eval(f'{num1}{opchoice}{num2}')):
        score += 1
        print("You won ✅!")
    else:
        bored = False
    numofrounds += 1

print(f"Your final score is {score} out of {numofrounds} rounds.")