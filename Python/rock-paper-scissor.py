import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_rule = [rock, paper, scissor]
usr_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissor \n"))
print(game_rule[usr_choice])
com_choice = random.randint(0, len(game_rule)-1)
print(game_rule[com_choice])
if usr_choice >= 3 or usr_choice < 0:
    print("You choose Invalid option, you lose!")
elif com_choice == usr_choice:
    print("Match drawn!")
elif com_choice == 0 and usr_choice == 1 :
    print("You wins!")
elif com_choice == 0 and usr_choice == 2 :
    print("You wins!")