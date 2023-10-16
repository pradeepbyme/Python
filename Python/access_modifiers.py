class Access(object):
    def __init__(self):
        self.var1 = 10
        self._var2 = 20
        self.__var3 = 30

a = Access()
print(a.var1) # public variable
print(a._var2)
