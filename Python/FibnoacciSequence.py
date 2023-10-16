def fibonnaci(usrinp):
    f0 = 0
    f1 = 1
    count = 0
    print(f0)
    while count < usrinp - 1:
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        print(f0)
        count += 1


usrinp = int(input("How many sequence ? "))
fibonnaci(usrinp)


# using recursion
