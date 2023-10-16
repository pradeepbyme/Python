# anonymous function doesn't name

# Normal Function
def add(x, y):
    return x + y


print(add(2, 3))

# Can be written as:
example = lambda x, y: x + y
retval = example(2, 3)
print(retval)
