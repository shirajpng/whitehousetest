#Now creating the login for the user inorder to enter to the program
# import os #used to check if the file exist or not

from TrackingOperation import ExpenseTrack

def Login():

    Name = input("Please Enter Your UserName: ")
    Password = input("Please Enter Password: ")

    try:
        with open(r"C:\Python\ExpenseTracker\Data\UserData.txt","r") as Login :
            for line in Login:
                if f"Name: {Name}" in line.strip():
                    if f"Password: {Password}" in line.strip():
                        print("Welcome To The Personal Expense Tracker")
                        # if hasattr(ExpenseTrack,"Users"):
                        # ExpenseTrack.Users(Name)
                        ExpenseTrack.options(Name)
                        break
                    else:
                        print("Sorry Your password doesn't match")
                        break
            else:
                print("Sorry No Record Found Of such check your username and password")
                

    except FileNotFoundError as e:
        print(f"Sorry: {e}")

