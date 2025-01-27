list_of = ['apple','apple','2','mango','apple','mango']
list_new = []

for list in list_of:
    if list not in list_new:
        list_new.append(list)
   
print(list_new)

