# Let's talk about args, kwargs
# args -> positional arbitary arguments (*)
# kargs -> keyword arbitary arguments (**)

def func(a, b, c, d, e):
    print(a, b, c, d, e)


func(2, 3, 4, 5, 6)

func(*(2, 3, 4, 5, 6))  # unpacks the values of positional arbitary arguments

func(**{'a': 14, 'c': 13, 'd': 12, 'b': 10})  # unpacks the values of keyword arbitary arguments
