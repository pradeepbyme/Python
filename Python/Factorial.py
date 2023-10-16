# def factorial(num):
#     fact = 1
#     for i in range(1,num + 1):
#         fact *= i
#     print(fact)
#
# factorial(5)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
