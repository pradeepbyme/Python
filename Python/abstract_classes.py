# This classes are abstract and abstract class can also contain
# concrete methods ( methods having body ) and for an abstract class,
# object can not be created.

# when implemented abstract methods in the subclass, all the abstract methods
# should be implemented, otherwise it throws an error.
from abc import ABC, abstractmethod


class Abstraction(ABC):

    """This class containing three abstract methods and two concrete methods
    Abstract methods:
    implement_sub1()
    implement_sub2()
    implement_sub3()
    Concrete methods:
    concrete_method1()
    concrete_method2()
    """

    @abstractmethod
    def implement_sub1(self):
        pass

    @abstractmethod
    def implement_sub2(self):
        pass

    @abstractmethod
    def implement_sub3(self):
        pass

    @staticmethod
    def concrete_method1():
        return "Concrete Method in abstraction"

    @staticmethod
    def concrete_method2():
        return "Concrete Method in abstraction"


class SubForAbstraction(Abstraction):

    def implement_sub1(self):
        print("Successfully Implemented implemented_sub1() From Sub Class.")

    def implement_sub2(self):
        print("Successfully Implemented implemented_sub2() From Sub Class.")

    def implement_sub3(self):
        print("Successfully Implemented implemented_sub3() From Sub Class.")


sub = SubForAbstraction()
sub.implement_sub1()
sub.implement_sub2()
sub.implement_sub3()
