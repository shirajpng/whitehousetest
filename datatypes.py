# Integer
age = 25
print(type(age))  # Output: <class 'int'>

# Floating-Point
pi = 3.14159
print(type(pi))  # Output: <class 'float'>

# String
name = "Alice" 
print(type(name)) # Output: <class 'str'>

# List
fruits = ["apple", "banana", "cherry", "cherry"]
print(fruits)  # Output: <class 'list'>

# Tuple 
my_tuple = (1, 2, 3, 4, 5, 3)
print(my_tuple)
# my_tuple[0] = 7 #error

# Dictionary
person = {"name": "Peter", "age": 20, "age":60}
print(person)  # Output: <class 'dict'>

# Set
unique_numbers = {1, 2, 3, 5, 5}
print(unique_numbers)  # Output: <class 'set'>

# Boolean
is_student = True
print(type(is_student))  # Output: <class 'bool'>

# Loops:
# For:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  break
  continue

# While:
count = 0
while (count < 3): 
    count = count + 1
    print("Hello Nepal")

# Conditionals: 
# if-elseif-else
i = 20
if (i == 10): 
    print("i is 10") 
elif (i == 15): 
    print("i is 15") 
elif (i == 20): 
    print("i is 20") 
else: 
    print("i is not present")

try:
  print(xm)
except:
  print("Something went wronggg")
finally:
  print("The 'try except' is finished")

# String concatenation
print("Go"+"Nepal")


# comparison operators ( <,>,=, ==)