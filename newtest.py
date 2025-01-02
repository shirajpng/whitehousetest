try:
    a = 9
    b=8
    print(isinstance(a, str))
    raise Exception()
except:
    print("there was an exception")
finally:
    print("this runs anyways")
