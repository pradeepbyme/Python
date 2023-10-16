# Decorator : Allows us to tack an extra functionality to an already existing function.
# They use the @ operator and are placed on the top of the original function
from _testcapi import instancemethod


# decorators on class methods

class Decorator:
    stat = 13

    def __init__(self, cls_var):
        self.cls_var = cls_var

    @instancemethod
    def instance_dec(self):
        print("Variable in Instance Method : ", self.cls_var)

    @classmethod
    def statis_met(cls):
        print("Variable in Static Method : ", cls.stat)

    @staticmethod
    def general_utility():
        print("This method doesn't use any variables")


# calling an instance method
decc = Decorator(23)
decc.instance_dec()

# calling a class method
Decorator.statis_met()

# calling a static method
Decorator.general_utility()
