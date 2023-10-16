# assertion in Python

try:
    key = int(input("Enter a value : "))
    assert key > 0
    print(key)
except AssertionError:
    print("Value should be greater than 0")
except ValueError:
    print("Value should not be a string")