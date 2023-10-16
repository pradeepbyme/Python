
def yeshidenow():
    try:
        final = [[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]
        print("Your money is safe with us !")
        row = int(input("Enter row : "))
        cols = int(input("Enter col : "))

        final[row][cols] = '*'

        print(final, '\n', "Your money is hidden !")
    except IndexError as e:
        print("This is 3*3 matrix, choose only valid option....")
        inp = input("Do you wanna hide now ? y/n : ")
        if inp == 'y':
            yeshidenow()
        elif inp == 'n':
            print("Your money is not safe, I believe ")
        else:
            print("Choose to hide or nothing else.")

yeshidenow()