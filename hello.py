# int
a=1
b="2"
print(a+int(b))

#
a="heloo"
b="word"
print(a+b)


# floating
a="1.5"
b=6.1
# print(a+b)


 
 
print(type(a))

data=[1,2,3,4,5,'hello']
data[0]=99
print(data)
print(type(data))


data={1,2,4,5,5}
print(data)
print(type(data))



#
a={"name":"ram","name":"shyam"}
print(a)
# type checking
print(type(a))

# tuple
a=(1,2,4,'hello')
b=(1,2,4,5)

print(a)
# a[0]=99

#for
for i in range(1,10):
    a="ram"
    print(f"hello {i} {a}")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#   break
  continue
  print("after continue")

# While:
count = 0


while (count < 3): 
    count = count + 1
    print(count)
    print("Hello Nepal")


# if

if a == 10:
    print("a is 10")
elif a == 20:
    print("a is 20")
elif a == 20:
    print("a is 20")
elif a == 20:
    print("a is 20")
else:
    print("a is not 10")