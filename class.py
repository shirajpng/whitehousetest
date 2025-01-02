
#  class
# class MyClass:
#   x = 5

# object
# p1 = MyClass()
# print(p1.x)

# The __init__() Function
# The __str__() Function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
# print(p1)