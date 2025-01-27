# this will be the entry point for any of the user to store the credentials of the user data
import user #importing the user.py file or module inorder to access to the user.py from the main.py
import Login
print("\t-----------------------------------------------------")
print("\t\tWelcome To Personal Expense Tracking System")
print("\t-----------------------------------------------------")

print("1. To Sign Up")
print("2. To Login")

option = int(input("Press the corresponding digit to perform your task "))

if option == 1:
    try:
        if hasattr(user,"UserSign"): #checks if the module has this attribute or not
            user.UserSign()

    except ModuleNotFoundError:
        print(f"Sorry the module is not found")
if option == 2:
       try:
            if hasattr(Login,"Login"): #checks if the module has this attribute or not
                Login.Login()

       except ModuleNotFoundError:
            print("Sorry the module is not found ")


