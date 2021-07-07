print("Text based calculator")
try:
    number = float(input("Enter your first number "))
    numbertwo = float(input("Enter your second number "))
except:
    print("You must enter a number")
    exit()

def add(number, numbertwo):
    return number + numbertwo

def div(number, numbertwo):
    return number / numbertwo
     

def sub(number, numbertwo):
    return number - numbertwo
    

def multiply(number, numbertwo):
    return number * numbertwo

def exponent(number, numbertwo):
    return number ** numbertwo
    

answer = input("What do you want to do ((s)ubtraction, (a)ddition, (d)ivison, (m)ultiplication, (e)xponents  ")
if answer == "a":
    print(add(number, numbertwo))
elif answer == "s":
    print(sub(number, numbertwo))
elif answer == "d":
    print(div(number, numbertwo))
elif answer == "m":
    print(multiply(number, numbertwo))
elif answer == "e":
    print(exponent(number, numbertwo))
