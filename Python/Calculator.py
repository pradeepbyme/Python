# A basic simple calculator

def add(x, y):
    print(f"{x} + {y} = {x + y}")
    return x + y


def sub(x, y):
    print(f"{x} - {y} = {x - y}")
    return x - y


def mul(x, y):
    print(f"{x} * {y} = {x * y}")
    return x * y


def div(x, y):
    print(f"{x} / {y} = {x / y}")
    return x / y


while True:
    n1 = int(input("Enter first number : "))


    def operations(num=0):
        n2 = int(input("Enter next number : "))
        if op not in ['+', '-', '*', '/']:
            print("Choose a valid operation!")
        elif op == '+':
            return add(n1, n2)
        elif op == '-':
            return sub(n1, n2)
        elif op == '*':
            return mul(n1, n2)
        elif op == '/':
            return div(n1, n2)
        else:
            exit()


    op = input("+\n-\n*\n/\nChoose the operation : ")
    z = operations()
    opinion = input(f"Do you wanna continue again with the {z} ? y/n ")
    if opinion == 'y':
        operations(z)
        break
    elif opinion == 'n':
        print("That's your opinion!")
        break
    else:
        print("Choose valid option!")
        break
