#option to perform the tracking 
import os
filePath = r"C:\Python\ExpenseTracker\Data\UserExpenses.txt"

class Users:
    # global CurrentUser
    def __init__(self,Name):
        self.name = Name
        # CurrentUser.append(self.name)
        self.AllInserted = [] #list to append all the data into the list
        print(self.name)
        
    # for performing the task of inserting the data into the file
    def Insert(self):
        
        Expense = input("Expense On: ")
        TotalSpend = input("Amount Spended(Rs): ")

        if not TotalSpend.isdigit():
            print("Please Enter the Amount in Digit")
            self.Insert()
        else:    
            self.AllInserted.append(f"spended by: {self.name} Spended On: {Expense}  Amount:{TotalSpend}")
            try:
                with open(filePath,"a") as insertData:
                    insertData.write(f"spended by: {self.name} \t spended on: {Expense} \t Amount:{TotalSpend} \n")
                    reInsert = str(input("press 'y' to continue any other to exit")).lower().strip()
                    if reInsert == 'y':
                        self.Insert()
                    else:
                        return
            except FileNotFoundError as e:    
                    print(f"You encounterd {e}")

    def display(self):
        Name=self.name
        print(f"This is the data of {Name}")
        getAmt = []
        
        try:
             with open(filePath,"r") as readLines:
                    for line in readLines:
                        if f"spended by: {Name}".lower().strip() in line.lower().strip():
                            print(line)
                            getAmt.append(line.split("Amount:")[1].strip())
                            # print(getAmt)
                        # if "Amount:" in line:  
                            
                    
                    global total
                    total=0
                    for Amt in getAmt:
                         total += int(Amt)
                    print(f"You have spent Rs {total} till now")



                                #  break
                            # total_amt  = sum()s
                    # print("Hello")
                            # print("Your total spent till now would be:") 
                    # for every in getAmt:
                     
                    #      total_exp = int(every)
                         
                         
                    # print(total)
        except FileNotFoundError as e:
             print(f"{e}")
             pass

    def delete(self):
        deleteUser = self.name
        # deleteData = [] #list to store the data list which will be deleted when the user confirms it
        option = input("Press 'y' to confirm your delete").lower()
        if option=='y':
            try:
                with open(filePath,"r+") as delUser: 
                        
                        deleteData = [delLine for delLine in delUser if f"spended by: {deleteUser}".lower().strip() not in delLine.lower().strip()]
                      
                        # for delLine in delUser:
                        #     if f"spended by: {deleteUser}".lower().strip() in delLine.lower().strip():
                        #     #     print(deleteData)
                        #         print(delLine)
                        delUser.seek(0)  
                        delUser.truncate()
                        for data in deleteData:
                            delUser.write(data)
                        print("Deleted Success...")
                            
                        # delUser.seek(0) #getting the pointer into the first line of the file
              



            except FileNotFoundError as e:
                print(f"Error: {e}")
        else:
            self.option()







def options(Name):
        # global user
        user = Users(Name)
       
        print(f"Hello: {user.name}")
        print("\t 1. Insert The Expenses Record")
        print("\t 2. Display All Record")
        print("\t 3. Delete Your Records Till Now ")
        option=int(input("\tPlease Select The Operation You Would Like To Perform: "))

        if option == 1:
            user.Insert()
        if option == 2:
             user.display()
        if option == 3:
            user.delete()

             

           





    
    
    
# UserList = [] #TO dynamically generate the object inorder to store the data