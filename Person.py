# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def display(self):
#         return 'Name: ' + self.name
#
# man = Person('Dennis')
# print(man.display())
# man.name = 'Jack'
# print(man.display())

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def display(self):
        return 'Name: ' + self.__name

man = Person('Dennis')
print(man.display())
man.__name = 'Anna'
print(man.display())
man.name = 'Anna'
print(man.display())
print(man.name)