def addressVal(address):
    dot = address.find(".") # checks for dot
    at = address.find("@") # checks for @
    if (dot == -1): # -1 = invalid
        print("Invalid")
    elif (at == -1): 
        print("Invalid")
    else:
        print("Valid")

print("This program will decide if your input is a valid email address")    
while(True):
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address: ")

    addressVal(x)

# -------------------------------------------------------
"""
Attemp 1 Recreation Score: 8/10

- Forgot the address.find on both variables
- Forgot the first print function before while(True)


"""