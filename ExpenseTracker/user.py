# This will show the user sign up for accessing the expense track


def UserSign():
    print("\t -----------------------------------------------")
    print("\t \n \t  Welcome to Personal Expense Tracking System \n")
    print("\t -----------------------------------------------")

    Name =  input("\t \t \t \n  Enter Your Username:  ")
    Password = input("\t \t \n Enter the password: \t ")
    if len(Name) != 0 and not Name.isdigit():
            if len(Password) >= 4:
                print("You username and the password is set...")
                   
            else:
                print(f"Sorry you should enter the password more than {len(Password)}")
    else:
        print("Sorry this username is not suitable enter the name")
                
    # opt = input("Do You want to Again perform the signUp...(press y to perform)").lower()
 

    try:
        with open(r"C:\Python\ExpenseTracker\Data\UserData.txt","a") as UserSign:
            UserSign.write(f"Name: {Name}  Password: {Password} \n")
            exit()
                
    except FileNotFoundError as e:
        print(f"Sorry the {e}")
    
            



