for x in range (20):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buxx")
    else:
        print(x)