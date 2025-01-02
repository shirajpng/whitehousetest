# def val(a):

#     first_val = a
#     # second_val = b

#     try:
#         if isinstance(first_val,int):
#             print("Helllo")
#         else:
#             raise Exception("Sorry the number is not integer")
#     except Exception as e:
#         print(e)



# val(4)

#class and object

class person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} -> {self.age} "


p1 = [] #list to creaete the object dynamically
def add_new():

    name = str(input("Enter your name:"))
    age = int(input("Enter your age:"))
    per = person(name,age)
    p1.append(per)
    reDo = input("Add another obj press")
    if reDo == 'y':
        add_new()
    else:
        print("Your data is saved")
        show()
        exit()

def show():
    for new in p1:
        print(new)

add_new()






